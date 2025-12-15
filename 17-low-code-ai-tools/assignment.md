# Assignment: Build and Deploy a Complete Low-Code ML Application

**Phase 17: Low-Code AI Tools**  
**Total Points:** 100  
**Due:** As specified by your instructor

---

## 📋 Assignment Overview

Build and deploy a complete machine learning application using low-code tools. Your application should include AutoML model training, an interactive interface (Gradio or Streamlit), and deployment to Hugging Face Spaces.

---

## 🎯 Learning Objectives

- Apply AutoML for model development
- Build user-friendly ML interfaces
- Deploy applications to the cloud
- Integrate multiple low-code tools
- Follow best practices for production ML

---

## 📝 Requirements

### Part 1: Dataset and Problem (15 points)

**Choose ONE of the following:**

#### Option A: Classification Problem
- Predict customer behavior (churn, purchase, click)
- Medical diagnosis
- Sentiment analysis
- Fraud detection

#### Option B: Regression Problem
- Price prediction (house, stock, product)
- Demand forecasting
- Performance estimation
- Time series prediction

**Deliverables:**
- Dataset description (source, size, features)
- Problem statement
- Success metrics
- Exploratory data analysis (EDA)

**Grading:**
- Clear problem definition (5 pts)
- Appropriate dataset (5 pts)
- EDA with visualizations (5 pts)

---

### Part 2: Model Training with AutoML (25 points)

Use **PyCaret**, **FLAML**, or **H2O AutoML** to train your model.

**Requirements:**
- Data preprocessing (handle missing values, encode categoricals)
- Train multiple models using AutoML
- Compare at least 5 different algorithms
- Tune hyperparameters of best model
- Evaluate performance (accuracy, precision, recall, etc.)
- Save final model

**Deliverables:**
- Jupyter notebook with AutoML pipeline
- Model comparison results
- Performance metrics on test set
- Saved model file (.pkl or .h5)

**Grading:**
- Proper data preprocessing (7 pts)
- Model comparison and selection (8 pts)
- Performance evaluation (5 pts)
- Model saved correctly (5 pts)

---

### Part 3: Interactive Interface (30 points)

Build **EITHER** a Gradio interface **OR** a Streamlit app.

#### Option A: Gradio Interface

**Requirements:**
- Clear input components for all features
- Prediction output with confidence score
- At least 3 example inputs
- Custom theme and styling
- Error handling for invalid inputs

#### Option B: Streamlit App

**Requirements:**
- Sidebar for input controls
- Main area for predictions and visualizations
- Session state for user interactions
- Caching for model loading
- Interactive charts (plotly or matplotlib)

**Both Options Must Include:**
- Clear instructions for users
- Feature descriptions/tooltips
- Actionable output (not just raw predictions)
- Professional appearance

**Deliverables:**
- app.py file with complete interface
- requirements.txt with all dependencies
- Screenshots of working interface

**Grading:**
- User-friendly design (10 pts)
- Proper functionality (10 pts)
- Error handling and edge cases (5 pts)
- Professional appearance (5 pts)

---

### Part 4: Deployment (20 points)

Deploy your application to **Hugging Face Spaces**.

**Requirements:**
- Create Hugging Face account
- Set up new Space (Gradio or Streamlit SDK)
- Upload all necessary files:
  - app.py
  - requirements.txt
  - README.md (with frontmatter)
  - Trained model
- Ensure app runs successfully
- Test all features in deployed version

**Deliverables:**
- Public Hugging Face Space URL
- README.md with:
  - App description
  - Usage instructions
  - Model information
  - Example inputs
- Working deployed application

**Grading:**
- Successful deployment (8 pts)
- Complete README (5 pts)
- App functionality (5 pts)
- Professional presentation (2 pts)

---

### Part 5: Documentation and Report (10 points)

**Create a comprehensive report including:**

1. **Introduction** (1-2 pages)
   - Problem description
   - Dataset overview
   - Approach summary

2. **Methods** (2-3 pages)
   - AutoML platform choice and justification
   - Model comparison process
   - Final model selection reasoning
   - Interface design decisions

3. **Results** (1-2 pages)
   - Model performance metrics
   - Comparison table
   - Visualizations of results
   - Discussion of strengths/limitations

4. **Deployment** (1 page)
   - Deployment process
   - Challenges faced
   - Solutions implemented

5. **Conclusion** (1 page)
   - Summary of achievements
   - Lessons learned
   - Future improvements

**Deliverables:**
- PDF report (5-10 pages)
- Well-organized sections
- Visualizations and tables
- References (if applicable)

**Grading:**
- Clarity and organization (4 pts)
- Technical accuracy (3 pts)
- Completeness (3 pts)

---

## 🌟 Bonus Points (Up to 15 extra points)

### Bonus Options:

1. **Advanced Features** (5 pts each, max 10 pts)
   - SHAP explanations for predictions
   - Batch prediction with file upload
   - Model comparison dashboard
   - Real-time data visualization
   - A/B testing different models

