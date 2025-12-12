# NumPy Examples - Consolidated & Deduplicated

This directory contains a comprehensive collection of NumPy tutorials, exercises, and examples, consolidated from multiple GitHub repositories and deduplicated for clarity.

## 📁 Directory Structure

### 01-basics/
**Beginner-friendly tutorials covering fundamental NumPy concepts**

Files from `python-bootcamp-numpy`:
- `01-NumPy Arrays.ipynb` - Array creation and basic operations
- `01-Python Crash Course.ipynb` - Python fundamentals
- `02-Numpy Indexing and Selection.ipynb` - Indexing, slicing, and selection
- `02-Python Crash Course Exercises.ipynb` - Python practice exercises
- `03-Numpy Operations.ipynb` - Mathematical operations and broadcasting

Files from `NumPy` tutorial:
- `NumPy Tutorial.ipynb` - Comprehensive basics tutorial

**Topics Covered:**
- Array creation (from lists, built-in methods)
- Array attributes (shape, dtype, size, ndim)
- Indexing and slicing
- Basic operations (arithmetic, broadcasting)
- Array manipulation

**Recommended Order:** Start with `01-NumPy Arrays.ipynb`, then `NumPy Tutorial.ipynb`

---

### 02-intermediate/
**Intermediate topics for deepening NumPy knowledge**

Files from `Intro_To_Numpy`:
- `intro.ipynb` - Introduction to NumPy concepts
- `intro2.ipynb` - Additional introductory material
- `copyview.ipynb` - Understanding copy vs view
- `filtering.ipynb` - Boolean indexing and filtering
- `fun.ipynb` - Fun NumPy tricks and patterns
- `it.ipynb` - Array iteration techniques
- `s.ipynb` - Stacking and splitting arrays
- `searcher.ipynb` - Searching in arrays
- `shaper.ipynb` - Reshaping and transposing
- `slice.ipynb` - Advanced slicing techniques
- `slice2d.ipynb` - 2D array slicing

**Topics Covered:**
- Memory management (copy vs view)
- Boolean indexing and fancy indexing
- Array searching and filtering
- Reshaping, stacking, splitting
- Advanced iteration patterns

**Note:** `numpy_youtube` directory was a duplicate of this content and has been excluded.

---

### 03-exercises/
**Practice exercises to test and improve your NumPy skills**

#### From `numpy-100`:
- `100_Numpy_exercises.ipynb` - 100 curated NumPy exercises

**Description:** A collection of 100 exercises from easy (★☆☆) to hard (★★★), covering all aspects of NumPy. Great for systematic practice.

#### From `numpy_exercises`:
Topic-based exercise sets with solutions:
- `1_Array_creation_routines.ipynb` / `1_Array_creation_routines_Solution.ipynb`
- `2_Array_manipulation_routines.ipynb` / `2_Array_manipulation_routines_Solution.ipynb`
- `3_Binary_operations.ipynb` / `3_Binary_operations_Solution.ipynb`
- `4_String_operations.ipynb` / `4_String_operations_Solution.ipynb`
- `5_Mathematical_functions.ipynb` / `5_Mathematical_functions_Solutions.ipynb`
- `6_Arithmetic_operations.ipynb` / `6_Arithmetic_operations_Solutions.ipynb`
- `7_Statistics.ipynb` / `7_Statistics_Solutions.ipynb`
- `8_Linear_Algebra.ipynb` / `8_Linear_Algebra_Solutions.ipynb`
- `9_Sorting_and_searching.ipynb` / `9_Sorting_and_searching_Solutions.ipynb`
- `10_Random_sampling.ipynb` / `10_Random_sampling_Solutions.ipynb`
- `11_Set_routines.ipynb` / `11_Set_routines_Solutions.ipynb`

**Recommended Approach:**
1. Start with `100_Numpy_exercises.ipynb` for breadth
2. Use topic-based exercises for depth in specific areas

---

### 04-advanced/
**Advanced tutorials and real-world applications**

#### numpy-tutorials/
Advanced tutorials from the official NumPy tutorials repository:

**Markdown Tutorials:**
- `mooreslaw-tutorial.md` - Data analysis with Moore's Law
- `pairing.md` - Pairing algorithms
- `save-load-arrays.md` - Saving and loading NumPy arrays
- `tutorial-air-quality-analysis.md` - Real-world data analysis
- `tutorial-deep-learning-on-mnist.md` - Deep learning with NumPy
- `tutorial-deep-reinforcement-learning-with-pong-from-pixels.md` - RL implementation
- `tutorial-ma.md` - Moving averages
- `tutorial-nlp-from-scratch.md` - NLP fundamentals
- `tutorial-plotting-fractals.md` - Fractal generation
- `tutorial-static_equilibrium.md` - Physics simulation
- `tutorial-style-guide.md` - NumPy coding best practices

