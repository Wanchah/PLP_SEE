# app.py — Streamlit App for CORD-19 Metadata Analysis

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load cleaned data
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv')
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))
    df = df.dropna(subset=['title', 'publish_time'])
    return df

df = load_data()

# App layout
st.title("📊 CORD-19 Data Explorer")
st.write("Explore COVID-19 research trends using the metadata from the CORD-19 dataset.")

# Sidebar filters
st.sidebar.header("Filter Options")
year_range = st.sidebar.slider("Select Year Range", 2019, 2022, (2020, 2021))
min_words = st.sidebar.slider("Minimum Abstract Word Count", 0, 1000, 100)

filtered_df = df[
    (df['year'].between(*year_range)) &
    (df['abstract_word_count'] >= min_words)
]

# Show sample data
st.subheader("📄 Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'year', 'abstract_word_count']].head(10))

# Publications by year
st.subheader("📅 Publications Over Time")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, palette='viridis')
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Top journals
st.subheader("🏛️ Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2, palette='mako')
ax2.set_title("Top Publishing Journals")
ax2.set_xlabel("Number of Papers")
ax2.set_ylabel("Journal")
st.pyplot(fig2)

# Word cloud
st.subheader("🔤 Common Words in Titles")
title_text = ' '.join(filtered_df['title'].dropna()).lower()
wc = WordCloud(width=800, height=400, background_color='white').generate(title_text)
fig3, ax3 = plt.subplots(figsize=(12, 6))
ax3.imshow(wc, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# Source distribution
st.subheader("📚 Top Sources")
source_counts = filtered_df['source_x'].value_counts().head(10)
fig4, ax4 = plt.subplots()
sns.barplot(x=source_counts.values, y=source_counts.index, ax=ax4, palette='cubehelix')
ax4.set_title("Top Sources of Papers")
ax4.set_xlabel("Number of Papers")
ax4.set_ylabel("Source")
st.pyplot(fig4)