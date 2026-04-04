#!/usr/bin/env python3
"""
Enrich shallow/auto-generated markdown explanation cells in Jupyter notebooks
with deep conceptual explanations of the code that follows.

Detects auto-generated or thin explanation cells and replaces them with
rich, concept-driven explanations that teach *what* and *why*, not just labels.
"""

import json
import re
import sys
from pathlib import Path

WORKSPACE = Path("/Users/pavanmudigonda/code/zero-to-ai")

# ────────────────────────────────────────────────────────────────────
# CONCEPT EXPLANATIONS DATABASE
# Maps specific code patterns (functions, operations) to rich explanations
# ────────────────────────────────────────────────────────────────────

CONCEPT_EXPLANATIONS = {
    # ── Linear Algebra / NumPy ──────────────────────────────────────
    "np.dot": (
        "**Dot Product (Inner Product):** The dot product of two vectors measures how much "
        "they point in the same direction. It's computed by multiplying corresponding elements "
        "and summing the results:\n\n"
        "$$\\mathbf{a} \\cdot \\mathbf{b} = \\sum_{i} a_i \\times b_i$$\n\n"
        "- If the result is **positive**, the vectors point in roughly the same direction\n"
        "- If **zero**, the vectors are perpendicular (orthogonal)\n"
        "- If **negative**, they point in opposite directions\n\n"
        "In ML, dot products are everywhere: every neuron in a neural network computes "
        "a dot product of inputs with weights, and cosine similarity is built on it."
    ),
    "np.linalg.norm": (
        "**Vector Norm (Magnitude):** The norm measures the \"length\" of a vector — "
        "its distance from the origin. The L2 (Euclidean) norm is:\n\n"
        "$$\\|\\mathbf{v}\\|_2 = \\sqrt{v_1^2 + v_2^2 + \\cdots + v_n^2}$$\n\n"
        "**Normalizing** a vector (dividing by its norm) produces a **unit vector** — same "
        "direction but length 1. This is critical in ML for:\n"
        "- **Cosine similarity**: comparing direction, not magnitude\n"
        "- **Gradient clipping**: preventing exploding gradients\n"
        "- **Regularization**: L1 norm encourages sparsity, L2 norm prevents large weights"
    ),
    "np.linalg.eig": (
        "**Eigenvalues and Eigenvectors:** When a matrix $A$ multiplies an eigenvector $\\mathbf{v}$, "
        "it only *stretches* (or flips) the vector — it doesn't change its direction:\n\n"
        "$$A\\mathbf{v} = \\lambda\\mathbf{v}$$\n\n"
        "The eigenvalue $\\lambda$ tells you the stretch factor. Intuitively, eigenvectors "
        "reveal the matrix's \"natural axes\" — the directions along which it acts most simply.\n\n"
        "**ML applications:**\n"
        "- **PCA**: eigenvectors of the covariance matrix are the principal components\n"
        "- **Graph analysis**: eigenvectors of adjacency matrices reveal community structure\n"
        "- **Stability**: eigenvalues of the Hessian tell you if you're at a minimum"
    ),
    "np.linalg.inv": (
        "**Matrix Inverse:** For a square matrix $A$, its inverse $A^{-1}$ satisfies "
        "$A \\cdot A^{-1} = I$ (the identity matrix). Think of it as \"undoing\" the "
        "transformation that $A$ represents.\n\n"
        "A matrix is **singular** (has no inverse) when its determinant is zero — meaning "
        "it squashes space into a lower dimension and information is lost.\n\n"
        "**In ML:** The normal equation for linear regression uses matrix inverse: "
        "$\\hat{\\beta} = (X^T X)^{-1} X^T y$. In practice, direct inversion is numerically "
        "unstable for large matrices, so pseudo-inverse or iterative solvers are preferred."
    ),
    "np.linalg.det": (
        "**Determinant:** A scalar that measures how a matrix scales area (in 2D) or volume "
        "(in higher dimensions). For a 2×2 matrix $\\begin{bmatrix}a & b\\\\c & d\\end{bmatrix}$, "
        "the determinant is $ad - bc$.\n\n"
        "- **det = 0**: The matrix is singular — it collapses space into a lower dimension "
        "(no inverse exists)\n"
        "- **det > 0**: Preserves orientation\n"
        "- **det < 0**: Flips orientation (like a mirror)\n\n"
        "In ML, determinants appear in multivariate Gaussian distributions and in checking "
        "whether a system of equations has a unique solution."
    ),
    "np.linalg.svd": (
        "**Singular Value Decomposition (SVD):** Factorizes any matrix $A$ into three parts:\n\n"
        "$$A = U \\Sigma V^T$$\n\n"
        "where $U$ and $V$ are orthogonal matrices (rotations) and $\\Sigma$ is diagonal "
        "(scaling factors called singular values).\n\n"
        "SVD is one of the most important tools in ML:\n"
        "- **Dimensionality reduction**: Keep only the top-k singular values (like PCA)\n"
        "- **Recommendation systems**: Matrix factorization for collaborative filtering\n"
        "- **NLP**: Latent Semantic Analysis decomposes term-document matrices via SVD\n"
        "- **Image compression**: Low-rank approximations discard small singular values"
    ),
    "np.matmul|@ B|np.dot(A": (
        "**Matrix Multiplication:** The core operation in nearly all ML. When you multiply "
        "matrices $A$ (m×n) and $B$ (n×p), each element of the result is a **dot product** — "
        "a row of $A$ dotted with a column of $B$:\n\n"
        "$$C_{ij} = \\sum_{k=1}^{n} A_{ik} \\cdot B_{kj}$$\n\n"
        "**Why it matters:**\n"
        "- Every neural network layer computes $\\text{output} = W \\cdot \\text{input} + b$\n"
        "- Transformers use matrix multiplication extensively for attention scores\n"
        "- The `@` operator in Python/NumPy is shorthand for `np.matmul()`"
    ),

    # ── Activation Functions ────────────────────────────────────────
    "softmax": (
        "**Softmax Function:** Converts a vector of raw scores (logits) into a **probability "
        "distribution** — all values between 0 and 1 that sum to 1:\n\n"
        "$$\\text{softmax}(z_i) = \\frac{e^{z_i}}{\\sum_j e^{z_j}}$$\n\n"
        "Softmax amplifies the largest values and suppresses smaller ones. It's used as the "
        "final layer in multi-class classification: the output tells you the model's confidence "
        "for each class."
    ),
    "sigmoid": (
        "**Sigmoid Function:** Squashes any real number into the range (0, 1):\n\n"
        "$$\\sigma(x) = \\frac{1}{1 + e^{-x}}$$\n\n"
        "Properties: smooth, differentiable, S-shaped curve. At $x=0$, output is 0.5.\n\n"
        "**Used for:** Binary classification (output = probability of positive class), "
        "gating mechanisms in LSTMs/GRUs. Downside: gradients vanish for very large/small "
        "inputs (the curve flattens), which is why ReLU often replaced it in hidden layers."
    ),
    "relu": (
        "**ReLU (Rectified Linear Unit):** The most common activation function in modern "
        "neural networks:\n\n"
        "$$\\text{ReLU}(x) = \\max(0, x)$$\n\n"
        "It simply passes positive values through and zeroes out negatives. Why it works so well:\n"
        "- **No vanishing gradient** for positive inputs (gradient is always 1)\n"
        "- **Sparse activation**: many neurons output 0, making the network efficient\n"
        "- **Computationally fast**: just a threshold, no exponentials\n\n"
        "Variants like Leaky ReLU ($\\max(0.01x, x)$) and GELU fix the \"dying ReLU\" "
        "problem where neurons can permanently output 0."
    ),

    # ── Loss Functions ──────────────────────────────────────────────
    "CrossEntropyLoss": (
        "**Cross-Entropy Loss:** The standard loss function for **classification** tasks. "
        "It measures how far the model's predicted probability distribution is from "
        "the true labels:\n\n"
        "$$\\mathcal{L} = -\\sum_{c} y_c \\log(\\hat{y}_c)$$\n\n"
        "where $y_c$ is the true label (one-hot) and $\\hat{y}_c$ is the predicted probability.\n\n"
        "- Heavily penalizes confident wrong predictions (e.g., predicting 0.01 for the true class)\n"
        "- Gently penalizes correct predictions (predicting 0.99 for the true class)"
    ),
    "BCELoss|binary_crossentropy": (
        "**Binary Cross-Entropy (BCE) Loss:** Used for **binary classification** (yes/no, "
        "positive/negative):\n\n"
        "$$\\mathcal{L} = -[y \\log(\\hat{y}) + (1-y) \\log(1-\\hat{y})]$$\n\n"
        "When the true label is 1, only the first term matters (penalizing low predictions). "
        "When the true label is 0, only the second term matters (penalizing high predictions). "
        "Pair it with a sigmoid output layer."
    ),
    "mean_squared_error|MSELoss|mse_loss": (
        "**Mean Squared Error (MSE) Loss:** The go-to loss for **regression** — predicting "
        "continuous values:\n\n"
        "$$\\text{MSE} = \\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2$$\n\n"
        "Squaring the errors means large mistakes are penalized much more than small ones. "
        "This makes MSE sensitive to outliers. For outlier-robust regression, consider "
        "MAE (Mean Absolute Error) or Huber loss."
    ),

    # ── Optimizers ──────────────────────────────────────────────────
    "Adam(|AdamW(": (
        "**Adam Optimizer:** The most popular optimizer in deep learning. Adam combines two ideas:\n"
        "1. **Momentum** (keeps a running average of past gradients to smooth updates)\n"
        "2. **Adaptive learning rate** (scales the learning rate per-parameter based on gradient history)\n\n"
        "$$m_t = \\beta_1 m_{t-1} + (1-\\beta_1) g_t \\quad \\text{(momentum)}$$\n"
        "$$v_t = \\beta_2 v_{t-1} + (1-\\beta_2) g_t^2 \\quad \\text{(adaptive rate)}$$\n\n"
        "**AdamW** adds proper weight decay (L2 regularization) for better generalization. "
        "Default learning rate is typically 1e-3 to 1e-5 depending on the task."
    ),
    "SGD(": (
        "**Stochastic Gradient Descent (SGD):** The foundational optimizer. Instead of computing "
        "the gradient over the entire dataset, SGD uses a small random batch to estimate it:\n\n"
        "$$\\theta \\leftarrow \\theta - \\eta \\nabla \\mathcal{L}(\\theta)$$\n\n"
        "Pure SGD with momentum often generalizes better than Adam for computer vision tasks, "
        "but requires more careful learning rate tuning."
    ),
    "optimizer.step(": (
        "**Optimizer Step:** This is the core of the training loop. After computing gradients "
        "via `.backward()`, `optimizer.step()` updates all model parameters by moving them "
        "in the direction that reduces the loss. The step size is controlled by the learning rate.\n\n"
        "The typical PyTorch training pattern is:\n"
        "1. `optimizer.zero_grad()` — clear old gradients\n"
        "2. `loss.backward()` — compute new gradients via backpropagation\n"
        "3. `optimizer.step()` — update weights using the gradients"
    ),
    ".backward(": (
        "**Backpropagation:** Calling `.backward()` triggers automatic differentiation — "
        "PyTorch walks backwards through the computation graph, computing the gradient of "
        "the loss with respect to every parameter using the **chain rule**.\n\n"
        "$$\\frac{\\partial \\mathcal{L}}{\\partial w} = \\frac{\\partial \\mathcal{L}}{\\partial z} "
        "\\cdot \\frac{\\partial z}{\\partial w}$$\n\n"
        "These gradients tell each parameter which direction to move to reduce the loss."
    ),

    # ── Neural Network Layers ───────────────────────────────────────
    "nn.Linear(": (
        "**Linear Layer (Fully Connected):** The fundamental building block of neural networks. "
        "It computes $y = xW^T + b$ — a matrix multiplication of the input with learned weights, "
        "plus a bias term.\n\n"
        "`nn.Linear(in_features, out_features)` creates a layer that transforms a vector of "
        "size `in_features` into one of size `out_features`. Without activation functions between "
        "linear layers, stacking them would be equivalent to a single linear layer (linearity is "
        "closed under composition)."
    ),
    "nn.Conv": (
        "**Convolutional Layer:** Slides a small filter (kernel) across the input to detect "
        "local patterns. Each filter learns to detect one feature (edges, textures, shapes).\n\n"
        "- `Conv1d`: For sequences (text, audio, time series)\n"
        "- `Conv2d`: For images — scans height and width\n"
        "- Key parameters: `in_channels` (depth of input), `out_channels` (number of filters), "
        "`kernel_size` (filter dimensions)\n\n"
        "Convolutions exploit **spatial locality** (nearby pixels relate to each other) and "
        "**parameter sharing** (same filter applied everywhere — far fewer parameters than a "
        "fully connected layer)."
    ),
    "nn.LSTM|nn.GRU|nn.RNN": (
        "**Recurrent Neural Network (RNN/LSTM/GRU):** Designed for **sequential data** where "
        "order matters (text, time series, audio). They maintain a hidden state $h_t$ that acts "
        "as a \"memory\" of previous time steps.\n\n"
        "- **LSTM** (Long Short-Term Memory): Uses gates (forget, input, output) to control "
        "what information to remember or discard — solves the vanishing gradient problem\n"
        "- **GRU** (Gated Recurrent Unit): Simplified LSTM with fewer parameters (merge forget "
        "and input gates)\n\n"
        "While Transformers have largely replaced RNNs for NLP, LSTMs remain competitive "
        "for time-series forecasting and streaming applications."
    ),
    "nn.Module": (
        "**nn.Module — PyTorch Model Definition:** All PyTorch neural networks inherit from "
        "`nn.Module`. This base class provides:\n"
        "- **Parameter tracking**: Automatically registers learnable weights\n"
        "- **GPU transfer**: `.to(device)` moves all parameters at once\n"
        "- **Serialization**: `.state_dict()` for saving/loading model weights\n\n"
        "You define the network architecture in `__init__()` (create layers) and the "
        "computation flow in `forward()` (connect layers). PyTorch auto-generates the "
        "backward pass for gradient computation."
    ),

    # ── Scikit-learn Models ─────────────────────────────────────────
    "train_test_split(": (
        "**Train/Test Split:** Divide your dataset into separate training and testing subsets "
        "to evaluate how well your model generalizes to unseen data.\n\n"
        "- **Training set** (~70-80%): The model learns from this data\n"
        "- **Test set** (~20-30%): Held out, only used for final evaluation\n\n"
        "Without this split, you'd have no way to detect **overfitting** — when a model "
        "memorizes training data but fails on new data. A common split is 80/20 with "
        "`random_state` set for reproducibility."
    ),
    "cross_val_score(": (
        "**Cross-Validation:** A more robust evaluation than a single train/test split. "
        "K-fold cross-validation:\n"
        "1. Split data into $k$ equal folds\n"
        "2. Train on $k-1$ folds, test on the remaining one\n"
        "3. Repeat $k$ times, each fold serving as the test set once\n"
        "4. Average the $k$ scores\n\n"
        "This gives a more reliable performance estimate because every data point is used "
        "for both training and testing. Common choice: $k=5$ or $k=10$."
    ),
    ".fit(": (
        "**Model Training (.fit()):** The `.fit()` method is where the model learns from data. "
        "It adjusts the model's internal parameters to minimize prediction errors on the "
        "training data.\n\n"
        "For different model types, `.fit()` does different things:\n"
        "- **Linear models**: Finds the best-fit line/plane (minimizes squared error)\n"
        "- **Decision trees**: Recursively splits data to separate classes/values\n"
        "- **Neural networks**: Runs gradient descent over many epochs\n"
        "- **Transformers (StandardScaler, PCA)**: Computes statistics (mean, variance, components) "
        "from the training data"
    ),
    ".predict(": (
        "**Model Prediction (.predict()):** After training, `.predict()` applies the learned "
        "model to new (unseen) data to generate predictions.\n\n"
        "- **Classification**: Returns predicted class labels\n"
        "- **Regression**: Returns predicted continuous values\n\n"
        "The quality of predictions depends on how well the model was trained and whether "
        "the new data resembles the training distribution."
    ),
    ".fit_transform(": (
        "**Fit and Transform (.fit_transform()):** A convenience method that combines `.fit()` "
        "and `.transform()` in one step — learns the transformation parameters from the data "
        "and immediately applies the transformation.\n\n"
        "**Important**: Use `.fit_transform()` only on **training data**. For test data, "
        "use `.transform()` alone to apply the same transformation learned from training. "
        "Otherwise, you leak test data statistics into the transformation (\"data leakage\")."
    ),
    ".transform(": (
        "**Transform (.transform()):** Applies a previously learned transformation to new data. "
        "For example, `StandardScaler.transform()` applies the mean and standard deviation "
        "computed during `.fit()` to scale new data the same way.\n\n"
        "Always use the same transformer object on training and test data to ensure consistent "
        "preprocessing."
    ),
    "StandardScaler(": (
        "**Standard Scaling (Z-score Normalization):** Transforms each feature to have "
        "**mean=0** and **standard deviation=1**:\n\n"
        "$$z = \\frac{x - \\mu}{\\sigma}$$\n\n"
        "**Why scale?** Many ML algorithms (SVM, KNN, gradient descent, PCA) are sensitive "
        "to feature magnitudes. A feature ranging 0-1000 would dominate one ranging 0-1 "
        "without scaling. Tree-based models (Random Forest, XGBoost) are scale-invariant."
    ),
    "MinMaxScaler(": (
        "**Min-Max Scaling:** Rescales features to a fixed range, typically [0, 1]:\n\n"
        "$$x_{\\text{scaled}} = \\frac{x - x_{\\min}}{x_{\\max} - x_{\\min}}$$\n\n"
        "Use Min-Max when you need bounded values (e.g., neural network inputs, image pixels). "
        "Unlike StandardScaler, it doesn't center the data at zero and is more sensitive to outliers."
    ),
    "PCA(": (
        "**Principal Component Analysis (PCA):** A dimensionality reduction technique that finds "
        "the directions (principal components) of maximum variance in the data.\n\n"
        "Under the hood, PCA computes the eigenvectors of the covariance matrix. The first "
        "principal component captures the most variance, the second captures the most of what's "
        "left (orthogonal to the first), and so on.\n\n"
        "**Uses:** Reducing features while preserving information, denoising, visualization "
        "(projecting high-dimensional data to 2D/3D)."
    ),
    "LogisticRegression(": (
        "**Logistic Regression:** Despite its name, this is a **classification** algorithm. "
        "It models the probability of a class using the sigmoid function:\n\n"
        "$$P(y=1|x) = \\sigma(w^T x + b) = \\frac{1}{1 + e^{-(w^T x + b)}}$$\n\n"
        "The decision boundary is a hyperplane — linear in the feature space. Logistic regression "
        "is fast, interpretable, and a strong baseline. Regularization (C parameter) controls "
        "model complexity."
    ),
    "LinearRegression(": (
        "**Linear Regression:** The simplest predictive model — fits a straight line (or hyperplane) "
        "through the data that minimizes the sum of squared errors:\n\n"
        "$$\\hat{y} = w_1 x_1 + w_2 x_2 + \\cdots + w_n x_n + b$$\n\n"
        "Each coefficient $w_i$ tells you how much the prediction changes when feature $x_i$ "
        "increases by 1, holding other features constant. The intercept $b$ is the prediction "
        "when all features are zero."
    ),
    "RandomForest": (
        "**Random Forest:** An ensemble method that builds many decision trees and averages "
        "their predictions (regression) or takes a majority vote (classification).\n\n"
        "Two key tricks make it powerful:\n"
        "1. **Bagging**: Each tree trains on a random subset of the data (with replacement)\n"
        "2. **Feature randomness**: Each split considers only a random subset of features\n\n"
        "This decorrelates the trees, reducing overfitting. Random Forests handle non-linear "
        "relationships, missing values, and mixed feature types well, with minimal tuning needed."
    ),
    "GradientBoosting|XGB|LGBM": (
        "**Gradient Boosting:** Builds trees sequentially — each new tree corrects the errors "
        "of the previous ones. Instead of independent trees (like Random Forest), boosting "
        "creates a chain where each tree learns from the \"residual\" mistakes.\n\n"
        "$$F_m(x) = F_{m-1}(x) + \\eta \\cdot h_m(x)$$\n\n"
        "where $h_m$ is the new tree fitted to the gradient of the loss, and $\\eta$ (learning "
        "rate) controls the contribution of each tree.\n\n"
        "XGBoost and LightGBM are optimized implementations that dominate tabular data competitions."
    ),
    "DecisionTree": (
        "**Decision Tree:** Makes predictions by learning a sequence of if/else rules from "
        "the training data. At each node, it picks the feature and threshold that best "
        "separates the data (measured by Gini impurity or information gain).\n\n"
        "**Pros:** Highly interpretable, handles non-linear relationships, requires no scaling.\n"
        "**Cons:** Prone to overfitting — a single tree will memorize the training data. "
        "That's why ensemble methods (Random Forest, Gradient Boosting) combine many trees."
    ),
    "SVC(|SVR(|SVM": (
        "**Support Vector Machine (SVM):** Finds the hyperplane that maximizes the **margin** — "
        "the distance to the nearest data points (support vectors) of each class.\n\n"
        "- **Linear SVM**: Straight-line decision boundary\n"
        "- **Kernel SVM**: Uses the \"kernel trick\" to map data into higher dimensions "
        "where it becomes linearly separable (RBF kernel is the most common)\n\n"
        "SVMs work well with high-dimensional data and small-to-medium datasets. For very "
        "large datasets, logistic regression or gradient boosting are often preferred."
    ),
    "KMeans(": (
        "**K-Means Clustering:** An unsupervised algorithm that groups data into $k$ clusters "
        "by iteratively:\n"
        "1. Assigning each point to its nearest centroid\n"
        "2. Moving each centroid to the mean of its assigned points\n\n"
        "Converges when assignments stop changing. You must choose $k$ in advance — "
        "the elbow method (plot inertia vs $k$) or silhouette score can help.\n\n"
        "K-Means assumes roughly spherical, equally-sized clusters. For other cluster shapes, "
        "consider DBSCAN or Gaussian Mixture Models."
    ),

    # ── Evaluation Metrics ──────────────────────────────────────────
    "accuracy_score(": (
        "**Accuracy:** The fraction of predictions that are correct:\n\n"
        "$$\\text{Accuracy} = \\frac{\\text{correct predictions}}{\\text{total predictions}}$$\n\n"
        "**Caution:** Accuracy can be misleading with imbalanced classes. If 95% of data is class A, "
        "a model that always predicts 'A' gets 95% accuracy while being useless. Use precision, "
        "recall, and F1-score for imbalanced datasets."
    ),
    "confusion_matrix(": (
        "**Confusion Matrix:** A table showing the four possible prediction outcomes:\n\n"
        "| | Predicted + | Predicted − |\n|---|---|---|\n"
        "| **Actual +** | True Positive (TP) | False Negative (FN) |\n"
        "| **Actual −** | False Positive (FP) | True Negative (TN) |\n\n"
        "From this table you can compute: Precision = TP/(TP+FP) (\"of all positive predictions, "
        "how many were correct?\") and Recall = TP/(TP+FN) (\"of all actual positives, how many "
        "did we find?\")."
    ),
    "classification_report(": (
        "**Classification Report:** A summary of key metrics per class:\n\n"
        "- **Precision**: Of all items predicted as class X, what fraction actually are? "
        "(Low precision = many false positives)\n"
        "- **Recall**: Of all actual class X items, what fraction did we catch? "
        "(Low recall = many false negatives)\n"
        "- **F1-Score**: Harmonic mean of precision and recall — balances both\n"
        "- **Support**: Number of actual instances per class"
    ),
    "r2_score(": (
        "**R² Score (Coefficient of Determination):** Measures how much of the variance in the "
        "target variable is explained by the model:\n\n"
        "$$R^2 = 1 - \\frac{\\sum (y_i - \\hat{y}_i)^2}{\\sum (y_i - \\bar{y})^2}$$\n\n"
        "- $R^2 = 1$: Perfect predictions\n"
        "- $R^2 = 0$: Model is no better than predicting the mean\n"
        "- $R^2 < 0$: Model is worse than predicting the mean"
    ),

    # ── Data Operations ─────────────────────────────────────────────
    "pd.read_csv(": (
        "**Load Data from CSV:** `pd.read_csv()` reads a comma-separated file into a "
        "Pandas DataFrame — the primary data structure for tabular data analysis. "
        "A DataFrame is like a spreadsheet: rows are observations, columns are features.\n\n"
        "Common parameters: `header`, `index_col`, `na_values`, `dtype`, `parse_dates`. "
        "For large files, use `chunksize` or `usecols` to load only what you need."
    ),
    "pd.DataFrame(": (
        "**Create a DataFrame:** Pandas DataFrames are 2D labeled data structures — "
        "they're the backbone of data science in Python. Each column can hold a different "
        "data type (numbers, strings, dates). DataFrames support powerful operations: "
        "filtering, grouping, merging, reshaping, and aggregation."
    ),
    ".groupby(": (
        "**GroupBy — Split-Apply-Combine:** One of the most powerful Pandas operations. It:\n"
        "1. **Splits** the data by one or more keys (categories)\n"
        "2. **Applies** a function to each group independently (mean, sum, count, custom)\n"
        "3. **Combines** the results back into a DataFrame\n\n"
        "Example: `df.groupby('city')['price'].mean()` computes the average price per city."
    ),
    ".merge(": (
        "**DataFrame Merge (Join):** Combines two DataFrames based on shared column(s), "
        "like a SQL JOIN:\n"
        "- **inner**: Only matching rows from both tables\n"
        "- **left/right**: All rows from one side, matching from the other\n"
        "- **outer**: All rows from both, filling NaN where there's no match\n\n"
        "Merging is essential for combining data from different sources into a single "
        "analysis-ready dataset."
    ),
    ".fillna(|.dropna(": (
        "**Handling Missing Data:** Real-world datasets almost always have missing values. "
        "Two main strategies:\n"
        "- **Drop** (`.dropna()`): Remove rows/columns with missing values — simple but "
        "loses data. Appropriate when few values are missing.\n"
        "- **Impute** (`.fillna()`): Replace missing values with estimated ones (mean, median, "
        "mode, or a model-based prediction). Preserves data size but introduces assumptions.\n\n"
        "Always investigate *why* data is missing before choosing a strategy — missingness "
        "can be informative."
    ),

    # ── Tokenization & NLP ──────────────────────────────────────────
    "AutoTokenizer|tokenizer": (
        "**Tokenizer:** Converts raw text into numerical token IDs that a model can process. "
        "The tokenizer defines the vocabulary — the set of all possible tokens.\n\n"
        "Modern tokenizers use **subword** algorithms:\n"
        "- **BPE** (Byte-Pair Encoding): Used by GPT models, learns frequent character pairs\n"
        "- **WordPiece**: Used by BERT, similar to BPE but uses likelihood\n"
        "- **SentencePiece**: Language-agnostic, works directly on raw text\n\n"
        "The tokenizer must match the model — using GPT's tokenizer with BERT would produce "
        "meaningless results."
    ),
    "SentenceTransformer(": (
        "**Sentence Transformers:** A library that fine-tunes transformer models to produce "
        "**meaningful sentence-level embeddings**. Unlike raw BERT embeddings (which are token-level), "
        "Sentence Transformers output a single vector per sentence where:\n"
        "- Semantically similar sentences have **high cosine similarity**\n"
        "- Dissimilar sentences have **low cosine similarity**\n\n"
        "Used for: semantic search, clustering, duplicate detection, and RAG retrieval."
    ),
    "cosine_similarity": (
        "**Cosine Similarity:** Measures the angle between two vectors, ignoring their magnitude:\n\n"
        "$$\\text{cos\\_sim}(\\mathbf{a}, \\mathbf{b}) = \\frac{\\mathbf{a} \\cdot \\mathbf{b}}"
        "{\\|\\mathbf{a}\\| \\|\\mathbf{b}\\|}$$\n\n"
        "- **1.0**: Identical direction (very similar)\n"
        "- **0.0**: Perpendicular (unrelated)\n"
        "- **-1.0**: Opposite direction (very dissimilar)\n\n"
        "Cosine similarity is the standard metric for comparing text embeddings because "
        "it's invariant to vector length — a longer document doesn't automatically get a higher score."
    ),
    "embedding": (
        "**Embeddings:** Dense, fixed-size vector representations that capture **semantic meaning**. "
        "Unlike one-hot encoding (sparse, high-dimensional, no similarity), embeddings map "
        "similar items to nearby points in vector space.\n\n"
        "- Words: \"king\" and \"queen\" have similar embeddings\n"
        "- Sentences: Paraphrases map to nearby vectors\n"
        "- Images: Similar images cluster together\n\n"
        "Embeddings are the bridge between human-readable content and mathematical operations "
        "— enabling search, clustering, classification, and recommendation."
    ),

    # ── Vector Databases ────────────────────────────────────────────
    "chromadb": (
        "**ChromaDB:** An open-source vector database designed for AI applications. It stores "
        "embeddings alongside metadata and supports fast similarity search using approximate "
        "nearest neighbor (ANN) algorithms.\n\n"
        "**Workflow:** Embed your data → Store in ChromaDB → Query with a new embedding "
        "→ Get the most similar results. This is the core of RAG (Retrieval-Augmented Generation) "
        "systems."
    ),
    "qdrant": (
        "**Qdrant:** A production-grade vector search engine with filtering capabilities. Unlike "
        "simpler vector stores, Qdrant supports combining vector similarity with metadata filters "
        "(e.g., \"find similar documents from the last month\"). It's designed for high-throughput, "
        "low-latency search at scale."
    ),
    "faiss": (
        "**FAISS (Facebook AI Similarity Search):** A highly optimized library for "
        "similarity search over dense vectors. FAISS provides multiple index types with "
        "different speed/accuracy/memory tradeoffs:\n"
        "- `IndexFlatL2`: Exact search, best accuracy but slowest\n"
        "- `IndexIVFFlat`: Inverted file index, much faster with slight accuracy trade-off\n"
        "- `IndexHNSW`: Graph-based, excellent for medium-scale datasets\n\n"
        "Use FAISS when you need raw speed and control over the index structure."
    ),

    # ── Visualization ───────────────────────────────────────────────
    "plt.scatter(": (
        "**Scatter Plot:** Displays individual data points as dots on a 2D plane. Each point's "
        "position is determined by its x and y values. Color and size can encode additional dimensions.\n\n"
        "**Use for:** Exploring relationships between two continuous variables, spotting clusters, "
        "identifying outliers, and visualizing model predictions vs. actual values."
    ),
    "plt.plot(": (
        "**Line Plot:** Connects data points with lines — ideal for showing trends over a "
        "continuous variable (often time). In ML, line plots are commonly used for:\n"
        "- Training/validation loss curves (to detect overfitting)\n"
        "- Learning rate schedules\n"
        "- Time series data"
    ),
    "plt.hist(": (
        "**Histogram:** Shows the distribution of a single variable by dividing values into "
        "bins and counting how many fall in each. Reveals the shape of the data: normal, "
        "skewed, bimodal, uniform, etc.\n\n"
        "Always check distributions before modeling — many algorithms assume normally "
        "distributed features."
    ),
    "plt.imshow(": (
        "**Image Display:** Renders a 2D array as an image. Used for:\n"
        "- Displaying actual images (RGB arrays)\n"
        "- Visualizing weight matrices, attention maps, or feature maps in neural networks\n"
        "- Showing heatmaps of correlation matrices\n\n"
        "Use `cmap` to set the colormap, `aspect` to control scaling."
    ),
    "plt.bar(": (
        "**Bar Chart:** Compares quantities across categories using rectangular bars. "
        "The length of each bar represents the value. Use for:\n"
        "- Feature importance rankings\n"
        "- Class balance visualization\n"
        "- Comparing model performance metrics side by side"
    ),
    "sns.heatmap(": (
        "**Heatmap:** A color-coded grid showing the magnitude of values in a 2D matrix. "
        "Commonly used for:\n"
        "- **Correlation matrices**: Quickly spot which features are related\n"
        "- **Confusion matrices**: Visualize classification performance\n"
        "- **Attention weights**: See where a Transformer focuses\n\n"
        "Annotate with values (`annot=True`) for readability."
    ),

    # ── Gradient Descent ────────────────────────────────────────────
    "gradient_descent": (
        "**Gradient Descent:** The fundamental optimization algorithm in ML. It iteratively "
        "adjusts parameters by moving in the direction of steepest descent (negative gradient) "
        "of the loss function:\n\n"
        "$$\\theta_{t+1} = \\theta_t - \\eta \\nabla_\\theta \\mathcal{L}(\\theta_t)$$\n\n"
        "where $\\eta$ is the **learning rate** — too large and it overshoots, too small "
        "and training is slow. The gradient $\\nabla \\mathcal{L}$ tells us the direction "
        "and steepness of the loss landscape at the current position."
    ),

    # ── Hugging Face / Transformers ─────────────────────────────────
    "AutoModel": (
        "**AutoModel — Pretrained Transformer Loading:** Hugging Face's `AutoModel` automatically "
        "detects and loads the correct model architecture from a model name or path. It handles "
        "BERT, GPT, T5, LLaMA, and hundreds of other architectures with the same API.\n\n"
        "Pretrained models have already learned language understanding from billions of words "
        "of text — you fine-tune them on your specific task for much better results than "
        "training from scratch."
    ),
    "load_dataset(": (
        "**Hugging Face Datasets:** A library for accessing and processing thousands of "
        "community-contributed datasets. It handles downloading, caching, and memory-efficient "
        "loading (datasets are memory-mapped, not loaded entirely into RAM).\n\n"
        "Supports streaming for very large datasets and integrates directly with "
        "the Transformers training pipeline."
    ),

    # ── OpenAI / API ────────────────────────────────────────────────
    "openai": (
        "**OpenAI API:** Interface to GPT and embedding models hosted by OpenAI. Requests "
        "are sent over HTTPS and billed per token.\n\n"
        "- **Chat completions**: Send a conversation and get a model response\n"
        "- **Embeddings**: Convert text into vector representations\n"
        "- **Fine-tuning**: Customize model behavior with your own examples\n\n"
        "Always handle API keys securely (environment variables, not hardcoded) and implement "
        "rate limiting and error handling."
    ),

    # ── Random / Data Generation ────────────────────────────────────
    "np.random.seed|random_state": (
        "**Random Seed:** Setting a seed ensures **reproducibility** — the same random numbers "
        "are generated each time the code runs. This is critical in ML experiments because:\n"
        "- Train/test splits will be the same\n"
        "- Weight initialization will be identical\n"
        "- Any randomized algorithm (dropout, data augmentation) will behave consistently\n\n"
        "Without a fixed seed, your results would vary between runs, making it impossible "
        "to debug or compare experiments."
    ),
}


