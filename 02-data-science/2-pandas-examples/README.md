# Pandas Examples - Consolidated & Organized

This directory contains a comprehensive collection of pandas tutorials, exercises, and real-world projects, consolidated from multiple sources and organized for progressive learning.

## 📁 Directory Structure

### 01-basics/
**Beginner-friendly tutorials covering fundamental pandas concepts**

#### Pandas 101 Series (YouTube Course):
- `Pandas 101 - Pandas Series and Dataframes.ipynb` - Core data structures
- `Pandas 101 - Reading in Files.ipynb` - Loading data from various sources
- `Pandas 101 - Data Cleaning in Pandas.ipynb` - Handling missing data, duplicates
- `Pandas 101 - Filtering and Ordering in Pandas.ipynb` - Boolean indexing, sorting
- `Pandas 101 - Group by and Aggregating in Pandas.ipynb` - Grouping and aggregations
- `Pandas 101 - Indexing in Pandas.ipynb` - Row/column selection techniques
- `Pandas 101 - Merge, Join, and Concatenate in Pandas.ipynb` - Combining DataFrames
- `Pandas 101 - Visualizing Data in Pandas.ipynb` - Creating plots
- `Pandas 101 - Exploratory Data Analysis in Pandas.ipynb` - EDA techniques

#### DataFrame Fundamentals:
- `DataFrames I.ipynb` - Introduction to DataFrames
- `DataFrames II.ipynb` - Intermediate DataFrame operations
- `DataFrames III.ipynb` - Advanced DataFrame techniques

#### Pandas & NumPy Integration:
- `pandas-numpy-lessons/` - Three lessons on pandas with NumPy
  - `lesson1/` - Basic integration
  - `lesson2/` - Intermediate techniques
  - `lesson3/` - Advanced operations

**Topics Covered:**
- Series and DataFrame creation
- Reading CSV, Excel, JSON files
- Data cleaning (missing values, duplicates, formatting)
- Indexing and selection (.loc, .iloc, boolean indexing)
- Filtering, sorting, and ordering
- Basic aggregations and statistics

**Recommended Order:**
1. Start with Pandas 101 series (in order listed above)
2. Work through DataFrames I-III
3. Explore pandas-numpy-lessons

---

### 02-intermediate/
**Intermediate topics for deepening pandas knowledge**

Comprehensive course from "Data Analysis with Pandas and Python":

**Core Operations:**
- `DataFrames 1.ipynb` - DataFrame fundamentals (review)
- `DataFrames 2.ipynb` - Intermediate operations
- `DataFrames 3.ipynb` - Advanced operations
- `GroupBy.ipynb` - Advanced grouping and aggregation
- `Input and Output.ipynb` - Reading/writing various formats
- `Merge, Join and Concat.ipynb` - Combining datasets
- `Multiindex.ipynb` - Hierarchical indexing
- `Options and Settings.ipynb` - Customizing pandas behavior

**Data Operations:**
- `Filtering Methods.ipynb` - Advanced filtering techniques
- `Missing Data.ipynb` - Handling NaN and None values
- `Text Methods and Filtering.ipynb` - String operations
- `Working with Dates and Times.ipynb` - DateTime operations

**Visualization & Analysis:**
- `Visualizations.ipynb` - Plotting with pandas
- `Working with Duplicates.ipynb` - Finding and removing duplicates

**Topics Covered:**
- Advanced groupby operations (multiple aggregations, transformations)
- Multi-level indexing (hierarchical data)
- DateTime manipulation and time series
- String methods and text processing
- Complex filtering and boolean logic
- Data type conversions and optimization
- Handling large datasets efficiently

---

### 03-exercises/
**Practice exercises to test and improve your pandas skills**

#### 100 Pandas Puzzles:
- `100-pandas-puzzles.ipynb` - 100 curated pandas challenges
- `100-pandas-puzzles-with-solutions.ipynb` - Same with solutions

**Description:** Inspired by 100 NumPy exercises, these puzzles focus on core DataFrame and Series manipulation, covering indexing, grouping, aggregating, and data cleaning.

**Difficulty Levels:**
- ★☆☆ Easy - Basic operations
- ★★☆ Medium - Combining multiple techniques
- ★★★ Hard - Complex multi-step solutions

