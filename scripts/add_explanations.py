#!/usr/bin/env python3
"""
Auto-generate markdown explanation cells for code cells in Jupyter notebooks.

Analyzes code content using heuristics to produce contextual explanations
for code cells that lack a preceding markdown cell with adequate explanation.
Only modifies source notebooks (excludes docs/, site/ mirrors).
"""

import ast
import json
import re
import sys
from pathlib import Path

WORKSPACE = Path("/Users/pavanmudigonda/code/zero-to-ai")

# Map of common library imports to their purpose descriptions
LIBRARY_DESCRIPTIONS = {
    "numpy": "NumPy for numerical computing and array operations",
    "np": "NumPy for numerical computing and array operations",
    "pandas": "Pandas for data manipulation and analysis",
    "pd": "Pandas for data manipulation and analysis",
    "matplotlib": "Matplotlib for creating static visualizations and plots",
    "matplotlib.pyplot": "Matplotlib's pyplot interface for creating plots",
    "plt": "Matplotlib's pyplot for creating plots",
    "seaborn": "Seaborn for statistical data visualization",
    "sns": "Seaborn for statistical data visualization",
    "sklearn": "scikit-learn for machine learning algorithms and utilities",
    "scipy": "SciPy for scientific and technical computing",
    "torch": "PyTorch for deep learning and tensor operations",
    "tensorflow": "TensorFlow for deep learning and neural networks",
    "tf": "TensorFlow for deep learning and neural networks",
    "keras": "Keras for high-level neural network API",
    "transformers": "Hugging Face Transformers for pretrained NLP/ML models",
    "tokenizers": "Hugging Face Tokenizers for fast text tokenization",
    "tiktoken": "tiktoken for OpenAI-compatible tokenization",
    "sentencepiece": "SentencePiece for unsupervised text tokenization",
    "openai": "OpenAI API client for GPT models and embeddings",
    "langchain": "LangChain for building LLM-powered applications",
    "llama_index": "LlamaIndex for connecting LLMs with external data",
    "chromadb": "ChromaDB vector database for embedding storage and search",
    "qdrant_client": "Qdrant vector database client",
    "weaviate": "Weaviate vector database client",
    "milvus": "Milvus vector database for similarity search",
    "pymilvus": "PyMilvus client for Milvus vector database",
    "pinecone": "Pinecone vector database for similarity search",
    "faiss": "FAISS for efficient similarity search and clustering",
    "sentence_transformers": "Sentence Transformers for computing text embeddings",
    "gradio": "Gradio for building ML demo web interfaces",
    "streamlit": "Streamlit for building data apps",
    "fastapi": "FastAPI for building high-performance web APIs",
    "mlflow": "MLflow for ML experiment tracking and model management",
    "wandb": "Weights & Biases for ML experiment tracking",
    "docker": "Docker SDK for container operations",
    "requests": "Requests library for making HTTP calls",
    "json": "Python's built-in JSON module for data serialization",
    "os": "Python's OS module for interacting with the operating system",
    "sys": "Python's sys module for system-specific parameters",
    "re": "Python's regex module for pattern matching",
    "math": "Python's built-in math module",
    "collections": "Python's collections module for specialized containers",
    "itertools": "Python's itertools for efficient looping",
    "functools": "Python's functools for higher-order functions",
    "typing": "Python's typing module for type hints",
    "pathlib": "Python's pathlib for object-oriented filesystem paths",
    "datetime": "Python's datetime for date and time operations",
    "time": "Python's time module for time-related functions",
    "random": "Python's random module for generating random values",
    "copy": "Python's copy module for shallow and deep copying",
    "warnings": "Python's warnings module for warning control",
    "tqdm": "tqdm for displaying progress bars",
    "PIL": "Pillow (PIL) for image processing",
    "cv2": "OpenCV for computer vision tasks",
    "networkx": "NetworkX for graph/network analysis",
    "sympy": "SymPy for symbolic mathematics",
    "statsmodels": "StatsModels for statistical modeling",
    "xgboost": "XGBoost for gradient boosting",
    "lightgbm": "LightGBM for gradient boosting",
    "prophet": "Prophet for time series forecasting",
    "dspy": "DSPy for programming (not prompting) language models",
    "gymnasium": "Gymnasium (OpenAI Gym) for reinforcement learning environments",
    "gym": "OpenAI Gym for reinforcement learning environments",
    "peft": "PEFT for parameter-efficient fine-tuning (LoRA, QLoRA)",
    "trl": "TRL for transformer reinforcement learning (SFT, DPO, RLHF)",
    "unsloth": "Unsloth for fast LLM fine-tuning",
    "datasets": "Hugging Face Datasets for loading and processing datasets",
    "evaluate": "Hugging Face Evaluate for model evaluation metrics",
    "accelerate": "Hugging Face Accelerate for distributed training",
    "bitsandbytes": "bitsandbytes for quantization (4-bit, 8-bit)",
    "auto_gptq": "AutoGPTQ for GPTQ quantization",
    "awq": "AWQ for activation-aware weight quantization",
    "vllm": "vLLM for high-throughput LLM serving",
    "ollama": "Ollama for running local LLMs",
    "dotenv": "python-dotenv for loading environment variables from .env files",
    "IPython": "IPython for enhanced interactive Python",
    "ipywidgets": "IPython widgets for interactive notebook elements",
    "dowhy": "DoWhy for causal inference",
    "econml": "EconML for causal machine learning",
    "shap": "SHAP for model interpretability and feature importance",
    "lime": "LIME for local interpretable model explanations",
    "captum": "Captum for PyTorch model interpretability",
}


