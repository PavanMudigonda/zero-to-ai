# setup
# Setup Guide - AIML Learning Repository

## Quick Start with UV (Recommended)

UV is an extremely fast Python package installer and resolver written in Rust. It's 10-100x faster than pip!

### 1. Run the installation script

```bash
./install_dependencies.sh
```

This will:
- Install UV if not already installed
- Create a virtual environment at `.venv/`
- Install all dependencies using UV
- Activate the environment

### 2. Activate the environment

```bash
source .venv/bin/activate
```

### 3. Start learning!

```bash
# Start Jupyter
jupyter notebook

# Or open a specific notebook
jupyter notebook 1-token/tiktoken_example.ipynb
```

---

## Manual Installation with UV

If you prefer manual control:

### Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Create virtual environment

```bash
uv venv .venv
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows
```

### Install dependencies

```bash
# Core dependencies
uv pip install -r requirements.txt

# With development tools
uv pip install -r requirements-dev.txt

# With AWS tools
uv pip install -r requirements-aws.txt

# Or install specific extras from pyproject.toml
uv pip install torch transformers tiktoken sentence-transformers jupyter
```

---

## Alternative: Traditional pip/venv

If you prefer not to use UV:

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Or with dev/AWS tools
pip install -r requirements-dev.txt
pip install -r requirements-aws.txt
```

---

## Verify Installation

```bash
# Check Python version
python --version  # Should be 3.11+

# Test imports
python -c "import torch; print(f'PyTorch {torch.__version__}')"
python -c "import transformers; print(f'Transformers {transformers.__version__}')"
python -c "import tiktoken; print('tiktoken ✅')"
python -c "import sentence_transformers; print('sentence-transformers ✅')"

# Start Jupyter
jupyter notebook
```

---

## Dependencies Overview

### Core ML/DL
- **PyTorch** - Deep learning framework
- **Transformers** - HuggingFace library (BERT, GPT, etc.)
- **Torchvision** - Vision models and datasets

### Tokenization
- **tiktoken** - OpenAI's tokenizer
- **tokenizers** - HuggingFace tokenizers library
- **sentencepiece** - Google's tokenizer

### Embeddings & Vector DBs
- **sentence-transformers** - Sentence embeddings
- **chromadb** - Vector database
- **qdrant-client** - Qdrant vector DB
- **weaviate-client** - Weaviate vector DB
- **pymilvus** - Milvus vector DB
- **pgvector** - PostgreSQL vector extension

### Data Science
- **numpy, pandas, scikit-learn, scipy** - Data science essentials
- **matplotlib, seaborn, plotly** - Visualization

### Development
- **jupyter** - Interactive notebooks
- **pytest, black, flake8** - Testing and formatting (dev extras)

---

## Learning Path

Once setup is complete, follow this path:

1. **23-glossary/** - AI/ML terminology
2. **04-token/** - Tokenization (tiktoken, sentencepiece)
3. **05-embeddings/** - Word/sentence embeddings
4. **07-vector-databases/** - Chroma, Qdrant, Weaviate, Milvus, pgvector
5. **06-neural-networks/** - From scratch to Transformers
6. Start with `00_START_HERE.ipynb` in each section!

---

## Which Requirements File to Use?

| File | Use When |
|------|----------|
| `requirements.txt` | Local development (pip) |
| `environment.yml` | Local development (Conda/Mamba) |
| `colab_requirements.txt` | Google Colab — skips pre-installed packages |
| `kaggle_requirements.txt` | Kaggle notebooks — skips pre-installed packages, requires Internet toggle enabled |
| `requirements-replit.txt` | Replit — auto-installed on run |
| `pyproject.toml` | `uv pip install -e .` or editable installs |

---

## Troubleshooting

### UV installation fails
```bash
# Try with pip instead
pip install uv
```

### PyTorch GPU support
For CUDA support, install PyTorch separately:
```bash
# See https://pytorch.org for your specific CUDA version
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### PostgreSQL dependencies
For pgvector to work, ensure PostgreSQL development headers are installed:
```bash
# macOS
brew install postgresql

# Ubuntu/Debian
sudo apt-get install postgresql-server-dev-all

# Then reinstall psycopg2-binary
uv pip install --force-reinstall psycopg2-binary
```

### Jupyter kernel not found
```bash
python -m ipykernel install --user --name=aiml
```

---

## Environment Variables

Some notebooks require API keys or database connections. Create a `.env` file:

```bash
# OpenAI (for embeddings notebooks)
OPENAI_API_KEY=your_key_here

# Aurora PostgreSQL (for 6-vector-databases/06_aurora_pgvector_guide.ipynb)
AURORA_HOST=your-cluster.region.rds.amazonaws.com
AURORA_PORT=5432
AURORA_DATABASE=vectordb
AURORA_USER=postgres
AURORA_PASSWORD=your_password

# AWS (optional, for AWS services)
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=us-east-1
```

---

## Why UV?

UV is a next-generation Python package manager:

✅ **10-100x faster** than pip  
✅ **Better dependency resolution** (like Poetry/PDM)  
✅ **Drop-in replacement** for pip commands  
✅ **Written in Rust** for maximum performance  
✅ **Creates reproducible environments**  

Example speed comparison:
- pip: ~45 seconds
- UV: ~2 seconds

---

## Need Help?

- Check notebook `00_START_HERE.ipynb` files in each section
- Review `README.md` in each folder

Happy learning! 🚀
