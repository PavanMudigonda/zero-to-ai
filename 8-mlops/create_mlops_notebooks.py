#!/usr/bin/env python3
"""Create MLOps notebook series"""

import json
import os

def nb(cells):
    """Create notebook structure"""
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

def md(text):
    """Create markdown cell"""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.split("\n")]
    }

def code(text):
    """Create code cell"""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in text.split("\n")]
    }

def save_notebook(filename, cells):
    """Save notebook to file"""
    with open(filename, 'w') as f:
        json.dump(nb(cells), f, indent=2)

# Notebook 00: START HERE - MLOps Overview
notebook_00 = [
    md("# MLOps: Machine Learning in Production\n\n## 🎯 What You'll Learn\n\nThis series covers the complete MLOps lifecycle:\n1. **Experiment Tracking** - MLflow, Weights & Biases\n2. **API Development** - FastAPI for model serving\n3. **Deployment** - Docker, cloud platforms\n4. **Monitoring** - Observability and alerts\n5. **CI/CD** - Automated ML pipelines\n6. **Production Best Practices** - Scalability, reliability\n\n## Why MLOps?\n\n**The Problem:** Most ML models never make it to production\n- Jupyter notebooks are great for experimentation\n- But production requires different skills\n- Need to handle scale, reliability, monitoring\n\n**The Solution:** MLOps practices\n- Version control for models and data\n- Automated testing and deployment\n- Continuous monitoring and improvement"),
    
    md("## The MLOps Lifecycle\n\n```\n┌─────────────────────────────────────────────────────┐\n│                   ML LIFECYCLE                      │\n├─────────────────────────────────────────────────────┤\n│                                                     │\n│  Data → Experiment → Train → Evaluate → Deploy     │\n│   ↑                                          ↓      │\n│   └────────────── Monitor & Retrain ─────────┘      │\n│                                                     │\n└─────────────────────────────────────────────────────┘\n```\n\n### Key Components\n\n1. **Experiment Tracking**\n   - Log hyperparameters, metrics, artifacts\n   - Compare different runs\n   - Reproduce experiments\n\n2. **Model Registry**\n   - Version control for models\n   - Track model lineage\n   - Manage staging/production models\n\n3. **Model Serving**\n   - REST APIs (FastAPI, Flask)\n   - Batch predictions\n   - Real-time inference\n\n4. **Monitoring**\n   - Model performance metrics\n   - Data drift detection\n   - System health (latency, errors)"),
    
    md("## Quick Demo: Simple ML API\n\nLet's build a minimal model serving API:"),
    
    code("# Install dependencies (uncomment to run)\n# !pip install fastapi uvicorn scikit-learn joblib"),
    
    code("# Simple model training\nfrom sklearn.datasets import load_iris\nfrom sklearn.ensemble import RandomForestClassifier\nimport joblib\n\n# Train model\niris = load_iris()\nmodel = RandomForestClassifier(n_estimators=10, random_state=42)\nmodel.fit(iris.data, iris.target)\n\n# Save model\njoblib.dump(model, 'iris_model.pkl')\nprint(\"✓ Model trained and saved\")"),
    
    code("# Create FastAPI application\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\nimport joblib\nimport numpy as np\n\napp = FastAPI(title=\"Iris Classifier API\")\n\n# Load model\nmodel = joblib.load('iris_model.pkl')\n\nclass PredictionRequest(BaseModel):\n    sepal_length: float\n    sepal_width: float\n    petal_length: float\n    petal_width: float\n\nclass PredictionResponse(BaseModel):\n    species: str\n    confidence: float\n\n@app.post(\"/predict\", response_model=PredictionResponse)\nasync def predict(request: PredictionRequest):\n    # Prepare features\n    features = np.array([[\n        request.sepal_length,\n        request.sepal_width,\n        request.petal_length,\n        request.petal_width\n    ]])\n    \n    # Predict\n    prediction = model.predict(features)[0]\n    probabilities = model.predict_proba(features)[0]\n    \n    species_names = ['setosa', 'versicolor', 'virginica']\n    \n    return PredictionResponse(\n        species=species_names[prediction],\n        confidence=float(probabilities[prediction])\n    )\n\n@app.get(\"/health\")\nasync def health():\n    return {\"status\": \"healthy\"}\n\nprint(\"✓ API created\")\nprint(\"Run with: uvicorn main:app --reload\")"),
    
    md("## Testing the API\n\nTo test this API:\n\n```bash\n# Start server\nuvicorn main:app --reload\n\n# Test with curl\ncurl -X POST \"http://localhost:8000/predict\" \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\"sepal_length\": 5.1, \"sepal_width\": 3.5, \"petal_length\": 1.4, \"petal_width\": 0.2}'\n```\n\nOr visit: http://localhost:8000/docs for interactive API documentation"),
    
    md("## What's Next?\n\nIn the following notebooks, you'll learn:\n\n1. **Experiment Tracking** - Track and compare models\n2. **FastAPI Deep Dive** - Advanced API features\n3. **Model Deployment** - Production serving strategies\n4. **Docker** - Containerize your applications\n5. **Monitoring** - Observe model behavior in production\n6. **CI/CD** - Automate your ML pipeline\n7. **Cloud Deployment** - Deploy to AWS/Azure/GCP\n\n🚀 Ready to take ML to production!")
]

