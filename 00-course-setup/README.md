# Course Setup - Zero to AI

## ⏱️ Quick Setup (5 minutes)

**Ready to start coding immediately?** Here's the fastest way:

1. **Fork & Clone**: Click "Fork" → `git clone https://github.com/YOUR-USERNAME/zero-to-ai.git`
2. **Install**: Run `./install_dependencies.sh` (uses UV - fastest!)
3. **Start**: `jupyter notebook` → Open any `.ipynb` file
4. **Begin Learning**: Start with [1-data-science/00_START_HERE.ipynb](../1-data-science/00_START_HERE.ipynb)

**Not ready?** See detailed setup below.

---

## 🎯 Introduction

Welcome to Zero to AI! This comprehensive learning path will take you from Python basics to production-ready AI systems. This setup guide will ensure you have everything you need to begin your AI journey.

## 🤝 Join Our Learning Community

Before you begin, connect with other learners and get support:

- ** Discussions**: [GitHub Discussions](https://github.com/PavanMudigonda/zero-to-ai/discussions)
- **🐛 Issues**: Found a bug or have a suggestion? [Create an issue](https://github.com/PavanMudigonda/zero-to-ai/issues)

## 🍴 Fork or Clone This Repository

### Step 1: Fork the Repository (Recommended)

Forking creates your own copy where you can track progress and make changes:

1. Click the **"Fork"** button at the top-right of [this page](https://github.com/PavanMudigonda/zero-to-ai)
2. This creates `https://github.com/YOUR-USERNAME/zero-to-ai`

### Step 2: Clone Your Fork

```bash
# Clone your forked repository
git clone https://github.com/YOUR-USERNAME/zero-to-ai.git
cd zero-to-ai

# Add upstream remote (to sync with original repo)
git remote add upstream https://github.com/PavanMudigonda/zero-to-ai.git
```

### Quick Clone Options

#### Full Clone (for complete learning)
```bash
git clone https://github.com/YOUR-USERNAME/zero-to-ai.git
```

#### Shallow Clone (faster, recent commits only)
```bash
git clone --depth 1 https://github.com/YOUR-USERNAME/zero-to-ai.git
```

#### Sparse Clone (specific sections only)
```bash
# Clone with minimal data
git clone --depth 1 --filter=blob:none --sparse https://github.com/YOUR-USERNAME/zero-to-ai.git
cd zero-to-ai

# Choose specific sections
git sparse-checkout set 1-data-science 5-neural-networks 10-prompt-engineering
```

## 🚀 Environment Setup

### Option 1: Quick Setup with UV (Recommended - Fastest!)

```bash
# Install UV package manager (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install all dependencies
./install_dependencies.sh

# Activate environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Option 2: Conda Environment (Recommended for ML/Data Science)

```bash
# Create environment from environment.yml
conda env create -f environment.yml

# Activate environment
conda activate aiml-learning
```

### Option 3: Traditional Python venv + pip

```bash
# Create virtual environment
python -m venv .venv

# Activate it
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Verify Installation

```bash
# Check Python version (should be 3.9+)
python --version

# Verify key packages
python -c "import numpy, pandas, sklearn, torch; print('✅ All packages installed!')"

# Start Jupyter
jupyter notebook
```

## 🎓 What You'll Need

### Hardware Requirements

| Component | Minimum | Recommended | Notes |
|-----------|---------|-------------|-------|
| **RAM** | 8GB | 16GB+ | 32GB for advanced topics |
| **Storage** | 10GB free | 50GB+ free | Large datasets & models |
| **CPU** | Any modern CPU | Multi-core (4+ cores) | Intel i5/AMD Ryzen or better |
| **GPU** | Optional | NVIDIA with CUDA | GTX 1060 or RTX 2060+ |
| **Internet** | Stable connection | High-speed | For cloud options & downloads |

### Prerequisites

- **Python Knowledge**: Basic understanding of Python (loops, functions, classes)
  - New to Python? Start with [0-python/](../0-python/) section first
- **Mathematics**: High school algebra (we'll teach the rest!)
- **Time Commitment**: 10-15 hours/week for 6-12 months
- **Hardware**: Any modern computer (GPU helpful but not required initially)

### Required Software

- **Python 3.9+** - [Download here](https://www.python.org/downloads/)
- **Git** - [Download here](https://git-scm.com/downloads)
- **Jupyter Notebook** - Installed via requirements.txt
- **VS Code** (recommended) - [Download here](https://code.visualstudio.com/)

### Optional but Recommended

- **GitHub Account** - For saving progress and collaboration
- **Google Colab Account** - For free GPU access
- **Kaggle Account** - For datasets and competitions

## 🌐 Cloud Development Options

### GitHub Codespaces (Recommended for No-Setup Experience)

1. Go to your forked repository on GitHub
2. Click **Code** → **Codespaces** → **Create codespace on main**
3. Wait for the environment to build (first time takes ~5 minutes)
4. Start coding! Everything is pre-installed

### Google Colab

- Click [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/zero-to-ai/blob/main)
- Each notebook can be opened directly in Colab
- Free GPU access available

### Replit

- Click [![Open in Replit](https://img.shields.io/badge/Open%20in-Replit-blue?style=flat&logo=replit)](https://replit.com/github/PavanMudigonda/zero-to-ai)
- Collaborative coding environment
- Great for learning with others

### Kaggle Kernels

- Click [![Open in Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com/code)
- Create a new notebook, enable Internet, and clone this repo from GitHub inside the notebook
- Access to free GPU/TPU
- Large dataset library included

## 📂 Repository Structure Overview

```
zero-to-ai/
├── 📘 00-course-setup/        ⭐ START HERE - Setup & orientation
├── 📚 01-python/                Python fundamentals (if needed)
├── 📊 02-data-science/          NumPy, Pandas, Scikit-learn (278 notebooks!)
│   ├── 1-numpy-examples/       Array operations & data manipulation
│   ├── 2-pandas-examples/      DataFrames & analysis
│   ├── 3-data-science-examples/ Statistical analysis & visualization
│   ├── 4-matplotlib/           Plotting & charts
│   └── 5-scikit-learn/         Machine learning algorithms
├── 🔢 03-maths/                 Linear Algebra, Calculus, Statistics (40+ notebooks)
│   ├── foundational/           Core math topics
│   ├── mml-book/              Mathematics for Machine Learning
│   ├── islp-book/             Statistical learning with Python
│   ├── cs229-course/          Stanford ML course
│   └── advanced/ 🆕           Learning theory, optimization
├── 🔤 04-token/                 Tokenization (tiktoken, sentencepiece, HF)
├── 🎯 05-embeddings/            Word & sentence embeddings
├── 🧠 06-neural-networks/       Deep learning from scratch to Transformers
├── 💾 07-vector-databases/      Chroma, Qdrant, Weaviate, Milvus, pgvector
├── 🔍 08-rag/                   Retrieval-Augmented Generation
├── 🚀 09-mlops/                 Deployment, monitoring, optimization
├── 🎨 10-specializations/       AI Agents, Computer Vision, NLP
├── 💬 11-prompt-engineering/    Advanced prompting techniques
├── ⚙️ 12-llm-finetuning/        LoRA, QLoRA, PEFT
├── 🎭 13-multimodal/            Vision, Audio, Video AI
├── 🏠 14-local-llms/            Ollama & private AI
├── 🧪 15-ai-agents/             Autonomous AI systems
├── 🔍 16-vector-search/         Advanced search & retrieval
├── 📈 17-ml-evaluation/         Model evaluation & metrics
├── 🔧 18-debugging/             Troubleshooting & optimization
├── ⚡ 19-low-code-ai/           No-code AI tools
├── 🛡️ 20-ai-safety/            AI safety & red teaming
├── 📡 21-real-time-streaming/   Live AI applications
├── 📝 22-quizzes/               Knowledge assessments
├── 📖 23-references/            Research papers & resources
├── 🧠 24-advanced-deep-learning/ Cutting-edge techniques
├── 📋 25-quizzes/               Progress assessments
└── 📚 scripts/                  Utility scripts & tools
```

## 🗺️ Your Learning Path

### Phase 0: Setup & Prerequisites (You are here!)
- ✅ Complete this setup guide
- ✅ Review [glossary/GLOSSARY.md](../glossary/GLOSSARY.md) for terminology
- ✅ If new to Python, start with [0-python/](../0-python/)

### Phase 1: Foundations (Weeks 1-8)
- **Lesson 1**: [Python & Data Science](../1-data-science/README.md) - 278 notebooks
- **Lesson 2**: [Mathematics for ML](../2-maths/README.md) - Linear algebra, calculus, stats

### Phase 2: Core AI (Weeks 9-20)
- **Lesson 3-7**: Tokenization → Embeddings → Neural Networks → Vector DBs → RAG

### Phase 3: Advanced Topics (Weeks 21-32)
- **Lesson 8-13**: MLOps → Specializations → Prompt Engineering → Fine-tuning → Multimodal → Local LLMs

## 📋 Next Steps

1. ✅ **Complete Setup**: Ensure your environment is working
2. ✅ **Read the Checklist**: Open [checklist.md](../checklist.md) - your complete roadmap
3. ✅ **Start Learning**: Begin with [1-data-science/00_START_HERE.ipynb](../1-data-science/00_START_HERE.ipynb)
4. ✅ **Track Progress**: Use `python scripts/view_progress.py` to monitor your journey
5. ✅ **Join Community**: Connect with other learners for support

## 🆘 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| `Python not found` | Ensure Python 3.9+ is installed and in PATH |
| `Jupyter kernel not found` | Run `python -m ipykernel install --user` |
| `Import torch fails` | Install PyTorch: `pip install torch` |
| `Out of memory errors` | Use Google Colab for free GPU |
| `Git clone too slow` | Use shallow clone: `git clone --depth 1 ...` |

### Getting Help

1. **Check [troubleshooting.md](./troubleshooting.md)** for detailed solutions
2. **Search [GitHub Issues](https://github.com/PavanMudigonda/zero-to-ai/issues)**
3. **Ask in [Discussions](https://github.com/PavanMudigonda/zero-to-ai/discussions)**

## 🎯 Verification Checklist

Before moving to Lesson 1, ensure:

- [ ] Repository cloned/forked successfully
- [ ] Python 3.9+ installed and accessible
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`pip list` shows numpy, pandas, sklearn, etc.)
- [ ] Jupyter Notebook launches successfully
- [ ] Can open and run a test notebook
- [ ] Read [checklist.md](../checklist.md) learning roadmap
- [ ] Familiar with [glossary/GLOSSARY.md](../glossary/GLOSSARY.md) terms

## 🎓 Ready to Start?

**Congratulations!** 🎉 You're all set up and ready to begin your AI journey!

**Next Stop**: [Lesson 1: Python & Data Science →](../1-data-science/README.md)

---

**📚 Additional Resources**

- [Main README](../README.md) - Repository overview
- [Learning Checklist](../checklist.md) - Complete roadmap
- [Setup Guide](../setup.md) - Detailed installation instructions
- [Contributing Guidelines](../CONTRIBUTING.md) - How to contribute
- [Code of Conduct](../CODE_OF_CONDUCT.md) - Community guidelines

---

**Need Help?** Open an [issue](https://github.com/PavanMudigonda/zero-to-ai/issues) or join our community!

**Found this helpful?** ⭐ Star this repo to support the project!
