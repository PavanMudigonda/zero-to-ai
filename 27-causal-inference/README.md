# 27: Causal Inference

> "Correlation does not imply causation, but causation implies correlation." - Statistics Proverb

Welcome to the **Causal Inference** phase of your zero-to-ai journey! This module bridges the gap between observational data analysis and true causal understanding - the holy grail of data science.

## 🎯 Why Causal Inference Matters

Traditional machine learning excels at prediction: "What will happen?" Causal inference answers the deeper questions: "Why does this happen?" and "What would happen if we intervened?"

### Real-World Impact
- **Policy Evaluation**: Does a new education program actually improve outcomes?
- **Business Decisions**: Will reducing prices increase revenue?
- **Medical Research**: Does this treatment actually cure the disease?
- **A/B Testing**: Understanding why a variant performs better

## 📋 Learning Objectives

By the end of this phase, you'll be able to:

### Foundational Knowledge
- **Distinguish correlation from causation** using real examples
- **Understand counterfactual reasoning** and potential outcomes
- **Master causal graphs** (DAGs) for modeling relationships
- **Apply d-separation** and backdoor criterion for causal identification

### Core Techniques
- **Randomized Controlled Trials (RCTs)**: The gold standard
- **Matching methods**: Propensity score matching, nearest neighbor
- **Instrumental Variables**: Natural experiments and exogenous variation
- **Regression Discontinuity**: Quasi-experimental designs
- **Difference-in-Differences**: Before-after comparisons

### Advanced Methods
- **Causal Discovery**: Learning causal structure from data
- **Causal Machine Learning**: Combining ML with causal reasoning
- **Mediation Analysis**: Understanding causal pathways
- **Heterogeneous Treatment Effects**: Who benefits most?

### Practical Applications
- **A/B Test Analysis**: Beyond simple comparisons
- **Policy Evaluation**: Measuring intervention effects
- **Business Analytics**: Causal insights for decision making
- **Healthcare Analytics**: Treatment effect estimation

## 📚 Prerequisites

### Required Knowledge
- **Statistics**: Probability, hypothesis testing, regression (Phases 02, 03)
- **Machine Learning**: Supervised learning basics (Phases 06, 07)
- **Python**: Data manipulation with pandas, numpy (Phases 01, 02)

### Recommended Background
- **Linear Algebra**: Matrix operations, eigenvalues (Phase 03)
- **Econometrics**: Basic regression concepts
- **Research Methods**: Experimental design principles

## 🗂️ Curriculum Structure

### Phase 27: Causal Inference (6 Notebooks)

#### 1. **Causal Fundamentals**
   - Correlation vs Causation
   - Counterfactual Framework
   - Potential Outcomes Model
   - Fundamental Problem of Causal Inference

#### 2. **Causal Graphs & DAGs**
   - Directed Acyclic Graphs
   - d-Separation & Independence
   - Backdoor Criterion
   - Frontdoor Criterion

#### 3. **Experimental Design**
   - Randomized Controlled Trials
   - Power Analysis & Sample Size
   - Blocking & Stratification
   - Ethical Considerations

#### 4. **Observational Methods**
   - Propensity Score Matching
   - Inverse Probability Weighting
   - Regression Adjustment
   - Doubly Robust Estimation

#### 5. **Quasi-Experimental Designs**
   - Instrumental Variables
   - Regression Discontinuity
   - Difference-in-Differences
   - Natural Experiments

#### 6. **Advanced Topics & Applications**
   - Causal Discovery Algorithms
   - Mediation Analysis
   - Heterogeneous Effects
   - Real-World Case Studies

## 🛠️ Technical Requirements

### Core Libraries
```python
# Foundational
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Causal Inference
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import NearestNeighbors

# Advanced Methods
import networkx as nx  # For causal graphs
from dowhy import CausalModel  # Microsoft DoWhy library
from econml import *  # Microsoft EconML for heterogeneous effects
```

### Installation
```bash
# Core packages
pip install numpy pandas matplotlib seaborn scikit-learn statsmodels

# Causal inference packages
pip install dowhy econml networkx

# Optional but recommended
pip install causalml pygam  # Additional causal ML tools
```

## 📊 Key Concepts You'll Master

### 1. **Counterfactual Reasoning**
```python
# Understanding what would have happened
# Y_i(1) = outcome if treated
# Y_i(0) = outcome if not treated
# Causal effect = Y_i(1) - Y_i(0)
```

### 2. **Causal Graphs**
```python
# Representing causal relationships
# A → B: A causes B
# A ← B: B causes A (different from A → B)
# A ↔ B: Bidirectional relationship
```

### 3. **Identification Strategies**
```python
# Backdoor criterion: Control for confounders
# Frontdoor criterion: Alternative identification
# Instrumental variables: Exogenous variation
```