# Notebook 01: Experiment Tracking
notebook_01 = [
    md("# Experiment Tracking with MLflow\n\n## 🎯 Learning Objectives\n\n- Track ML experiments systematically\n- Log parameters, metrics, and artifacts\n- Compare different model runs\n- Register and version models\n- Reproduce experiments\n\n## Why Track Experiments?\n\n**Without tracking:**\n- \"Which hyperparameters gave the best result?\"\n- \"Can we reproduce last week's model?\"\n- \"What changed between version 1 and 2?\"\n\n**With tracking:**\n- All experiments logged automatically\n- Easy comparison of runs\n- Model versioning and lineage\n- Reproducible results"),
    
    code("# Install MLflow\n# !pip install mlflow scikit-learn"),
    
    md("## Basic MLflow Usage"),
    
    code("import mlflow\nimport mlflow.sklearn\nfrom sklearn.datasets import load_wine\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import accuracy_score, f1_score\nimport numpy as np\n\n# Load data\nwine = load_wine()\nX_train, X_test, y_train, y_test = train_test_split(\n    wine.data, wine.target, test_size=0.2, random_state=42\n)\n\nprint(\"Data loaded:\", X_train.shape)"),
    
    md("## Experiment 1: Baseline Model"),
    
    code("# Start MLflow run\nwith mlflow.start_run(run_name=\"baseline_rf\"):\n    # Set hyperparameters\n    n_estimators = 50\n    max_depth = 5\n    \n    # Log parameters\n    mlflow.log_param(\"n_estimators\", n_estimators)\n    mlflow.log_param(\"max_depth\", max_depth)\n    mlflow.log_param(\"model_type\", \"RandomForest\")\n    \n    # Train model\n    model = RandomForestClassifier(\n        n_estimators=n_estimators,\n        max_depth=max_depth,\n        random_state=42\n    )\n    model.fit(X_train, y_train)\n    \n    # Evaluate\n    y_pred = model.predict(X_test)\n    accuracy = accuracy_score(y_test, y_pred)\n    f1 = f1_score(y_test, y_pred, average='weighted')\n    \n    # Log metrics\n    mlflow.log_metric(\"accuracy\", accuracy)\n    mlflow.log_metric(\"f1_score\", f1)\n    \n    # Log model\n    mlflow.sklearn.log_model(model, \"model\")\n    \n    print(f\"Baseline - Accuracy: {accuracy:.4f}, F1: {f1:.4f}\")"),
    
    md("## Experiment 2: Hyperparameter Tuning"),
    
    code("# Try different hyperparameters\nfor n_est in [50, 100, 200]:\n    for depth in [5, 10, 15]:\n        with mlflow.start_run(run_name=f\"rf_nest{n_est}_depth{depth}\"):\n            # Log params\n            mlflow.log_param(\"n_estimators\", n_est)\n            mlflow.log_param(\"max_depth\", depth)\n            mlflow.log_param(\"model_type\", \"RandomForest\")\n            \n            # Train\n            model = RandomForestClassifier(\n                n_estimators=n_est,\n                max_depth=depth,\n                random_state=42\n            )\n            model.fit(X_train, y_train)\n            \n            # Evaluate\n            y_pred = model.predict(X_test)\n            accuracy = accuracy_score(y_test, y_pred)\n            f1 = f1_score(y_test, y_pred, average='weighted')\n            \n            # Log metrics\n            mlflow.log_metric(\"accuracy\", accuracy)\n            mlflow.log_metric(\"f1_score\", f1)\n            \n            # Log model\n            mlflow.sklearn.log_model(model, \"model\")\n            \n            print(f\"n={n_est}, depth={depth}: Acc={accuracy:.4f}\")"),
    
    md("## Viewing Results\n\n### MLflow UI\n\nLaunch the MLflow UI to compare experiments:\n\n```bash\nmlflow ui\n```\n\nThen visit: http://localhost:5000\n\n### Features:\n- Compare metrics across runs\n- Visualize parameter vs metric relationships\n- View logged artifacts\n- Download models"),
    
    md("## Model Registry\n\nRegister the best model for production:"),
    
    code("# Register model (after finding best run)\nmodel_name = \"wine_classifier\"\n\n# This would be done in the MLflow UI or programmatically:\n# mlflow.register_model(\n#     model_uri=f\"runs:/<run_id>/model\",\n#     name=model_name\n# )\n\n# Transition model to production\n# client = mlflow.tracking.MlflowClient()\n# client.transition_model_version_stage(\n#     name=model_name,\n#     version=1,\n#     stage=\"Production\"\n# )\n\nprint(\"Model registered and promoted to production\")"),
    
    md("## Advanced: Autologging\n\nMLflow can automatically log parameters, metrics, and models:"),
    
    code("# Enable autologging\nmlflow.sklearn.autolog()\n\nwith mlflow.start_run(run_name=\"autolog_example\"):\n    model = RandomForestClassifier(n_estimators=100, random_state=42)\n    model.fit(X_train, y_train)\n    \n    # MLflow automatically logs:\n    # - All hyperparameters\n    # - Training metrics\n    # - Model artifacts\n    # - Feature importance\n    \n    print(\"✓ Everything logged automatically!\")"),
    
    md("## Best Practices\n\n1. **Consistent naming**: Use descriptive run names\n2. **Log everything**: Parameters, metrics, datasets, code\n3. **Tag runs**: Add tags for easy filtering\n4. **Document**: Add notes about each experiment\n5. **Clean up**: Delete failed or duplicate runs\n\n## Key Takeaways\n\n✅ Track all experiments systematically\n✅ Log parameters, metrics, and artifacts\n✅ Use MLflow UI for comparison\n✅ Register production-ready models\n✅ Enable autologging when possible")
]