#### Topic-Based Exercises:

Located in `topic-based-exercises/`:

**01 - Getting & Knowing Your Data:**
- Chipotle, Occupation, World Food Facts datasets
- Basic exploration, info, describe, shape, columns

**02 - Filtering & Sorting:**
- Chipotle, Euro12, Fictional Army datasets
- Boolean indexing, sorting, conditional selection

**03 - Grouping:**
- Alcohol Consumption, Occupation, Regiment datasets
- GroupBy operations, aggregations, transformations

**04 - Apply:**
- Students Alcohol Consumption, US Crime Rates
- Apply, map, applymap functions

**05 - Merge:**
- Auto MPG, Fictitious Names, Housing Market
- Merge, join, concat operations

**06 - Stats:**
- US Baby Names, Wind Stats
- Statistical operations, rolling windows

**07 - Visualization:**
- Chipotle, Online Retail, Scores, Tips, Titanic
- Matplotlib integration, plotting techniques

**08 - Creating Series and DataFrames:**
- Pokemon dataset
- Programmatic DataFrame creation

**09 - Time Series:**
- Apple Stock, Financial Data, Investor Flows
- DateTime indexing, resampling, time-based operations

**10 - Deleting:**
- Iris, Wine datasets
- Dropping rows, columns, duplicates

**11 - Indexing:**
- Advanced indexing exercises
- Setting, resetting, multi-level indices

**Each topic includes:**
- Exercises.ipynb (practice problems)
- Solutions.ipynb (detailed solutions with explanations)

---

### 04-advanced/
**Advanced techniques and specialized topics**

#### pandas-cookbook/
A comprehensive cookbook with advanced recipes.

**Located in:** `pandas-cookbook/`

**Contents:**
- Advanced data manipulation techniques
- Performance optimization strategies
- Memory-efficient operations
- Complex transformations and aggregations
- Integration with other libraries

**Topics:**
- Custom aggregation functions
- Window functions and rolling operations
- Categorical data optimization
- Working with large datasets
- Advanced indexing patterns
- Data pipeline design

---

### 05-real-world-projects/
**Real-world data analysis projects**

**Projects:**

1. **Apple Health Data.ipynb**
   - Analyzing personal health data exports
   - Time series analysis of activity, heart rate, sleep
   - Visualization of health trends

2. **Electronic Production India.ipynb**
   - Economic data analysis
   - Industry production trends
   - Regional comparisons

**Datasets:**
- `bigmac.csv` - Big Mac Index data (purchasing power parity)
- `chicago.csv` - Chicago city data
- `crime_india.csv` - Crime statistics
- Additional real-world datasets

**Skills Applied:**
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Time series analysis
- Statistical analysis
- Data visualization
- Insight generation and reporting

---

## 🎯 Learning Path

### Beginner (0-3 weeks)
```
01-basics/
  ├── Complete Pandas 101 series (9 notebooks)
  ├── DataFrames I-III
  └── Practice: First 30 puzzles from 100-pandas-puzzles
  
Time: 2-3 hours daily
Goal: Understand Series, DataFrames, basic operations
```

### Intermediate (3-8 weeks)
```
02-intermediate/
  ├── All notebooks (focus on GroupBy, MultiIndex, DateTime)
  
03-exercises/
  ├── Complete 100 pandas puzzles
  └── Topics 01-05 from topic-based-exercises
  
Time: 1-2 hours daily
Goal: Master grouping, merging, advanced indexing
```

### Advanced (8-12 weeks)
```
03-exercises/
  ├── Topics 06-11 (Stats, Viz, Time Series)
  
04-advanced/
  └── pandas-cookbook (select relevant recipes)
  
05-real-world-projects/
  └── Complete both projects
  
Time: 1-2 hours daily
Goal: Apply techniques to real-world scenarios
```

---

## 📊 Content Statistics

- **Total Notebooks:** 151 notebooks
- **Total Size:** 173 MB
- **Exercise Sets:** 100+ puzzles + 11 topic-based sets
- **Real-World Projects:** 2 complete projects
- **Datasets:** 20+ CSV/Excel files included

---

## 🗂️ Source Repositories

This consolidated collection combines content from:

