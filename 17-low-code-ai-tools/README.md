# Phase 17: Low-Code AI Tools

Build and deploy ML applications with minimal coding using modern low-code platforms and tools.

---

## 📋 Overview

Low-code AI tools democratize machine learning by enabling developers to build, deploy, and share ML applications with minimal code. This phase covers popular frameworks and platforms that accelerate development and make AI accessible.

**Duration:** 8-10 hours  
**Difficulty:** ⭐⭐⭐ Intermediate  
**Prerequisites:** Phases 1-15, Basic Python, ML model training

---

## 🎯 Learning Objectives

By the end of this phase, you will:

1. **Build Interactive UIs** - Create web interfaces for ML models using Gradio
2. **Develop Dashboards** - Build data apps and dashboards with Streamlit
3. **Deploy to Cloud** - Host ML demos on Hugging Face Spaces
4. **Use AutoML** - Leverage automated ML platforms for rapid prototyping
5. **Share Applications** - Deploy and share ML applications with users

---

## 📚 Notebooks

### 1. Introduction to Gradio (90 min)
**File:** [01_gradio_basics.ipynb](01_gradio_basics.ipynb)

Build interactive ML interfaces with just a few lines of code.

**Topics:**
- Gradio fundamentals and interface types
- Image classification demo
- Text generation interface
- Audio processing demo
- Multiple inputs/outputs
- Custom themes and styling

**Key Concepts:**
- `gr.Interface()` for simple demos
- `gr.Blocks()` for complex layouts
- Input/output components
- Live inference
- Sharing with public links

---

### 2. Building with Streamlit (90 min)
**File:** [02_streamlit_apps.ipynb](02_streamlit_apps.ipynb)

Create data-driven web applications and ML dashboards.

**Topics:**
- Streamlit fundamentals
- ML model deployment app
- Data exploration dashboard
- Interactive visualizations
- State management
- Caching for performance

**Key Concepts:**
- `st.write()`, `st.dataframe()`, `st.plotly_chart()`
- Session state
- `@st.cache_data`, `@st.cache_resource`
- Sidebar and columns
- File uploaders

---

### 3. Hugging Face Spaces (75 min)
**File:** [03_huggingface_spaces.ipynb](03_huggingface_spaces.ipynb)

Deploy and host ML demos on the cloud for free.

**Topics:**
- Hugging Face Spaces overview
- Deploying Gradio apps
- Deploying Streamlit apps
- Using pre-trained models from Hub
- Custom requirements and dependencies
- Space configuration

**Key Concepts:**
- Spaces SDK (Gradio, Streamlit, Docker)
- `requirements.txt` and `packages.txt`
- Environment variables and secrets
- Public vs private spaces
- Community sharing

---

### 4. AutoML Platforms (90 min)
**File:** [04_automl_platforms.ipynb](04_automl_platforms.ipynb)

Automate model selection, hyperparameter tuning, and optimization.

**Topics:**
- AutoML overview and use cases
- PyCaret for automated ML
- H2O.ai AutoML
- Auto-sklearn
- FLAML (Fast Lightweight AutoML)
- Comparing AutoML results

**Key Concepts:**
- Automated feature engineering
- Model selection
- Hyperparameter optimization
- Ensemble methods
- Leaderboards and model comparison

---

### 5. End-to-End Low-Code Project (120 min)
**File:** [05_end_to_end_project.ipynb](05_end_to_end_project.ipynb)

Build a complete ML application from data to deployment.

**Topics:**
- Project: Customer Churn Prediction App
- Data loading and exploration
- AutoML model training
- Gradio interface creation
- Streamlit dashboard
- Deployment to Hugging Face Spaces

**Key Concepts:**
- Complete ML workflow
- Model persistence
- User input validation
- Production considerations
- Monitoring and updates

---

## 🛠️ Tools & Libraries

### Core Frameworks
```bash
pip install gradio streamlit
pip install huggingface-hub
pip install pycaret h2o auto-sklearn flaml
```

### Utilities
```bash
pip install scikit-learn pandas numpy
pip install plotly matplotlib seaborn
pip install Pillow opencv-python
```

### Deployment
- **Hugging Face Spaces** - Free ML demo hosting
- **Streamlit Cloud** - Free Streamlit app hosting
- **Gradio** - Built-in sharing via `share=True`

---

## 🎨 Low-Code Workflow

```
┌─────────────────────────────────────────────────┐
│           LOW-CODE ML DEVELOPMENT               │
└─────────────────────────────────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   1. Data Preparation  │
         │   - Load datasets      │
         │   - Basic cleaning     │
         └────────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   2. Model Training    │
         │   - Use AutoML         │
         │   - Compare models     │
         │   - Select best        │
         └────────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   3. Build Interface   │
         │   - Gradio for demos   │
         │   - Streamlit for apps │
         │   - Test locally       │
         └────────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   4. Deploy to Cloud   │
         │   - Hugging Face Space │
         │   - Streamlit Cloud    │
         │   - Share with users   │
         └────────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   5. Monitor & Update  │
         │   - Gather feedback    │
         │   - Improve model      │
         │   - Update deployment  │
         └────────────────────────┘
```

---

## 🎯 Common Use Cases

### When to Use Low-Code Tools

✅ **Gradio**
- Quick ML demos
- Prototype testing
- Research showcases
- Model comparisons
- Educational demos