# Notebook 02: FastAPI Basics
notebook_02 = [
    md("# Building ML APIs with FastAPI\n\n## 🎯 Learning Objectives\n\n- Build REST APIs for ML models\n- Handle request validation\n- Create API documentation\n- Implement async endpoints\n- Add authentication and error handling\n\n## Why FastAPI?\n\n- **Fast**: High performance (comparable to NodeJS/Go)\n- **Easy**: Intuitive Python syntax\n- **Auto-docs**: Swagger UI out of the box\n- **Type safety**: Pydantic validation\n- **Async**: Native async/await support"),
    
    code("# Install dependencies\n# !pip install fastapi uvicorn pydantic"),
    
    md("## Hello World API"),
    
    code("from fastapi import FastAPI\n\napp = FastAPI(title=\"My First ML API\")\n\n@app.get(\"/\")\nasync def root():\n    return {\"message\": \"Hello, MLOps!\"}\n\n@app.get(\"/health\")\nasync def health_check():\n    return {\"status\": \"healthy\"}\n\nprint(\"API created!\")\nprint(\"Run with: uvicorn main:app --reload\")"),
    
    md("## Request/Response Models with Pydantic"),
    
    code("from pydantic import BaseModel, Field\nfrom typing import List\n\nclass TextInput(BaseModel):\n    text: str = Field(..., min_length=1, max_length=1000)\n    language: str = Field(default=\"en\")\n\nclass SentimentOutput(BaseModel):\n    label: str\n    confidence: float\n    scores: dict\n\n# Example usage\nsample_input = TextInput(\n    text=\"FastAPI is amazing!\",\n    language=\"en\"\n)\n\nprint(sample_input.model_dump())"),
    
    md("## ML Model Endpoint"),
    
    code("from fastapi import FastAPI, HTTPException\nfrom pydantic import BaseModel\nimport numpy as np\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.naive_bayes import MultinomialNB\nimport joblib\n\napp = FastAPI(title=\"Sentiment Analysis API\")\n\n# Mock training data\ntrain_texts = [\n    \"I love this product\",\n    \"This is amazing\",\n    \"Terrible experience\",\n    \"Very disappointing\"\n]\ntrain_labels = [1, 1, 0, 0]  # 1=positive, 0=negative\n\n# Train simple model\nvectorizer = TfidfVectorizer(max_features=100)\nX_train = vectorizer.fit_transform(train_texts)\nmodel = MultinomialNB()\nmodel.fit(X_train, train_labels)\n\nprint(\"✓ Model trained\")\n\nclass TextRequest(BaseModel):\n    text: str\n\nclass SentimentResponse(BaseModel):\n    sentiment: str\n    confidence: float\n\n@app.post(\"/predict\", response_model=SentimentResponse)\nasync def predict_sentiment(request: TextRequest):\n    try:\n        # Vectorize input\n        X = vectorizer.transform([request.text])\n        \n        # Predict\n        prediction = model.predict(X)[0]\n        probabilities = model.predict_proba(X)[0]\n        \n        sentiment = \"positive\" if prediction == 1 else \"negative\"\n        confidence = float(probabilities[prediction])\n        \n        return SentimentResponse(\n            sentiment=sentiment,\n            confidence=confidence\n        )\n    except Exception as e:\n        raise HTTPException(status_code=500, detail=str(e))\n\nprint(\"✓ Sentiment endpoint created\")"),
    
    md("## Batch Predictions"),
    
    code("from typing import List\n\nclass BatchRequest(BaseModel):\n    texts: List[str]\n\nclass BatchResponse(BaseModel):\n    predictions: List[SentimentResponse]\n\n@app.post(\"/batch_predict\", response_model=BatchResponse)\nasync def batch_predict(request: BatchRequest):\n    predictions = []\n    \n    for text in request.texts:\n        X = vectorizer.transform([text])\n        pred = model.predict(X)[0]\n        proba = model.predict_proba(X)[0]\n        \n        predictions.append(SentimentResponse(\n            sentiment=\"positive\" if pred == 1 else \"negative\",\n            confidence=float(proba[pred])\n        ))\n    \n    return BatchResponse(predictions=predictions)\n\nprint(\"✓ Batch endpoint created\")"),
    
    md("## Error Handling"),
    
    code("from fastapi import HTTPException, status\n\n@app.post(\"/predict_with_validation\")\nasync def predict_with_validation(request: TextRequest):\n    # Validate input\n    if len(request.text) < 3:\n        raise HTTPException(\n            status_code=status.HTTP_400_BAD_REQUEST,\n            detail=\"Text must be at least 3 characters\"\n        )\n    \n    if len(request.text) > 1000:\n        raise HTTPException(\n            status_code=status.HTTP_400_BAD_REQUEST,\n            detail=\"Text too long (max 1000 characters)\"\n        )\n    \n    # Process request\n    X = vectorizer.transform([request.text])\n    prediction = model.predict(X)[0]\n    \n    return {\n        \"sentiment\": \"positive\" if prediction == 1 else \"negative\"\n    }"),
    
    md("## API Documentation\n\nFastAPI automatically generates interactive documentation:\n\n- **Swagger UI**: http://localhost:8000/docs\n- **ReDoc**: http://localhost:8000/redoc\n\nNo extra work needed!"),
    
    md("## Running the API\n\n```bash\n# Development mode (auto-reload)\nuvicorn main:app --reload\n\n# Production mode\nuvicorn main:app --host 0.0.0.0 --port 8000 --workers 4\n```"),
    
    md("## Testing the API\n\n```bash\n# Using curl\ncurl -X POST \"http://localhost:8000/predict\" \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\"text\": \"This is fantastic!\"}'\n\n# Using Python\nimport requests\n\nresponse = requests.post(\n    \"http://localhost:8000/predict\",\n    json={\"text\": \"This is fantastic!\"}\n)\n\nprint(response.json())\n```"),
    
    md("## Best Practices\n\n1. **Use Pydantic models** for request/response validation\n2. **Add proper error handling** with HTTPException\n3. **Implement health checks** for monitoring\n4. **Use async/await** for I/O operations\n5. **Add API versioning** (/v1/predict, /v2/predict)\n6. **Document endpoints** with docstrings\n7. **Add rate limiting** for production\n8. **Implement authentication** for security\n\n## Key Takeaways\n\n✅ FastAPI makes building ML APIs simple\n✅ Pydantic ensures type safety and validation\n✅ Auto-generated docs save time\n✅ Async support for better performance\n✅ Ready for production with proper error handling")
]

