'use client';

import React from 'react';
import { Notebook } from '@jupyter-kit/react';
import '@jupyter-kit/theme-default/default.css';
import '@jupyter-kit/theme-default/syntax/one-dark.css';
import 'katex/dist/katex.min.css';

// Language parsing
import { python } from '@jupyter-kit/core/langs/python';
import { python as cmPython } from '@codemirror/lang-python';

// Editor and Executor features
import { createEditorPlugin } from '@jupyter-kit/editor-codemirror';
import { createPyodideExecutor } from '@jupyter-kit/executor-pyodide';

// KaTeX for math rendering
import { createKatexPlugin } from '@jupyter-kit/katex';

const myPyodide = createPyodideExecutor({ packages: [] });
const myEditor = createEditorPlugin({
  languages: { python: cmPython() }
});
const myKatex = createKatexPlugin();

export default function NotebookViewer({ ipynb }: { ipynb: any }) {
  return (
    <div className="my-8 jk-notebook-container overflow-hidden rounded shadow-sm border border-gray-200 dark:border-gray-800">
      <Notebook 
        ipynb={ipynb} 
        language="python" 
        languages={[python]} 
        executor={myPyodide}
        plugins={[myEditor, myKatex]}
        mathAlign="left"
      />
    </div>
  );
}
