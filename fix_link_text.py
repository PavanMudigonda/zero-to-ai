import re

files_to_fix = {
    "docs/curriculum/02-data-science/3-data-science-examples/01-microsoft-course/3-Data-Visualization/09-visualization-quantities/README.md": [
        (r'\[here\]\(https://matplotlib\.org/cheatsheets/cheatsheets\.pdf\)', r'[Matplotlib cheat sheets](https://matplotlib.org/cheatsheets/cheatsheets.pdf)')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/01-microsoft-course/3-Data-Visualization/09-visualization-quantities/translations/README.hi.md": [
        (r'\[here\]\(https://matplotlib\.org/cheatsheets/cheatsheets\.pdf\)', r'[Matplotlib cheat sheets](https://matplotlib.org/cheatsheets/cheatsheets.pdf)')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/01-microsoft-course/3-Data-Visualization/09-visualization-quantities/translations/README.ko.md": [
        (r'\[here\]\(https://matplotlib\.org/cheatsheets/cheatsheets\.pdf\)', r'[Matplotlib cheat sheets](https://matplotlib.org/cheatsheets/cheatsheets.pdf)')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/01-microsoft-course/3-Data-Visualization/R/11-visualization-proportions/README.md": [
        (r'learn more about it \[here\]\(https://www\.r-graph-gallery\.com/128-ring-or-donut-plot\.html\)', r'read the [R graph gallery donut plot guide](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html)')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/01-microsoft-course/2-Working-With-Data/06-non-relational/README.md": [
        (r'Read more about the Emulator \[here\]\(https://docs\.microsoft\.com/en-us/azure/cosmos-db/local-emulator\?tabs=ssl-netstd21\)', r'Read the [Cosmos DB Emulator documentation](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21)')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/01-microsoft-course/2-Working-With-Data/07-python/notebook-papers.ipynb": [
        (r'described \[here\]\(https://www\.nltk\.org/book/ch07\.html\)', r'described in the [NLTK book, Chapter 7](https://www.nltk.org/book/ch07.html)'),
        (r'\[this blog post\]\(https://soshnikov\.com', r'[this blog post on entity extraction](https://soshnikov.com')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/01-microsoft-course/1-Introduction/04-stats-and-probability/assignment.md": [
        (r'taken from \[here\]\(https://www4\.stat\.ncsu\.edu/~boos/var\.select/diabetes\.html\)', r'taken from the [NCSU diabetes dataset repository](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html)')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/01-microsoft-course/5-Data-Science-In-Cloud/19-Azure/README.md": [
        (r'Check \[here\]\(\.\./18-Low-Code/README\.md\) the Heart failure prediction project', r'Check the [Heart failure prediction project introduction](../18-Low-Code/README.md)')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/05-reference-notebooks/spark/spark.ipynb": [
        (r'provided \[here\]\(http://ramhiser\.com', r'provided in the [IPython Notebook Support for PySpark guide](http://ramhiser.com')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/04-deep-learning/tensorflow-keras/tensor-flow-examples/Setup_TensorFlow.md": [
        (r'\[here\]\(#virtualenv_install\)', r'[the virtualenv installation section](#virtualenv_install)'),
        (r'\[here\]\(http://bazel\.io/docs/install\.html\)', r'[the Bazel installation documentation](http://bazel.io/docs/install.html)'),
        (r'\[this\]\(http://bazel\.io/docs/install\.html\) page', r'[the Bazel installation documentation](http://bazel.io/docs/install.html)'),
        (r'\[here\]\(http://docs\.scipy\.org/doc/numpy/user/install\.html\)', r'[the NumPy installation guide](http://docs.scipy.org/doc/numpy/user/install.html)')
    ],
    "docs/curriculum/02-data-science/3-data-science-examples/04-deep-learning/tensorflow-keras/keras-tutorial/2.2.1-Supervised-Learning-ConvNet-HandsOn-Part-I.ipynb": [
        (r'\(\[link\]\(http://yann\.lecun\.com/exdb/mnist\)\)', r'([MNIST database source](http://yann.lecun.com/exdb/mnist))')
    ],
    "docs/curriculum/02-data-science/1-numpy-examples/04-advanced/numpy-tutorials/tutorial-nlp-from-scratch.md": [
        (r'\[this\]\(https://link\.springer\.com/chapter/10\.1007%2F978-3-030-14524-8_11\) source', r'[this Springer Springer NLP publication](https://link.springer.com/chapter/10.1007%2F978-3-030-14524-8_11)')
    ]
}

replaced = 0
for filepath, replacements in files_to_fix.items():
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements:
            content, count = re.subn(old, new, content)
            replaced += count
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except FileNotFoundError:
        pass

print(f"Made {replaced} generic link text replacements.")