# ────────────────────────────────────────────────────────────────────
# SHALLOW CELL DETECTION
# ────────────────────────────────────────────────────────────────────

SHALLOW_PATTERNS = [
    r"^### (Mathematical Operations|Visualize the Results|Define the `|Define Helper|Import Required|Setup\b|Environment Setup|Data Manipulation|Iterative Processing|Data Transformation|File Operations|Error Handling|API Interaction|Tensor Operations|Compute Embeddings|Tokenization\b|Vector Database|Generate Predictions|Build the Model|Train the Model|Evaluate Model|Load the Data|Preprocess the Data|Configure Loss)",
    r"^(Set up the variables|Display output to verify|Execute the next step|Work with Python lists|Work with Python diction|Use a loop to process|Use conditional logic|Perform string manipul|Evaluate the (expression|arithmetic)|Use a Python comprehension|Set up variables and display)",
    # Auto-generated thin section headings (heading only, <50 chars total)
    r"^### (Vector Operations|Matrix Operations|Visualizing (Vectors|Matrix|Eigenvectors))\s*$",
]


def is_shallow(md_source: str) -> bool:
    """Check if a markdown cell is an auto-generated shallow explanation."""
    text = md_source.strip()
    for pat in SHALLOW_PATTERNS:
        if re.search(pat, text, re.MULTILINE):
            return True
    return False


