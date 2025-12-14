# DevContainer Configuration

This directory contains the configuration for GitHub Codespaces and VS Code Dev Containers.

## Features

- **Python 3.11** environment pre-configured
- **Jupyter** extensions and kernels
- **GitHub Copilot** for AI-assisted coding
- **Auto-install** dependencies on container creation
- **Port forwarding** for Jupyter (8888), Streamlit (8501), TensorBoard (6006)

## Usage

### GitHub Codespaces
1. Click the "Open in Codespaces" badge in README
2. Wait for container to build (~2-3 minutes first time)
3. Dependencies auto-install via `install_dependencies.sh`
4. Start coding!

### VS Code Dev Containers
1. Install "Dev Containers" extension in VS Code
2. Open this repo in VS Code
3. Click "Reopen in Container" when prompted
4. Wait for build and dependency installation

## Customization

Edit `devcontainer.json` to:
- Add more VS Code extensions
- Change Python version
- Modify port forwarding
- Add additional features

## Troubleshooting

**Container build fails:**
- Check Docker is running
- Try: "Rebuild Container" from command palette

**Dependencies not installing:**
- Manually run: `bash install_dependencies.sh`
- Check `install_dependencies.sh` has execute permissions

**Jupyter not starting:**
- Port 8888 might be in use
- Try: `jupyter notebook --port=8889`
