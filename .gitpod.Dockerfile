FROM gitpod/workspace-python-3.11

# Install system dependencies
RUN sudo apt-get update && \
    sudo apt-get install -y \
    build-essential \
    git \
    curl \
    && sudo rm -rf /var/lib/apt/lists/*

# Set Python 3.11 as default
RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# Upgrade pip
RUN python -m pip install --upgrade pip setuptools wheel

# Pre-install common packages (optional, speeds up first launch)
RUN pip install jupyter numpy pandas matplotlib scikit-learn
