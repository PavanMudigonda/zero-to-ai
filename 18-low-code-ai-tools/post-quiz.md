# Post-Quiz: Low-Code AI Tools

**Phase 17: Low-Code AI Tools**  
**Duration:** 25 minutes  
**Questions:** 18

---

## Instructions

This quiz assesses your understanding after completing Phase 17.

- Answer all questions
- Reference course materials if needed
- Select the best answer for each question
- Aim for 80%+ to demonstrate mastery

---

## Section 1: Gradio Fundamentals (Questions 1-5)

### 1. Which Gradio function creates a simple interface with a single function?

A) `gr.Blocks()`  
B) `gr.Interface()`  
C) `gr.App()`  
D) `gr.create()`

<details>
<summary>Answer</summary>

**B) gr.Interface()**

`gr.Interface()` creates a simple interface by wrapping a function with input and output components.
</details>

---

### 2. What is the main advantage of `gr.Blocks()` over `gr.Interface()`?

A) Faster performance  
B) More customizable layouts and complex workflows  
C) Requires less code  
D) Better mobile support

<details>
<summary>Answer</summary>

**B) More customizable layouts and complex workflows**

`gr.Blocks()` provides full control over layout and enables multi-step workflows, conditional displays, and custom arrangements.
</details>

---

### 3. Which component would you use for image classification output?

A) `gr.Image()`  
B) `gr.Text()`  
C) `gr.Label()`  
D) `gr.Plot()`

<details>
<summary>Answer</summary>

**C) gr.Label()**

`gr.Label()` displays classification results with class names and confidence scores, perfect for classification tasks.
</details>

---

### 4. How do you create a custom theme in Gradio?

A) `gr.Theme(primary_color="blue")`  
B) `gr.themes.Soft()`  
C) Modify CSS directly  
D) Both B and C

<details>
<summary>Answer</summary>

**D) Both B and C**

You can use built-in themes like `gr.themes.Soft()` or customize with CSS for complete control.
</details>

---

### 5. What is the purpose of providing `examples` in Gradio?

A) To train the model  
B) To help users understand expected inputs  
C) To validate inputs  
D) To cache results

<details>
<summary>Answer</summary>

**B) To help users understand expected inputs**

Examples show users what kind of inputs work well and improve the user experience by providing ready-to-test data.
</details>

---

## Section 2: Streamlit Applications (Questions 6-10)

### 6. What happens when a user interacts with any Streamlit widget?

A) Only that widget updates  
B) The entire script reruns from top to bottom  
C) The app crashes  
D) Nothing happens

<details>
<summary>Answer</summary>

**B) The entire script reruns from top to bottom**

Streamlit's reactive model reruns the entire script whenever a widget changes, which is why caching and session state are important.
</details>

---

### 7. Which decorator should you use to cache a trained ML model in Streamlit?

A) `@st.cache`  
B) `@st.cache_data`  
C) `@st.cache_resource`  
D) `@st.memo`

<details>
<summary>Answer</summary>

**C) @st.cache_resource**

`@st.cache_resource` is used for resources that should persist across reruns and not be copied, like ML models or database connections.
</details>

---

### 8. How do you organize content into tabs in Streamlit?

A) `st.sidebar()`  
B) `st.tabs(["Tab1", "Tab2"])`  
C) `st.columns()`  
D) `st.expander()`

<details>
<summary>Answer</summary>

**B) st.tabs(["Tab1", "Tab2"])**

`st.tabs()` creates tabbed sections, returning tab objects that can be used with context managers.
</details>

---

### 9. What's the correct way to persist a counter across Streamlit reruns?

A) Use a global variable  
B) Use `st.session_state.counter`  
C) Store in a file  
D) Use `@st.cache_data`

<details>
<summary>Answer</summary>

**B) Use st.session_state.counter**

`st.session_state` is the proper way to persist values across reruns in Streamlit.
</details>

---

### 10. Which is better for displaying interactive plots in Streamlit?

A) matplotlib  
B) seaborn  
C) plotly  
D) ASCII art

<details>
<summary>Answer</summary>

**C) plotly**

While Streamlit supports all plotting libraries, Plotly provides interactive features like zoom, pan, and hover that work seamlessly in Streamlit.
</details>

---

## Section 3: Hugging Face Spaces (Questions 11-13)

### 11. What are the three main SDK options for Hugging Face Spaces?

A) Python, Java, JavaScript  
B) Gradio, Streamlit, Docker  
C) Flask, Django, FastAPI  
D) React, Vue, Angular

<details>
<summary>Answer</summary>

**B) Gradio, Streamlit, Docker**

Hugging Face Spaces supports Gradio SDK, Streamlit SDK, Docker SDK, and Static (HTML) sites.
</details>

---

### 12. Where should you specify your Space's SDK in Hugging Face?

A) In requirements.txt  
B) In README.md frontmatter  
C) In app.py  
D) In config.json

<details>
<summary>Answer</summary>

**B) In README.md frontmatter**

The README.md frontmatter (YAML at the top) specifies configuration like SDK type, version, and other metadata.
</details>

---

### 13. How do you manage sensitive API keys in a Hugging Face Space?

A) Hard-code them in app.py  
B) Put them in README.md  
C) Use Space Settings → Repository secrets  
D) Include them in requirements.txt

<details>
<summary>Answer</summary>

**C) Use Space Settings → Repository secrets**

Repository secrets in Space Settings allow secure storage of API keys accessible via `os.environ` without exposing them in code.
</details>

---

## Section 4: AutoML (Questions 14-16)

### 14. What does PyCaret's `compare_models()` function do?

