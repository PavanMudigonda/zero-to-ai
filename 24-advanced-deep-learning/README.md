# Advanced Deep Learning Research Topics

This section covers cutting-edge deep learning research topics with mathematical rigor and practical implementations.

**Prerequisites:** 
- Complete 06-neural-networks/
- Advanced mathematics (03-maths/advanced/)
- Understanding of PyTorch/TensorFlow

**Audience:** Researchers, PhD students, advanced ML practitioners

---

## 📚 Table of Contents

### Part I: Advanced Generative Models

#### 1. Generative Adversarial Networks (GANs)
- **01_gan_mathematics.ipynb** - Traditional GAN theory, game theory perspective
- **02_wgan_theory.ipynb** - Wasserstein GAN, optimal transport
- **03_infogan.ipynb** - Information-theoretic regularization
- **04_bayesian_gan.ipynb** - Bayesian approach to GANs

#### 2. Variational Autoencoders & Extensions
- **05_vae_deep_dive.ipynb** - VAE theory, ELBO derivation
- **06_importance_weighted_vae.ipynb** - IWAE, tighter bounds
- **07_normalizing_flows.ipynb** - Flow-based models, invertible networks
- **08_adversarial_vae.ipynb** - Combining VAE and GAN

#### 3. Modern Generative Models
- **09_flow_matching.ipynb** - Continuous normalizing flows
- **10_diffusion_models.ipynb** - Denoising diffusion, score matching
- **11_mixture_models.ipynb** - Mixture Density Networks, Stick-Breaking VAE

### Part II: Optimization & Training

#### 4. Variance Reduction Techniques
- **12_rebar_algorithm.ipynb** - REBAR for discrete variables
- **13_relax_algorithm.ipynb** - RELAX improvements
- **14_gumbel_max_trick.ipynb** - Reparameterization for discrete distributions
- **15_gradient_estimators.ipynb** - Survey of gradient estimation methods

#### 5. Advanced Optimization
- **16_gradient_descent_research.ipynb** - Implicit bias, implicit regularization
- **17_second_order_methods.ipynb** - Natural gradient, K-FAC
- **18_adaptive_learning_rates.ipynb** - Adam variants, lookahead optimizers

### Part III: Model Understanding

#### 6. Neural Network Theory
- **19_neural_tangent_kernel.ipynb** - NTK theory, infinite-width limits
- **20_neural_ode.ipynb** - Continuous depth networks
- **21_adjoint_methods.ipynb** - Memory-efficient backpropagation

#### 7. Attention & Transformers
- **22_attention_variants.ipynb** - Linear attention, efficient transformers
- **23_sparse_attention.ipynb** - Longformer, BigBird patterns
- **24_rotary_embeddings.ipynb** - RoPE, ALiBi positional encodings
- **25_moe_transformers.ipynb** - Mixture of Experts architectures

### Part IV: Advanced Applications

#### 8. 3D Computer Vision
- **26_camera_models.ipynb** - Intrinsic/extrinsic parameters
- **27_epipolar_geometry.ipynb** - Fundamental matrix, essential matrix
- **28_3d_reconstruction.ipynb** - Structure from motion
- **29_depth_estimation.ipynb** - Monocular depth prediction
- **30_3d_pose_estimation.ipynb** - Multi-person, multi-view pose

#### 9. Advanced NLP
- **31_transformer_deep_dive.ipynb** - Advanced transformer architectures
- **32_efficient_transformers.ipynb** - Linformer, Performer
- **33_multimodal_transformers.ipynb** - Vision-language models

### Part V: Special Topics

#### 10. Probabilistic Deep Learning
- **34_bayesian_neural_nets.ipynb** - Uncertainty quantification
- **35_neural_processes.ipynb** - Meta-learning for functions
- **36_gaussian_processes_nn.ipynb** - GP connections to deep learning

#### 11. Modern Architectures
- **37_capsule_networks.ipynb** - Dynamic routing, capsule theory
- **38_graph_neural_networks.ipynb** - GCN, GAT, message passing
- **39_neural_architecture_search.ipynb** - AutoML, DARTS

---

## 🎯 Learning Paths

### Path 1: Generative Modeling Expert
```
01-04 GANs → 05-08 VAEs → 09-11 Modern Generative → 34-36 Probabilistic
```

### Path 2: Optimization Researcher
```
16-18 Advanced Optimization → 12-15 Variance Reduction → 19-21 Theory
```

### Path 3: Computer Vision Specialist
```
26-30 3D Computer Vision → 01-04 GANs → 10 Diffusion Models
```

### Path 4: Transformer/NLP Expert
```
22-25 Advanced Attention → 31-33 Advanced NLP → 37-39 Modern Architectures
```