def find_matching_concepts(code: str) -> list[str]:
    """Find all concept explanations that match the code content."""
    matches = []
    matched_keys = set()
    for pattern_key, explanation in CONCEPT_EXPLANATIONS.items():
        # Key might be a regex with | for alternatives
        parts = pattern_key.split("|")
        for part in parts:
            if part in code and pattern_key not in matched_keys:
                matches.append(explanation)
                matched_keys.add(pattern_key)
                break
    return matches


def get_notebook_topic(nb_path: str) -> str:
    """Infer topic from notebook path."""
    p = nb_path.lower()
    topic_map = [
        ("token", "tokenization"), ("embedding", "embeddings"),
        ("neural", "neural networks"), ("vector.*database", "vector databases"),
        ("rag", "RAG"), ("mlops", "MLOps"), ("prompt", "prompt engineering"),
        ("finetun", "LLM fine-tuning"), ("multimodal", "multimodal AI"),
        ("agent", "AI agents"), ("evaluation|metric", "model evaluation"),
        ("debug|troubleshoot", "debugging"), ("safety|redteam", "AI safety"),
        ("streaming", "real-time streaming"), ("time.series|time_series", "time series"),
        ("reinforcement|q_learn", "reinforcement learning"),
        ("causal", "causal inference"), ("deep.learn|deep_learn|advanced", "deep learning"),
        ("linear.algebra|linear_algebra", "linear algebra"),
        ("calculus|derivative", "calculus"), ("probability|statistic", "statistics"),
        ("gradient", "optimization"), ("numpy", "NumPy"),
        ("pandas|dataframe", "Pandas"), ("matplotlib", "visualization"),
        ("scikit|sklearn", "scikit-learn"), ("python|crash", "Python"),
        ("data.science|data_science", "data science"), ("local.llm|ollama", "local LLMs"),
        ("inference.*optim", "inference optimization"), ("low.code|gradio|streamlit", "low-code AI"),
        ("math", "mathematics for AI"), ("islp", "statistical learning"),
        ("hardware|validation", "AI hardware"), ("practical", "practical data science"),
    ]
    for pat, topic in topic_map:
        if re.search(pat, p):
            return topic
    return "AI/ML"