**Data Files:**
- `air-quality-data.csv` - Air quality dataset
- `transistor_data.csv` - Transistor data for Moore's Law

**Topics Covered:**
- Real-world data analysis
- Scientific computing (physics, engineering)
- Deep learning from scratch
- Reinforcement learning
- NLP fundamentals
- Data visualization
- Performance optimization

---

### 05-ml-applications/
**Machine learning algorithms implemented from scratch with NumPy**

#### numpy-ml/
A complete library of ML algorithms implemented in pure NumPy.

**Repository:** `https://github.com/ddbourgin/numpy-ml`

**Contents:**
- Neural networks (MLP, CNNs, RNNs, LSTMs, attention mechanisms)
- Reinforcement learning (DQN, A3C, DDPG)
- Decision trees and ensemble methods
- Linear models (regression, classification)
- Gaussian processes
- Hidden Markov Models
- Bayesian models
- Preprocessing utilities

**Use Cases:**
- Understanding ML algorithms at a low level
- Educational implementations
- Reference for algorithm details
- Building custom ML pipelines

**Note:** This is a complete library. See its README.md for detailed documentation.

---

## 🎯 Learning Path

### Beginner (0-2 weeks)
1. Start with `01-basics/01-NumPy Arrays.ipynb`
2. Work through `01-basics/NumPy Tutorial.ipynb`
3. Practice with first 30 exercises in `03-exercises/100_Numpy_exercises.ipynb`

### Intermediate (2-6 weeks)
1. Complete all notebooks in `02-intermediate/`
2. Finish remaining exercises in `03-exercises/100_Numpy_exercises.ipynb`
3. Work through topic-based exercises in `03-exercises/` (with solutions)

### Advanced (6+ weeks)
1. Study tutorials in `04-advanced/numpy-tutorials/`
2. Implement projects from the tutorials
3. Explore `05-ml-applications/numpy-ml/` for ML implementations

---

## 📊 Content Statistics

- **Total Notebooks:** ~50+ unique notebooks
- **Total Exercises:** 100+ (numpy-100) + 11 topic sets
- **Advanced Tutorials:** 10+ real-world applications
- **ML Implementations:** Complete library with 100+ algorithms

---

## 🗑️ Excluded Content (Duplicates)

The following directories were **excluded** because they contained duplicate content:

### numpy_youtube/
- **Status:** Duplicate of `Intro_To_Numpy/`
- **Reason:** Contains identical files with same filenames
- **Files:** copyview.ipynb, filtering.ipynb, fun.ipynb, intro.ipynb, it.ipynb, s.ipynb, searcher.ipynb, shaper.ipynb, slice.ipynb, slice2d.ipynb

---

## 📚 Source Repositories

This consolidated collection was created from the following GitHub repositories:

1. **python-bootcamp-numpy** - Pierian Data Python for Data Science Bootcamp
2. **NumPy Tutorial** - Basic NumPy tutorial
3. **Intro_To_Numpy** - YouTube-based NumPy course
4. **numpy-100** - https://github.com/rougier/numpy-100
5. **numpy_exercises** - Topic-based NumPy exercises
6. **numpy-tutorials** - https://github.com/numpy/numpy-tutorials
7. **numpy-ml** - https://github.com/ddbourgin/numpy-ml

---

## 🚀 Getting Started

```python
# Install NumPy
pip install numpy

# Import NumPy
import numpy as np

# Verify installation
print(np.__version__)
```

---

## 💡 Tips for Success

1. **Practice Daily:** Work through 3-5 exercises per day
2. **Type Code:** Don't copy-paste; type out examples to build muscle memory
3. **Experiment:** Modify examples to test your understanding
4. **Read Docs:** Use `np.array?` in Jupyter to access documentation
5. **Debug:** Use `print()` statements to understand array shapes and values
6. **Performance:** Use `%timeit` to compare different approaches

---

## 🔗 Additional Resources

- [Official NumPy Documentation](https://numpy.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)
- [NumPy API Reference](https://numpy.org/doc/stable/reference/index.html)
- [From Python to NumPy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)

---

## 📝 Contributing

If you find errors or have improvements:
1. Note the specific file and line number
2. Describe the issue or improvement
3. Submit corrections or enhancements

---

## 📄 License

Individual directories may have their own licenses. Please refer to original repository licenses for attribution and usage rights.

---

**Last Updated:** December 2024
**Consolidated By:** Automated deduplication process
**Total Files Before:** 158 files across 8 directories
**Total Files After:** ~60 unique files (62% reduction)
