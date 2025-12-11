# resources
## 🚀 Beginner Track: Core Resources

Three foundational resources form the entry track for beginners:

### 1. Mathematics for Machine Learning (MML)

- [ ] **Authors:** Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong (2020)  
- [ ] **Link:** Free textbook  
- [ ] **Coverage:** Linear algebra, calculus, probability for ML context  
- [ ] **Use for:** Part 1 for math review, Chapter 8 for ML introduction

### 2. Introduction to Statistical Learning with Python (ISLP)

- [ ] **Authors:** Gareth James, Daniela Witten, Trevor Hastie, Rob Tibshirani (2023)  
- [ ] **Link:** Free textbook  
- [ ] **Coverage:** Classic ML algorithms, statistical learning theory  
- [ ] **Use for:** Main textbook for supervised/unsupervised learning methods

### 3. Deep Learning Specialization

- [ ] **Instructor:** Andrew Ng  
- [ ] **Platform:** deeplearning.ai / Coursera  
- [ ] **Coverage:** Neural networks, CNNs, RNNs, sequence models  
- [ ] **Use for:** Practical deep learning implementation

---

## 🗺️ Learning Roadmap

[ ] Original guide: [Beginner Learning Path](https://trics.me/beginner.html)

```
Math    ML       DL                   Subfields and data types
=====   =======  =================    ============================

          +-------------------------> Tabular data and time series
          |
MML   -> ISLP -> deeplearning.ai  -> Text and speech (NLP)
(free)   (free)  Deep Learning        Transformers (the T in ChatGPT)
          |      Specialization  +    Computer vision (CV)
          |      any of 3 free   |    Reinforcement learning (RL)
          |      textbooks       |
          |                      |
         Practical manuals:      |
         - scipy lectures        |
         - Müller, Géron, Burkov |
                                 v
                        Choose your specialization
```

### Python Packages by Domain

**Math & Computation:**

- `numpy` - Numerical computing, arrays, linear algebra
- `scipy` - Scientific computing, optimization, statistics

**Machine Learning:**

- `scikit-learn` - Classic ML algorithms (see [Gaël Varoquaux 2023 interview](https://www.youtube.com/watch?v=ONb2OcLRQTo))

**Deep Learning:**

- `torch` (PyTorch) - Most advanced, research-focused
- `tensorflow` - Most cited, production-ready
- `keras` - Easier interface, high-level API

**Data Handling:**

- `pandas` or `polars` - Tabular data manipulation

**Visualization:**

- `matplotlib` - Standard plotting
- `plotly`, `bokeh` - Interactive visualizations

---

## 📚 Reference Textbooks

These denser textbooks serve as references alongside the core beginner track:

### Classic Machine Learning

- [ ] **Bishop (2006)** - Pattern Recognition and Machine Learning
- [ ] **Murphy (2022)** - Probabilistic Machine Learning

### Deep Learning

- [ ] **Goodfellow, Bengio, Courville (2016)** - Deep Learning Book (DLB)
  - The reference text with continuous citations
- [ ] **Zhang, Lipton, Li, Smola (2021)** - [Dive into Deep Learning (d2l)](https://d2l.ai/)
  - Jupyter notebooks integrating exposition, math, and runnable code
  - Freely available with interactive examples
- [ ] **Prince (2023)** - [Understanding Deep Learning (UDL)](https://udlbook.github.io/udlbook/)
  - Recent textbook with updated content

### Specialized Domains

- [ ] **Jurafsky and Martin** - Speech and Language Processing (NLP)
- [ ] **Sutton and Barto** - Reinforcement Learning: An Introduction (RL)

---

## 🎥 Video Series (Essential)

### StatQuest by Josh Starmer

- [ ] **Focus:** Statistics and ML concepts explained intuitively
- [ ] **Style:** Visual, step-by-step breakdowns
- [ ] **Best for:** Understanding core concepts (PCA, regression, neural nets, etc.)
- [ ] **Link:** YouTube channel

### 3Blue1Brown by Grant Sanderson

- [ ] **Focus:** Mathematical visualization
- [ ] **Notable Series:**
  - [ ] [Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
  - [ ] [Essence of Linear Algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
  - [ ] [Essence of Calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
  - [ ] [Lockdown Math](https://www.youtube.com/watch?v=ppWPuXsnf1Q&list=PLZHQObOWTQDP5CVelJJ1bNDouqrAhVPev)
  - [ ] [Differential Equations](https://www.youtube.com/watch?v=p_di4Zn4wz4&list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6)
  - [ ] [Multivariable Calculus](https://www.youtube.com/playlist?list=PLSQl0a2vh4HC5feHa6Rc5c0wbRTx56nF7)
  - [ ] [Central Limit Theorem](https://www.youtube.com/watch?v=zeJD6dqJ5lo&list=PLZHQObOWTQDOMxJDswBaLu8xBMKxSTvg8)
  - [ ] [Convolutions in Image Processing](https://www.youtube.com/watch?v=8rrHTtUzyZA&list=PLZHQObOWTQDMp_VZelDYjka8tnXNpXhzJ)
  - [ ] [Binomial Distributions](https://www.youtube.com/watch?v=8idr1WZ1A7Q&list=PLZHQObOWTQDOjmo3Y6ADm0ScWAlEXf-fp)
  - [ ] [Binary, Hanoi and Sierpinski](https://www.youtube.com/watch?v=2SUvWfNJSsM&list=PLZHQObOWTQDMRtm8h9bG9P06WINNoBnCR)
  - [ ] [Space Filling Curves](https://www.youtube.com/watch?v=RU0wScIj36o&list=PLZHQObOWTQDO__zBYmoxntqx3yBpuXQBl)
  - [ ] [Block Collision Puzzle](https://www.youtube.com/watch?v=HEfHFsfGXjs&list=PLZHQObOWTQDMalCO_AXOC5GWsuY8bOC_Y)
  - [ ] [Explainers](https://www.youtube.com/watch?v=r6sGWTCMz2k&list=PLZHQObOWTQDN52m7Y21ePrTbvXkPaWVSg)
  - [ ] [The Brachistochrone with Steven Strogatz](https://www.youtube.com/watch?v=Cld0p3a43fU&list=PLZHQObOWTQDM7GZNAL2pvtP5rZVCeHGgz)
- [ ] **Style:** Beautiful animations explaining mathematical intuition
- [ ] **Best for:** Deep understanding of math behind ML
- [ ] **Link:** YouTube channel

### Andrej Karpathy

- [ ] **Focus:** Neural networks, transformers, GPT architecture
- [ ] **Notable:** [NanoGPT](https://github.com/karpathy/nanoGPT) - minimal GPT implementation
- [ ] **Style:** Code walkthroughs, architectural deep dives
- [ ] **Best for:** Understanding modern transformer architectures
- [ ] **Link:** YouTube and GitHub

### Andrew Ng

- [ ] **Free Course:** [Machine Learning Specialization](https://www.youtube.com/watch?v=PPLop4L2eGk&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)
- [ ] **Focus:** Comprehensive ML fundamentals
- [ ] **Best for:** Structured learning path from basics to advanced

### PyTorch Deep Dive

- [ ] **[PyTorch Full Course](https://www.youtube.com/watch?v=Z_ikDlimN6A)** - Complete PyTorch tutorial

### Additional ML Resources

- [ ] [Colah's Blog](http://colah.github.io/) - Clear explanations of neural network concepts
- [ ] [Distill.pub](https://distill.pub/) - Interactive ML research articles
- [ ] [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) - Free online book
  - [GitHub Repository](https://github.com/mnielsen/neural-networks-and-deep-learning)
- [ ] [Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html) - Mechanistic interpretability
- [ ] [GPT Learning Hub](https://www.gptlearninghub.ai/codingproblems) - Coding problems
- [ ] [Neural Network Zoo](https://www.asimovinstitute.org/neural-network-zoo/) - Visual architecture guide
- [ ] [AI Warehouse YouTube](https://www.youtube.com/@aiwarehouse) - Curated AI content

### Essential YouTube Channels (Not Yet Listed)

**Deep Learning & Theory:**

- [ ] **[Yannic Kilcher](https://www.youtube.com/@YannicKilcher)** - Paper explanations, daily ML news
  - Deep dives into latest research papers
  - Critical analysis of AI developments
- [ ] **[Two Minute Papers](https://www.youtube.com/@TwoMinutePapers)** - Latest AI research in digestible format
  - Computer graphics and AI breakthroughs
  - "What a time to be alive!"
- [ ] **[Arxiv Insights](https://www.youtube.com/@ArxivInsights)** - Research paper summaries
- [ ] **[AI Coffee Break with Letitia](https://www.youtube.com/@AICoffeeBreak)** - AI ethics & research

**Practical Implementation:**

- [ ] **[sentdex](https://www.youtube.com/@sentdex)** - Python, ML, and neural networks
  - Practical Python tutorials
  - Deep learning from scratch series
- [ ] **[Nicholas Renotte](https://www.youtube.com/@NicholasRenotte)** - Computer vision & deep learning projects
  - Real-world CV applications
  - TensorFlow tutorials
- [ ] **[Aladdin Persson](https://www.youtube.com/@AladdinPersson)** - PyTorch implementations
  - Paper implementations in PyTorch
  - Clear code walkthroughs
- [ ] **[Abhishek Thakur](https://www.youtube.com/@abhishekkrthakur)** - Kaggle grandmaster, practical ML
  - Competition strategies
  - End-to-end ML projects

**NLP & LLMs:**

- [ ] **[Hugging Face](https://www.youtube.com/@HuggingFace)** - Transformers, NLP, latest models
  - Model releases and demos
  - Transformers library tutorials
- [ ] **[Sam Witteveen](https://www.youtube.com/@samwitteveenai)** - LangChain, LLM applications
  - Practical LLM tutorials
  - RAG implementations
- [ ] **[James Briggs](https://www.youtube.com/@jamesbriggs)** - Vector databases, semantic search
  - Pinecone and vector DB tutorials
  - LLM engineering

**System Design & MLOps:**

- [ ] **[ML System Design Interview](https://www.youtube.com/@MLSystemDesignInterview)** - Production ML systems
- [ ] **[Neptune.ai](https://www.youtube.com/@neptune-ai)** - MLOps practices
- [ ] **[Made With ML](https://www.youtube.com/@madewithml)** - MLOps by Goku Mohandas

**Mathematics Deep Dives:**

- [ ] **[Khan Academy](https://www.youtube.com/@khanacademy)** - Linear algebra, statistics, calculus
- [ ] **[MIT OpenCourseWare](https://www.youtube.com/@mitocw)** - Gilbert Strang's Linear Algebra (18.06)
  - [ ] [Linear Algebra Full Course](https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D)
- [ ] **[Professor Leonard](https://www.youtube.com/@ProfessorLeonard)** - Calculus series
- [ ] **[Steve Brunton](https://www.youtube.com/@Eigensteve)** - Control theory, data-driven methods
  - Singular Value Decomposition
  - Dynamic Mode Decomposition

**Computer Science Fundamentals:**

- [ ] **[CS50](https://www.youtube.com/@cs50)** - Harvard's CS fundamentals
- [ ] **[MIT 6.006 Introduction to Algorithms](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)**
- [ ] **[Computerphile](https://www.youtube.com/@Computerphile)** - CS concepts explained

**AI News & Trends:**

- [ ] **[AI Explained](https://www.youtube.com/@aiexplained-official)** - AI developments analysis
- [ ] **[Matthew Berman](https://www.youtube.com/@matthew_berman)** - Local LLMs, AI tools
- [ ] **[Prompt Engineering](https://www.youtube.com/@engineerprompt)** - LLM prompting techniques
- [ ] **[Wes Roth](https://www.youtube.com/@WesRoth)** - AI news and analysis

**Interview Prep & Career:**

- [ ] **[Clément Mihailescu](https://www.youtube.com/@clem)** - Coding interviews (general SWE)
- [ ] **[Data Science Jay](https://www.youtube.com/@DataScienceJay)** - DS interview prep
- [ ] **[Tina Huang](https://www.youtube.com/@TinaHuang1)** - Data science career advice

**Specific Must-Watch Videos:**

- [ ] [But what is a neural network? | 3Blue1Brown](https://www.youtube.com/watch?v=aircAruvnKk) - Start here
- [ ] [Attention is All You Need - Explained](https://www.youtube.com/watch?v=iDulhoQ2pro) - Yannic Kilcher
- [ ] [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) - Jay Alammar (blog)
- [ ] [Stanford CS229: Machine Learning](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) - Full course
- [ ] [Stanford CS224N: NLP with Deep Learning](https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ)
- [ ] [Stanford CS231N: CNNs for Visual Recognition](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)
- [ ] [MIT 6.S191: Intro to Deep Learning](https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI)
- [ ] [DeepMind x UCL: Deep Learning Lectures](https://www.youtube.com/playlist?list=PLqYmG7hTraZCDxZ44o4p3N5Anz3lLRVZF)
- [ ] [Fast.ai Practical Deep Learning for Coders](https://www.youtube.com/playlist?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU)

---

## 🛠️ What Else? Supplementary Resources

### Probability and Statistics

- [ ] **Probability for Data Science (P4D)** - Introductory course
- [ ] **Seeing Theory** - Visual introduction to probability and statistics

### Mathematics for Machine Learning

**Books & Courses:**

- [ ] [Mathematics for Machine Learning (MML) book](https://mml-book.github.io/)
- [ ] [Introduction to Statistical Learning with Python (ISLP)](https://www.statlearning.com/)
- [ ] [Coursera Mathematics for Machine Learning Specialization](https://www.coursera.org/specializations/mathematics-machine-learning)
- [ ] [Linear Algebra Done Right videos by Axler](https://linear.axler.net/LADRvideos.html)
- [ ] [Mathematics for ML GitHub Resources](https://github.com/dair-ai/Mathematics-for-ML)

**Online Resources:**

- [ ] [Math Visual Proofs YouTube](https://www.youtube.com/@MathVisualProofs/videos)
- [ ] [Sinc Press](https://sincxpress.com/)
- [ ] [EdX - Math for Machine Learning with Python](https://www.edx.org/learn/math/edx-math-for-machine-learning-with-python)
- [ ] [Google's ML Crash Course Prerequisites](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework)

### Practical Python for ML

- [ ] **scipy lectures** - Underappreciated resource by scikit-learn package authors
- [ ] **Python Data Science Handbook** - Jake VanderPlas (includes ML chapter)
- [ ] **Practical books** (combine concepts + code):
  - [ ] Müller & Guido - Introduction to Machine Learning with Python (paid)
  - [ ] Géron - Hands-On Machine Learning (paid)
  - [ ] Burkov - The Hundred-Page Machine Learning Book (free preview)

### Online Learning Platforms

- [ ] [Fast.ai](https://www.fast.ai/) - Practical deep learning courses
- [ ] [Applied AI Course](https://www.appliedaicourse.com) - Industry-focused ML
- [ ] [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2017/09/common-machine-learning-algorithms/)
- [ ] [Analytics Vidhya Learning Plan](https://www.analyticsvidhya.com/blog/2017/01/the-most-comprehensive-data-science-learning-plan-for-2017/)

### Code Collections and Practice

- [ ] **ML-From-Scratch** - Implementing algorithms from scratch
- [ ] **Kaggle competitions** - Real datasets and competitions
  - Note: Kaggle is Google-owned, emphasizes TensorFlow over PyTorch

### Kaggle YouTube Learning Playlists

**Official Micro-Courses (Free):**

- [ ] **[Intro to Machine Learning](https://www.youtube.com/playlist?list=PLqFaTIg4myu8t5ycqvp7I07jTjol3RCl9)** - 7 lessons, scikit-learn basics
- [ ] **[Intermediate Machine Learning](https://www.youtube.com/playlist?list=PLqFaTIg4myu-dNobDHQZPrD2wH27PthCG)** - Missing values, categorical variables, pipelines
- [ ] **[Feature Engineering](https://www.youtube.com/playlist?list=PLqFaTIg4myu-Q4NTmxSwAdTjZSGxMXnvP)** - Creating better features
- [ ] **[Intro to Deep Learning](https://www.youtube.com/playlist?list=PLqFaTIg4myu-b1PlxitQdY0UYIbys-2es)** - Neural networks with TensorFlow/Keras
- [ ] **[Computer Vision](https://www.youtube.com/playlist?list=PLqFaTIg4myu-b1PlxitQdY0UYIbys-2es)** - CNNs, image classification
- [ ] **[Time Series](https://www.youtube.com/playlist?list=PLqFaTIg4myu8gbDh6oBl7XRYNBlthpDEW)** - Forecasting techniques
- [ ] **[Data Cleaning](https://www.youtube.com/playlist?list=PLqFaTIg4myu-mXKiZIC7XvJN1VsN7cUqp)** - Handling messy data
- [ ] **[Intro to SQL](https://www.youtube.com/playlist?list=PLqFaTIg4myu8a_AJx1pF3pYIRBe8vPWLh)** - BigQuery for data science
- [ ] **[Advanced SQL](https://www.youtube.com/playlist?list=PLqFaTIg4myu-p5FlWLbXAipm0dqBRDuZm)** - Joins, CTEs, window functions
- [ ] **[Geospatial Analysis](https://www.youtube.com/playlist?list=PLqFaTIg4myu8qRNyJKwLVxmJLbD34LTcf)** - Working with location data
- [ ] **[Machine Learning Explainability](https://www.youtube.com/playlist?list=PLqFaTIg4myu8oo7MQrjRGLt7bTLGpSKEr)** - SHAP, permutation importance
- [ ] **[Intro to Game AI and Reinforcement Learning](https://www.youtube.com/playlist?list=PLqFaTIg4myu-dNobDHQZPrD2wH27PthCG)** - RL basics
- [ ] **[Natural Language Processing](https://www.youtube.com/playlist?list=PLqFaTIg4myu-7FrcD9xvjQs0EJK8OjW0x)** - Text processing, embeddings
- [ ] **[Intro to AI Ethics](https://www.youtube.com/playlist?list=PLqFaTIg4myu-VZxY-Y0x93VkYb-X90Kut)** - Fairness, bias, accountability
- [ ] **[Data Visualization](https://www.youtube.com/playlist?list=PLqFaTIg4myu-Tv2-xdVCVQJ8RQZuoXQiF)** - Seaborn, matplotlib

**Competition & Project Content:**

- [ ] **[Kaggle Days Meetup](https://www.youtube.com/playlist?list=PLqFaTIg4myu8t3j_kIRk3I3tNFGPDUYhm)** - Community presentations
- [ ] **[Kaggle CareerCon](https://www.youtube.com/playlist?list=PLqFaTIg4myu9f21aM1POYVxMWlTALbxIj)** - Career advice from data scientists
- [ ] **[Kaggle Solutions](https://www.youtube.com/playlist?list=PLqFaTIg4myu-FVeGI6lZCxz8yYlKNOqeM)** - How winners solved competitions
- [ ] **[Kaggle Notebooks Showcases](https://www.youtube.com/playlist?list=PLqFaTIg4myu-2nkFgHTbRHYCaSjBPFO3r)** - Featured community notebooks

**Interview & Tutorial Series:**

- [ ] **[Kaggle Reading Group](https://www.youtube.com/playlist?list=PLqFaTIg4myu-qfK4RsxL6YlVYyYdBfCKH)** - Paper discussions
- [ ] **[Kaggle Data Science for Good](https://www.youtube.com/playlist?list=PLqFaTIg4myu9jLJQFaIRy4IQRqk0tBz3a)** - Social impact projects
- [ ] **[Grandmaster Series](https://www.youtube.com/playlist?list=PLqFaTIg4myu8gbDh6oBl7XRYNBlthpDEW)** - Interviews with Kaggle GMs

### Domain-Specific Modeling

- [ ] **Econometrics** - [Econ 1630](https://www.brown.edu/Departments/Economics/Faculty/Glenn_Loury/louryhomepage/teaching/Ec_1630/) chapters 1, 2, 4, 5
- [ ] **Data analysis vocabulary** - Industry perspectives from:
  - Google, Mathworks, H2O.ai, NVIDIA documentation

### Research Papers and Advanced Topics

- [ ] Statistical Learning Theory (loss, risk, PAC-Bayes)
- [ ] Breiman's "Two Cultures" (2001) - Inference vs. prediction debate
- [ ] Current ML/AI research on arXiv

---

## ⚠️ Not in Scope (But Important)

This guide focuses on ML concepts and modeling. These related skills are NOT deeply covered but are essential for professional work:

- **Python programming depth** - Advanced OOP, design patterns, performance optimization
- **Linux and cloud computing** - DevOps, containerization, orchestration
- **Data processing pipelines** - Airflow, Spark, real-time streaming
- **Model productization** - API design, scalability, monitoring
- **Experiment design** - A/B testing, causal inference, statistical power
- **Advanced statistics** - Bayesian methods, time series, survival analysis
- **Non-ML modeling** - Optimization, simulation, control theory
- **Domain knowledge** - Business understanding, subject matter expertise
- **ML adoption outcomes** - Organizational change, ethics, governance

For coverage of these topics, refer to the complete MDTP sections below.

---

## Extended Modelling Process

The table below summarizes steps in the extended modeling process, from initial idea to business/societal benefits:  

| Section / steps | Typical questions | An example |
| :---- | :---- | :---- |
| Idea | Why bother collecting data and modelling in this area? | Everyone else is doing this (usually bad). Space for improvements (good). |
| Models | What kind formulas do I need? What are their limitations? | Linear regression and OLS. |
| Data – provenance | How is the data collected? Does this reflect what we need to know?  | Some said the data is valid. |
| Data – artifacts and datasets | Do we have the data? Can we store and manage this data?  | There is a CSV file or a database that allows a SQL query. |
| Software | What software should I use?  | Python pandas and statmodels libraries. |
|  | How do I write my own code? | In a Jupyter notebook. |
| Infrastructure | Where do I put my code and data? | Laptop or Google Colab. |
| Teams and roles | Who is working on a project?  | Just myself.  |
| Business value | Does the modlling result provide any improvements for the business? | Adjust goods purchases to seasonality. |
| Society benefits | Are there any gains for everyone not just a specific company? | Rise in productivity in agrofood sector. Improved food security. |

#

# **M. Models**

~~Non-essential topics are strike-through~~