### 4. **Treatment Effect Estimation**
```python
# Average Treatment Effect (ATE)
# Conditional Average Treatment Effect (CATE)
# Individual Treatment Effect (ITE)
```

## 🎯 Hands-On Projects

### Project 1: A/B Test Analysis
- Analyze a marketing campaign A/B test
- Estimate treatment effects with confidence intervals
- Handle practical complications (non-compliance, attrition)

### Project 2: Observational Study
- Evaluate the impact of a policy change
- Use matching methods to balance covariates
- Compare results with experimental data

### Project 3: Causal Discovery
- Learn causal structure from observational data
- Validate discovered relationships
- Apply to real-world datasets

## 📈 Learning Outcomes

### Technical Skills
- **Causal identification** in complex systems
- **Experimental design** for valid inference
- **Robust estimation** under various assumptions
- **Sensitivity analysis** for causal claims

### Critical Thinking
- **Question assumptions** in data analysis
- **Design better experiments** and studies
- **Communicate uncertainty** in causal claims
- **Avoid common pitfalls** in causal reasoning

### Practical Application
- **Policy evaluation** with real data
- **Business decision-making** with causal evidence
- **Research design** for causal questions
- **Impact assessment** of interventions

## 🚨 Common Pitfalls to Avoid

### 1. **Confusing Correlation with Causation**
```python
# Example: Ice cream sales and drowning deaths
# Both increase in summer, but ice cream doesn't cause drowning
```

### 2. **Selection Bias**
```python
# Example: Volunteer bias in medical studies
# Health-conscious people more likely to participate
```

### 3. **Reverse Causation**
```python
# Example: Does depression cause poverty, or poverty cause depression?
# Need careful temporal ordering
```

### 4. **Omitted Variable Bias**
```python
# Example: Education and income correlation
# Intelligence affects both (confounder)
```

## 🔬 Real-World Applications

### Healthcare
- Treatment effectiveness evaluation
- Drug safety assessment
- Healthcare policy impact analysis

### Business & Marketing
- Campaign effectiveness measurement
- Pricing strategy optimization
- Customer behavior analysis

### Policy & Social Science
- Education program evaluation
- Economic policy impact assessment
- Social intervention studies

### Technology & Product
- Feature impact measurement
- User experience optimization
- Product recommendation systems

## 📚 Recommended Resources

### Books
- **"Causal Inference in Statistics"** by Judea Pearl
- **"Mostly Harmless Econometrics"** by Angrist & Pischke
- **"The Book of Why"** by Judea Pearl & Dana Mackenzie
- **"Causal Inference: What If"** by Hernán & Robins

### Online Courses
- **Causal Inference** (Coursera - Brady Neal)
- **A Crash Course in Causality** (Coursera - Pearl)
- **Causal Diagrams** (YouTube - StatQuest)

### Libraries & Tools
- **DoWhy**: Microsoft causal inference library
- **EconML**: Heterogeneous treatment effects
- **CausalML**: Uplift modeling and causal inference
- **PyMC**: Bayesian causal modeling

## 🎯 Success Metrics

### Knowledge Check
- Can you distinguish correlation from causation?
- Can you draw and interpret causal DAGs?
- Can you identify valid identification strategies?

### Skills Assessment
- Can you design a valid experiment?
- Can you estimate treatment effects from observational data?
- Can you communicate causal findings clearly?

### Practical Application
- Can you apply causal methods to business problems?
- Can you critically evaluate causal claims in research?
- Can you design studies to answer causal questions?

## 🚀 Career Impact

### Job Roles Enhanced
- **Data Scientist**: More rigorous analysis
- **Research Scientist**: Better experimental design
- **Policy Analyst**: Stronger impact evaluation
- **Product Manager**: Better feature testing

### Industry Applications
- **Tech**: A/B testing, user behavior analysis
- **Healthcare**: Treatment evaluation, drug development
- **Finance**: Risk assessment, investment decisions
- **Policy**: Government program evaluation

## 🎉 Phase Completion

Upon completing this phase, you'll have mastered:

✅ **Causal thinking** - Beyond correlation to causation  
✅ **Experimental design** - RCTs and quasi-experiments  
✅ **Observational methods** - When experiments aren't possible  
✅ **Causal discovery** - Learning from data  
✅ **Real-world application** - Business and policy impact  

---

**Ready to begin?** Let's dive into the fascinating world of causal inference, where we move beyond "what" to "why" and "what if"!

*"All that is gold does not glitter, not all those who wander are lost; the old that is strong does not wither, deep roots are not reached by the frost."* - J.R.R. Tolkien

The deepest insights come from understanding cause and effect. Let's uncover them together! 🌟