2. **Additional Deployment** (5 pts)
   - Deploy to multiple platforms (Docker, Cloud Run, etc.)
   - Set up CI/CD pipeline
   - Add monitoring/logging

3. **Outstanding Quality** (5 pts)
   - Exceptional documentation
   - Production-ready code quality
   - Comprehensive error handling
   - Accessibility features

---

## 📤 Submission Guidelines

### Submit the following:

1. **GitHub Repository** containing:
   - Jupyter notebook(s) for model training
   - app.py for interface
   - requirements.txt
   - README.md
   - Saved model file
   - Any additional code files

2. **Hugging Face Space URL**
   - Working deployed application
   - Complete README on Space

3. **Report (PDF)**
   - Following structure outlined above

4. **Submission Form** with:
   - Your name and student ID
   - GitHub repository URL
   - Hugging Face Space URL
   - Report PDF
   - Brief summary (200 words)

### Submission Format:
- ZIP file containing all materials
- Named: `LastName_FirstName_Phase17_Assignment.zip`
- Submit via course platform by deadline

---

## ✅ Evaluation Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Dataset & Problem** | 15 | Clear problem, appropriate data, EDA |
| **AutoML Training** | 25 | Proper workflow, model comparison, evaluation |
| **Interface** | 30 | User-friendly, functional, professional |
| **Deployment** | 20 | Working app, complete README, accessible |
| **Documentation** | 10 | Clear, organized, comprehensive report |
| **Bonus** | +15 | Advanced features, extra deployment, quality |
| **TOTAL** | 100 (+15) | |

---

## 💡 Tips for Success

### Technical Tips:
1. **Start simple** - Get basic version working first
2. **Test locally** - Debug before deploying
3. **Version control** - Commit frequently
4. **Pin dependencies** - Specify exact versions
5. **Handle errors** - Add try-except blocks

### Design Tips:
1. **User-first** - Think about user experience
2. **Clear labels** - Make inputs obvious
3. **Provide examples** - Help users understand
4. **Show confidence** - Display prediction uncertainty
5. **Add context** - Explain what predictions mean

### Deployment Tips:
1. **Check requirements** - Test all dependencies
2. **Optimize model** - Reduce size if possible
3. **Test thoroughly** - Try edge cases
4. **Monitor logs** - Watch build process
5. **Update README** - Keep documentation current

---

## 📚 Resources

### AutoML Platforms:
- [PyCaret Documentation](https://pycaret.org/)
- [FLAML Documentation](https://microsoft.github.io/FLAML/)
- [H2O AutoML Guide](https://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html)

### Interface Tools:
- [Gradio Documentation](https://gradio.app/docs/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Gradio Themes](https://gradio.app/theming-guide/)

### Deployment:
- [Hugging Face Spaces Docs](https://huggingface.co/docs/hub/spaces)
- [Spaces Configuration](https://huggingface.co/docs/hub/spaces-config-reference)
- [Docker Deployment](https://huggingface.co/docs/hub/spaces-sdks-docker)

### Example Projects:
- Browse Hugging Face Spaces for inspiration
- Check course notebooks for patterns
- Review PyCaret examples

---

## ❓ FAQ

**Q: Can I use my own dataset?**  
A: Yes! As long as it meets the requirements (appropriate size, clear problem).

**Q: Which AutoML platform should I use?**  
A: PyCaret is recommended for beginners. FLAML for faster training. H2O for larger datasets.

**Q: Gradio or Streamlit?**  
A: Gradio is simpler for basic interfaces. Streamlit offers more customization.

**Q: What if my model is too large to upload?**  
A: Use model compression, reduce features, or use Git LFS for large files.

**Q: How long should my app take to load?**  
A: Aim for < 30 seconds initial load, < 2 seconds per prediction.

**Q: Can I work in a group?**  
A: Check with your instructor. Usually individual work is required.

**Q: What if deployment fails?**  
A: Check logs, verify requirements.txt, test locally first, ask for help.

---

## 🎯 Example Project Ideas

### Beginner Level:
- Iris flower classifier
- Boston house price predictor
- Titanic survival predictor
- Wine quality estimator

### Intermediate Level:
- Customer churn predictor
- Loan default predictor
- Product recommendation system
- Sentiment analyzer

### Advanced Level:
- Real-time fraud detection
- Medical diagnosis assistant
- Stock price forecaster
- Image classification system

---

## 🏆 Grading Timeline

- **Week 1:** Dataset selection and EDA
- **Week 2:** Model training and evaluation
- **Week 3:** Interface development
- **Week 4:** Deployment and documentation
- **Final:** Submit complete project

**Late Submission:** -10% per day, up to 3 days

---

## 📧 Getting Help

- **Office Hours:** [Specify times]
- **Discussion Forum:** [Link]
- **Email:** [Instructor email]
- **Technical Issues:** Include error logs and screenshots

---

**Good luck! Build something amazing! 🚀**