def build_rich_explanation(code: str, existing_md: str, topic: str) -> str:
    """Build a rich explanation for a code cell, using concept database + code analysis."""
    concepts = find_matching_concepts(code)
    comments = []
    for line in code.split("\n"):
        line_s = line.strip()
        if line_s.startswith("#") and len(line_s) > 3:
            c = line_s.lstrip("#").strip()
            if c and not c.startswith("!") and not c.startswith("%%"):
                comments.append(c)

    # Preserve the existing heading if it's a proper section heading (##)
    existing_heading = ""
    for line in existing_md.split("\n"):
        if line.strip().startswith("## ") and len(line.strip()) > 5:
            existing_heading = line.strip()
            break

    parts = []

    # If we have concept matches, use those
    if concepts:
        if existing_heading:
            parts.append(existing_heading + "\n")
        # Combine all matching concept explanations
        for i, concept_text in enumerate(concepts):
            parts.append(concept_text)
            if i < len(concepts) - 1:
                parts.append("")  # blank line separator
    else:
        # No concept match — generate explanation from code structure
        lines = [l.strip() for l in code.split("\n") if l.strip() and not l.strip().startswith("#")]

        # Detect what the code does based on structure
        has_imports = any(re.match(r"^(import|from)\s+", l.strip()) for l in code.split("\n"))
        has_func_def = any(re.match(r"^(async\s+)?def\s+", l.strip()) for l in code.split("\n"))
        has_class_def = any(re.match(r"^class\s+", l.strip()) for l in code.split("\n"))
        has_print = any(l.strip().startswith("print(") for l in code.split("\n"))
        is_simple_expr = (
            len(lines) == 1 and len(lines[0]) < 40
            and not any(kw in lines[0] for kw in ["import", "def ", "class ", "for ", "while ", "if ", "="])
        )

        if has_imports and not has_func_def:
            imports = re.findall(r"(?:from|import)\s+(\S+)", code)
            base_libs = list(dict.fromkeys(lib.split(".")[0] for lib in imports))
            if existing_heading:
                parts.append(existing_heading + "\n")
            else:
                parts.append("### Import Required Libraries\n")
            parts.append("Load the libraries needed for this section:\n")
            LIB_DESCS = {
                "numpy": "NumPy for numerical computing and array operations",
                "np": "NumPy for numerical computing and array operations",
                "pandas": "Pandas for data manipulation and analysis",
                "pd": "Pandas for data manipulation and analysis",
                "matplotlib": "Matplotlib for creating visualizations and plots",
                "plt": "Matplotlib's pyplot for creating plots",
                "seaborn": "Seaborn for statistical data visualization",
                "sns": "Seaborn for statistical data visualization",
                "sklearn": "scikit-learn for machine learning algorithms",
                "scipy": "SciPy for scientific computing",
                "torch": "PyTorch for deep learning and tensor operations",
                "tensorflow": "TensorFlow for deep learning",
                "transformers": "Hugging Face Transformers for pretrained models",
                "tokenizers": "Hugging Face Tokenizers for text tokenization",
                "tiktoken": "tiktoken for OpenAI-compatible tokenization",
                "openai": "OpenAI API client for GPT models",
                "langchain": "LangChain for LLM-powered applications",
                "chromadb": "ChromaDB vector database",
                "sentence_transformers": "Sentence Transformers for text embeddings",
                "gradio": "Gradio for ML demo interfaces",
                "streamlit": "Streamlit for data apps",
                "fastapi": "FastAPI for web APIs",
                "mlflow": "MLflow for experiment tracking",
                "requests": "HTTP requests library",
                "json": "JSON serialization",
                "os": "Operating system interface",
                "re": "Regular expressions for pattern matching",
                "pathlib": "Object-oriented filesystem paths",
                "tqdm": "Progress bar library",
                "PIL": "Pillow for image processing",
                "cv2": "OpenCV for computer vision",
                "datasets": "Hugging Face Datasets",
                "peft": "PEFT for parameter-efficient fine-tuning",
                "trl": "TRL for transformer reinforcement learning",
                "warnings": "Warning control",
                "dotenv": "Environment variable loading from .env",
            }
            for lib in base_libs:
                desc = LIB_DESCS.get(lib, lib)
                parts.append(f"- **{lib}**: {desc}")

        elif has_func_def:
            func_names = re.findall(r"(?:async\s+)?def\s+(\w+)", code)
            for fn in func_names:
                readable = fn.replace("_", " ")
                parts.append(f"### Define `{fn}()`\n")
                # Try to extract docstring or first comment
                fn_comments = [c for c in comments if readable.lower() not in c.lower()]
                if fn_comments:
                    parts.append(fn_comments[0])
                else:
                    parts.append(f"A helper function that {readable}.")

        elif has_class_def:
            class_names = re.findall(r"class\s+(\w+)", code)
            for cn in class_names:
                readable = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", cn).lower()
                parts.append(f"### Define `{cn}`\n")
                parts.append(f"A class implementing {readable}.")

        elif is_simple_expr:
            expr = lines[0]
            if re.match(r"^\d+\s*[\+\-\*\/\%\*]+\s*\d+$", expr):
                ops = {"*": "multiplication", "+": "addition", "-": "subtraction",
                       "/": "division", "%": "modulo (remainder)", "**": "exponentiation"}
                op_name = "arithmetic"
                for op_sym, op_str in ops.items():
                    if op_sym in expr:
                        op_name = op_str
                parts.append(
                    f"**Python {op_name.title()}:** Evaluate `{expr}`. "
                    "In Jupyter, the last expression in a cell is automatically displayed "
                    "as output without needing `print()`."
                )
            elif re.match(r"^[a-zA-Z_]\w*$", expr):
                parts.append(
                    f"**Inspect variable `{expr}`:** Display its current value. "
                    "Jupyter automatically renders the last expression in a cell."
                )
            elif "[" in expr:
                parts.append(
                    f"**Indexing/Slicing:** `{expr}` — Python uses zero-based indexing. "
                    "Slicing with `[start:end]` returns elements from `start` up to (but not "
                    "including) `end`. Negative indices count from the end."
                )
            else:
                parts.append(f"Evaluate the expression `{expr}` and display the result.")

        else:
            # Fall back to using comments as explanation
            if existing_heading:
                parts.append(existing_heading + "\n")
            if comments:
                parts.append("\n".join(comments[:3]) + "\n")
                parts.append(f"The code below implements this step in the {topic} workflow.")
            elif has_print:
                parts.append(
                    f"Run this code and examine the printed output to verify the {topic} "
                    f"operations produce the expected results."
                )
            else:
                parts.append(
                    f"This code implements the next step in the {topic} workflow. "
                    "Review the inline comments for details on each operation."
                )

    result = "\n".join(parts)
    # Avoid creating empty or whitespace-only cells
    return result.strip() if result.strip() else None


