'use client';

import React from 'react';
import { usePathname } from 'next/navigation';
import { Notebook } from '@jupyter-kit/react';
import { normalizeNotebookLinks } from '@/lib/notebook-link-utils';
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
  const pathname = usePathname();
  const normalizedNotebook = normalizeNotebookLinks(ipynb, pathname || '/');

  // Infer the GitHub notebook path intelligently from the App router URL structure
  const segments = typeof pathname === 'string' ? pathname.split('/').filter(Boolean) : [];
  const folderName = segments.length > 0 ? segments[segments.length - 1] : '';
  const isDemo = segments.length === 0;
  const notebookFileName = isDemo ? 'demo.ipynb' : `${folderName}.ipynb`;

  const repoBase = "PavanMudigonda/zero-to-ai";
  const branch = "main";
  const githubPath = isDemo ? `next-docs/src/app/${notebookFileName}` : `next-docs/src/app${pathname}/${notebookFileName}`;
  
  const githubUrl = `https://github.com/${repoBase}/blob/${branch}/${githubPath}`;
  const colabUrl = `https://colab.research.google.com/github/${repoBase}/blob/${branch}/${githubPath}`;
  const kaggleUrl = `https://kaggle.com/kernels/welcome?src=${githubUrl}`;
  const studioLabUrl = `https://studiolab.sagemaker.aws/import/github/${repoBase}/blob/${branch}/${githubPath}`;

  const linkClass = "text-xs font-medium px-2.5 py-1.5 rounded border border-gray-200 dark:border-gray-700 bg-white dark:bg-[#111] text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors inline-flex items-center justify-center gap-1.5 shadow-sm";

  return (
    <div className="my-8 overflow-hidden rounded-lg shadow-sm border border-gray-200 dark:border-gray-800 bg-[var(--nextra-bg)]">
      {/* External Action Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 px-4 py-3 bg-gray-50/80 dark:bg-[#0a0a0a] border-b border-gray-200 dark:border-gray-800">
        <div className="flex items-center gap-2 text-sm font-semibold text-gray-700 dark:text-gray-200">
          <svg className="w-5 h-5 text-yellow-500" viewBox="0 0 128 128" fill="none" xmlns="http://www.w3.org/2000/svg">
             <path d="M63.882 121.761C95.955 121.761 122 95.836 122 63.881C122 31.925 95.955 6 63.882 6C31.81 6 5.765 31.925 5.765 63.881C5.765 95.836 31.81 121.761 63.882 121.761Z" fill="#F37626"/>
             <path d="M63.882 108.972C88.85 108.972 109.117 88.788 109.117 63.881C109.117 38.974 88.85 18.79 63.882 18.79C38.914 18.79 18.647 38.974 18.647 63.881C18.647 88.788 38.914 108.972 63.882 108.972Z" fill="white"/>
             <path d="M63.882 101.272C84.582 101.272 101.378 84.537 101.378 63.881C101.378 43.225 84.582 26.49 63.882 26.49C43.181 26.49 26.386 43.225 26.386 63.881C26.386 84.537 43.181 101.272 63.882 101.272Z" fill="#F37626"/>
             <path d="M47.014 47.917C50.298 47.917 52.96 45.263 52.96 41.989C52.96 38.715 50.298 36.061 47.014 36.061C43.73 36.061 41.068 38.715 41.068 41.989C41.068 45.263 43.73 47.917 47.014 47.917Z" fill="white"/>
             <path d="M80.009 84.452C83.293 84.452 85.955 81.798 85.955 78.524C85.955 75.25 83.293 72.596 80.009 72.596C76.725 72.596 74.063 75.25 74.063 78.524C74.063 81.798 76.725 84.452 80.009 84.452Z" fill="white"/>
          </svg>
          Jupyter 
        </div>
        <div className="flex items-center gap-2">
          <a href={colabUrl} target="_blank" rel="noreferrer" className={linkClass}>
             <svg className="w-3.5 h-3.5" viewBox="0 0 256 256" fill="none"><path d="M128 0C57.307 0 0 57.307 0 128c0 70.693 57.307 128 128 128 70.693 0 128-57.307 128-128C256 57.307 198.693 0 128 0Zm0 230.4c-56.452 0-102.4-45.948-102.4-102.4S71.548 25.6 128 25.6 230.4 71.548 230.4 128 184.452 230.4 128 230.4Z" fill="#F9AB00"/><path d="M128 51.2c-42.348 0-76.8 34.452-76.8 76.8s34.452 76.8 76.8 76.8 76.8-34.452 76.8-76.8-34.452-76.8-76.8-76.8Zm0 128c-28.226 0-51.2-22.974-51.2-51.2S99.774 76.8 128 76.8 179.2 99.774 179.2 128s-22.974 51.2-51.2 51.2Z" fill="#F9AB00"/></svg>
             Colab
          </a>
          <a href={kaggleUrl} target="_blank" rel="noreferrer" className={linkClass}>
             <svg className="w-3.5 h-3.5 text-blue-500" viewBox="0 0 32 32" fill="currentColor"><path d="M28.468 31.423l-10.155-14.28 9.948-15.688h-4.85l-7.391 11.83-1.637-2.612V1.455H10v29.968h4.382V20.21l1.78 2.378 7.558 8.835h4.748z"/></svg>
             Kaggle
          </a>
          <a href={studioLabUrl} target="_blank" rel="noreferrer" className={linkClass}>
             <svg className="w-3.5 h-3.5 text-orange-500" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.376L4.016 7v10.024L12 21.624l7.984-4.592V7Z"/></svg>
             SageMaker
          </a>
        </div>
      </div>
      
      {/* Internal Notebook Engine */}
      <div className="jk-notebook-container">
        <Notebook 
          ipynb={normalizedNotebook} 
          language="python" 
          languages={[python]} 
          executor={myPyodide}
          plugins={[myEditor, myKatex]}
          mathAlign="left"
        />
      </div>
    </div>
  );
}
