# Zero to AI - Complete Learning Path 🚀

### A comprehensive curriculum teaching everything you need to build production-ready AI systems

[![GitHub license](https://img.shields.io/github/license/PavanMudigonda/zero-to-ai.svg)](https://github.com/PavanMudigonda/zero-to-ai/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/PavanMudigonda/zero-to-ai.svg)](https://GitHub.com/PavanMudigonda/zero-to-ai/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/PavanMudigonda/zero-to-ai.svg)](https://GitHub.com/PavanMudigonda/zero-to-ai/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/PavanMudigonda/zero-to-ai.svg)](https://GitHub.com/PavanMudigonda/zero-to-ai/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/PavanMudigonda/zero-to-ai.svg?style=social&label=Watch)](https://GitHub.com/PavanMudigonda/zero-to-ai/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/PavanMudigonda/zero-to-ai.svg?style=social&label=Fork)](https://GitHub.com/PavanMudigonda/zero-to-ai/network/)
[![GitHub stars](https://img.shields.io/github/stars/PavanMudigonda/zero-to-ai.svg?style=social&label=Star)](https://GitHub.com/PavanMudigonda/zero-to-ai/stargazers/)

---

[![Open in Browser](https://img.shields.io/badge/Open%20in-Browser-F38020?style=flat&logo=cloudflare)](https://zero-to-ai.dev/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/zero-to-ai/blob/main)
[![Open in Replit](https://img.shields.io/badge/Open%20in-Replit-blue?style=flat&logo=replit)](https://replit.com/github/PavanMudigonda/zero-to-ai)
[![Open in Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com/code)
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-black?style=flat&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=PavanMudigonda/zero-to-ai)
[![github.dev](https://img.shields.io/badge/Open%20in-github.dev-black?style=flat&logo=github)](https://github.dev/PavanMudigonda/zero-to-ai)

**Click any badge above to start coding in seconds!**

---

## 📊 Course Overview

> **From Zero to AI Mastery** WORK IN PROGRESS. OPEN FOR FEEDBACK.

---

## 🌱 Getting Started

This comprehensive AI/ML curriculum uses progressive numbered modules covering everything from Python fundamentals to cutting-edge AI systems and advanced research topics. Each module includes hands-on notebooks, projects, and practical applications.

**Don't forget to:**
- ⭐ [Star this repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars) to find it easily later
- 🍴 [Fork this repo](https://github.com/PavanMudigonda/zero-to-ai/fork) to track your personal progress

---

## 🚀 Quick Start

### Prerequisites
- Basic Python knowledge (or start with [01-python/](01-python/))
- High school mathematics
- A computer (GPU helpful but not required initially)
- If you are buying new device for the course i suggest below
  - MacBook Neo (8 GB) - cheaper option
  - MacBook Air (16 GB) - sufficient for most users
  - MacBook Pro (16 GB min) - if you are heavy user choose
- Use Google Colab account or Kaggle Account in addition to your device as per program you are working with
- 10-15 hours/week

### Installation (Choose One)

#### Option 1: UV - Fast & Recommended
```bash
# Clone the repository
git clone https://github.com/PavanMudigonda/zero-to-ai.git
cd zero-to-ai

# Install dependencies with UV (fastest!)
./install_dependencies.sh

# Start learning
jupyter notebook
```

Optional developer tooling for Phase 31:

```bash
# Install Node-based coding tools such as OpenCode
npm install

# Install the dedicated AI developer tools environment
# (used for OpenHands because it currently needs Python 3.12)
INSTALL_AI_DEV_TOOLS=1 ./install_dependencies.sh
```

#### Option 2: Conda - Best for ML/Data Science
```bash
# Clone the repository
git clone https://github.com/PavanMudigonda/zero-to-ai.git
cd zero-to-ai

# Create conda environment
conda env create -f environment.yml
conda activate aiml-learning

# Start learning
jupyter notebook
```

#### Option 3: Cloud (No Installation!)

- **GitHub Codespaces**: Click [![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-black?logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=PavanMudigonda/zero-to-ai) — fully automated, all dependencies install via `install_dependencies.sh`

- **Google Colab**: Click [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/zero-to-ai/blob/main) — then run this in the first cell:
  ```python
  !pip install -q -r https://raw.githubusercontent.com/PavanMudigonda/zero-to-ai/main/colab_requirements.txt
  ```

- **Kaggle**: Click [![Open in Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?logo=kaggle)](https://www.kaggle.com/code) and create a **New Notebook**, then enable **Internet** in notebook settings and run:
  ```python
  !git clone https://github.com/PavanMudigonda/zero-to-ai.git
  %cd zero-to-ai
  !pip install -q -r https://raw.githubusercontent.com/PavanMudigonda/zero-to-ai/main/kaggle_requirements.txt
  ```

- **Replit**: Click [![Open in Replit](https://img.shields.io/badge/Open%20in-Replit-blue?logo=replit)](https://replit.com/github/PavanMudigonda/zero-to-ai) — packages auto-install on first run via `requirements-replit.txt`

- **github.dev**: Click [![github.dev](https://img.shields.io/badge/Open%20in-github.dev-black?logo=github)](https://github.dev/PavanMudigonda/zero-to-ai) — browser-based editor only (no execution)

---

## 📂 Repository Structure

```
zero-to-ai/
├── 📘 00-course-setup/        ⭐ START HERE - Setup & orientation
├── 📚 01-python/                Python fundamentals (if needed)
├── 📊 02-data-science/          NumPy, Pandas, Scikit-learn (278 notebooks!)
├── 🔢 03-maths/                 Linear Algebra, Calculus, Statistics (40+ notebooks)
│   ├── foundational/           Core math topics
│   ├── mml-book/              MML textbook implementation
│   ├── islp-book/             Statistical learning with Python
│   ├── cs229-course/          Stanford ML course
│   └── advanced/ 🆕           Learning theory, advanced optimization, Bayesian non-parametrics
├── 🔤 04-token/                 Tokenization (tiktoken, sentencepiece, HF)
├── 🎯 05-embeddings/            Text, multimodal, and retrieval embeddings
├── 🧠 06-neural-networks/       Deep learning from scratch to Transformers
├── 💾 07-vector-databases/      Chroma, Qdrant, Weaviate, Milvus, pgvector
├── 🔍 08-rag/                   Retrieval-Augmented Generation
├── 🚀 09-mlops/                 Deployment, monitoring, optimization
├── 🎨 10-specializations/       AI Agents, Computer Vision, NLP
├── 💬 11-prompt-engineering/   Advanced prompting, context engineering, reasoning patterns
├── ⚙️ 12-llm-finetuning/      LoRA, QLoRA, PEFT fine-tuning
├── 🎭 13-multimodal/           Vision, audio, video, realtime multimodal AI
├── 🏠 14-local-llms/           Ollama, llama.cpp, MLX, local serving
├── 🤖 15-ai-agents/            Function calling, MCP, OpenAI Agents SDK, LangGraph
├── 📊 16-model-evaluation/     Metrics, fairness, LLM-as-judge, agent evaluation
├── 🐛 17-debugging-troubleshooting/ Profiling, data issues, debugging
├── 🎨 18-low-code-ai-tools/    Gradio, Streamlit, Flowise, Langflow, Dify, AutoML
├── 🔒 19-ai-safety-redteaming/ Security, bias, red teaming
├── ⚡ 20-real-time-streaming/  Streaming AI, WebSockets, WebRTC, realtime voice
├── ❓ 21-quizzes/              Questions to test your knowledge
├── 🧪 22-references/           Resources, papers, external materials
├── 📖 23-glossary/             AI/ML terminology & concepts
├── 🔬 24-advanced-deep-learning/ 🆕 **39 notebooks**: GANs, VAEs, NeRF, Diffusion, BNNs
├── 🎲 25-reinforcement-learning/ 🆕 **6 notebooks**: MDP, Q-Learning, Policy Gradients, Actor-Critic
├── 📈 26-time-series-analysis/ 🆕 **6 notebooks**: ARIMA, Prophet, LSTM, Transformer forecasting
├── 📊 27-causal-inference/ 🆕 **6 notebooks**: DAGs, Experimental Design, Observational Methods, Quasi-Experimental
├── 🔨 28-practical-data-science/ Interview prep & hands-on practice
├── 🔧 29-ai-hardware-llm-validation/ 🆕 **9 guides + 8 labs**: Silicon validation for AMD, NVIDIA, Qualcomm, TPU, Apple Silicon
├── 🚄 30-inference-optimization/ 🆕 KV cache, vLLM, TensorRT-LLM, quantization, speculative decoding
├── 🛠️ 31-ai-powered-dev-tools/ 🆕 VS Code AI setup, MCP deep dive, custom instructions, tool workflows
├── docs/
│   ├── ✅ checklist.md             Your complete learning roadmap
│   ├── 📋 setup.md                 Detailed installation guide
│   ├── 📖 MASTER_STUDY_GUIDE.md    Phase-by-phase study guide & track picker
│   ├── 📚 REFERENCES.md            Videos, repos, courses, papers by phase
│   └── !! COMPARISON_MATRICES.md   Comparison of LLM Models
```

**💡 Pro Tip**: Start with `00_START_HERE.ipynb` in each section for guided learning!

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

- **🐛 Report Issues**: Found a bug or error? [Open an issue](https://github.com/PavanMudigonda/zero-to-ai/issues)
- **✨ Suggest Features**: Have an idea? Share it in [Discussions](https://github.com/PavanMudigonda/zero-to-ai/discussions)
- **📝 Improve Documentation**: Fix typos, clarify explanations
- **💻 Add Examples**: Contribute new notebooks or examples
- **🌍 Translations**: Help translate content to other languages

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## 🙏 Acknowledgments

This learning path is inspired by and integrates content from:

- **Microsoft Learn** - Official AI/ML curriculum
- **Microsoft for Beginners Series** - AI, ML, GenAI, Agents courses
- **Stanford University** - CS229, CS224N, CS231N courses
- **3Blue1Brown** - Visual mathematics explanations
- **Andrej Karpathy** - Neural networks from scratch
- **DeepLearning.AI** - Practical AI courses
- **Fast.ai** - Practical deep learning approach

**Special Thanks** to all contributors, educators, and the open-source community!

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](docs/LICENSE.md) file for details.

---

**🚀 From Zero to AI - Your Journey Starts Here!**

> "The best time to start learning AI was yesterday. The second best time is now."


---

**Questions?** Open an [issue](https://github.com/PavanMudigonda/zero-to-ai/issues) or start a [discussion](https://github.com/PavanMudigonda/zero-to-ai/discussions)!

**Found this helpful?** ⭐ Star this repo and share it with others!