✅ **Streamlit**
- Data dashboards
- ML applications
- Interactive reports
- Internal tools
- Data exploration

✅ **AutoML**
- Baseline models
- Rapid prototyping
- Non-ML experts
- Time constraints
- Model comparison

❌ **When NOT to Use**
- Highly custom UIs needed
- Very large scale (millions of users)
- Complex backend logic
- Strict performance requirements
- Enterprise security needs (unless self-hosted)

---

## 📊 Platform Comparison

| Feature | Gradio | Streamlit | HF Spaces |
|---------|--------|-----------|-----------|
| **Ease of Use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **ML Focus** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Customization** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Deployment** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Free Hosting** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Learning Curve** | Very Low | Low | Low |
| **Best For** | ML demos | Data apps | Sharing |

---

## 🚀 Quick Start Examples

### Gradio - Image Classifier
```python
import gradio as gr
from transformers import pipeline

classifier = pipeline("image-classification")

def classify_image(img):
    return {label: score for label, score in classifier(img)}

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3)
)

demo.launch()
```

### Streamlit - ML Dashboard
```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("ML Model Dashboard")

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(px.histogram(df, x=df.columns[0]))
    with col2:
        st.plotly_chart(px.box(df, y=df.columns[0]))
```

### AutoML - Quick Training
```python
from pycaret.classification import *

# Load data
data = pd.read_csv('data.csv')

# Initialize setup
clf = setup(data, target='target_column', session_id=42)

# Compare models
best_model = compare_models()

# Make predictions
predictions = predict_model(best_model, data=test_data)
```

---

## 💡 Best Practices

### Interface Design
1. **Keep it simple** - Minimize inputs, clear outputs
2. **Provide examples** - Show users how to use it
3. **Add descriptions** - Explain what the model does
4. **Handle errors** - Validate inputs, show helpful messages
5. **Show processing** - Use progress bars for long operations

### Performance
1. **Cache models** - Load once, reuse
2. **Optimize preprocessing** - Minimize computation
3. **Use appropriate types** - NumPy arrays vs PIL images
4. **Batch when possible** - Process multiple inputs together
5. **Set timeouts** - Prevent hanging requests

### Deployment
1. **Pin dependencies** - Specify exact versions
2. **Test locally first** - Ensure it works before deploying
3. **Monitor usage** - Track errors and performance
4. **Update regularly** - Fix bugs, improve models
5. **Document well** - README with usage instructions

---

## 🔍 Debugging Tips

### Gradio Issues
- **Interface not launching:** Check port availability, use `server_port` parameter
- **Slow inference:** Cache model loading, optimize preprocessing
- **Sharing fails:** Check firewall settings, try `share=True` alternatives

### Streamlit Issues
- **State not persisting:** Use `st.session_state` correctly
- **Constant reruns:** Use `@st.cache_data` for expensive operations
- **Layout problems:** Check column ratios, use containers

### Deployment Issues
- **Space won't start:** Check requirements.txt, review build logs
- **Out of memory:** Reduce model size, use quantization
- **Slow cold starts:** Use smaller models, optimize imports

---

## 🎓 Assessment

### Pre-Quiz
Test your baseline knowledge: [pre-quiz.md](pre-quiz.md)

### Post-Quiz
Verify your learning: [post-quiz.md](post-quiz.md)

### Assignment
**End-to-End ML Application** (100 points)

Build and deploy a complete ML application:
- Train model with AutoML (25 pts)
- Create Gradio demo (25 pts)
- Build Streamlit dashboard (25 pts)
- Deploy to Hugging Face Spaces (25 pts)

Details: [assignment.md](assignment.md)

### Challenges
7 progressive challenges from basic demos to production apps: [challenges.md](challenges.md)

---

## 📈 Success Metrics

You've mastered this phase when you can:

- ✅ Build a Gradio interface in < 10 lines of code
- ✅ Create a Streamlit dashboard with multiple visualizations
- ✅ Deploy an ML app to Hugging Face Spaces
- ✅ Use AutoML to quickly prototype solutions
- ✅ Compare and choose appropriate tools for different use cases
- ✅ Debug and fix common deployment issues
- ✅ Share your ML work with non-technical users

---

## 🔗 Additional Resources

### Documentation
- [Gradio Documentation](https://gradio.app/docs/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces)
- [PyCaret Documentation](https://pycaret.org/)

### Tutorials
- [Gradio Quickstart](https://gradio.app/quickstart/)
- [Streamlit Get Started](https://docs.streamlit.io/get-started)
- [AutoML Comparison](https://epistasislab.github.io/tpot/)

### Community
- [Gradio Discord](https://discord.gg/gradio)
- [Streamlit Forum](https://discuss.streamlit.io/)
- [Hugging Face Discord](https://discord.gg/huggingface)

---

## 🎯 What's Next?

After completing Phase 17:

1. **Phase 18:** Production ML Systems
2. **Advanced Topics:** Custom deployment strategies
3. **Specializations:** Industry-specific applications
4. **Projects:** Build your portfolio of deployed apps

---

## 🏆 Phase Completion

Track your progress:

- [ ] Complete all 5 notebooks
- [ ] Pass pre and post quizzes (70%+)
- [ ] Complete assignment (70%+)
- [ ] Attempt 3+ challenges
- [ ] Deploy at least one app to Hugging Face Spaces
- [ ] Share your work with the community

---

**Ready to democratize AI? Let's build! 🚀**