def get_notebook_topic(nb_path: str) -> str:
    """Infer the topic from the notebook path for more contextual explanations."""
    path_lower = nb_path.lower()
    if "token" in path_lower:
        return "tokenization"
    elif "embedding" in path_lower:
        return "embeddings"
    elif "neural" in path_lower or "nn" in path_lower:
        return "neural networks"
    elif "vector" in path_lower and "database" in path_lower:
        return "vector databases"
    elif "rag" in path_lower:
        return "retrieval-augmented generation"
    elif "mlops" in path_lower:
        return "MLOps"
    elif "prompt" in path_lower:
        return "prompt engineering"
    elif "finetun" in path_lower:
        return "LLM fine-tuning"
    elif "multimodal" in path_lower:
        return "multimodal AI"
    elif "agent" in path_lower:
        return "AI agents"
    elif "evaluation" in path_lower or "metric" in path_lower:
        return "model evaluation"
    elif "debug" in path_lower or "troubleshoot" in path_lower:
        return "debugging & troubleshooting"
    elif "safety" in path_lower or "redteam" in path_lower:
        return "AI safety"
    elif "streaming" in path_lower:
        return "real-time streaming"
    elif "time.series" in path_lower or "time_series" in path_lower:
        return "time series analysis"
    elif "reinforcement" in path_lower or "q_learn" in path_lower:
        return "reinforcement learning"
    elif "causal" in path_lower:
        return "causal inference"
    elif "deep.learn" in path_lower or "deep_learn" in path_lower:
        return "advanced deep learning"
    elif "gan" in path_lower:
        return "generative adversarial networks"
    elif "vae" in path_lower:
        return "variational autoencoders"
    elif "transformer" in path_lower:
        return "transformers"
    elif "attention" in path_lower:
        return "attention mechanisms"
    elif "linear.algebra" in path_lower:
        return "linear algebra"
    elif "calculus" in path_lower or "derivative" in path_lower:
        return "calculus"
    elif "probability" in path_lower or "statistic" in path_lower:
        return "probability & statistics"
    elif "gradient" in path_lower:
        return "gradient descent & optimization"
    elif "numpy" in path_lower:
        return "NumPy array operations"
    elif "pandas" in path_lower or "dataframe" in path_lower:
        return "Pandas data manipulation"
    elif "matplotlib" in path_lower:
        return "data visualization"
    elif "scikit" in path_lower or "sklearn" in path_lower:
        return "scikit-learn machine learning"
    elif "python" in path_lower or "crash" in path_lower:
        return "Python fundamentals"
    elif "data.science" in path_lower or "data_science" in path_lower:
        return "data science"
    elif "local.llm" in path_lower or "local_llm" in path_lower or "ollama" in path_lower:
        return "local LLMs"
    elif "inference" in path_lower and "optim" in path_lower:
        return "inference optimization"
    elif "low.code" in path_lower or "low_code" in path_lower:
        return "low-code AI tools"
    elif "gradio" in path_lower:
        return "Gradio interfaces"
    elif "streamlit" in path_lower:
        return "Streamlit apps"
    elif "math" in path_lower:
        return "mathematics for AI"
    elif "islp" in path_lower:
        return "statistical learning (ISLP)"
    else:
        return "AI/ML"


