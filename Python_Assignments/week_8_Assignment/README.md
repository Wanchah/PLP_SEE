---

## 📁 Recommended Repo Structure: `Frameworks_Assignment`

```
Frameworks_Assignment/
│
├── app.py                     # Streamlit app
├── CORD19_Analysis.ipynb      # Jupyter notebook for EDA
├── metadata.csv               # Dataset (or link to download)
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and instructions
```

---

## 📄 `requirements.txt`

```txt
pandas
matplotlib
seaborn
streamlit
wordcloud
```

---

## 📝 `README.md`

Here’s a complete draft you can use:

```markdown
# 🧠 CORD-19 Metadata Analysis & Streamlit App

This project explores the metadata from the CORD-19 dataset, focusing on COVID-19 research papers. It includes a Jupyter notebook for data cleaning and analysis, and a Streamlit app for interactive visualization.

## 📦 Dataset

- Source: [CORD-19 Research Challenge on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
- File used: `metadata.csv`

## 🎯 Objectives

- Load and explore real-world research metadata
- Clean and prepare data for analysis
- Visualize trends in publication year, journal frequency, and title keywords
- Build an interactive Streamlit app to present findings

## 📁 Project Structure

```
Frameworks_Assignment/
├── app.py                     # Streamlit app
├── CORD19_Analysis.ipynb      # Jupyter notebook for EDA
├── metadata.csv               # Dataset (or link to download)
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and instructions
```

## 🧪 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/Frameworks_Assignment.git
cd Frameworks_Assignment
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

## 📊 Visualizations Included

- Publications by year
- Top publishing journals
- Word cloud of common title words
- Source distribution

## 📝 Reflection

This project helped me:
- Practice real-world data cleaning and transformation
- Understand trends in COVID-19 research
- Build a functional web app using Streamlit

## 📌 Notes

- The full CORD-19 dataset is large; this project uses only the `metadata.csv` file.
- If `metadata.csv` is not included, download it from Kaggle and place it in the root folder.

## 📦 Dataset

Due to file size limits, `metadata.csv` is not included in this repo.

You can download it directly from Kaggle:  
🔗 [CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Place `metadata.csv` in the root folder before running the notebook or app.
---