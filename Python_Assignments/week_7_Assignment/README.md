## 📘 README: Iris Dataset Analysis

### 🧠 Project Overview

This project demonstrates a complete data analysis workflow using the **Iris dataset**, a classic dataset in machine learning and statistics. The notebook walks through data loading, exploration, basic statistical analysis, and visualizations using Python libraries like `pandas`, `matplotlib`, and `seaborn`.

The goal is to showcase foundational data science skills including:
- Data cleaning and inspection
- Descriptive statistics
- Grouped analysis
- Visual storytelling through charts

---

### 📂 Files Included

- `iris_analysis.ipynb` — Jupyter notebook containing all code, outputs, and explanations

---

### 🛠️ Tools & Libraries

- `pandas` — for data manipulation and analysis  
- `matplotlib` — for plotting basic charts  
- `seaborn` — for enhanced visual styling  
- `sklearn.datasets` — to load the Iris dataset

---

### 📊 Analysis Workflow

#### 1. **Data Loading & Exploration**
- Loaded the Iris dataset using `sklearn.datasets.load_iris()`
- Converted it into a `pandas.DataFrame`
- Inspected the first few rows using `.head()`
- Checked data types and missing values
- Verified dataset cleanliness (no nulls)

#### 2. **Basic Statistical Analysis**
- Used `.describe()` to compute mean, median, standard deviation, etc.
- Grouped data by species and calculated average feature values
- Identified patterns in petal and sepal measurements across species

#### 3. **Data Visualization**
Created four distinct visualizations:
- 📈 **Line Chart** — Simulated time-series of sepal length
- 📊 **Bar Chart** — Average petal length per species
- 📉 **Histogram** — Distribution of sepal width
- 🔵 **Scatter Plot** — Relationship between sepal length and petal length

Each plot includes:
- Titles
- Axis labels
- Legends (where applicable)
- Custom styling via `seaborn`

---

### 📌 Key Findings

- *Setosa* species has significantly smaller petal dimensions compared to *Versicolor* and *Virginica*  
- Sepal length and petal length show a positive correlation across species  
- Feature distributions vary distinctly between species, supporting classification potential

---

### 🚀 How to Run

1. Clone the repository or download the notebook
2. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
3. Open the notebook:
   ```bash
   jupyter notebook iris_analysis.ipynb
   ```
4. Run each cell sequentially to view outputs and plots

---

### 📬 CREDITS

**Abdulquddus**  
🔗 GitHub: [github.com/Wanchah](https://github.com/Wanchah)