1. **100-pandas-puzzles** - https://github.com/ajcr/100-pandas-puzzles
2. **Data-Analysis-with-Pandas-and-Python** - Udemy course materials
3. **data-analysis-with-python-and-pandas** - Another pandas course
4. **pandas_exercises** - https://github.com/guipsamora/pandas_exercises
5. **pandas-and-numpy** - Integration tutorial
6. **pandas-cookbook** - Advanced recipes and techniques
7. **PandasYouTubeSeries** - YouTube Pandas 101 course

---

## 🚀 Getting Started

### Installation
```bash
# Install pandas
pip install pandas

# Optional: Install visualization libraries
pip install matplotlib seaborn

# Optional: Install additional data libraries
pip install openpyxl xlrd
```

### Quick Start
```python
import pandas as pd
import numpy as np

# Verify installation
print(f"pandas version: {pd.__version__}")

# Create a simple DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'SF', 'LA']
})

print(df)
```

---

## 💡 Study Tips

1. **Hands-On Practice**
   - Type all examples (don't copy-paste)
   - Modify examples to test understanding
   - Complete exercises before looking at solutions

2. **Use Documentation**
   - `df.method?` in Jupyter for quick help
   - Official pandas docs: https://pandas.pydata.org/docs/

3. **Practice Daily**
   - 30-60 minutes daily beats weekend cramming
   - Complete 3-5 exercises per session

4. **Learn Shortcuts**
   - Method chaining for cleaner code
   - Vectorized operations over loops
   - Use `.pipe()` for custom operations

5. **Benchmark Performance**
   - Use `%timeit` to compare approaches
   - Learn memory-efficient techniques
   - Understand when to use `.loc` vs `.iloc`

6. **Real Data Practice**
   - Use Kaggle datasets for practice
   - Analyze your own data (fitness, finance, etc.)
   - Contribute to open-source projects

---

## 🔍 Key Pandas Concepts

### Must-Know Operations
1. **Selection:** `.loc[]`, `.iloc[]`, boolean indexing
2. **Filtering:** Boolean conditions, `.query()`
3. **Grouping:** `.groupby()`, aggregations
4. **Merging:** `.merge()`, `.join()`, `.concat()`
5. **Reshaping:** `.pivot()`, `.melt()`, `.stack()`, `.unstack()`
6. **DateTime:** `.dt` accessor, resampling
7. **Strings:** `.str` accessor methods
8. **Missing Data:** `.isna()`, `.fillna()`, `.dropna()`

### Performance Tips
- Use categorical dtype for strings with few unique values
- Use `.query()` for complex boolean operations
- Prefer vectorized operations over `.apply()`
- Use `.pipe()` for readable method chains
- Consider chunking for very large datasets

---

## 📖 Additional Resources

### Official Documentation
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)
- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

### Books (Free Online)
- [Python for Data Analysis (3rd Edition)](https://wesmckinney.com/book/) by Wes McKinney (pandas creator)
- [Pandas Cookbook](https://github.com/PacktPublishing/Pandas-Cookbook)

### Practice Datasets
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
- [FiveThirtyEight Data](https://data.fivethirtyeight.com/)

---

## 🎓 Certification Readiness

This collection prepares you for:
- Data Analyst roles
- Data Science positions (pandas foundation)
- Python for Data Analysis certifications
- Kaggle competitions

**Skills You'll Master:**
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Statistical analysis
- Data visualization
- Time series analysis
- Data transformation and aggregation

---

## 📝 Next Steps After Completion

1. **Apply to Real Projects**
   - Analyze public datasets
   - Contribute to data science blogs
   - Build a portfolio on GitHub

2. **Advanced Topics**
   - Dask for big data (out-of-memory datasets)
   - Polars (faster alternative to pandas)
   - PySpark for distributed computing

3. **Domain Applications**
   - Finance: stock analysis, portfolio optimization
   - Healthcare: patient data analysis
   - Marketing: customer segmentation
   - Sports: performance analytics

---

## 📄 License

Individual directories may have their own licenses. Please refer to original repository licenses for attribution and usage rights.

---

**Last Updated:** December 2024  
**Consolidated By:** Automated organization process  
**Original Size:** 188 MB (166 files across 7 directories)  
**Consolidated Size:** 173 MB (151 notebooks - 8% reduction)  
**Organization:** Beginner → Intermediate → Exercises → Advanced → Projects