# Notebook 03: Model Deployment
notebook_03 = [
    md("# Model Deployment Strategies\n\n## 🎯 Learning Objectives\n\n- Understand deployment patterns\n- Implement model versioning\n- Handle model updates safely\n- Monitor model performance\n- Scale serving infrastructure\n\n## Deployment Patterns\n\n### 1. Blue-Green Deployment\n```\nBlue (v1)  ────────┐\n                   ├──→ Load Balancer → Users\nGreen (v2) ────────┘\n                   ↑\n              Switch traffic\n```\n\n### 2. Canary Deployment\n```\nOld (v1):  90% traffic\nNew (v2):  10% traffic → Monitor → 100% if good\n```\n\n### 3. A/B Testing\n```\nModel A: 50% users → Compare metrics\nModel B: 50% users → Choose winner\n```"),
    
    code("# Install dependencies\n# !pip install fastapi uvicorn joblib scikit-learn"),
    
    md("## Model Versioning"),
    
    code("import joblib\nimport os\nfrom datetime import datetime\nfrom pathlib import Path\n\nclass ModelRegistry:\n    \"\"\"Simple model registry for versioning\"\"\"\n    \n    def __init__(self, base_path=\"models\"):\n        self.base_path = Path(base_path)\n        self.base_path.mkdir(exist_ok=True)\n    \n    def save_model(self, model, model_name, version=None):\n        \"\"\"Save model with version\"\"\"\n        if version is None:\n            version = datetime.now().strftime(\"%Y%m%d_%H%M%S\")\n        \n        model_path = self.base_path / model_name / version\n        model_path.mkdir(parents=True, exist_ok=True)\n        \n        # Save model\n        model_file = model_path / \"model.pkl\"\n        joblib.dump(model, model_file)\n        \n        # Save metadata\n        metadata = {\n            \"version\": version,\n            \"created_at\": datetime.now().isoformat(),\n            \"model_type\": type(model).__name__\n        }\n        \n        import json\n        with open(model_path / \"metadata.json\", \"w\") as f:\n            json.dump(metadata, f, indent=2)\n        \n        print(f\"✓ Model saved: {model_name}/{version}\")\n        return version\n    \n    def load_model(self, model_name, version=\"latest\"):\n        \"\"\"Load specific model version\"\"\"\n        model_dir = self.base_path / model_name\n        \n        if version == \"latest\":\n            # Get latest version\n            versions = sorted(os.listdir(model_dir))\n            version = versions[-1] if versions else None\n        \n        if version is None:\n            raise ValueError(f\"No versions found for {model_name}\")\n        \n        model_path = model_dir / version / \"model.pkl\"\n        model = joblib.load(model_path)\n        \n        print(f\"✓ Loaded: {model_name}/{version}\")\n        return model\n    \n    def list_versions(self, model_name):\n        \"\"\"List all versions of a model\"\"\"\n        model_dir = self.base_path / model_name\n        if not model_dir.exists():\n            return []\n        return sorted(os.listdir(model_dir))\n\n# Example usage\nregistry = ModelRegistry()\nprint(\"Model registry created\")"),
    
    md("## Deploying with Version Control"),
    
    code("from fastapi import FastAPI, HTTPException\nfrom pydantic import BaseModel\nimport numpy as np\n\napp = FastAPI(title=\"Versioned Model API\")\n\n# Initialize registry\nregistry = ModelRegistry()\n\nclass PredictionRequest(BaseModel):\n    features: list\n    model_version: str = \"latest\"\n\nclass PredictionResponse(BaseModel):\n    prediction: float\n    model_version: str\n\n@app.post(\"/predict\", response_model=PredictionResponse)\nasync def predict(request: PredictionRequest):\n    try:\n        # Load requested model version\n        model = registry.load_model(\n            \"iris_classifier\",\n            version=request.model_version\n        )\n        \n        # Predict\n        features = np.array(request.features).reshape(1, -1)\n        prediction = model.predict(features)[0]\n        \n        return PredictionResponse(\n            prediction=float(prediction),\n            model_version=request.model_version\n        )\n    except Exception as e:\n        raise HTTPException(status_code=500, detail=str(e))\n\n@app.get(\"/models/{model_name}/versions\")\nasync def list_model_versions(model_name: str):\n    versions = registry.list_versions(model_name)\n    return {\"model\": model_name, \"versions\": versions}\n\nprint(\"✓ Versioned API created\")"),
    
    md("## A/B Testing Framework"),
    
    code("import random\nfrom typing import Dict\n\nclass ABTestController:\n    \"\"\"Control A/B testing for models\"\"\"\n    \n    def __init__(self, registry: ModelRegistry):\n        self.registry = registry\n        self.experiments: Dict[str, dict] = {}\n    \n    def create_experiment(self, name, model_a, model_b, split=0.5):\n        \"\"\"Create new A/B test\"\"\"\n        self.experiments[name] = {\n            \"model_a\": model_a,\n            \"model_b\": model_b,\n            \"split\": split,  # % traffic to model_b\n            \"results\": {\"a\": [], \"b\": []}\n        }\n        print(f\"✓ Experiment '{name}' created\")\n    \n    def get_model(self, experiment_name):\n        \"\"\"Get model based on A/B split\"\"\"\n        exp = self.experiments[experiment_name]\n        \n        # Randomly assign to A or B\n        if random.random() < exp[\"split\"]:\n            variant = \"b\"\n            model_version = exp[\"model_b\"]\n        else:\n            variant = \"a\"\n            model_version = exp[\"model_a\"]\n        \n        model = self.registry.load_model(\"classifier\", model_version)\n        return model, variant\n    \n    def log_result(self, experiment_name, variant, metric_value):\n        \"\"\"Log experiment result\"\"\"\n        self.experiments[experiment_name][\"results\"][variant].append(metric_value)\n    \n    def get_results(self, experiment_name):\n        \"\"\"Get experiment results\"\"\"\n        results = self.experiments[experiment_name][\"results\"]\n        return {\n            \"model_a\": {\n                \"count\": len(results[\"a\"]),\n                \"mean\": np.mean(results[\"a\"]) if results[\"a\"] else 0\n            },\n            \"model_b\": {\n                \"count\": len(results[\"b\"]),\n                \"mean\": np.mean(results[\"b\"]) if results[\"b\"] else 0\n            }\n        }\n\n# Example\nab_controller = ABTestController(registry)\nab_controller.create_experiment(\n    \"sentiment_test\",\n    model_a=\"v1.0\",\n    model_b=\"v2.0\",\n    split=0.2  # 20% to new model\n)\nprint(\"A/B test configured\")"),
    
    md("## Canary Deployment"),
    
    code("class CanaryDeployment:\n    \"\"\"Gradual rollout controller\"\"\"\n    \n    def __init__(self, registry, model_name):\n        self.registry = registry\n        self.model_name = model_name\n        self.canary_percentage = 0  # Start at 0%\n        self.stable_version = None\n        self.canary_version = None\n    \n    def start_canary(self, stable_version, canary_version, initial_percentage=10):\n        \"\"\"Start canary deployment\"\"\"\n        self.stable_version = stable_version\n        self.canary_version = canary_version\n        self.canary_percentage = initial_percentage\n        print(f\"🐤 Canary started: {canary_percentage}% traffic to {canary_version}\")\n    \n    def increase_canary(self, increment=10):\n        \"\"\"Increase canary traffic\"\"\"\n        self.canary_percentage = min(100, self.canary_percentage + increment)\n        print(f\"�� Canary increased to {self.canary_percentage}%\")\n    \n    def rollback(self):\n        \"\"\"Rollback to stable version\"\"\"\n        self.canary_percentage = 0\n        print(f\"⏮️  Rolled back to {self.stable_version}\")\n    \n    def promote_canary(self):\n        \"\"\"Promote canary to stable\"\"\"\n        self.stable_version = self.canary_version\n        self.canary_percentage = 0\n        print(f\"✅ Promoted {self.canary_version} to stable\")\n    \n    def get_model(self):\n        \"\"\"Get model based on canary percentage\"\"\"\n        if random.random() * 100 < self.canary_percentage:\n            version = self.canary_version\n        else:\n            version = self.stable_version\n        \n        return self.registry.load_model(self.model_name, version)\n\n# Example\ncanary = CanaryDeployment(registry, \"classifier\")\ncanary.start_canary(stable_version=\"v1.0\", canary_version=\"v2.0\", initial_percentage=5)\nprint(\"Canary deployment ready\")"),
    
    md("## Monitoring Deployments"),
    
    code("from collections import defaultdict\nfrom datetime import datetime\n\nclass DeploymentMonitor:\n    \"\"\"Monitor model performance in production\"\"\"\n    \n    def __init__(self):\n        self.metrics = defaultdict(list)\n    \n    def log_prediction(self, model_version, latency_ms, success=True):\n        \"\"\"Log prediction metrics\"\"\"\n        self.metrics[model_version].append({\n            \"timestamp\": datetime.now(),\n            \"latency_ms\": latency_ms,\n            \"success\": success\n        })\n    \n    def get_stats(self, model_version):\n        \"\"\"Get model statistics\"\"\"\n        data = self.metrics[model_version]\n        if not data:\n            return None\n        \n        latencies = [d[\"latency_ms\"] for d in data]\n        successes = [d[\"success\"] for d in data]\n        \n        return {\n            \"total_requests\": len(data),\n            \"success_rate\": sum(successes) / len(successes),\n            \"avg_latency_ms\": np.mean(latencies),\n            \"p95_latency_ms\": np.percentile(latencies, 95),\n            \"p99_latency_ms\": np.percentile(latencies, 99)\n        }\n    \n    def check_health(self, model_version, max_latency_ms=100, min_success_rate=0.95):\n        \"\"\"Check if model is healthy\"\"\"\n        stats = self.get_stats(model_version)\n        if not stats:\n            return True\n        \n        if stats[\"avg_latency_ms\"] > max_latency_ms:\n            print(f\"⚠️  High latency: {stats['avg_latency_ms']:.2f}ms\")\n            return False\n        \n        if stats[\"success_rate\"] < min_success_rate:\n            print(f\"⚠️  Low success rate: {stats['success_rate']:.2%}\")\n            return False\n        \n        print(f\"✅ Model {model_version} is healthy\")\n        return True\n\nmonitor = DeploymentMonitor()\nprint(\"Deployment monitor created\")"),
    
    md("## Best Practices\n\n1. **Version Everything**\n   - Models\n   - Training data\n   - Code\n   - Dependencies\n\n2. **Test Before Deploy**\n   - Unit tests\n   - Integration tests\n   - Load tests\n   - Shadow testing\n\n3. **Deploy Gradually**\n   - Start with small percentage\n   - Monitor metrics closely\n   - Be ready to rollback\n\n4. **Monitor Continuously**\n   - Latency (p50, p95, p99)\n   - Error rate\n   - Model metrics\n   - Resource usage\n\n5. **Enable Rollback**\n   - Keep previous versions\n   - Automated rollback triggers\n   - Clear rollback procedures\n\n## Key Takeaways\n\n✅ Multiple deployment strategies available\n✅ Version control is critical\n✅ Gradual rollouts reduce risk\n✅ Continuous monitoring enables fast response\n✅ Always have a rollback plan")
]

print("Creating MLOps Notebooks...")
print("=" * 70)

save_notebook("00_START_HERE.ipynb", notebook_00)
print("✓ Notebook 00: START HERE - MLOps Overview")

save_notebook("01_experiment_tracking.ipynb", notebook_01)
print("✓ Notebook 01: Experiment Tracking with MLflow")

save_notebook("02_fastapi_basics.ipynb", notebook_02)
print("✓ Notebook 02: Building ML APIs with FastAPI")

save_notebook("03_model_deployment.ipynb", notebook_03)
print("✓ Notebook 03: Model Deployment Strategies")

print("=" * 70)
print("🎉 SUCCESS! Created 4 MLOps notebooks!")
print("\nNext: Run the remaining notebooks creation script")