def analyze_imports(code: str) -> list[str]:
    """Extract imported library names from code."""
    imports = []
    for line in code.split("\n"):
        line = line.strip()
        match = re.match(r"^(?:from\s+(\S+)|import\s+(\S+))", line)
        if match:
            lib = (match.group(1) or match.group(2)).split(".")[0]
            imports.append(lib)
    return imports


def detect_code_patterns(code: str) -> dict:
    """Detect what patterns are present in the code."""
    patterns = {
        "imports": False,
        "data_loading": False,
        "dataframe_ops": False,
        "visualization": False,
        "model_creation": False,
        "model_training": False,
        "model_prediction": False,
        "evaluation": False,
        "function_def": False,
        "class_def": False,
        "string_ops": False,
        "list_ops": False,
        "dict_ops": False,
        "loop": False,
        "conditional": False,
        "file_io": False,
        "api_call": False,
        "tokenization": False,
        "embedding": False,
        "vector_db": False,
        "math_ops": False,
        "tensor_ops": False,
        "neural_net": False,
        "loss_function": False,
        "optimizer": False,
        "data_transform": False,
        "print_output": False,
        "variable_assignment": False,
        "exception_handling": False,
        "decorator": False,
        "comprehension": False,
        "type_hints": False,
        "assertion": False,
        "env_setup": False,
        "simple_expression": False,
    }

    lines = [l.strip() for l in code.split("\n") if l.strip() and not l.strip().startswith("#")]

    if not lines:
        return patterns

    # Check for simple expressions (like `1+1`, `x`, `s[2]`)
    if len(lines) == 1 and len(lines[0]) < 40:
        expr = lines[0]
        if not any(kw in expr for kw in ["import", "def ", "class ", "for ", "while ", "if ", "="]):
            patterns["simple_expression"] = True

    for line in code.split("\n"):
        line_s = line.strip()
        if re.match(r"^(import|from)\s+", line_s):
            patterns["imports"] = True
        if re.search(r"\.(read_csv|read_excel|read_json|read_parquet|load_dataset|read_sql|read_html|read_clipboard|read_fwf|read_table)", line_s):
            patterns["data_loading"] = True
        if re.search(r"\.(DataFrame|groupby|merge|concat|pivot|melt|join|drop|fillna|dropna|rename|apply|map|replace|sort_values|value_counts|describe|info|head|tail|shape|columns|dtypes|iloc|loc|at|iat|query|filter)", line_s):
            patterns["dataframe_ops"] = True
        if re.search(r"(plt\.|\.plot|\.scatter|\.bar|\.hist|\.show|\.figure|\.subplot|\.imshow|sns\.|\.heatmap|\.boxplot|\.violinplot|\.countplot|\.pairplot|\.distplot|\.kdeplot|\.lineplot|go\.)", line_s):
            patterns["visualization"] = True
        if re.search(r"(Sequential|Dense|Linear|Conv[12]d|LSTM|GRU|Transformer|nn\.Module|Model\(|Classifier\(|Regressor\(|Pipeline\(|make_pipeline|SVC|SVR|RandomForest|GradientBoosting|XGB|LGBM|KMeans|PCA|DecisionTree|LogisticRegression|LinearRegression|Ridge|Lasso|ElasticNet)", line_s):
            patterns["model_creation"] = True
        if re.search(r"\.(fit|train|backward|step|compile)\(", line_s):
            patterns["model_training"] = True
        if re.search(r"\.(predict|generate|forward|inference|transform)\(", line_s):
            patterns["model_prediction"] = True
        if re.search(r"(accuracy|precision|recall|f1|roc_auc|confusion_matrix|classification_report|mean_squared|r2_score|evaluate|score\(|cross_val|metric|perplexity|bleu|rouge)", line_s):
            patterns["evaluation"] = True
        if re.match(r"^(async\s+)?def\s+", line_s):
            patterns["function_def"] = True
        if re.match(r"^class\s+", line_s):
            patterns["class_def"] = True
        if re.search(r"(\.split|\.join|\.strip|\.replace|\.upper|\.lower|\.find|\.startswith|\.endswith|\.format|f['\"])", line_s):
            patterns["string_ops"] = True
        if re.search(r"(\.append|\.extend|\.pop|\.insert|\.sort\(|\.reverse\(|sorted\(|len\(|range\(|\[\s*\d+\s*\]|\[\s*\d+\s*:\s*\d*\s*\])", line_s):
            patterns["list_ops"] = True
        if re.search(r"(\{.*:.*\}|\.keys|\.values|\.items|\.get\(|\.update\(|dict\()", line_s):
            patterns["dict_ops"] = True
        if re.search(r"^(for|while)\s+", line_s):
            patterns["loop"] = True
        if re.match(r"^(if|elif|else)\s*", line_s):
            patterns["conditional"] = True
        if re.search(r"(open\(|\.read\(|\.write\(|\.close\(|with open|Path\(|os\.path)", line_s):
            patterns["file_io"] = True
        if re.search(r"(requests\.|\.post\(|\.get\(|api_key|endpoint|client\.|\.create\(|openai\.|httpx)", line_s):
            patterns["api_call"] = True
        if re.search(r"(tokenize|encode|decode|vocab|token|BPE|WordPiece|SentencePiece|tiktoken|\.tokenizer|AutoTokenizer)", line_s, re.IGNORECASE):
            patterns["tokenization"] = True
        if re.search(r"(embed|embedding|encode_text|encode_sentences|SentenceTransformer|get_embedding|similarity)", line_s, re.IGNORECASE):
            patterns["embedding"] = True
        if re.search(r"(chromadb|qdrant|weaviate|milvus|pinecone|faiss|collection\.add|\.upsert|\.search\(|annoy|index\.add)", line_s, re.IGNORECASE):
            patterns["vector_db"] = True
        if re.search(r"(np\.|numpy|linalg|eigenvalue|eigenvector|matrix|dot\(|cross\(|norm\(|det\(|inv\(|svd\(|transpose|reshape)", line_s):
            patterns["math_ops"] = True
        if re.search(r"(tensor|torch\.|\.cuda|\.to\(device|tf\.|\.numpy\(\)|\.detach\(|requires_grad|nn\.)", line_s):
            patterns["tensor_ops"] = True
        if re.search(r"(nn\.|Layer|Module|forward|backward|activation|relu|sigmoid|softmax|dropout|batch_norm|layer_norm)", line_s):
            patterns["neural_net"] = True
        if re.search(r"(loss|criterion|CrossEntropy|MSE|BCE|NLL|mse_loss|huber|focal)", line_s):
            patterns["loss_function"] = True
        if re.search(r"(optimizer|optim\.|Adam|SGD|AdamW|RMSprop|lr_scheduler|learning_rate|weight_decay)", line_s):
            patterns["optimizer"] = True
        if re.search(r"(StandardScaler|MinMaxScaler|Normalizer|LabelEncoder|OneHotEncoder|train_test_split|ColumnTransformer|FeatureUnion)", line_s):
            patterns["data_transform"] = True
        if re.search(r"^print\(", line_s):
            patterns["print_output"] = True
        if re.search(r"^[a-zA-Z_]\w*\s*=\s*", line_s) and not re.match(r"^(import|from|def|class|for|while|if|elif|else|try|except|with)", line_s):
            patterns["variable_assignment"] = True
        if re.search(r"(try:|except|raise|finally:)", line_s):
            patterns["exception_handling"] = True
        if re.match(r"^@", line_s):
            patterns["decorator"] = True
        if re.search(r"\[.*\bfor\b.*\bin\b.*\]|\{.*\bfor\b.*\bin\b.*\}|\(.*\bfor\b.*\bin\b.*\)", line_s):
            patterns["comprehension"] = True
        if re.search(r"(assert\s+)", line_s):
            patterns["assertion"] = True
        if re.search(r"(os\.environ|getenv|load_dotenv|%env|%set_env|!pip|!conda|%pip|%conda|warnings\.filter)", line_s):
            patterns["env_setup"] = True

    return patterns