A) Compares two specific models  
B) Trains and evaluates multiple algorithms, returning the best  
C) Only compares model sizes  
D) Compares training times only

<details>
<summary>Answer</summary>

**B) Trains and evaluates multiple algorithms, returning the best**

`compare_models()` trains 10+ algorithms, evaluates them on various metrics, and returns the top performers sorted by your chosen metric.
</details>

---

### 15. In FLAML, what does the `time_budget` parameter control?

A) Total project timeline  
B) Maximum seconds for AutoML search  
C) Inference time per prediction  
D) Data loading time

<details>
<summary>Answer</summary>

**B) Maximum seconds for AutoML search**

`time_budget` sets the maximum time (in seconds) FLAML will spend searching for the best model configuration.
</details>

---

### 16. Which AutoML platform is best for very large datasets?

A) PyCaret  
B) FLAML  
C) H2O AutoML  
D) Manual GridSearch

<details>
<summary>Answer</summary>

**C) H2O AutoML**

H2O AutoML is designed for distributed computing and can handle very large datasets efficiently across clusters.
</details>

---

## Section 5: Integration & Best Practices (Questions 17-18)

### 17. What's the recommended workflow for deploying an ML app?

A) Deploy directly → Test in production  
B) Train → Interface → Test locally → Deploy → Monitor  
C) Test → Train → Deploy  
D) Deploy → Train → Monitor

<details>
<summary>Answer</summary>

**B) Train → Interface → Test locally → Deploy → Monitor**

The proper workflow is: train model, build interface, test thoroughly locally, deploy to production, then monitor performance.
</details>

---

### 18. Which is a production-ready best practice?

A) Use random model predictions  
B) Pin exact dependency versions  
C) Never handle errors  
D) Skip documentation

<details>
<summary>Answer</summary>

**B) Pin exact dependency versions**

Pinning exact versions (e.g., `gradio==4.0.0`) ensures reproducible builds and prevents breaking changes from updates.
</details>

---

## Bonus Questions (Optional, +5 points each)

### B1. How would you implement batch predictions in a Gradio app?

A) Run predict() in a loop  
B) Use `gr.File()` for CSV upload, process DataFrame  
C) Not possible in Gradio  
D) Use multiple interfaces

<details>
<summary>Answer</summary>

**B) Use gr.File() for CSV upload, process DataFrame**

Accept a CSV file with `gr.File()`, read it into a DataFrame, run predictions on all rows, and return results as a downloadable file.
</details>

---

### B2. What's the best way to explain model predictions to users?

A) Show only the prediction  
B) Add SHAP values, feature importance, or confidence scores  
C) Show model architecture  
D) Display training data

<details>
<summary>Answer</summary>

**B) Add SHAP values, feature importance, or confidence scores**

Explanations like SHAP values, feature importance, and confidence scores help users understand and trust predictions.
</details>

---

### B3. How can you reduce cold start time for a deployed ML app?

A) Use larger models  
B) Cache model loading with @st.cache_resource or preload  
C) Increase memory  
D) Deploy multiple times

<details>
<summary>Answer</summary>

**B) Cache model loading with @st.cache_resource or preload**

Loading models once at startup and caching them prevents reload on every request, dramatically improving response time.
</details>

---

## Scoring Guide

### Standard Questions (18 questions, 5 points each = 90 points):
- **16-18 correct (85-100%):** 🏆 Excellent! You've mastered low-code ML tools.
- **14-15 correct (75-85%):** ✅ Great! Solid understanding.
- **11-13 correct (60-75%):** 📚 Good! Review challenging topics.
- **Below 11 (< 60%):** 🔄 Review course materials and retake.

### Bonus Questions (3 questions, 5 points each = +15 points max):
- **Total possible:** 105 points

---

## Answer Summary

Quick reference (don't peek before completing!):

1. B | 2. B | 3. C | 4. D | 5. B | 6. B  
7. C | 8. B | 9. B | 10. C | 11. B | 12. B  
13. C | 14. B | 15. B | 16. C | 17. B | 18. B  
B1. B | B2. B | B3. B

---

## Weak Areas Review Guide

If you missed questions in:

**Section 1 (Gradio):** Review Notebook 1
- `gr.Interface()` vs `gr.Blocks()`
- Component types
- Themes and customization

**Section 2 (Streamlit):** Review Notebook 2
- Rerun behavior
- Caching strategies
- Session state
- Widgets and layout

**Section 3 (Hugging Face):** Review Notebook 3
- Space configuration
- Deployment process
- Secrets management

**Section 4 (AutoML):** Review Notebook 4
- PyCaret workflow
- FLAML time budgets
- Platform selection

**Section 5 (Integration):** Review Notebook 5
- End-to-end workflow
- Best practices
- Production considerations

---

## Next Steps

### If you scored 85%+:
✅ You're ready for production ML app development!  
✅ Try the advanced challenges  
✅ Build and deploy your own project  
✅ Share your knowledge with others

### If you scored 60-84%:
📚 Review sections where you struggled  
📚 Revisit relevant notebooks  
📚 Complete practice exercises  
📚 Retake quiz in a few days

### If you scored < 60%:
🔄 Review all course materials  
🔄 Work through notebooks step-by-step  
🔄 Complete challenges 1-3  
🔄 Seek help from instructor/community  
🔄 Retake quiz after review

---

## Certificate Eligibility

To earn Phase 17 completion certificate:
- Score 80%+ on this quiz
- Complete assignment (70%+ grade)
- Finish at least 3 challenges

---

**Congratulations on completing Phase 17! 🎉**

Keep building amazing ML applications! 🚀
