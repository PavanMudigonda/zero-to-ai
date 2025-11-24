# Machine Learning Guide

**Machine Learning Checklist**  

---

## 📑 Table of Contents

### Introduction & Getting Started

- [Prerequisites](#-prerequisites)
- [Beginner Track: Core Resources](#-beginner-track-core-resources)
- [Learning Roadmap](#️-learning-roadmap)
- [Reference Textbooks](#-reference-textbooks)
- [Video Series (Essential)](#-video-series-essential)
- [Supplementary Resources](#️-what-else-supplementary-resources)
- [Not in Scope](#️-not-in-scope-but-important)
- [Extended Modelling Process](#extended-modelling-process)

### MDTP Framework: Models, Data, Tools, Productisation

**M. Models**

- [M0. Statistical thinking and intuition](#m0-statistical-thinking-and-intuition)
- [M1. Statistical inference](#m1-statistical-inference)
- [M2. Econometrics](#m2-econometrics)
- [M3. Bayesian modeling and causal inference](#m3-bayesian-modeling-and-causal-inference)
- [M4. Classic machine learning](#m4-classic-machine-learning)
- [M5. Neural nets (NN) and deep learning](#m5-neural-nets-nn-and-deep-learning)
- [M6. NLP, CV and RL subfields](#m6-nlp-cv-and-rl-subfields)
- [M7. Other modelling techniques](#m7-other-modelling-techniques)
- [M8. Additional topics (harder or less exciting)](#m8-additional-topics-harder-or-less-exciting)
- [M9. Modern AI Architectures (2020-2025)](#m9-modern-ai-architectures-2020-2025)

**D. Data**

- [D1. Data sources](#d1-data-sources)
- [D2. Data analysis](#d2-data-analysis)
- [D3. Data engineering](#d3-data-engineering)
- [D4. Pipelines and orchestration](#d4-pipelines-and-orchestration)
- [D5. Data management](#d5-data-management)

**T. Tools – Code and Infrastructure**

- [T0. Writing code](#t0-writing-code)
- [T1. Software tools](#t1-software-tools)
- [T2. Cloud and computing infrastructure](#t2-cloud-and-computing-infrastructure)
- [T3. Development Tools and Environment](#t3-development-tools-and-environment)

**P. Productisation**

- [P1. Productisation and business value](#p1-productisation-and-business-value)
- [P2. Applications, domains and cases](#p2-applications-domains-and-cases)
- [P3. Society impacts and regulation](#p3-society-impacts-and-regulation)

**E. Extra**

- [E1. Companies](#e1-companies)

### Personalized Learning Path

- [Your Current Position](#-your-current-position)
- [Phase 1: Foundation](#phase-1-foundation)
- [Phase 2: Embeddings & Vectors](#phase-2-embeddings--vectors-current-focus)
- [Phase 3: Neural Networks & Architecture](#phase-3-neural-networks--architecture)
- [Phase 4: LLMs & Modern AI](#phase-4-llms--modern-ai-)
- [Phase 5: Specialized Domains](#phase-5-specialized-domains)
- [Phase 6: ML Engineering & Production](#phase-6-ml-engineering--production)
- [Phase 7: Ethics, Safety & Advanced Concepts](#phase-7-ethics-safety--advanced-concepts)

### Microsoft AI/Agent Framework Ecosystem

- [Microsoft Agent Frameworks & Courses](#-microsoft-agent-frameworks--courses)

### AWS Machine Learning

- [AWS ML & Certification Resources](#️-aws-machine-learning--certification-resources)

### Career & Community

- [Interviews & Career Insights](#-interviews--career-insights)
- [Influential Educators & Thinkers](#-influential-educators--thinkers)
- [Professional Glossary & Common Terms](#-professional-glossary--common-terms)

---

This guide provides a comprehensive roadmap for learning machine learning, from foundational mathematics to production-ready AI systems. It combines:

- **M (models)**: probability, statistics, econometrics, machine learning, deep learning and other modelling areas.  
- **D (data)**: data engineering, data management and data governance.  
- **T (tools)**: software tools, databases and computing infrastructure.  
- **P (productisation)**: ok, now you have the data, a model and a server running, but what's the benefit?

## 📋 Prerequisites

Before diving into machine learning, ensure you have:

- **Working knowledge of Python** - Basic programming concepts, data structures, control flow
  - [] [Python Bro Code Refresher](https://github.com/PavanMudigondaTR/python-bro-code)
- **Mathematical foundations** - Comfort with mathematical notation and concepts from:
  - Linear algebra (vectors, matrices, operations) -
    - [] [Khan Academy Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
  - Calculus (derivatives, gradients, chain rule)
    - [] [Khan Academy Calculus 1](https://www.khanacademy.org/math/calculus-1)
  - Basic probability and statistics -
    - [] [Khan Academy Statistics & Probability](https://www.khanacademy.org/math/statistics-probability)

If you need to strengthen these areas, refer to Khan Academy's free courses above or the resources in the sections below.

---

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

## **M0. Statistical thinking and intuition**

- [ ] Probability, random variables, distributions.  
- [ ] Model vs. reality. Digital twins.
- [ ] Structure and causality.
- [ ] Inference (econometrics) vs generalisation (machine learning). Breiman's *[Two Cultures](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)* (2001) and rebuttals.  
- [ ] Observation, experiment and experiment design.  
- [ ] Treatment and treatment effects.
- [ ] Measurement errors and missing data.

## **M1. Statistical inference**

- [ ] Data generating process, sample vs population.  
- [ ] Sampling techniques and inference. Statistical model.
- [ ] Frequentist and Bayesian views of a statistical model.  
- [ ] ~~Modelling tradeoffs and “no free lunch”.~~  
- [ ] Measuring model quality and performance.  
- [ ] Model lifecyle, data and model drift.

## **M2. Econometrics**

- [ ] Cross-section, time series, panel and spatial data.
- [ ] Linear regression and ordinary least squares (OLS).  
- [ ] Violation of OLS assumptions. [*Peter Kennedy*](https://en.wikipedia.org/wiki/Peter_Kennedy_\(economist\)) textbook and the [*10 Commandments*](https://www.principlesofeconometrics.com/poe5/writing/kennedy.pdf).  
- [ ] ~~Difference-in-differences, instrumental variables, regression discontinuity.~~  
- [ ] ~~Time series. Seasonal adjustment, smoothing, filtering.~~  
- [ ] ~~Systems of equations.~~  
- [ ] Estimation techniques: OLS and varieties, GMM, maximum likelihood, Bayesian estimates.

## **M3. Bayesian modeling and causal inference.**

- [ ] ~~Bayesian modeling and probabilistic programming.~~  
- [ ] ~~Causal inference and do-notation.~~

## **M4. Classic machine learning.**

- [ ] Tasks: classification, regression, clustering, dimensionality reduction, decision trees, support vector machines and discriminant analysis.  
- [ ] Criteria for model selection and performance evaluation.
- [ ] ~~Statistical learning theory (loss, theoretical and empirical risk, PAC-Bayes)~~  
- [ ] ~~Forecast combination, choosing forecasts and AutoML.~~

## **M5. Neural nets (NN) and deep learning.**

- [ ] Simple perceptron and NN construction (gradient descent, backpropagation, regularization).  
- [ ] Traditional NN architectures (feed-forward, convolutional, recurrent, generative аdversarial, transformers).  
- [ ] **Embeddings and vector representations** (word2vec, sentence-transformers, dense vectors for semantic meaning).  
- [ ] **Tokenization** (BPE, WordPiece, SentencePiece for modern LLMs).  
- [ ] **Attention mechanism** (self-attention, multi-head attention - foundational for transformers).  
- [ ] **Mixture of Experts (MoE)** architecture for efficient scaling.  
- [ ] Artificial general intelligence (AGI) and tests for intelligence.

## **M6. NLP, CV and RL subfields.**

- [ ] Text and speech – classic NLP. [*Jurafsky and Martin*](https://web.stanford.edu/~jurafsky/slp3/)*.*
- [ ] **Large Language Models (LLMs)** - GPT-4, Claude, LLaMA, Gemini architecture and capabilities.  
- [ ] Transformer architecture, prompt engineering, RAGs and fine-tuning.  
- [ ] **Instruction tuning and alignment** (RLHF, DPO, constitutional AI).  
- [ ] **In-context learning** (few-shot, zero-shot, chain-of-thought prompting).  
- [ ] **Model compression** (quantization: 4-bit, 8-bit; distillation; LoRA/QLoRA).  
- [ ] **Hallucination detection and mitigation** in generative models.  
- [ ] Computer vision (CV).  
- [ ] **Multimodal models** (CLIP, GPT-4V, vision-language integration).  
- [ ] **Diffusion models** (Stable Diffusion, DALL-E, Midjourney for image generation).  
- [ ] ~~Reinforcement learning (RL). [*Sutton and Barto*](http://www.incompleteideas.net/book/the-book-2nd.html)*.*~~  
- [ ] ~~Robotics. [*Underactuated Robotics*](https://underactuated.csail.mit.edu/) *course notes by [Russ Tedrake](http://people.csail.mit.edu/russt/).*~~

## **M7. Other modelling techniques.**

- [ ] ~~Graphs and networks. [*NetworkX bibliography.*](https://networkx.org/documentation/stable/#bibliography)~~  
- [ ] ~~Agent-based modeling (ABM).~~
- [ ] ~~Game theory and auction design.~~  
- [ ] ~~Optimisation and linear programming (LP). [*MOSEK and*](https://docs.mosek.com/modeling-cookbook/zbiblio.html#id181)~~
      [*JuMP*](https://jump.dev/JuMP.jl/stable/background/bibliography/) *[bibliographies.](https://docs.mosek.com/modeling-cookbook/zbiblio.html#id181) [Stephen Boyd](https://web.stanford.edu/~boyd) books and classes.*  
- [ ] ~~System dynamics (SD). [*Jay Forrester.*](https://systemdynamics.org/news/memorial/jay-w-forrester/)~~  
- [ ] ~~Control theory. [*r/ControlTheory wiki*](https://www.reddit.com/r/ControlTheory/wiki/index/) *and [Feedback Systems by Aström and Murray](https://www.cds.caltech.edu/~murray/books/AM08/pdf/am08-complete_28Sep12.pdf)*.~~

## **M9. Modern AI Architectures (2020-2025).**

- [ ] **Transformer variants** (encoder-only: BERT; decoder-only: GPT; encoder-decoder: T5).  
- [ ] **Vision Transformers (ViT)** for image understanding.  
- [ ] **State Space Models** (Mamba, structured state spaces for efficient sequence modeling).  
- [ ] **Retrieval-augmented architectures** (RAG systems combining retrieval and generation).  
- [ ] **Sparse models and efficient transformers** (Sparse Transformers, Longformer, sliding window attention).

## **M8. Additional topics (harder or less exciting)**

- [ ] ~~Combinatorics… *[is hard.](https://www.reddit.com/r/mathematics/comments/17e0h2h/combinatorics_destroying_my_ego_the_strangest_of/)*~~  
- [ ] ~~Mathematical statistics (point estimation, confidence bands, hypothesis testing).~~  
- [ ] ~~Central limit theorems, asymptotics and convergence.~~  
- [ ] ~~Non-parametric statistics. [*All of Nonparametric Statistics*](https://link.springer.com/book/10.1007/0-387-30623-4)*.*~~  
- [ ] ~~Entropy, cross-entropy and information theory.~~  
- [ ] ~~Differential equations and random processes.~~  
- [ ] ~~Probability as part of measure theory.~~

# **D. Data**

## **D1. Data sources.**

- [ ] Data collection, observation vs experiment, registration protocols.
- [ ] Physical sensors.  
- [ ] Proprietary vs open data, disclosure requirements, official statistics.  
- [ ] Data distribution and providers. Data markets.  
- [ ] Data protection and privacy.

## **D2. Data analysis.**

- [ ] EDA and descriptive statistics.  
- [ ] Graphs, visualizations, dashboards.  
- [ ] Analysis as a DAG.
- [ ] Reproducible research.

## **D3. Data engineering.**

- [ ] Structured data. Serialization formats (CSV, JSON, XML). Binary data formats.  
- [ ] SQL for tabular data. Dataframes (pandas, polars) and dataframe backends.  
- [ ] Processing large datasets (MapReduce, Hadoop, Spark).  
- [ ] Everything as a vector: text, images, sound and video.
- [ ] Data ingestion, transform, storage, retrieval.  
- [ ] **Vector databases** (Pinecone, Weaviate, ChromaDB, pgvector for embedding storage).  
- [ ] **Embedding storage and retrieval** (semantic search, nearest neighbor, HNSW, FAISS).  
- [ ] **Real-time data streaming** (Kafka, Flink, event-driven architectures).  
- [ ] **Data versioning** (DVC, LakeFS for reproducibility).

## **D4. Pipelines and orchestration.**

- [ ] Modelling pipelines (Airflow and similar).  
- [ ] Model delivery (eg FastAPI).  
- [ ] **MLOps platforms** (MLflow, Weights & Biases, Kubeflow, Neptune).  
- [ ] **Feature stores** (Feast, Tecton for feature management).  
- [ ] **A/B testing and experimentation frameworks** for production ML.  
- [ ] **Model versioning and registry** (tracking model lineage and artifacts).  

## **D5. Data management**

- [ ] Data quality  
- [ ] Corporate data governance (DMBOK).

# **T. Tools – Code and Infrastructure**

## **T0. Writing code**

- [ ] Linux and command line on a local and remote machine.  
- [ ] Software development practices for data modelling (version control, unit testing, APIs, DevOps, product thinking and metrics, architecture).  
- [ ] Python, R, Julia ecosystems for machine learning.

## **T1. Software tools.**

- [ ] Proprietary statistical packages and their documentation.  
- [ ] Open software for statistics (R), machine learning (scikit-learn) and neural networks (pytorch, tensorflow and keras).  
- [ ] Managed services for machine learning (H20, DataRobot, etc).  
- [ ] **LLM frameworks** (LangChain, LlamaIndex, Haystack for LLM applications).  
- [ ] **Hugging Face ecosystem** (Transformers, Datasets, Accelerate, PEFT for model training).  
- [ ] **Vector database libraries** (FAISS, Annoy, hnswlib for similarity search).  
- [ ] **Modern ML frameworks** (JAX, XGBoost, LightGBM, CatBoost for gradient boosting).

## **T2. Cloud and computing infrastructure.**

- [ ] Cloud services and infrastructure provisioning.  
- [ ] **GPU computing** (CUDA, distributed training, multi-GPU setups).  
- [ ] **Container orchestration** (Docker, Kubernetes for ML workloads).  
- [ ] **Serverless ML** (AWS Lambda for inference, Modal, Banana, Replicate).  
- [ ] **Edge deployment** (TensorFlow Lite, ONNX Runtime, model optimization for edge devices).  
- [ ] **LLM hosting** (vLLM, TGI Text Generation Inference, Ollama for local models).

### ☁️ Understanding the Cloud (Business Perspective)

**Client-Server Foundation:**

- Your machine isn't the most powerful (would be too costly)
- Connect to remote machines as admin (e.g., via SSH)
- Users connect to servers for workloads (e.g., API calls)
- Compute and storage happen at the server
- Software evolved from monolith to modular

**Cloud Mindmap:**

- **Virtualization**: Server is no longer a single physical machine (resource efficiency)
- **Storage Solutions**: Various data storage options (S3, block, object storage)
- **Containerization**: Applications spin off containers
- **Orchestration**: Smart container management (Kubernetes)
- **PaaS**: Hosted application environments
- **Serverless**: Small, event-driven functions (Lambda)
- **Networking**: Zones, CDNs, load balancing

**On-Premise vs. Cloud Criteria:**

- Hardware costs vs. operational expenses
- Maintenance costs and staff requirements
- Security and compliance
- Speed and latency
- Flexibility and scalability
- Data ownership and control

**Economics of Cloud Computing:**

- **Virtualization** (hypervisor, VM) achieves higher hardware utilization
- **Decoupling**: Storage (S3) separate from compute (EC2)
- **Load switching** and containerization (Kubernetes, OpenShift)
- Network costs and data transfer pricing
- Data center economies of scale

**Cloud Providers:**

- **Major**: AWS (50% market share), GCP, Azure
- **Service Models**: SaaS / PaaS / IaaS
- **Vendor Lock-in**: Switching costs can be high
- **Competition**: EU antitrust investigations ongoing

**Important Trends:**

- "Managed" and "hybrid" clouds emerged
- Providers offer myriad of services (often with terrible APIs)
- Cannot easily switch providers
- Some companies "grow out of cloud" and return to on-premise

**Data Centers & Energy:**

- Hyperscalers vs. smaller providers
- Energy efficiency critical for sustainability

**Major Deals:**

- Broadcom buying VMware for $68B (2023)
- Microsoft settles EU cloud complaint for €22M (2024)

**Resources:**

- Microsoft: [Economics of the Cloud](https://news.microsoft.com/download/archived/presskits/cloud/docs/The-Economics-of-the-Cloud.pdf)
- Computer Weekly: Broadcom's VMware acquisition impact

### 🗄️ Databases and Storage

**Storage Fundamentals:**

- **HDD vs. SSD vs. Cloud (S3)**: Cost, speed, accessibility tradeoffs
- **File Systems**: HDFS (Hadoop Distributed File System)
- Disk costs and access time considerations

**Database Management Systems (DBMS):**

- **Relational Databases**: SQL-based (PostgreSQL, MySQL, Oracle, SQL Server)
- **NoSQL Types**:
  - Key-Value (Redis, DynamoDB)
  - Document (MongoDB, CouchDB)
  - Column (Cassandra, HBase)
  - Graph (Neo4j, Neptune)
  - **Vector** (Pinecone, Weaviate, ChromaDB, pgvector)
  - Time Series (InfluxDB, TimescaleDB)

**Database Popularity Rankings:**

- <https://db-engines.com/en/ranking>
- JetBrains Developer Ecosystem Survey
- Stack Overflow Developer Survey

**Large Data Processing:**

- **MapReduce**: Programming model for large datasets
- **Hadoop**: HDFS + YARN + MapReduce
- **Spark**: Fast, in-memory distributed computing

**Search Databases:**

- ElasticSearch, Splunk, Solr for full-text search

**Data Warehouses (DW):**

- Architecture: Decoupling storage and compute
- **Cloud Providers**: AWS (Redshift), GCP (BigQuery), Azure (Synapse)
- **New Players**: Snowflake, Databricks (venture-funded, high valuations)

**Database Theory:**

- Relational algebra and ER-diagrams
- **ACID** (Atomicity, Consistency, Isolation, Durability)
- **CAP Theorem** (Consistency, Availability, Partition Tolerance)
- **BASE** (Basically Available, Soft state, Eventually consistent)
- DDL (Data Definition Language) and DML (Data Manipulation Language)
- Normalization and normal forms
- Hashing and B-trees
- **OLAP** (Online Analytical Processing) vs. **OLTP** (Online Transaction Processing)

**Industry Consolidation:**

- Sun buys MySQL (2008), Oracle buys Sun (2010)
- SAP acquires Sybase (2010)
- Cloudera-Hortonworks merger (2019)
- Valkey: Redis fork after license change (2024)

**Learning Resources:**

- DuckDB co-founder: "The Ancient Art of Data Management" (2023 video)
- Lecture notes on database engineering (VSUUT, India)

### 🔧 Data Engineering Tools

**Data Engineering Lifecycle** (from Fundamentals of Data Engineering, O'Reilly):

```
Generation → Storage → Ingestion → Transformation → Serving
```

See also: [Exploring the Modern Data Warehouse](https://learn.microsoft.com/training/) by Microsoft Learn

**Workflow & Orchestration:**

- **Apache Airflow**: Most popular workflow orchestration
- **Prefect**, **Luigi**, **Dagster**: Modern alternatives
- **MLFlow**: ML lifecycle management

**Modern Data Stack:**

```
Data Sources → Ingestion → Storage → Transform → BI/Analytics
               (Fivetran)   (Snowflake) (dbt)     (Looker)
```

**Key Components:**

- Ingestion: Fivetran, Airbyte, Stitch
- Storage: Snowflake, Databricks, BigQuery
- Transform: dbt (data build tool), Spark
- BI: Looker, Tableau, PowerBI
- Reverse ETL: Census, Hightouch

**Additional Resources:**

- Andriy Burukov: MLOps book
- Data Engineering Zoomcamp
- MAD (ML/AI/Data) landscape: firstmark.com
- Reddit: Comments on weekly plan for DE job interview (pipeline2insights)

---

## **T3. Development Tools and Environment.**

- [ ] **Jupyter ecosystem** (JupyterLab, Jupyter notebooks, extensions, interactive computing).  
- [ ] **IDEs and AI coding assistants** (VS Code, Cursor, GitHub Copilot, Windsurf).  
- [ ] **Experiment tracking** (Weights & Biases, Neptune, Comet for reproducibility).  
- [ ] **Data labeling tools** (Label Studio, Prodigy, Scale AI for annotation).

#

# **P. Productisation**

Delivering value for users, business stakeholders and society from data and models.

Note: “model producisation” usually means two things – taking a model out of a single author usage to a workable system – thus making a pipeline, or designing a task ina  way that is likely to serve a business purpose

## **P1. Productisation and business value.**

- [ ] Risk, learning and experimentation in business context.  
- [ ] Modelling hypothesis and expected outcomes.  
- [ ] Data-model-action workflows.  
- [ ] Team roles, rationale for these roles and hiring.  
- [ ] Measuring business outcomes and business impact of ML.  
- [ ] **RAG systems** (Retrieval Augmented Generation architecture and implementation).  
- [ ] **Prompt engineering** as a systematic discipline for LLM applications.  
- [ ] **AI agent frameworks** (AutoGPT, LangChain agents, function calling for autonomous agents).  
- [ ] **Model monitoring** (drift detection, performance tracking in production).  
- [ ] **Cost optimization** (token usage tracking, caching strategies, batch processing).

### 🔄 ML Project Lifecycle Framework

**The Business-Driven ML Process:**

**A. Identify the Business Case**

- Hypothesis where you can earn more or save money
- Clear articulation of expected improvements
- Motivation: Why is this worth pursuing?

**B. Create the Adequate Model**

- Simplified representation of value chain or business process
- **Control points**: Where you make decisions and take actions
- **Data points**: Where you collect data to inform decisions and measure success

**C. State the Proposed Change**

- **Why**: Motivation and business justification
- **What/How/Where**: Detailed proposal
- **Success Criteria**: How to measure if it worked
- **Estimate ROI**: Is it worth the investment?
- **Test Plan**: Simplest way to validate the hypothesis

**D. Prove with Experiments**

- Run controlled tests
- Measure actual impact vs. expected
- Iterate based on results

**E. Scale or Pivot**

- If profitable: Scale the solution
- If not: Update model, change approach, or move to next opportunity
- Document lessons learned

**F. Continuous Improvement**

- Iterate faster, cheaper, with better outcomes
- Build feedback loops into production systems

### 👥 Data Team Roles & Responsibilities

**Perfect World (the "Bam" scenario):**

```
Idea → Good data → Known model → Quick inference → 
Bam to production → Bam cool effect → Bam business liked it
```

**Practically Perfect World (Reality):**

```
Many ideas → Business hypothesis → Expected result → 
Where to deploy? → Which model? → Is there data? → 
Can we train? → Does it work? → Can we deploy? → 
Production monitoring → Can we improve? → Is business happy? → 
How long will results persist?
```

**Role Breakdown - Who Does What?**

1. **Full-Stack Data Scientist** - End-to-end ownership: data → model → deployment
2. **Data Scientist / Modeler** - Focus on model development and experimentation
3. **Data Engineer / Data Architect** - Data pipelines, storage, and infrastructure
4. **Machine Learning Engineer** - Model deployment, serving, production optimization
5. **Software Engineers** - Application development and integration
6. **Research Scientist** - Novel algorithms and state-of-the-art research
7. **Business Analyst** - Requirements, metrics, stakeholder communication
8. **Business Lead / Product Manager** - Strategy, ROI, and product vision
9. **Vendor/Consultant** - External expertise and specialized tools

### 🚀 When Does a Pipeline Become a "Product"?

- Any pipeline that delivered business results (however simple)
- Complex systems beyond model+prediction (frontend, hardware, business rules)
- Anything with data/intelligence that users want
- Industry-specific sellable solutions

### ⚠️ Production Challenges

**Technical:** Data quality, model drift, infrastructure failures, integration issues

**Organizational:** Silos, vested interests, unclear responsibilities, misaligned incentives

**Business:** Unclear success criteria, changing requirements, insufficient ROI

### 📚 ML Production Resources

- **ITMO University Role Model**: <https://github.com/aimclub/ai-competency-model/>
- **Awesome Production ML**: <https://github.com/EthicalML/awesome-production-machine-learning>

**Key Insight from "Demystifying AI for the Enterprise":**
> Feedback loops and ongoing monitoring are most critical for production success.

---

## **P2. Applications, domains and cases**

- [ ] Recommender systems (RecSys).  
- [ ] Clinical trials.  
- [ ] Quality control and industrial automation.  
- [ ] Finance.  
- [ ] **Conversational AI and chatbots** (customer service, virtual assistants).  
- [ ] **Code generation** (GitHub Copilot, code assistants, automated programming).  
- [ ] **Document intelligence** (Q&A over documents, summarization, extraction).  
- [ ] **Search and information retrieval** (semantic search, hybrid search systems).

## **P3. Society impacts and regulation.**

- [ ] Fairness, biases, equity, human loop and ethics.  
- [ ] Grounds for AI regulation and policy.
- [ ] Generation-scale and wicked problems.  
- [ ] **AI safety and alignment** (value alignment, red teaming, adversarial testing).  
- [ ] **Prompt injection and security** vulnerabilities in LLM systems.  
- [ ] **Environmental impact** (carbon footprint of training large models).  
- [ ] **AI watermarking and detection** (synthetic content identification).  
- [ ] **Copyright and intellectual property** issues with generative AI.

# **E. Extra topics**

## **E1. Companies**

- [ ] ~~Academic vs corporate research.~~  
- [ ] ~~Company valuations.~~  
- [ ] ~~Data ownership.~~

---

# **Personalized Learning Roadmap**

This section provides a structured, phase-based approach to learning AI/ML, tailored for progressive skill building from foundations to advanced applications.

## 🎯 Your Current Position

**Phase 1 - Foundation** [ ] (You've completed tokenization basics)  
**Phase 2 - Embeddings & Vectors** 🎯 (You are here - working on embeddings)  
**Phase 3 - Neural Networks & Transformers** ⏭️ (Coming next)  
**Phase 4 - LLMs & Applications** 🔜 (Advanced topics)

---

## 📚 Phase 1: Foundation (2-3 months | 200-300 hours)

> **Goal**: Build mathematical and programming foundations essential for ML
> **Prerequisites**: Basic programming knowledge
> **Outcome**: Ready to understand ML algorithms and implement them

### Core Topics Checklist

**Core Concepts**

- [ ] Artificial Intelligence (AI)
- [ ] Machine Learning (ML)
- [ ] Supervised / Unsupervised / Semi‑Supervised Learning
- [ ] Reinforcement Learning (RL)
- [ ] Offline vs Online Machine Learning
- [ ] Overfitting, Underfitting, Bias, Variance

**Math & Statistics Basics**

- [ ] Loss Functions (Cross‑Entropy, Mean Squared Error)
- [ ] Optimization (gradients, backpropagation basics)
- [ ] L1 Norm, L2 Norm, Regularisation
- [ ] Probability (Naïve Bayes, distributions)

**Data Fundamentals**

- [ ] Features, Labels, Annotation
- [ ] Training/Validation/Testing Sets
- [ ] Feature Engineering & Feature Extraction
- [ ] Normalisation

### 📖 Required Resources (Phase 1)

**Mathematics (80-120 hours)**

- [ ] **[3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)** (~8 hours) ⭐ ESSENTIAL
  - Visual intuition for vectors, matrices, transformations
- [ ] **[3Blue1Brown - Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)** (~6 hours) ⭐ ESSENTIAL
  - Derivatives, integrals, chain rule
- [ ] **[Gilbert Strang - MIT Linear Algebra 18.06](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8)** (~35 hours)
  - Deep dive into linear algebra theory
- [ ] **[Khan Academy](https://www.khanacademy.org/)** - Statistics, Probability, Calculus (30-50 hours)
  - Fill gaps in mathematical knowledge

**Programming (40-60 hours)**

- [ ] **[Python for Beginners - Microsoft](https://github.com/microsoft/c9-python-getting-started)** (10-15 hours)
- [ ] **NumPy, Pandas basics** (20-30 hours)
  - [NumPy Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
  - [Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [ ] **Matplotlib/Seaborn for visualization** (10-15 hours)

**ML Fundamentals (80-120 hours)**

- [ ] **[Andrew Ng - Machine Learning Specialization](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)** (60-80 hours) ⭐ ESSENTIAL
  - Course 1: Supervised ML (Regression, Classification)
  - Course 2: Advanced Learning Algorithms
  - Course 3: Unsupervised Learning, Recommenders, RL
- [ ] **[ISLP Book](https://www.statlearning.com/)** - Introduction to Statistical Learning with Python (40-60 hours)
  - Read chapters 1-8 (linear regression through tree-based methods)

### 🎯 Phase 1 Projects

- [ ] **Project 1**: Linear regression on housing prices (Boston/California dataset)
- [ ] **Project 2**: Classification with logistic regression (Iris/Titanic)
- [ ] **Project 3**: K-means clustering on customer segmentation
- [ ] **Project 4**: Decision tree for loan approval prediction

### ✅ Phase 1 Completion Criteria

Before moving to Phase 2, you should be able to:

- [ ] Explain gradient descent and backpropagation conceptually
- [ ] Implement linear/logistic regression from scratch in NumPy
- [ ] Use scikit-learn for basic ML tasks
- [ ] Understand train/validation/test splits and cross-validation
- [ ] Read and understand mathematical notation in ML papers (basic level)

---

## 📚 Phase 2: Embeddings & Vectors (3-4 weeks | 60-80 hours)

> **Goal**: Understand vector representations and semantic search
> **Prerequisites**: Phase 1 complete
> **Outcome**: Build RAG systems and work with embeddings

### Core Topics Checklist

**Tokenization**

- [ ] Tokens - Text broken into processable units
- [ ] Tokenization algorithms (BPE, WordPiece, SentencePiece)
- [ ] Subword tokenization concepts

**Embeddings** 🔥

- [ ] Embeddings - Dense vector representations
- [ ] Word2Vec, fastText, Doc2Vec
- [ ] Semantic meaning in vector space
- [ ] Cosine Similarity - Measuring semantic similarity
- [ ] Vector operations (addition, subtraction, distance)

**Vector Storage & Retrieval**

- [ ] Vector Database (Pinecone, Weaviate, ChromaDB)
- [ ] Semantic search vs keyword search
- [ ] Nearest neighbor search (FAISS, HNSW)
- [ ] Dimensionality (384, 768, 1536 dimensions)

**Text Representations (Classical)**

- [ ] Bag of Words, N‑grams (Bigrams, Trigrams)
- [ ] TF (Term Frequency), IDF (Inverse Document Frequency)
- [ ] TF‑IDF weighting

### 📖 Required Resources (Phase 2)

**Core Learning (30-40 hours)**

- [ ] **[Word2Vec Paper](https://arxiv.org/abs/1301.3781)** - Original embeddings paper (3-4 hours)
- [ ] **[Jay Alammar - Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/)** (1 hour)
- [ ] **[Sentence Transformers Documentation](https://www.sbert.net/)** (5-10 hours)
  - Learn modern embedding models
- [ ] **Hugging Face - [Embeddings Course](https://huggingface.co/learn/nlp-course/)** (Chapter 5) (10-15 hours)

**Vector Databases (15-20 hours)**

- [ ] **[Pinecone Documentation](https://docs.pinecone.io/)** (5-8 hours)
- [ ] **[ChromaDB Tutorial](https://docs.trychroma.com/)** (3-5 hours)
- [ ] **[FAISS Tutorial](https://github.com/facebookresearch/faiss/wiki)** (5-7 hours)

**Practical Implementation (15-20 hours)**

- [ ] Build semantic search engine with sentence-transformers
- [ ] Create vector database with ChromaDB or Pinecone
- [ ] Implement similarity search and ranking

### 🎯 Phase 2 Projects

- [ ] **Project 1**: Semantic search engine for your documents
- [ ] **Project 2**: Question-answering with document retrieval
- [ ] **Project 3**: Duplicate detection using embeddings
- [ ] **Project 4**: Text clustering and visualization with t-SNE/UMAP

### ✅ Phase 2 Completion Criteria

- [ ] Generate embeddings using sentence-transformers
- [ ] Build and query a vector database
- [ ] Implement semantic search from scratch
- [ ] Understand cosine similarity vs. Euclidean distance
- [ ] Explain difference between sparse (TF-IDF) and dense (embeddings) representations

---

## 📚 Phase 3: Neural Networks & Architecture (2-3 months | 200-300 hours)

**Neural Network Basics**

- [ ] Neural Networks, Hidden Layers
- [ ] Activation Functions (ReLU, sigmoid, tanh)
- [ ] Backpropagation (in depth)
- [ ] Gradient descent & optimization
- [ ] Epoch, Batch Size, Learning rate
- [ ] Dropout, Regularization techniques

**Deep Learning Architectures**

- [ ] Deep Learning fundamentals
- [ ] CNNs (Convolutional Neural Networks) - for images
- [ ] RNNs (Recurrent Neural Networks) - for sequences
- [ ] LSTMs (Long Short-Term Memory) - for long sequences
- [ ] Autoencoders - dimensionality reduction

**Attention & Transformers** 🌟

- [ ] Attention Mechanism - focusing on relevant parts
- [ ] Self-Attention - all tokens attend to each other
- [ ] Multi-Head Attention - multiple attention in parallel
- [ ] Transformer Architecture - the foundation of modern NLP
- [ ] Encoder-Decoder Architecture
- [ ] Positional Encoding

---

## Phase 4: LLMs & Modern AI 🚀

**Large Language Models**

- [ ] LLMs (Large Language Models) - GPT, Claude, LLaMA
- [ ] GPT (Generative Pre-trained Transformer)
- [ ] BERT (Bidirectional Encoder Representations)
- [ ] Foundation Models - pre-trained models
- [ ] Context Window - token limits
- [ ] Perplexity - model evaluation

**Working with LLMs**

- [ ] Prompt Engineering - crafting effective prompts
- [ ] Temperature - controlling randomness
- [ ] Few-Shot / One-Shot / Zero-Shot Learning
- [ ] In-Context Learning
- [ ] Chain-of-Thought (CoT) prompting
- [ ] Instruction Tuning

**Fine-tuning & Optimization**

- [ ] Transfer Learning
- [ ] Fine-tuning pre-trained models
- [ ] LoRA (Low-Rank Adaptation) - efficient fine-tuning
- [ ] Quantization - 4-bit, 8-bit model compression
- [ ] Distillation - creating smaller models
- [ ] RLHF (Reinforcement Learning from Human Feedback)

**RAG & Knowledge Systems**

- [ ] RAG (Retrieval Augmented Generation) 🔥
- [ ] Information Retrieval (IR)
- [ ] Semantic search with embeddings
- [ ] Combining retrieval + generation
- [ ] Knowledge Graphs

---

## Phase 5: Specialized Domains

**Natural Language Processing (NLP)**

- [ ] NLP fundamentals
- [ ] Named Entity Recognition (NER)
- [ ] Sentiment Classification
- [ ] Machine Translation (MT)
- [ ] Sequence‑to‑Sequence (Seq2Seq)
- [ ] Abstractive vs Extractive Summarisation
- [ ] Natural Language Generation (NLG)
- [ ] Chatbots & conversational AI

**Computer Vision (CV)**

- [ ] Computer Vision concepts
- [ ] CNN applications (classification, detection)
- [ ] Image embeddings (CLIP)
- [ ] Stable Diffusion - text-to-image
- [ ] Diffusion Models
- [ ] GANs (Generative Adversarial Networks)
- [ ] Multimodal AI - text + vision

**Advanced Topics**

- [ ] AI Agents - autonomous decision-making
- [ ] Mixture of Experts (MoE)
- [ ] Active Learning
- [ ] Recommender Systems
- [ ] Anomaly Detection
- [ ] Human in the Loop (HITL) systems

---

## Phase 6: ML Engineering & Production

**Model Evaluation**

- [ ] Accuracy, Precision, Recall, F1 Score
- [ ] Cross‑Validation
- [ ] Confusion Matrix
- [ ] BLEU, ROUGE (for generation tasks)

**Data Engineering**

- [ ] Data pipelines
- [ ] ETL (Extract, Transform, Load)
- [ ] Data versioning
- [ ] Batch vs streaming processing

**ML Tools & Libraries**

- [ ] NumPy - numerical computing
- [ ] Pandas - data manipulation
- [ ] Scikit‑Learn - classical ML
- [ ] PyTorch / TensorFlow / Keras - deep learning
- [ ] Hugging Face Transformers
- [ ] LangChain - LLM applications

**MLOps & Deployment**

- [ ] ML Pipelines (Kedro, Airflow)
- [ ] Model versioning & monitoring
- [ ] Cloud platforms (AWS SageMaker, Azure ML, GCP)
- [ ] API deployment (FastAPI, Flask)
- [ ] Model serving & inference optimization
- [ ] A/B testing

---

## Phase 7: Ethics, Safety & Advanced Concepts

**AI Safety & Alignment**

- [ ] Hallucination - factual accuracy issues
- [ ] Alignment - matching human values
- [ ] Constitutional AI
- [ ] Prompt Injection - security concerns
- [ ] Bias & fairness in AI
- [ ] Explainability & interpretability

**Model Types Comparison**

- [ ] Generative vs Discriminative models
- [ ] Supervised vs Unsupervised vs RL
- [ ] Rules‑Based vs ML-based systems
- [ ] Classical ML vs Deep Learning tradeoffs

---

## 📚 Learning Resources by Phase

**Phase 1-2 (Foundation + Embeddings):**

- [ ] Start with your current examples: `tiktoken_example.py`, `embeddings_intro.py`
- [ ] Practice: Create embeddings for different texts, compare similarities
- [ ] Build: Simple semantic search with your own documents

**Phase 3 (Neural Networks):**

- [ ] Implement: Simple neural network from scratch
- [ ] Study: 3Blue1Brown neural network series
- [ ] Practice: MNIST digit classification with PyTorch

**Phase 4 (LLMs):**

- [ ] Use: OpenAI API, Anthropic Claude, or local LLMs
- [ ] Build: RAG system with your own knowledge base
- [ ] Practice: Prompt engineering for different tasks

**Phase 5+ (Specialization):**

- [ ] Choose your focus: NLP, CV, or multimodal
- [ ] Build end-to-end projects
- [ ] Contribute to open source (Hugging Face, LangChain)

## 🤖 Microsoft Agent Frameworks & Courses

Microsoft offers a comprehensive ecosystem of AI/agent frameworks, educational courses, and development tools. This section provides a structured learning path through Microsoft's offerings.

### 🎓 Educational Courses & Tutorials

#### AI Agent Development

- [ ] **[AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** ⭐ 45k stars
  - 15-lesson curriculum covering agent fundamentals to production
  - Topics: Introduction to agents → Agent patterns → Production deployment
  - Hands-on examples with Python and practical implementations
  - 15.2k forks, 422 watchers - highly active community

#### Model Context Protocol (MCP)

- [ ] **[MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)** ⭐ 13.3k stars
  - 11 modules on Model Context Protocol
  - Emerging standard for AI-tool communication
  - Multi-language support: C#, Java, JavaScript, Python, Rust, TypeScript
  - 4.3k forks - growing adoption

#### IoT Development

- [ ] **[IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners)** ⭐ 16.6k stars
  - 24 lessons covering complete IoT development lifecycle
  - Topics: Sensors → Cloud integration → Production systems
  - Practical projects: Farm → Transport → Manufacturing → Retail → Consumer
  - 2.7k forks

#### Python Fundamentals

- [ ] **[Python for Beginners](https://github.com/microsoft/c9-python-getting-started)** ⭐ 7.9k stars
  - Channel 9 series with 3-course progression
  - Beginner-friendly introduction to Python programming
  - Foundation for ML/AI development

#### GitHub Copilot & AI-Assisted Development

- [ ] **[GitHub Copilot Tutorial](https://github.com/features/copilot)** - Comprehensive guide
  - **Mission Control**: Multi-step workflows in VS Code
  - **Agent Mode**: Autonomous coding with feedback loops
  - **Copilot CLI**: Terminal integration (`copilot explain`, `copilot fix tests`)
  - **Code Review**: Automated PR review with risk detection
  - **Coding Agent**: Async task handling with issue assignments
  - **Best Practices**: Review everything, prompt with context, small increments
  - **Prompt Patterns**: Specific examples for caching, CSV import, test generation

### � Microsoft Developer YouTube Playlists

**AI & Machine Learning Courses:**

- [ ] **[AI Agents for Beginners - Video Course](https://www.youtube.com/playlist?list=PLlrxD0HtieHgKcRjd5-8DT9TbwdlDO-OC)** - Complete video series
- [ ] **[MCP for Beginners - Video Course](https://www.youtube.com/playlist?list=PLlrxD0HtieHjYfVUpGl_-ai7D6FRBjV-d)** - Model Context Protocol
- [ ] **[Java and AI for Beginners](https://www.youtube.com/playlist?list=PLlrxD0HtieHglvVKJ79O3EFuF1kpaNDKk)** - AI with Java
- [ ] **[How Microsoft Engineers Build AI](https://www.youtube.com/playlist?list=PLlrxD0HtieHiXtHy_rJAjLHuBciGEW1Xs)** - Engineering practices
- [ ] **[AI Red Teaming 101](https://www.youtube.com/playlist?list=PLlrxD0HtieHhXnVUQM42aKRPrirbUIDdh)** - AI security testing
- [ ] **[Multimodality using Azure AI Content Understanding](https://www.youtube.com/playlist?list=PLlrxD0HtieHiy0w4peKmU-1eyMwFHd8UL)**

**Microsoft Build 2025 Sessions:**

- [ ] **[AI, Copilot & Agents | Build 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHg4OIwuQGsVgpQhTKl4fFdE)** - Latest AI announcements
- [ ] **[MCP at Build 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHgmDWDYPh5YmsnQAX9AihJv)** - MCP updates
- [ ] **[Data & Analytics | Build 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHhgw1Heysdf8_F0oWHXqoUj)** - Data platform
- [ ] **[Cloud Platform | Build 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHgukvOrEw3CqZuKtxiu_wnM)** - Azure updates
- [ ] **[Security | Build 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHjO0rYEHYT86Os9zvbaEM3v)** - Security best practices
- [ ] **[Developer Tools & .NET | Build 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHgzfZCDP1dYD-AvB7zrQ7O2)** - Developer tooling
- [ ] **[Windows | Build 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHg_i6-m--pwP3Xf4vpz2h8b)** - Windows development
- [ ] **[Demo Theatre Sessions | Build 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHh4Hi58Cj02JCD6H9WcBYZK)** - Live demos
- [ ] **[Microsoft Build 2025 - Full Conference](https://www.youtube.com/playlist?list=PLlrxD0HtieHgFYS4DKbJ_xCYNE94ZLJjj)** - All sessions

**Azure & Cloud Development:**

- [ ] **[Inside Azure AI Foundry](https://www.youtube.com/playlist?list=PLlrxD0HtieHj61bBwrAqd5yHvwjB8s_oz)** - Azure AI platform
- [ ] **[Python on Azure](https://www.youtube.com/playlist?list=PLlrxD0HtieHhdAox_GWvRO7phbPRcILRm)** - Python cloud development
- [ ] **[Azure Database for PostgreSQL](https://www.youtube.com/playlist?list=PLlrxD0HtieHitWlq3erWOoxH5XFkI9mtO)** - Database talks
- [ ] **[POSETTE: Postgres 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHjHHYfXx3llOlESrX1IpJro)** - PostgreSQL event

**Developer Community & Events:**

- [ ] **[MCP Dev Days](https://www.youtube.com/playlist?list=PLlrxD0HtieHgcpcE1DqEM3glmk02RJmzV)** - MCP community event
- [ ] **[Context Window](https://www.youtube.com/playlist?list=PLlrxD0HtieHgbm7PGBQQvOEMqAl1Wgu0n)** - Developer discussions
- [ ] **[PyCon 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHhgNpHEBAg58PG2nBMUIsd7)** - Python conference
- [ ] **[MVPs at Build 2025](https://www.youtube.com/playlist?list=PLlrxD0HtieHhKeaQDpBLbskrDDxq8IjuO)** - MVP insights
- [ ] **[Sharp and Unfiltered](https://www.youtube.com/playlist?list=PLlrxD0HtieHh7wwfLMFV19aXy0VtWobIS)** - C# discussions

**Security & Best Practices:**

- [ ] **[Developer Security Quick-Fire Questions](https://www.youtube.com/playlist?list=PLlrxD0HtieHhS0duvF68agcio7edpL882)** - Security Q&A
- [ ] **[Talking Security with Michael Howard](https://www.youtube.com/playlist?list=PLlrxD0HtieHiw2hOnceQHt1OEQjmk8zzC)** - Security deep dives

### �🔧 Agent Frameworks & Tools

#### Core Agent Frameworks

- [ ] **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)** ⭐ 5.1k stars
  - Core offering for building AI agents
  - Python and .NET support
  - Layered API design: Core API → AgentChat API → Extensions
  - Production-ready architecture

- [ ] **[Agent Lightning](https://github.com/microsoft/agent-lightning)** ⭐ 8.5k stars
  - RL training framework for any agent
  - Works with minimal code changes
  - Enables reinforcement learning without framework lock-in

- [ ] **[AutoGen](https://github.com/microsoft/autogen)** ⭐ 51.7k stars (Legacy/Maintained)
  - Multi-agent framework (original Microsoft offering)
  - Now directing users to Microsoft Agent Framework
  - Still maintained but considered legacy
  - Large community and extensive examples

#### Prompt Engineering & Orchestration

- [ ] **[POML (Prompt Orchestration Markup Language)](https://github.com/microsoft/poml)** ⭐ 4.7k stars
  - Markup language for prompt engineering
  - HTML-like syntax for structured prompts
  - VS Code extension available
  - Declarative approach to prompt design

- [ ] **[GenAIScript](https://github.com/microsoft/genaiscript)** ⭐ 2.8k stars
  - JavaScript/TypeScript framework for programmatic prompt assembly
  - Compose prompts with code logic
  - Integrate with existing workflows
  - Type-safe prompt construction

#### AI Development & Testing Tools

- [ ] **[PromptBench](https://github.com/microsoft/promptbench)** ⭐ 2.7k stars
  - Python library for LLM evaluation and benchmarking
  - Adversarial testing capabilities
  - Dynamic evaluation frameworks
  - Performance metrics and analysis

- [ ] **[Intelligence Toolkit](https://github.com/microsoft/intelligence-toolkit)** ⭐ 94 stars
  - Interactive workflows for AI intelligence reports
  - Case/entity/text intelligence analysis
  - Data-driven insights generation
  - Production intelligence workflows

#### Development Environment & Tools

- [ ] **[VS Code Tools for AI](https://github.com/microsoft/vscode-tools-for-ai)** ⭐ 340 stars
  - Azure ML VS Code extension
  - Build, train, and deploy ML models
  - Integrated development experience
  - Azure Machine Learning integration

### 📚 Learning Path Recommendations

#### Beginner Path (Start Here)

1. [ ] **Python for Beginners** - Get comfortable with Python
2. [ ] **AI Agents for Beginners** - Learn agent fundamentals (Lessons 1-5)
3. [ ] **GitHub Copilot Tutorial** - Familiarize with AI-assisted coding
4. [ ] **MCP for Beginners** - Understand the protocol standard (Modules 1-3)

#### Intermediate Path

1. [ ] **AI Agents for Beginners** - Complete remaining lessons (6-15)
2. [ ] **Microsoft Agent Framework** - Build your first agent
3. [ ] **GenAIScript** or **POML** - Choose your prompt engineering approach
4. [ ] **PromptBench** - Test and evaluate your models

#### Advanced Path

1. [ ] **Agent Lightning** - Add RL capabilities to agents
2. [ ] **AutoGen** (optional) - Explore multi-agent patterns
3. [ ] **Intelligence Toolkit** - Production intelligence workflows
4. [ ] **MCP for Beginners** - Complete advanced modules (8-11)

---

## ☁️ AWS Machine Learning & Certification Resources

Comprehensive resources for AWS SageMaker, ML services, and AWS Certified Machine Learning Specialty certification.

### 📺 AWS SageMaker Video Series

#### Emily Weber's Deep Dive Series

- [ ] **[Emily Weber's Deep Dive Series on AWS SageMaker](https://www.youtube.com/playlist?list=PLhr1KZpdzukcOr_6j_zmSrvYnLUtgqsZz)** - Complete playlist
- [ ] [SageMaker Inference](https://youtu.be/bRUNpuRGeZc?si=E2Epj7oWNIfSD5OF)
- [ ] [SageMaker Studio](https://youtu.be/stB-F6jswno?si=MzCMmfDgoUNKMUej)
- [ ] [Overview of in-built ML algorithms](https://youtu.be/Y8FzvaQBS6s?si=qwCSp3ELOGnc9ZsH)
- [ ] [SageMaker Hyperparameter Tuning](https://youtu.be/i2-M7x9dJXQ?si=KzkdPFjSeVf0K5A_)
- [ ] [ML Governance](https://youtu.be/3lHTZHk7hDE?si=gK-inZTKkCbntR24)
- [ ] [SageMaker Data Wrangler](https://youtu.be/Slq3i8EeRXI?si=PMpuJx-LQrkv6ZCe)
- [ ] [SageMaker Autopilot](https://youtu.be/9pwYlb1Kit0?si=Ou221ojn7tC3QCf4)
- [ ] [SageMaker FeatureStore](https://youtu.be/kgI0Rwn41S0?si=RlgU51_XyaO7nxaJ)
- [ ] [SageMaker Experiments](https://youtu.be/kK1ohrpJFC0?si=FZua46-4KyixQnux)
- [ ] [How VPC works](https://youtu.be/2doSoMN2xvI?si=M8-1At1FU0gC6mkW)
- [ ] [Security and compliance in SageMaker](https://youtu.be/HlSEUvApDZE?si=Ma2jZctl3prxEYIQ)

#### MLOps & Best Practices

- [x] [MLOps 2022](https://youtu.be/UnAN35gu3Rw?si=AJH5ZOShRn71jeet)
- [ ] [MLOps 2023](https://www.youtube.com/watch?v=2kzJPhgDkDE)

### 📚 AWS YouTube Channels

- [ ] [AWS Official Channel](https://www.youtube.com/@amazonwebservices)
- [ ] [Be a Better Dev](https://www.youtube.com/@BeABetterDev)
- [ ] [AWS with Chetan](https://www.youtube.com/@AWSwithChetan)
- [ ] [Julien Simon](https://www.youtube.com/@juliensimonfr)
- [ ] [Data Science Garage](https://www.youtube.com/@DataScienceGarage)
- [ ] [Travis Media](https://www.youtube.com/@TravisMedia)
- [ ] [AWS This Is My Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)
  - [Playlist](https://www.youtube.com/playlist?list=PLhr1KZpdzukdeX8mQ2qO73bg6UKQHYsHb)

### 📺 AWS Official YouTube Playlists

#### Latest Announcements & AI Services

- [ ] [Just Announced](https://www.youtube.com/playlist?list=PLhr1KZpdzukcqC4WBSssSqrQXDjAUMCp5) - Latest AWS product launches (Amazon Quick Suite, QuickSight, Quick Research, Quick Flows, Quick Automate)
- [ ] [Exploring AWS AI Services](https://www.youtube.com/playlist?list=PLhr1KZpdzukdNS_OcR8CF2BUsS5CnCNGs) - Amazon Quick Suite, SageMaker HyperPod, SageMaker AI, Amazon Q Business, Nova Multimodal Models, Nova Reel video generation

#### Getting Started & Fundamentals

- [ ] [Getting Started with AWS](https://www.youtube.com/playlist?list=PLhr1KZpdzukf4p57gUnTyToXYJxGAPx03) - What is AWS?, Cloud Computing basics, Free Tier program, Global Infrastructure, Skills Guild training

#### Core AWS Services

- [ ] [AWS Cloud Storage](https://www.youtube.com/playlist?list=PLhr1KZpdzukdcp4VEgsSKVUPH3OizmeRa) - Storage solutions (S3, EBS, EFS)
- [ ] [AWS Databases](https://www.youtube.com/playlist?list=PLhr1KZpdzukc7S4YkuWujjSBmyLofNwPz) - Database services (RDS, DynamoDB, Aurora)
- [ ] [AWS Compute](https://www.youtube.com/playlist?list=PLhr1KZpdzukduV91ar4X6hPU80Ubkwe0T) - Compute services (EC2, Lambda, ECS)
- [ ] [AWS Cloud Security](https://www.youtube.com/playlist?list=PLhr1KZpdzukebFY9fWXIFdWIM3mrjkdW0) - Security best practices and IAM
- [ ] [Application Integration on AWS](https://www.youtube.com/playlist?list=PLhr1KZpdzukd7OwXdKMbbXWWfmcEKy9t6) - Integration patterns (SQS, SNS, EventBridge)

#### Learning & Support

- [ ] [Latest AWS Tutorials](https://www.youtube.com/playlist?list=PLhr1KZpdzukcONwoeZOK3oCZiOngt4-o4) - Technical demos and walkthroughs (SES, IoT, various AWS services)
- [ ] [AWS Knowledge Center Videos](https://www.youtube.com/playlist?list=PLhr1KZpdzukfdjsOHZ-BazZt1iK1J8UUw) - Short troubleshooting videos for common AWS problems (SageMaker, Aurora, Athena, DMS)
- [ ] [Latest AWS Podcasts](https://www.youtube.com/playlist?list=PLhr1KZpdzukfFtjuF85ydw0r-qlnLFkM9) - AWS for AI Podcast, Amazon Q Podcast, Agentic AI discussions, customer stories

#### Customer Stories & Real-World Use Cases

- [ ] [AWS Customer Success Stories](https://www.youtube.com/playlist?list=PLFC4DF7286B2419F9) - How companies use AWS (Deloitte, Rackspace, Trend Micro, U.S. Bank, Videoamp)

**Pro Tip:** Start with "Getting Started with AWS" for foundational knowledge, then explore "Exploring AWS AI Services" for ML/AI focus. The Knowledge Center Videos are invaluable for troubleshooting specific SageMaker and other service issues during hands-on practice.

### � Google Cloud AI/ML YouTube Playlists

#### Google Cloud Tech - AI & ML Focus

- [ ] [Building an AI tutor with Memory on ADK](https://www.youtube.com/playlist?list=PLIivdWyY5sqK9XkA-jfNcylZzLnxh6d2T) - Building AI applications with memory capabilities
- [ ] [Cloud Next 2025](https://www.youtube.com/playlist?list=PLIivdWyY5sqK9-Va4chd7r9R6WMpPHTVQ) - Latest announcements and innovations
- [ ] [Google AI Studio: From Prompt to Prototype](https://www.youtube.com/playlist?list=PLIivdWyY5sqIagw3_50GeVHIwcUoOwTa7) - Complete course on AI Studio
- [ ] [The Agent Factory](https://www.youtube.com/playlist?list=PLIivdWyY5sqLXR1eSkiM5bE6pFlXC-OSs) - Building AI agents
- [ ] [Cloud at Google I/O 2025](https://www.youtube.com/playlist?list=PLIivdWyY5sqKKhwKTKZHKyAmsEwr2OHR0) - Google I/O cloud & AI sessions
- [ ] [Gemini Cloud Assist](https://www.youtube.com/playlist?list=PLIivdWyY5sqJz-AILC4SR4WslySHm4lnh) - Using Gemini for cloud development
- [ ] [Generative AI Experiences for Developers](https://www.youtube.com/playlist?list=PLIivdWyY5sqL9GfauU_6pEZPnBIPPUez8) - Building with generative AI
- [ ] [AI Guide for Cloud Developers](https://www.youtube.com/playlist?list=PLIivdWyY5sqJio2yeg1dlfILOUO2FoFRx) - Comprehensive AI development guide
- [ ] [Google Cloud: Building with Hugging Face](https://www.youtube.com/playlist?list=PLIivdWyY5sqIwEOfjCSVl87ND7Rn3m1Fd) - Integrating Hugging Face models
- [ ] [Real Terms for AI](https://www.youtube.com/playlist?list=PLIivdWyY5sqLvGdVLJZh2EMax97_T-OIB) - AI terminology explained
- [ ] [Google Cloud Data Analytics Certificate](https://www.youtube.com/playlist?list=PLIivdWyY5sqJCaLucJ4ey9hL3LkQEsd4m) - Data analytics fundamentals
- [ ] [Google Cloud Tech at Google I/O 2024](https://www.youtube.com/playlist?list=PLIivdWyY5sqKE4sZedjigeO11mEzuuRWq) - Previous year's I/O sessions
- [ ] [Google Cloud Next 2024](https://www.youtube.com/playlist?list=PLIivdWyY5sqLHU6fh9ozZ7mxsj7GcPjRF) - Cloud Next 2024 sessions
- [ ] [Generative AI for Developers](https://www.youtube.com/playlist?list=PLIivdWyY5sqLRCzKJyixrIDPQKwU6XHpn) - Developer-focused gen AI content
- [ ] [Deploying AI](https://www.youtube.com/playlist?list=PLIivdWyY5sqLVnGp10d9tQacZsvVh2_zM) - Production AI deployment

#### Google Cloud - AI & ML Focus

- [ ] [AI for Startups: A Comprehensive Guide](https://www.youtube.com/playlist?list=PLBgogxgQVM9vYmseCf6mVKpt3qQ_EqQ8w) - AI implementation for startups
- [ ] [Google's AI Builders Forum 2025](https://www.youtube.com/playlist?list=PLBgogxgQVM9siibI9EyxcnVUD59cRh86H) - AI Builders community sessions
- [ ] [Model Armor: Securing AI Deployments](https://www.youtube.com/playlist?list=PLBgogxgQVM9s34an_v57QwxuyZHVv7grt) - AI security best practices
- [ ] [Become a Gen AI Leader!](https://www.youtube.com/playlist?list=PLBgogxgQVM9sYOdfEVGux1sbOqbLm1Mxz) - Leadership in generative AI
- [ ] [Gen AI Success Stories](https://www.youtube.com/playlist?list=PLBgogxgQVM9sXs7khA1lc8xWSx6CkQQRe) - Real-world generative AI implementations
- [ ] [Next '25 Keynote demos](https://www.youtube.com/playlist?list=PLBgogxgQVM9uBYqU3tH3MS2yBcQ8imAaZ) - Latest product demos

#### Google DeepMind - Research & Learning

- [ ] [Gemini 2.5 demos](https://www.youtube.com/playlist?list=PLqYmG7hTraZCFhSuoJc5w_zQWkzOPCTyc) - Creating complex code with single prompts
- [ ] [Gemini Robotics 1.5](https://www.youtube.com/playlist?list=PLqYmG7hTraZD65Oohj7Ujq1D-vtsurG08) - Latest robotics capabilities
- [ ] [Gemini Robotics](https://www.youtube.com/playlist?list=PLqYmG7hTraZC4Mx6pEKr6FVJehafA7vWE) - Core robotics demonstrations
- [ ] [Gemini 2.0: Agentic AI](https://www.youtube.com/playlist?list=PLqYmG7hTraZD8qyQmEfXrJMpGsQKk-LCY) - New AI model for agents
- [ ] [Veo 2: Video Generation](https://www.youtube.com/playlist?list=PLqYmG7hTraZC__kUbiDqBsRxtX_urLkcn) - State-of-the-art video generation
- [ ] [Veo: Video Generation Model](https://www.youtube.com/playlist?list=PLqYmG7hTraZAwi0L13zfmM_r20Xps15xR) - Video generation fundamentals
- [ ] [Project Astra](https://www.youtube.com/playlist?list=PLqYmG7hTraZBNoGqfQoE-tjWpUd1G6XYB) - Advanced AI assistant
- [ ] [AI for Science Forum](https://www.youtube.com/playlist?list=PLqYmG7hTraZBwZQwCxzIlsyFxC3WKH_Ii) - Royal Society x DeepMind
- [ ] [The story of AlphaFold](https://www.youtube.com/playlist?list=PLqYmG7hTraZAhkAh72kzzLC4r2O4VoVgz) - Protein folding breakthrough
- [ ] [Learning resources](https://www.youtube.com/playlist?list=PLqYmG7hTraZCRwoyGxvQkqVrZgDQi4m-5) - General AI/ML learning
- [ ] [Talks | AI for science](https://www.youtube.com/playlist?list=PLqYmG7hTraZB664MPwgI4Yv-wbdvkLzGw) - Scientific applications of AI
- [ ] [DeepMind x UCL | Deep Learning 2021](https://www.youtube.com/playlist?list=PLqYmG7hTraZDVH599EItlEWsUOsJbAodm) - Latest DL lecture series
- [ ] [DeepMind x UCL | Deep Learning 2020](https://www.youtube.com/playlist?list=PLqYmG7hTraZCDxZ44o4p3N5Anz3lLRVZF) - Deep learning fundamentals
- [ ] [DeepMind x UCL | RL Course 2018](https://www.youtube.com/playlist?list=PLqYmG7hTraZBKeNJ-JE_eyJHZ7XgBoAyb) - Reinforcement learning course
- [ ] [DeepMind x UCL | Deep Learning 2018](https://www.youtube.com/playlist?list=PLqYmG7hTraZCkftCvihsG2eCTH2OyGScc) - 2018 lecture series
- [ ] [DeepMind x UCL | RL 2015](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ) - Introduction to RL (David Silver)
- [ ] [Talks](https://www.youtube.com/playlist?list=PLqYmG7hTraZC9yNDSlv0_1ctNaG1WKuIx) - Research talks and presentations
- [ ] [Research](https://www.youtube.com/playlist?list=PLqYmG7hTraZDbUxknZhkFYIS685TUW5Wc) - Latest research updates
- [ ] [Google DeepMind: The Podcast](https://www.youtube.com/playlist?list=PLqYmG7hTraZBiUr6_Qf8YTS2Oqy3OGZEj) - In-depth discussions
- [ ] [The story of AlphaGo](https://www.youtube.com/playlist?list=PLqYmG7hTraZBy7J_4ynYPc0Ml1RUGcLmD) - Historic Go AI breakthrough

**Pro Tip:** Start with DeepMind x UCL courses for theory (Deep Learning 2021, RL 2018). For practical Google Cloud AI, follow "AI Guide for Cloud Developers" and "Generative AI for Developers". DeepMind's research playlists (Gemini, AlphaFold) showcase cutting-edge capabilities.

### 📺 OpenAI YouTube Playlists

#### Latest Models & Announcements

- [ ] [DevDay 2025](https://www.youtube.com/playlist?list=PLOXw6I10VTv8-mTZk0v7oy1Bxfo3D2K5o) - Latest OpenAI DevDay announcements
- [ ] [Introducing GPT-5](https://www.youtube.com/playlist?list=PLOXw6I10VTv9tIp5Oh-RT_Gz8yE5iz799) - GPT-5 model release
- [ ] [Introducing ChatGPT agent](https://www.youtube.com/playlist?list=PLOXw6I10VTv_9xLWUFMRDL6DWwVRg0Ts7) - ChatGPT agent capabilities
- [ ] [Introducing OpenAI o1](https://www.youtube.com/playlist?list=PLOXw6I10VTv_T9QV-DKXhq7HFUQRkGQLI) - o1 reasoning model
- [ ] [Introducing GPT-4o](https://www.youtube.com/playlist?list=PLOXw6I10VTv8VOvPNVQ8c4D4NyMRMotXh) - GPT-4o multimodal model
- [ ] [Introducing 4o Image Generation](https://www.youtube.com/playlist?list=PLOXw6I10VTv8aE6_cu4b9J_VaraH1kYMo) - Image generation with 4o
- [ ] [12 Days of OpenAI](https://www.youtube.com/playlist?list=PLOXw6I10VTv9lin5AzsHAHCTrC7BdVdEM) - Product announcements series
- [ ] [OpenAI DevDay 2024](https://www.youtube.com/playlist?list=PLOXw6I10VTv_o0ZLpFu2IQyQOho1l-v7y) - Previous DevDay sessions

#### Sora (Video Generation)

- [ ] [This is Sora 2.](https://www.youtube.com/playlist?list=PLOXw6I10VTv8scMJVOydXK4kfd2k4p-yl) - Sora 2.0 capabilities
- [ ] [Sora](https://www.youtube.com/playlist?list=PLOXw6I10VTv9z1fIBypnJB_iZuqCKrX3P) - Original Sora demos
- [ ] [Sora Tutorials](https://www.youtube.com/playlist?list=PLOXw6I10VTv8q5PPOsuECYDFqohnJqbYB) - How to use Sora
- [ ] [Sora Fellows Tutorials](https://www.youtube.com/playlist?list=PLOXw6I10VTv_GLpoVPTpbXQf2LS8PTztP) - Advanced Sora techniques

#### ChatGPT & Features

- [ ] [ChatGPT Atlas](https://www.youtube.com/playlist?list=PLOXw6I10VTv-QP2Bd0heMM48S5okc0glG) - ChatGPT capabilities overview
- [ ] [With ChatGPT](https://www.youtube.com/playlist?list=PLOXw6I10VTv_T8_5Ogpg6X08zBxSteZVJ) - Using ChatGPT effectively
- [ ] [ChatGPT Features](https://www.youtube.com/playlist?list=PLOXw6I10VTv9AIB10rnngD1XYN76xHuzV) - Feature demonstrations

#### Developer Resources

- [ ] [OpenAI Build Hours](https://www.youtube.com/playlist?list=PLOXw6I10VTv9zUbhqqaT62O9AFjlndmjn) - Live coding sessions
- [ ] [Codex Tutorials](https://www.youtube.com/playlist?list=PLOXw6I10VTv-ZkTjAFQx8P3i4QurANKyG) - Codex programming tutorials
- [ ] [Introducing Codex](https://www.youtube.com/playlist?list=PLOXw6I10VTv-IwPfAPgK9F2YQOcgr1N8s) - Codex model introduction
- [ ] [OpenAI for Business](https://www.youtube.com/playlist?list=PLOXw6I10VTv9x2ibdc5Iu7HQlhnibqYZm) - Enterprise use cases

#### Community & Learning

- [ ] [Community Creations: OpenAI o1](https://www.youtube.com/playlist?list=PLOXw6I10VTv8CRYkTeeeL1M4_9BRJ1X0c) - User-created o1 applications
- [ ] [OpenAI on OpenAI](https://www.youtube.com/playlist?list=PLOXw6I10VTv90Fvo0IAS1OWFw9moK6TRX) - Inside OpenAI discussions
- [ ] [The OpenAI Podcast](https://www.youtube.com/playlist?list=PLOXw6I10VTv9GAOCZjUAAkSVyW2cDXs4u) - In-depth conversations
- [ ] [Customer Stories](https://www.youtube.com/playlist?list=PLOXw6I10VTv_nRb6Cn0fxfuem0N9J30lR) - Real-world implementations
- [ ] [Events and Talks](https://www.youtube.com/playlist?list=PLOXw6I10VTv9DFXRidukLC2hgAAkmexWx) - Conferences and presentations
- [ ] [Research Releases](https://www.youtube.com/playlist?list=PLOXw6I10VTv8QSr-BMwe2RNICiF_E-5Ls) - Latest research papers

**Pro Tip:** Start with "Introducing GPT-4o" and "Introducing OpenAI o1" to understand latest models. "OpenAI Build Hours" provides hands-on coding experience. For video generation, explore "Sora Tutorials". The "12 Days of OpenAI" series showcases rapid innovation pace.

### Meta Open Source YouTube Playlists

#### AI & Machine Learning

- [ ] [AI & ML at Meta Open Source](https://www.youtube.com/playlist?list=PLzIwronG0sE5I0BQJfkww6sllGzre_eJ0) - Meta's AI/ML projects and tools
- [ ] [The Diff Podcast](https://www.youtube.com/playlist?list=PLzIwronG0sE6471XKz0-mcVHg-ikzZxHa) - Tech discussions and innovations

#### Project Aria - Egocentric AI & AR Research

- [ ] [Project Aria at ICCV 2025](https://www.youtube.com/playlist?list=PLzIwronG0sE7TzMH2vHNiR4PkrJVzRlff) - Hands-on egocentric research tutorial
- [ ] [Project Aria at CVPR 2025 - 3D Digital Twin Workshop](https://www.youtube.com/playlist?list=PLzIwronG0sE5PTbSdi6Er7ppAXB3dB14i) - Progress and future directions
- [ ] [Project Aria CVPR 2025 - EgoVis Workshop](https://www.youtube.com/playlist?list=PLzIwronG0sE4Isbg2UFpXI70H4K43mazj) - Egocentric vision research
- [ ] [Project Aria CVPR 2024 Tutorials](https://www.youtube.com/playlist?list=PLzIwronG0sE5i556l6na7wNBRqeMKHgZw) - Latest tutorials
- [ ] [Project Aria at ECCV 2024](https://www.youtube.com/playlist?list=PLzIwronG0sE6cfevS3757zknk3ewiJBMy) - European computer vision conference
- [ ] [Project Aria CVPR 2023 Tutorials](https://www.youtube.com/playlist?list=PLzIwronG0sE4jYwmSTZaAhkkqdydHULqc) - Foundational tutorials
- [ ] [Project Aria CVPR 2022 Tutorials](https://www.youtube.com/playlist?list=PLzIwronG0sE4cem9otDv_fEHXeWk0oL3f) - Initial tutorials
- [ ] [Project Aria Research Kit](https://www.youtube.com/playlist?list=PLzIwronG0sE45VbKpv3ENn633B1Sd-Yo2) - Research toolkit overview

#### AR/VR & Data

- [ ] [AR & VR at Meta Open Source](https://www.youtube.com/playlist?list=PLzIwronG0sE4Ooku7Nvlpd4locUZAHzjb) - Augmented and virtual reality projects
- [ ] [Data at Meta Open Source](https://www.youtube.com/playlist?list=PLzIwronG0sE6TLHbTxxAeEzU9UEZSKv1W) - Data infrastructure and tools

**Pro Tip:** Start with "AI & ML at Meta Open Source" for overview of Meta's AI ecosystem. Project Aria playlists are excellent for cutting-edge egocentric AI research and AR/VR development. Follow the chronological CVPR/ICCV tutorials (2022→2025) to see research evolution. "The Diff Podcast" provides insights into engineering culture at Meta.

### IBM Technology YouTube Playlists

#### AI & Machine Learning

- [ ] [AI Technical Tutorials](https://www.youtube.com/playlist?list=PLOspHqNVtKACI0uR7Oa-bkWbtTufpJNhi) - Hands-on AI tutorials
- [ ] [AI in Action](https://www.youtube.com/playlist?list=PLOspHqNVtKADcG4vf83D97cKUrs5WdXXR) - Real-world AI implementations
- [ ] [Understanding AI Models](https://www.youtube.com/playlist?list=PLOspHqNVtKAC-FUNMq8qjYVw6_semZHw0) - Deep dive into AI model architectures
- [ ] [Large Language Models and Chatbots](https://www.youtube.com/playlist?list=PLOspHqNVtKAAsiohuZj1Bt4XpA3_bkS3c) - LLMs and conversational AI
- [ ] [Mixture of Experts](https://www.youtube.com/playlist?list=PLOspHqNVtKADvnJYHm3HButDlWykOTzlP) - MoE model architecture
- [ ] [AI Academy](https://www.youtube.com/playlist?list=PLOspHqNVtKACJx_ue2EXC1MerohY_lLKO) - Comprehensive AI learning path
- [ ] [AI Ethics and Governance](https://www.youtube.com/playlist?list=PLOspHqNVtKABEKVgWGrf6_x6OQYnYnCiM) - Responsible AI practices

#### Data Science & Engineering

- [ ] [Data and AI](https://www.youtube.com/playlist?list=PLOspHqNVtKABpPMnwkx27tEO2KOBvHLu6) - Data-driven AI solutions
- [ ] [Data Management](https://www.youtube.com/playlist?list=PLOspHqNVtKAD74tcRKW9FhETyKSaKxl3J) - Data architecture and management
- [ ] [Data Fabric](https://www.youtube.com/playlist?list=PLOspHqNVtKABIVwvKy4xY0lz0FUPnH1JD) - Modern data architecture
- [ ] [Data Lake Essentials](https://www.youtube.com/playlist?list=PLOspHqNVtKADA_xaKgpekj_bgqsC58VXm) - Data lake concepts and practices

#### AI Operations & Automation

- [ ] [DevOps: AiOps, Application Health and Observability](https://www.youtube.com/playlist?list=PLOspHqNVtKAA75RfVxm-CLdARe0VpBwbx) - AI for IT operations
- [ ] [Making Work Easier with Digital Workers](https://www.youtube.com/playlist?list=PLOspHqNVtKAA8MySFyyqtw6bG3npTTcYn) - AI automation and RPA

#### Advanced Computing

- [ ] [Quantum Computing Essentials](https://www.youtube.com/playlist?list=PLOspHqNVtKADPNAxbcP2u6CPzD1g_bBhe) - Quantum computing fundamentals

#### Podcasts & Talks

- [ ] [Smart Talks with IBM](https://www.youtube.com/playlist?list=PLOspHqNVtKAC0-KCayX4_nEfSjE8VhbZx) - Expert discussions on tech trends

**Pro Tip:** Start with "AI Academy" for structured learning, then dive into "AI Technical Tutorials" for hands-on practice. "Understanding AI Models" and "Large Language Models and Chatbots" provide essential theory. For enterprise AI, explore "AI in Action" and "Data and AI". IBM's watsonx platform integration is covered across multiple playlists. "AI Ethics and Governance" is crucial for responsible AI development.

### 3Blue1Brown YouTube Playlists

#### Essential Mathematics for AI/ML

- [ ] [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) - Complete linear algebra fundamentals with visual intuition
- [ ] [Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) - Calculus concepts explained visually
- [ ] [Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) - Deep learning fundamentals from scratch
- [ ] [Differential Equations](https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6) - Understanding differential equations

#### Probability & Statistics

- [ ] [Probabilities of Probabilities](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjmo3Y6ADm0ScWAlEXf-fp) - Bayesian thinking and probability
- [ ] [Central Limit Theorem](https://www.youtube.com/playlist?list=PLZHQObOWTQDOMxJDswBaLu8xBMKxSTvg8) - Statistical foundations

#### Applied Mathematics & Computing

- [ ] [Selected Lectures on Computational Thinking for MIT 18.S191](https://www.youtube.com/playlist?list=PLZHQObOWTQDMp_VZelDYjka8tnXNpXhzJ) - Computational thinking with Julia
- [ ] [Binary, Hanoi and Sierpinski](https://www.youtube.com/playlist?list=PLZHQObOWTQDMRtm8h9bG9P06WINNoBnCR) - Computer science foundations
- [ ] [Explainers](https://www.youtube.com/playlist?list=PLZHQObOWTQDN52m7Y21ePrTbvXkPaWVSg) - Mathematical concepts explained

#### Mathematical Puzzles & Applications

- [ ] [Lockdown Math](https://www.youtube.com/playlist?list=PLZHQObOWTQDP5CVelJJ1bNDouqrAhVPev) - Interesting mathematical problems
- [ ] [Puzzles with Beautiful Solutions](https://www.youtube.com/playlist?list=PLZHQObOWTQDPSKntUcMArGheySM4gL7wS) - Creative problem solving
- [ ] [The Block Collision Puzzle](https://www.youtube.com/playlist?list=PLZHQObOWTQDMalCO_AXOC5GWsuY8bOC_Y) - Physics meets mathematics
- [ ] [Physics](https://www.youtube.com/playlist?list=PLZHQObOWTQDPHLHBuY0nPbAQ_WGEjtzLW) - Mathematical physics concepts

**Pro Tip:** Start with "Essence of Linear Algebra" and "Essence of Calculus" - these are ESSENTIAL foundations for understanding machine learning mathematics. The "Neural Networks" series provides one of the best visual explanations of backpropagation and gradient descent. "Probabilities of Probabilities" is excellent for understanding Bayesian ML. Grant Sanderson's visual approach makes complex mathematical concepts intuitive - these playlists are highly recommended for building deep mathematical understanding required for AI/ML work.

### Weights & Biases YouTube Playlists

#### LLM & Generative AI Courses

- [ ] [Training & Fine-Tuning LLMs Course](https://www.youtube.com/playlist?list=PLD80i8An1OEGqqXeNZ5w0IBmeZcxpZEYL) - Complete LLM training and fine-tuning
- [ ] [Building LLM-Powered Apps Course](https://www.youtube.com/playlist?list=PLD80i8An1OEFSltPIrg4jMVAoivNuAP3a) - Production LLM applications
- [ ] [RAG++ Course: From POC to Production](https://www.youtube.com/playlist?list=PLD80i8An1OEEOpalEVeFKAM09ESgxZ6Cz) - Advanced RAG techniques
- [ ] [GPT-3 Series](https://www.youtube.com/playlist?list=PLD80i8An1OEFLiKHEITMT6M3xDEMqDdpI) - GPT-3 deep dive

#### MLOps & Production ML

- [ ] [MLOps Course](https://www.youtube.com/playlist?list=PLD80i8An1OEGTHqzwta0SUGxjpGfo_Qzv) - Complete MLOps practices
- [ ] [Model CI/CD Course](https://www.youtube.com/playlist?list=PLD80i8An1OEGECFPgY-HPCNjXgGu-qGO6) - Continuous integration for ML models
- [ ] [Model Management](https://www.youtube.com/playlist?list=PLD80i8An1OEEZmp1xuibzXg5HO4ZgIO1l) - ML model lifecycle management
- [ ] [W&B 101](https://www.youtube.com/playlist?list=PLD80i8An1OEEgxMpH-SOdBCjWpT5Io5rJ) - Getting started with Weights & Biases

#### Deep Learning Frameworks

- [ ] [PyTorch Study Group](https://www.youtube.com/playlist?list=PLD80i8An1OEGuvT8YQvLjM6ohQr78v9Lc) - PyTorch fundamentals and advanced topics
- [ ] [JAX Course](https://www.youtube.com/playlist?list=PLD80i8An1OEFy7Yrw8Q8VgG0vpWbd_LLu) - JAX for machine learning
- [ ] [Keras Reading Group](https://www.youtube.com/playlist?list=PLD80i8An1OEEb4yvP_wDZDfxV9Ok8pmbX) - Keras deep dives
- [ ] [W&B Study Group: fastai x Hugging Face](https://www.youtube.com/playlist?list=PLD80i8An1OEF8UOb9N9uSoidOGIMKW96t) - fastai and Hugging Face integration

#### Reinforcement Learning & Advanced Topics

- [ ] [Proximal Policy Optimization (PPO) Implementation Deep Dive](https://www.youtube.com/playlist?list=PLD80i8An1OEHhcxclwq8jOMam0m0M9dQ_) - PPO algorithm implementation
- [ ] [Minibatch Learning](https://www.youtube.com/playlist?list=PLD80i8An1OEHVSxnNEORssIEHeiC4C6mT) - Efficient training techniques

#### ML Community & Competitions

- [ ] [Chai Time Kaggle Talks](https://www.youtube.com/playlist?list=PLD80i8An1OEH8yrp_Ii0i3HxrVIHhRz2s) - Kaggle competitions and discussions
- [ ] [NeurIPS Hacker Cup AI Live Lecture Series](https://www.youtube.com/playlist?list=PLD80i8An1OEH3hjuc2qkyU7XhaaiNOCh5) - NeurIPS competition lectures

**Pro Tip:** Start with "W&B 101" to understand experiment tracking, then move to "MLOps Course" for production best practices. The "Training & Fine-Tuning LLMs Course" is excellent for modern LLM work. "Building LLM-Powered Apps" and "RAG++ Course" cover practical production scenarios. "PyTorch Study Group" provides deep framework knowledge. Weights & Biases focuses on production ML and MLOps - essential for real-world deployment.

### freeCodeCamp YouTube Playlists

#### Machine Learning & AI

- [ ] [Machine Learning](https://www.youtube.com/playlist?list=PLWKjhJtqVAblStefaz_YOVpDWqcRScc2s) - Comprehensive machine learning courses
- [ ] [Deep Learning with PyTorch Course](https://www.youtube.com/playlist?list=PLWKjhJtqVAbm5dir5TLEy2aZQMG7cHEZp) - PyTorch deep learning (Dec 2020)
- [ ] [Deep Learning with PyTorch Live Course](https://www.youtube.com/playlist?list=PLWKjhJtqVAbm3T2Eq1_KgloC7ogdXxdRa) - Live PyTorch course

#### Data Science & Analysis

- [ ] [Data Science](https://www.youtube.com/playlist?list=PLWKjhJtqVAblQe2CCWqV4Zy3LY01Z8aF1) - Complete data science path
- [ ] [Data Analysis with Python Course](https://www.youtube.com/playlist?list=PLWKjhJtqVAblvI1i46ScbKV2jH1gdL7VQ) - Python data analysis

#### Mathematics

- [ ] [Mathematics](https://www.youtube.com/playlist?list=PLWKjhJtqVAbl5SlE6aBHzUVZ1e6q1Wz0v) - Math fundamentals for programming and CS

#### Computer Science Fundamentals

- [ ] [Introduction to Computer Science - Harvard's CS50](https://www.youtube.com/playlist?list=PLWKjhJtqVAbmGw5fN5BQlwuug-8bDmabi) - Harvard's famous CS50 course
- [ ] [CS50's Introduction to Game Development](https://www.youtube.com/playlist?list=PLWKjhJtqVAbluXJKKbCIb4xd7fcRkpzoz) - Game development with CS50

**Pro Tip:** freeCodeCamp offers comprehensive, beginner-friendly courses. Start with "Introduction to Computer Science - Harvard's CS50" for solid fundamentals. The "Machine Learning" playlist covers ML from basics to advanced topics. "Mathematics" playlist provides essential math background. "Deep Learning with PyTorch" courses are excellent hands-on resources. All content is completely free and community-driven - perfect for self-paced learning.

### Jon Krohn - Mathematics & ML YouTube Playlists

#### Mathematics for Machine Learning (Essential Foundation)

- [ ] [Linear Algebra for Machine Learning](https://www.youtube.com/playlist?list=PLRDl2inPrWQW1QSWhBU0ki-jq_uElkh2a) - Complete linear algebra course for ML
- [ ] [Calculus for Machine Learning](https://www.youtube.com/playlist?list=PLRDl2inPrWQVu2OvnTvtkRpJ-wz-URMJx) - Calculus foundations for ML
- [ ] [Probability for Machine Learning](https://www.youtube.com/playlist?list=PLRDl2inPrWQWwJ1mh4tCUxlLfZ76C1zge) - Probability theory for ML

#### AI & Machine Learning

- [ ] [Agentic AI](https://www.youtube.com/playlist?list=PLRDl2inPrWQUip-YYLB3vFyBOwPJa9XIe) - Building AI agents
- [ ] [Talks and Tutorials](https://www.youtube.com/playlist?list=PLRDl2inPrWQXSDfCjPKSeEMFLwYpfytxH) - Various ML topics and tutorials

#### Podcasts

- [ ] [Super Data Science Podcast](https://www.youtube.com/playlist?list=PLRDl2inPrWQVW4aBgenJsTvw97qMhRtb8) - Data science discussions and interviews

**Pro Tip:** Jon Krohn's mathematics trilogy (Linear Algebra, Calculus, Probability) is specifically designed for machine learning practitioners. His teaching style focuses on building intuition with rigorous mathematical foundations. Start with Linear Algebra, then Calculus, followed by Probability - this order builds concepts progressively. These courses are perfect companions to 3Blue1Brown for deeper mathematical understanding. Jon is author of "Deep Learning Illustrated" and teaches at Columbia University.

### MIT OpenCourseWare YouTube Playlists

#### Core Mathematics & Computer Science

- [ ] [MIT 18.06 Linear Algebra, Spring 2010 (Gilbert Strang)](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8) - Legendary linear algebra course
- [ ] [MIT 18.065 Matrix Methods in Data Analysis, Signal Processing, and Machine Learning, Spring 2018](https://www.youtube.com/playlist?list=PLUl4u3cNGP63oMNUHXqIUcrkS2PivhN3k) - Applied linear algebra for ML
- [ ] [MIT 6.1200J Mathematics for Computer Science, Spring 2024](https://www.youtube.com/playlist?list=PLUl4u3cNGP61VNvICqk2HXJTonnKgAc9d) - Discrete mathematics and CS theory
- [ ] [MIT 18.100B Real Analysis, Spring 2025](https://www.youtube.com/playlist?list=PLUl4u3cNGP62Ie7F_tTAhhXoX5_Cl8meG) - Real analysis foundations
- [ ] [MIT 18.226 Probabilistic Methods in Combinatorics, Fall 2024](https://www.youtube.com/playlist?list=PLUl4u3cNGP61cYB5ymvFiEbIb-wWHfaqO) - Advanced probability theory

#### Machine Learning & AI

- [ ] [MIT 6.S191 Introduction to Deep Learning](https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI) - Modern deep learning course
- [ ] [MIT 6.034 Artificial Intelligence, Fall 2010](https://www.youtube.com/playlist?list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi) - Classic AI course
- [ ] [MIT AI + Open Education Initiative Speaker Series](https://www.youtube.com/playlist?list=PLUl4u3cNGP61TqXrdKbZtb59uXsy5tCXN) - Latest AI research and education

#### Programming & Data Science

- [ ] [MIT 6.100L Introduction to CS and Programming using Python, Fall 2022](https://www.youtube.com/playlist?list=PLUl4u3cNGP62A-ynp6v6-LGBCzeH3VAQB) - Python programming fundamentals
- [ ] [MIT RES.1-002 Introduction to R and GIS, Fall 2023](https://www.youtube.com/playlist?list=PLUl4u3cNGP602LxEgWcCyo89B2Q-zg8gm) - R programming and geospatial analysis

**Pro Tip:** MIT OpenCourseWare provides world-class university courses for free. Gilbert Strang's Linear Algebra (18.06) is legendary - one of the most watched math courses ever. For modern ML, start with "6.S191 Introduction to Deep Learning" and "18.065 Matrix Methods" which applies linear algebra directly to ML problems. The "6.034 Artificial Intelligence" course provides classic AI foundations. MIT courses are rigorous and comprehensive - excellent for building deep theoretical understanding alongside practical learning.

### 📖 Books & Study Materials

#### Machine Learning Books

- [ ] **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** by Aurélien Géron - Comprehensive ML book
- [ ] **Jason Brownlee's books** at [Machine Learning Mastery](https://machinelearningmastery.com)
- [ ] **Practical Natural Language Processing** by Vajjala, Majumder
- [ ] **Learning from Imbalanced Data Sets** by Fernández
- [ ] **D2L (Dive into Deep Learning)** - [GitHub](https://github.com/d2l-ai/d2l-en)

### 🎓 AWS Certification Courses

#### Udemy Courses

- [ ] [Stephane Maarek & Frank Kane - AWS Machine Learning](https://www.udemy.com/course/aws-machine-learning/)
- [ ] [Chandra Lingam's Complete Guide](https://www.udemy.com/course/aws-machine-learning-a-complete-guide-with-python/)
- [ ] Abhishek Singh course
- [x] A Cloud Guru course (acloud.guru)
- [ ] [Stephen Maarek AI Practitioner](https://www.udemy.com/course/aws-ai-practitioner-certified/)
- [ ] [Frank Kane AI Practitioner](https://www.udemy.com/course/aws-certified-ai-practitioner-aif-c01-hands-on-in-depth/)

#### Official AWS Training

- [ ] [AWS Skill Builder - Exam Prep Questions](https://explore.skillbuilder.aws/learn/course/external/view/elearning/12469/exam-prep-official-practice-question-set-aws-certified-machine-learning-specialty-mls-c01-english)
- [ ] [Exam Readiness: AWS Certified Machine Learning - Specialty](https://www.aws.training/Details/eLearning?id=42183) ⭐ 10/10
- [ ] [AWS Documentation](https://docs.aws.amazon.com/sagemaker/index.html)

### 📝 Practice Exams (Quality Rankings)

**Highly Recommended:**

- [ ] **AWS Official** (exams/practice tests/sample questions) - 10/10 ⭐
- [ ] [Tutorials Dojo by Jon Bonso](https://portal.tutorialsdojo.com/courses/aws-certified-machine-learning-specialty-practice-exams/) - 4/10 (+SageMaker; -ML theory)
- [ ] AWS SkillBuilder sample questions and practice exam

**Supplementary:**

- [ ] Whizlabs practice exams
- [ ] Chandra's practice tests - 2/10 (+ML questions; -SageMaker)
- [ ] Abhishek's ML questions - 1/10 (Rote memory focused, not exam-style)
- [ ] A Cloud Guru - 1/10 (Low quality)
- [ ] Stephen Maarek's practice - 1/10 (Low quality, not exam-relevant)

### 🔗 GitHub Study Repos

- [ ] [AWS-Machine-Learning by JShollaj](https://github.com/JShollaj/AWS-Machine-Learning)
- [ ] [awsCertification by gauravsatav](https://github.com/gauravsatav/awsCertification)
- [ ] [ml-aws-specialty-lab by FabG](https://github.com/FabG/ml-aws-specialty-lab)
- [ ] [Cheat-Sheets by MahmadSharaf](https://github.com/MahmadSharaf/Cheat-Sheets/tree/master/aws)
- [ ] [aws-machine-learning by sameer-goel](https://github.com/sameer-goel/aws-machine-learning)
- [ ] [aws-machine-learning-speciality by moabdelmoez](https://github.com/moabdelmoez/aws-machine-learning-speciality)

**Pro Tip:** Convert GitHub markdowns to PDFs using VSCode Markdown Preview extension

### 📰 Study Blogs & Guides

- [ ] [AWS MLS-C01 Comprehensive Guide](https://rxhl.notion.site/AWS-Machine-Learning-Specialty-4c51dfb5ae1e476284e215305b7a5d5b) ⭐ Highly detailed
- [ ] [Jayendra Patil's Learning Path](https://jayendrapatil.com/aws-certified-machine-learning-specialty-mls-c01-exam-learning-path/)
- [ ] [Passing AWS ML Specialty - Level Up](https://levelup.gitconnected.com/passing-the-aws-machine-learning-speciality-exam-8c90d87bb011)
- [ ] [Journey to AWS ML Certification - Medium](https://dipayan-x-das.medium.com/journey-towards-aws-certified-machine-learning-specialty-mls-c01-certification-6272a4ef5423)
- [ ] [Capital One Tech - Exam Advice](https://www.capitalone.com/tech/machine-learning/advice-for-taking-the-aws-machine-learning-specialty-exam/)
- [ ] [No Frills Guide - Towards Data Science](https://towardsdatascience.com/no-frills-guide-to-passing-the-aws-certified-machine-learning-specialty-exam-55624579353f)
- [ ] [My Path to Passing - Adam Dejans](https://medium.com/@adam.dejans/my-path-to-passing-the-aws-machine-learning-certification-e8fc45ad7762)
- [ ] [How to Pass AWS ML Specialty](https://towardsdatascience.com/how-to-pass-the-aws-machine-learning-speciality-exam-b00bf0f811ed)

### 🧪 Free Quizzes & Practice

- [ ] [ProProfs Quiz](https://www.proprofs.com/quiz-school/story.php?title=mjkwotcyoafj5t)
- [ ] [Whizlabs Free Test](https://www.whizlabs.com/learn/course/aws-certified-machine-learning-specialty/281/quiz/15001/ft/)
- [ ] [AWS Official Sample Questions](https://amazonmr.au1.qualtrics.com/jfe/form/SV_2nt0z0Far6DzAwJ)
- [ ] [ExamTopics Questions](https://www.examtopics.com/exams/amazon/aws-certified-machine-learning-specialty/)

### 💬 Reddit Success Stories

- [ ] [Passed AWS ML Specialty](https://www.reddit.com/r/AWSCertifications/comments/in3dy5/passed_aws_machine_learning_specialty/)
- [ ] [Passed MLS-C01](https://www.reddit.com/r/AWSCertifications/comments/l720gz/i_have_passed_machine_learning_speciality_mlsc01/)
- [ ] [Just Passed AWS ML](https://www.reddit.com/r/AWSCertifications/comments/t7ql0a/just_passed_my_aws_machine_learning_specialty/)
- [ ] [Passed with Limited ML Experience](https://www.reddit.com/r/AWSCertifications/comments/pxbg2u/passed_mlsc01_with_limited_ml_experience_lol/)

### 🎯 Key Exam Topics

**SageMaker Focus:**

- [ ] Built-in algorithms (Linear Learner, XGBoost, etc.)
- [ ] Model training & hyperparameter tuning
- [ ] Endpoint deployments & inference
- [ ] SageMaker security & VPC configuration
- [ ] Model input formats (Parquet, RecordIO)

**Data Engineering:**

- [ ] AWS Glue (Data Catalog, ETL)
- [ ] Kinesis Streams & Kinesis Firehose
- [ ] Data preprocessing (imputation, unbalanced data)
- [ ] Apache technologies (Hadoop, Hive, HBase)
- [ ] Data conversions and integrations

**ML Theory:**

- [ ] Confusion matrix (Precision, Recall, F1)
- [ ] Hyperparameter tuning strategies
- [ ] Supervised vs Unsupervised learning
- [ ] Overfitting/underfitting mitigation
- [ ] Deep Learning (CNN, RNN architectures)

**AWS ML Services:**

- [ ] Amazon Comprehend (NLP)
- [ ] Amazon Forecast (Time series)
- [ ] Amazon Rekognition (Computer Vision)
- [ ] Amazon Transcribe & Translate
- [ ] Amazon Lex & Polly
- [ ] Amazon Mechanical Turk & Augmented AI

**Production & MLOps:**

- [ ] Model versioning & monitoring
- [ ] A/B testing strategies
- [ ] Distributed processing
- [ ] EMR, Redshift, Quicksight
- [ ] MSK (Managed Streaming for Kafka)
- [ ] Lake Formation

### 💡 Study Tips & Notes

**What to Focus On:**

- White papers referenced in practice exam explanations
- Use cases and scenario-based questions (exam is heavy on these)
- Service integrations (which services work together)
- Avoid rote memorization (e.g., port numbers) - AWS doesn't test this

**Study Strategy:**

1. Complete official AWS training first (10/10 quality)
2. Read AWS documentation for SageMaker thoroughly
3. Take practice exams to identify weak areas
4. Review white papers mentioned in explanations
5. Hands-on practice with SageMaker is essential

---

## 🎤 Interviews & Career Insights

### Featured Interview: randomlyCoding

**Topic:** Production pipelines, engineering skills and job roles

**Key Takeaways:**

- Importance of understanding production systems beyond modeling
- Skills balance: modeling + engineering + business understanding
- Real-world constraints differ significantly from academic projects
- Team collaboration and communication are critical skills

**Full Interview:** Available on MLMW website

### Essential for Job Success

**Must-Have Cloud Knowledge:**
> "One thing I would say is usually a *must* is familiarity with Linux and a cloud provider (AWS, GCP, Azure). You don't need to know all 3 cloud providers (pick AWS if you don't know any yet - it has 50% market share) but if you don't know any of them it'll be harder to onboard you and your first few weeks would be a lot more overwhelming – even knowing a different one to the one you use at a specific job will help as they all have similar functionality."

**Interview Preparation Resources:**

- **CIS 4190/5190: Applied Machine Learning** (Spring 2023) - Great list of resources on one page
- **deepmleet** (deepmleet.streamlit.app) - The leetcode of machine learning
- **Society of Actuaries (SOA)**: Statistics for Risk Modeling (SRM) Exam
  - Note: Topics are solid but literature slightly dated (ISLR instead of ISLP)

---

## 👥 Influential Educators & Thinkers

People who make complex things accessible through courses, books, and personal interaction:

### Highly Recommended Educators

- **Will Curt** - Clear explanations of statistical concepts
- **Scott Cunningham** - Causal Inference: The Mixtape author
- **Laura Mayoral** - Econometrics educator
- **Allen Downey** (r/AllenDowney/) - Think Stats, Think Bayes author

### Active Researchers on Social Media

Many professors and textbook authors are surprisingly reachable:

- **Jeffrey Wooldridge** (@jmwooldridge) - Econometrics
- **Paul Goldsmith-Pinkham** (@paulgp)
  - Repo: Yale Applied Empirical Methods PhD Course
  - Video lectures available (PGP playlist)

### Video Content Creators

Already covered in Video Series section:

- Josh Starmer (StatQuest) - "This man is a genius"
- Grant Sanderson (3Blue1Brown) - "Very high quality content"
- Andrej Karpathy - Transformer architecture deep dives

### Additional Recommendation

- **Machine Learning Street Talk**
  - Reader note: "Sometimes a bit too dense for absolute beginners but really good. They list resources, papers, books."

### Hall of Shame

- **Siraj Raval** - Story of plagiarism in education (cautionary tale)

---

## 📖 Professional Glossary & Common Terms

### Common ML Terms

**Supervised vs. Unsupervised vs. Semi-Supervised Learning:**

- **Supervised**: Learning with labeled data (input-output pairs)
- **Unsupervised**: Learning patterns from unlabeled data (clustering, dimensionality reduction)
- **Semi-Supervised**: Combination of labeled and unlabeled data

**Structured vs. Unstructured Data:**

- **Structured**: Organized in tables/databases (SQL, CSV, Excel)
- **Unstructured**: No predefined format (text, images, audio, video)

### Professional Slang

**Feature Engineering:**

- Variable selection and transformation
- Creating new features from existing data
- Domain knowledge applied to improve model inputs

**ETL vs. ELT:**

- **ETL** (Extract, Transform, Load): Traditional data integration - transform before loading
- **ELT** (Extract, Load, Transform): Modern approach - transform after loading into warehouse

### Fading Buzzwords

**Data Mining:** (1990s-2000s)

- Early term for discovering patterns in data
- Largely replaced by "machine learning" and "analytics"

**Big Data:** (2010s)

- Emphasis on volume, velocity, variety (3 Vs)
- Now implicit in "data engineering" and "cloud computing"