def extract_comments(code: str) -> list[str]:
    """Extract meaningful comments from code."""
    comments = []
    for line in code.split("\n"):
        stripped = line.strip()
        if stripped.startswith("#") and len(stripped) > 3:
            comment = stripped.lstrip("#").strip()
            if comment and not comment.startswith("!") and not comment.startswith("%%"):
                comments.append(comment)
    return comments


def generate_explanation(code: str, patterns: dict, topic: str, prev_code: str = "") -> str:
    """Generate a contextual markdown explanation for a code cell."""
    comments = extract_comments(code)
    imports = analyze_imports(code)
    lines = [l.strip() for l in code.split("\n") if l.strip() and not l.strip().startswith("#")]

    # Build explanation based on detected patterns
    parts = []

    # --- Import cells ---
    if patterns["imports"] and not any(
        patterns[k] for k in patterns if k != "imports" and k != "env_setup" and k != "variable_assignment" and patterns[k]
    ):
        lib_descs = []
        for lib in imports:
            desc = LIBRARY_DESCRIPTIONS.get(lib, None)
            if desc:
                lib_descs.append(f"- **{lib}**: {desc}")
            else:
                lib_descs.append(f"- **{lib}**")

        if lib_descs:
            parts.append("### Import Required Libraries\n")
            parts.append("Load the libraries needed for this section:\n")
            parts.append("\n".join(lib_descs))
        else:
            parts.append("### Setup\n")
            parts.append("Import the required modules.")
        return "\n".join(parts)

    # --- Environment setup ---
    if patterns["env_setup"] and not any(
        patterns[k] for k in ["model_creation", "model_training", "visualization"]
        if patterns[k]
    ):
        parts.append("### Environment Setup\n")
        if "load_dotenv" in code or "environ" in code:
            parts.append("Configure environment variables and API keys needed for this notebook.")
        elif "pip" in code or "conda" in code:
            parts.append("Install or update the Python packages required for this section.")
        elif "warnings" in code:
            parts.append("Configure warning settings to keep the output clean.")
        else:
            parts.append("Set up the runtime environment and configuration.")
        return "\n".join(parts)

    # --- Simple expression (like `1+1`, `x`, `s[2]`) ---
    if patterns["simple_expression"] and len(lines) == 1:
        expr = lines[0]
        if re.match(r"^\d+\s*[\+\-\*\/\%\*]+\s*\d+$", expr):
            parts.append(f"Evaluate the arithmetic expression `{expr}` — Python returns the result directly when an expression is the last line of a cell.")
        elif re.match(r"^[a-zA-Z_]\w*$", expr):
            parts.append(f"Display the current value of `{expr}` — Jupyter automatically prints the value of the last expression in a cell.")
        elif "[" in expr:
            parts.append(f"Access an element or slice using indexing — `{expr}`. Python uses zero-based indexing, so the first element is at index 0.")
        else:
            parts.append(f"Evaluate the expression `{expr}` and display the result.")
        return "\n".join(parts)

    # --- Function definitions ---
    if patterns["function_def"]:
        func_names = re.findall(r"(?:async\s+)?def\s+(\w+)", code)
        if func_names:
            if len(func_names) == 1:
                parts.append(f"### Define the `{func_names[0]}` Function\n")
            else:
                parts.append(f"### Define Helper Functions\n")
            if comments:
                parts.append(" ".join(comments[:3]))
            else:
                parts.append(f"Define {'these utility functions' if len(func_names) > 1 else 'a function'} that will be used in subsequent cells:")
                for fn in func_names:
                    readable = fn.replace("_", " ")
                    parts.append(f"- `{fn}()`: {readable}")

        return "\n".join(parts)

    # --- Class definitions ---
    if patterns["class_def"]:
        class_names = re.findall(r"class\s+(\w+)", code)
        if class_names:
            if len(class_names) == 1:
                parts.append(f"### Define the `{class_names[0]}` Class\n")
            else:
                parts.append(f"### Define Classes\n")
            if comments:
                parts.append(" ".join(comments[:3]))
            else:
                for cn in class_names:
                    readable = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", cn).lower()
                    parts.append(f"- `{cn}`: {readable}")
        return "\n".join(parts)

    # --- Data loading ---
    if patterns["data_loading"]:
        parts.append("### Load the Data\n")
        if comments:
            parts.append(" ".join(comments[:2]))
        else:
            parts.append(f"Read the dataset into memory for analysis. This is a common first step in any {topic} workflow — loading raw data so we can explore, clean, and model it.")
        return "\n".join(parts)

    # --- Visualization ---
    if patterns["visualization"] and not patterns["model_training"]:
        parts.append("### Visualize the Results\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            if patterns["dataframe_ops"]:
                parts.append("Create a visualization of the data to identify patterns, trends, and potential outliers. Visual exploration is critical before modeling.")
            elif patterns["math_ops"]:
                parts.append("Plot the mathematical concepts to build geometric intuition. Visualizing abstract math helps connect formulas to their real-world meaning.")
            elif patterns["neural_net"] or patterns["loss_function"]:
                parts.append("Visualize the training progress and model behavior. Monitoring loss curves and metrics helps diagnose issues like overfitting or underfitting.")
            else:
                parts.append(f"Create a chart to visualize the results. In {topic}, plots help us understand data distributions, model performance, and key relationships at a glance.")
        return "\n".join(parts)

    # --- Model training ---
    if patterns["model_training"]:
        parts.append("### Train the Model\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            if patterns["neural_net"] or patterns["tensor_ops"]:
                parts.append("Run the training loop — the model processes batches of data, computes the loss, and updates its weights via backpropagation. Each epoch iterates over the full dataset.")
            else:
                parts.append(f"Fit the model to our training data. The `.fit()` method learns patterns from the features (X) and target (y) by adjusting internal parameters to minimize prediction error.")
        return "\n".join(parts)

    # --- Model creation ---
    if patterns["model_creation"]:
        parts.append("### Build the Model\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            if patterns["neural_net"]:
                parts.append("Define the neural network architecture — specifying layers, activation functions, and connections. The architecture determines what patterns the model can learn.")
            else:
                parts.append(f"Instantiate the model with its hyperparameters. Choosing the right algorithm and settings is a key decision in any {topic} pipeline.")
        return "\n".join(parts)

    # --- Model prediction / inference ---
    if patterns["model_prediction"]:
        parts.append("### Generate Predictions\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Use the trained model to make predictions on new data. The model applies what it learned during training to produce outputs for unseen inputs.")
        return "\n".join(parts)

    # --- Evaluation ---
    if patterns["evaluation"]:
        parts.append("### Evaluate Model Performance\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Measure how well the model performs using standard metrics. Evaluation tells us whether the model generalizes well to unseen data or is overfitting to the training set.")
        return "\n".join(parts)

    # --- Loss function setup ---
    if patterns["loss_function"] and patterns["optimizer"]:
        parts.append("### Configure Loss Function and Optimizer\n")
        parts.append("Set up the loss function (which measures how far predictions are from targets) and the optimizer (which adjusts model weights to minimize that loss). These two components drive the entire training process.")
        return "\n".join(parts)

    # --- Data transformation / preprocessing ---
    if patterns["data_transform"]:
        parts.append("### Preprocess the Data\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Transform the raw data into a format suitable for modeling. Preprocessing steps like scaling, encoding, and splitting are essential — models perform better when features are on comparable scales and categorical values are properly encoded.")
        return "\n".join(parts)

    # --- DataFrame operations ---
    if patterns["dataframe_ops"]:
        parts.append("### Data Manipulation\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append(f"Process and transform the data using Pandas operations. In {topic}, clean and well-structured data is the foundation of accurate analysis.")
        return "\n".join(parts)

    # --- Tokenization ---
    if patterns["tokenization"]:
        parts.append("### Tokenization\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Tokenize the text — breaking it into smaller units (tokens) that the model can process. Tokenization is the critical first step in any NLP pipeline, converting human-readable text into numerical IDs the model understands.")
        return "\n".join(parts)

    # --- Embeddings ---
    if patterns["embedding"]:
        parts.append("### Compute Embeddings\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Generate vector embeddings — dense numerical representations that capture semantic meaning. Similar texts produce similar vectors, enabling tasks like search, clustering, and recommendation.")
        return "\n".join(parts)

    # --- Vector database ---
    if patterns["vector_db"]:
        parts.append("### Vector Database Operations\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Interact with the vector database to store or retrieve embeddings. Vector databases enable fast similarity search over millions of high-dimensional vectors.")
        return "\n".join(parts)

    # --- API calls ---
    if patterns["api_call"]:
        parts.append("### API Interaction\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Make an API call to interact with an external service. This pattern is common when working with hosted models, data sources, or cloud services.")
        return "\n".join(parts)

    # --- Math operations ---
    if patterns["math_ops"] and not patterns["visualization"]:
        parts.append("### Mathematical Operations\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append(f"Perform numerical computations that underpin the {topic} concepts covered in this section. Understanding the math builds intuition for how algorithms work under the hood.")
        return "\n".join(parts)

    # --- Tensor operations ---
    if patterns["tensor_ops"]:
        parts.append("### Tensor Operations\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Work with tensors — the fundamental data structure in deep learning frameworks. Tensors are multi-dimensional arrays that flow through neural network layers during forward and backward passes.")
        return "\n".join(parts)

    # --- File I/O ---
    if patterns["file_io"]:
        parts.append("### File Operations\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Read from or write to files on disk. File I/O is essential for loading data, saving model checkpoints, and persisting results.")
        return "\n".join(parts)

    # --- Exception handling ---
    if patterns["exception_handling"]:
        parts.append("### Error Handling\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Use try/except blocks to handle potential errors gracefully. Robust error handling prevents the program from crashing on edge cases and provides informative feedback.")
        return "\n".join(parts)

    # --- Loops ---
    if patterns["loop"] and not any(patterns[k] for k in ["model_training", "visualization", "dataframe_ops"]):
        parts.append("### Iterative Processing\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Use a loop to process items one at a time. Iteration is a core programming pattern for applying operations to sequences of data.")
        return "\n".join(parts)

    # --- Comprehensions ---
    if patterns["comprehension"]:
        parts.append("### Data Transformation\n")
        if comments:
            parts.append(" ".join(comments[:3]))
        else:
            parts.append("Use a Python comprehension — a concise, readable way to create new lists, dicts, or sets by transforming and filtering existing data in a single expression.")
        return "\n".join(parts)

    # --- Variable assignment with context ---
    if patterns["variable_assignment"] and patterns["print_output"]:
        if comments:
            parts.append(f"### {comments[0]}\n")
            parts.append(" ".join(comments[1:3]) if len(comments) > 1 else "Define variables and print their values to verify the results.")
        else:
            parts.append(f"Set up variables and display their values to verify the output. In {topic}, printing intermediate results helps confirm each step works as expected.")
        return "\n".join(parts)

    # --- Fallback: use comments if available ---
    if comments:
        # Use the first comment as a heading if it's descriptive enough
        heading = comments[0]
        if len(heading) > 10:
            parts.append(f"### {heading}\n")
            if len(comments) > 1:
                parts.append(" ".join(comments[1:3]))
            else:
                parts.append(f"The code below implements this step in the {topic} workflow.")
        else:
            parts.append(f"### {heading}\n")
            parts.append(f"Execute this step in the {topic} pipeline.")
        return "\n".join(parts)

    # --- Fallback: generic but topic-aware ---
    if patterns["print_output"]:
        parts.append(f"Display output to verify the results of the operation above. Printing intermediate values is a good practice for understanding data flow in {topic}.")
    elif patterns["variable_assignment"]:
        parts.append(f"Set up the variables needed for the next step. This prepares the data or configuration for subsequent operations in this {topic} workflow.")
    elif patterns["string_ops"]:
        parts.append("Perform string manipulation — processing text data is a fundamental skill in Python, especially for NLP and data cleaning tasks.")
    elif patterns["list_ops"]:
        parts.append("Work with Python lists — ordered, mutable collections that are one of Python's most versatile data structures for storing and processing sequences of items.")
    elif patterns["dict_ops"]:
        parts.append("Work with Python dictionaries — key-value stores that provide fast lookups and are widely used for configuration, data mapping, and JSON-like data.")
    elif patterns["conditional"]:
        parts.append("Use conditional logic to branch execution based on specific conditions. This is how programs make decisions and handle different scenarios.")
    else:
        parts.append(f"Execute the next step in this {topic} workflow. Run this cell to see the output and proceed to the following section.")

    return "\n".join(parts)


def has_adequate_explanation(cells: list, idx: int) -> bool:
    """Check if a code cell at idx has an adequate preceding markdown explanation."""
    if idx == 0:
        return False

    prev = cells[idx - 1]
    if prev.get("cell_type") != "markdown":
        return False

    md_source = "".join(prev.get("source", []))
    md_lines = [l.strip() for l in md_source.split("\n") if l.strip()]

    # Consider it explained if there's at least 2 non-empty lines
    # or a single line with meaningful content (>50 chars)
    if len(md_lines) >= 2:
        return True
    if len(md_lines) == 1 and len(md_lines[0]) > 50:
        return True

    return False


def process_notebook(nb_path: Path, topic: str) -> tuple[int, int]:
    """Process a single notebook: add explanations where missing. Returns (cells_added, total_code_cells)."""
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    if not cells:
        return 0, 0

    new_cells = []
    cells_added = 0
    total_code_cells = 0
    prev_code = ""

    for i, cell in enumerate(cells):
        if cell.get("cell_type") == "code":
            total_code_cells += 1
            source = "".join(cell.get("source", []))

            if not source.strip():
                new_cells.append(cell)
                continue

            if not has_adequate_explanation(cells, i):
                patterns = detect_code_patterns(source)
                explanation = generate_explanation(source, patterns, topic, prev_code)

                if explanation:
                    # Create a new markdown cell
                    md_cell = {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [explanation]
                    }
                    new_cells.append(md_cell)
                    cells_added += 1

            prev_code = source

        new_cells.append(cell)

    if cells_added > 0:
        nb["cells"] = new_cells
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write("\n")

    return cells_added, total_code_cells


def main():
    # Load the audit report to know which notebooks need work
    report_path = WORKSPACE / "scripts" / "audit_report.json"
    with open(report_path, "r") as f:
        audit = json.load(f)

    # Process all notebooks that need work (source + docs mirrors)
    source_notebooks = audit

    print(f"Processing {len(source_notebooks)} notebooks...\n")

    total_added = 0
    total_notebooks_modified = 0

    for rel_path in sorted(source_notebooks.keys()):
        nb_path = WORKSPACE / rel_path
        if not nb_path.exists():
            print(f"  SKIP (not found): {rel_path}")
            continue

        topic = get_notebook_topic(rel_path)

        try:
            added, total = process_notebook(nb_path, topic)
            if added > 0:
                total_notebooks_modified += 1
                total_added += added
                print(f"  Added {added:3d} explanations: {rel_path}")
        except (json.JSONDecodeError, KeyError, Exception) as e:
            print(f"  ERROR: {rel_path}: {e}")

    print(f"\n{'=' * 60}")
    print(f"Summary: Added {total_added} explanation cells across {total_notebooks_modified} notebooks")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