### Path 5: Complete Research Track
Work through all notebooks sequentially

---

## 📖 Key Research Papers

### Generative Models
- **GANs**: "Generative Adversarial Networks" (Goodfellow et al., 2014)
- **W-GAN**: "Wasserstein GAN" (Arjovsky et al., 2017)
- **VAE**: "Auto-Encoding Variational Bayes" (Kingma & Welling, 2013)
- **Diffusion**: "Denoising Diffusion Probabilistic Models" (Ho et al., 2020)

### Optimization
- **REBAR**: "REBAR: Low-variance gradient estimates" (Tucker et al., 2017)
- **NTK**: "Neural Tangent Kernel" (Jacot et al., 2018)
- **Neural ODE**: "Neural Ordinary Differential Equations" (Chen et al., 2018)

### Transformers
- **Original**: "Attention Is All You Need" (Vaswani et al., 2017)
- **RoPE**: "RoFormer: Enhanced Transformer with Rotary Position Embedding" (Su et al., 2021)
- **Efficient**: "Linformer", "Performer", "Longformer" (2020)

### 3D Vision
- Structure from Motion: Hartley & Zisserman, "Multiple View Geometry"
- Depth estimation: Recent survey papers

Full references in individual notebooks.

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install torch torchvision matplotlib numpy scipy
pip install transformers diffusers  # For modern models

# Optional: 3D vision libraries
pip install opencv-python open3d

# Start with GAN mathematics
jupyter notebook 01_gan_mathematics.ipynb
```

---

## 💻 Code Implementation

Each notebook includes:

### From Scratch
- ✅ Pure NumPy/PyTorch implementations
- 📐 Mathematical derivations
- 🔬 Step-by-step explanations

### Production Ready
- 🚀 Using modern libraries (Hugging Face, etc.)
- ⚡ Optimized implementations
- 🏭 Best practices

### Visualizations
- 📊 Training dynamics
- 🎨 Generated samples
- 📈 Metrics and comparisons

---

## 🎓 Connection to Course

This section extends:

| Foundation | Advanced Extension |
|------------|-------------------|
| 06-neural-networks/05_transformer | 22-25 Advanced Attention |
| 13-multimodal/ | 33 Multimodal Transformers |
| 12-llm-finetuning/ | 16-18 Advanced Optimization |
| 08-rag/ | 19-21 Neural Network Theory |

---

## 📊 Practical Projects

Apply what you learn:

1. **GAN Art Generator**: Train W-GAN on art datasets
2. **VAE for Molecules**: Generate novel molecular structures
3. **3D Scene Reconstruction**: Build SfM pipeline
4. **Efficient Transformer**: Implement linear attention
5. **Neural ODE Classifier**: Continuous depth networks

Project templates included in notebooks.

---

## 🔬 Research Implementation Notes

### Reproducibility
- Exact hyperparameters from papers
- Random seeds for reproducibility
- Multiple runs with error bars

### Computational Requirements
- 🟢 CPU-friendly: Theory, small demos
- 🟡 GPU recommended: Most models
- 🔴 Multi-GPU: Large-scale training

Hardware requirements noted in each notebook.

---

## 🤝 Based on Research From

- **Prof. Yida Xu** - Machine learning research notes
- **DeeCamp Lectures** - Advanced deep learning seminars
- **Recent Publications** - 2018-2024 research papers
- **Industry Practices** - Production-grade implementations

---

## ⚠️ Difficulty Level

**Research/Graduate Level** 🔴🔴🔴🔴

Prerequisites:
- ✅ Strong mathematics (calculus, linear algebra, probability)
- ✅ Deep learning fundamentals
- ✅ PyTorch proficiency
- ✅ Research paper reading experience
- ✅ Graduate-level theoretical understanding

---

## 📬 Questions & Contributions

- **Issues**: Report bugs or ask questions
- **Discussions**: Theoretical discussions, paper recommendations
- **PRs**: Contribute new implementations or improvements

Tags: `advanced-dl`, `research`, `generative-models`, `optimization`

---

## 🎯 Learning Objectives

After completing this section, you will:

1. ✅ Understand cutting-edge generative model theory
2. ✅ Implement advanced optimization techniques
3. ✅ Master variance reduction for discrete variables
4. ✅ Build efficient transformer architectures
5. ✅ Apply deep learning to 3D computer vision
6. ✅ Understand theoretical foundations (NTK, Neural ODE)
7. ✅ Read and implement recent research papers
8. ✅ Contribute to ML research

---

**From Research to Reality** 🚀🔬

> "Research is what I'm doing when I don't know what I'm doing." - Wernher von Braun

Let's discover together! 🌟