def process_notebook(nb_path: Path, topic: str) -> tuple[int, int]:
    """Process a notebook: replace shallow explanation cells with rich ones."""
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    if not cells:
        return 0, 0

    enriched = 0
    total_shallow = 0

    for i, cell in enumerate(cells):
        if cell.get("cell_type") != "markdown":
            continue

        src = cell.get("source", "")
        if isinstance(src, list):
            src = "".join(src)

        if not is_shallow(src):
            continue

        total_shallow += 1

        # Find the next code cell
        code_src = ""
        for j in range(i + 1, min(i + 3, len(cells))):
            if cells[j].get("cell_type") == "code":
                code_src = cells[j].get("source", "")
                if isinstance(code_src, list):
                    code_src = "".join(code_src)
                break

        if not code_src.strip():
            continue

        new_md = build_rich_explanation(code_src, src, topic)
        if new_md and new_md != src.strip():
            cell["source"] = [new_md]
            enriched += 1

    if enriched > 0:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write("\n")

    return enriched, total_shallow


def main():
    # Find all notebooks (source + docs mirrors)
    nbs = sorted(WORKSPACE.rglob("*.ipynb"))
    nbs = [
        n for n in nbs
        if ".ipynb_checkpoints" not in str(n)
        and "site/" not in str(n)
        and ".venv/" not in str(n)
        and "node_modules/" not in str(n)
    ]

    print(f"Scanning {len(nbs)} notebooks for shallow explanations...\n")

    total_enriched = 0
    total_shallow = 0
    notebooks_modified = 0

    for nb_path in nbs:
        rel = str(nb_path.relative_to(WORKSPACE))
        topic = get_notebook_topic(rel)

        try:
            enriched, shallow = process_notebook(nb_path, topic)
            if enriched > 0:
                notebooks_modified += 1
                total_enriched += enriched
                print(f"  Enriched {enriched:3d}/{shallow:3d} cells: {rel}")
            total_shallow += shallow
        except Exception as e:
            print(f"  ERROR: {rel}: {e}")

    print(f"\n{'=' * 60}")
    print(f"Summary: Enriched {total_enriched}/{total_shallow} shallow cells across {notebooks_modified} notebooks")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
