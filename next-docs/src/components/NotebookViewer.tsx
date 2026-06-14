'use client';

import React, { useEffect, useRef, useState } from 'react';
import { usePathname } from 'next/navigation';
import { Notebook } from '@jupyter-kit/react';
import type { Ipynb } from '@jupyter-kit/core';
import generatedRouteIndex from '@/generated/route-index';
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

type NotebookResource = {
  label: string;
  url: string;
};

const myPyodide = createPyodideExecutor({ packages: [] });
const myEditor = createEditorPlugin({
  languages: { python: cmPython() }
});
const myKatex = createKatexPlugin();

const YOUTUBE_URL_PATTERN = /https?:\/\/(?:www\.)?(?:youtube\.com|youtu\.be)\/[^\s)"']+/i;
const MARKDOWN_EXTERNAL_LINK_PATTERN = /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/gi;
const EXCLUDED_RESOURCE_HOSTS = new Set([
  'youtube.com',
  'www.youtube.com',
  'youtu.be',
]);

const PROVIDER_METADATA_REGEX = /^(?:#|<!--)\s*resource\.(video|docs|paper|repo):\s*(https?:\/\/[^\s]+)/gm;

function extractNotebookMetadata(ipynb: Ipynb): Record<string, string> {
  const meta: Record<string, string> = {};

  if (!ipynb.cells || ipynb.cells.length === 0) {
    return meta;
  }

  // Look only at the first few cells to avoid scanning entire notebooks
  const searchCells = ipynb.cells.slice(0, 3);

  for (const cell of searchCells) {
    if (cell.cell_type !== 'markdown' || !cell.source) continue;
    const source = Array.isArray(cell.source) ? cell.source.join('') : cell.source;

    for (const match of source.matchAll(PROVIDER_METADATA_REGEX)) {
      const type = match[1];
      const url = match[2];
      if (type && url) {
        meta[type] = url;
      }
    }
  }

  return meta;
}

function toHostname(url: string): string {
  try {
    return new URL(url).hostname.toLowerCase();
  } catch {
    return '';
  }
}

function formatResourceLabel(rawLabel: string, url: string): string {
  const trimmedLabel = rawLabel.trim().replace(/^[#*\-\d.\s]+/, '');
  const hostname = toHostname(url).replace(/^www\./, '');

  if (trimmedLabel && trimmedLabel.length <= 24) {
    return trimmedLabel;
  }

  if (hostname === 'github.com') {
    return 'GitHub';
  }

  if (hostname === 'huggingface.co') {
    return 'Hugging Face';
  }

  if (hostname === 'arxiv.org') {
    return 'arXiv';
  }

  if (hostname === 'artificialanalysis.ai') {
    return 'Artificial Analysis';
  }

  if (hostname === 'docs.docker.com') {
    return 'Docker Docs';
  }

  if (!hostname) {
    return 'Resource';
  }

  const primarySegment = hostname.split('.')[0] || 'Resource';

  return primarySegment
    .split(/[-_]/g)
    .filter(Boolean)
    .map((segment) => segment.charAt(0).toUpperCase() + segment.slice(1))
    .join(' ');
}

function extractFirstYouTubeLink(ipynb: Ipynb): string | null {
  for (const cell of ipynb.cells) {
    if (cell.cell_type !== 'markdown' || !cell.source) {
      continue;
    }

    const source = Array.isArray(cell.source) ? cell.source.join('') : cell.source;
    const match = source.match(YOUTUBE_URL_PATTERN);

    if (match) {
      return match[0];
    }
  }

  return null;
}

function extractNotebookResources(ipynb: Ipynb, limit = 2): NotebookResource[] {
  const resources: NotebookResource[] = [];
  const seenUrls = new Set<string>();

  for (const cell of ipynb.cells) {
    if (cell.cell_type !== 'markdown' || !cell.source) {
      continue;
    }

    const source = Array.isArray(cell.source) ? cell.source.join('') : cell.source;

    for (const match of source.matchAll(MARKDOWN_EXTERNAL_LINK_PATTERN)) {
      const label = match[1]?.trim();
      const url = match[2]?.trim();

      if (!url || seenUrls.has(url)) {
        continue;
      }

      const hostname = toHostname(url);
      if (!hostname || EXCLUDED_RESOURCE_HOSTS.has(hostname)) {
        continue;
      }

      seenUrls.add(url);
      resources.push({
        label: formatResourceLabel(label || '', url),
        url,
      });

      if (resources.length >= limit) {
        return resources;
      }
    }
  }

  return resources;
}

export default function NotebookViewer({ ipynb }: { ipynb: Ipynb }) {
  const pathname = usePathname();
  const routeIndex = generatedRouteIndex;
  const [isExpanded, setIsExpanded] = useState(false);
  const notebookContainerRef = useRef<HTMLDivElement | null>(null);
  const expandedNotebookContainerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const containers = [notebookContainerRef.current, expandedNotebookContainerRef.current].filter(
      (container): container is HTMLDivElement => Boolean(container),
    );

    if (containers.length === 0) {
      return;
    }

    const selectors = [
      '.input_area',
      '.text_cell_render pre',
    ];

    const copyButtonClassName = 'jk-copy-button';

    const copyText = async (text: string) => {
      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(text);
          return true;
        }
      } catch (err) {
        console.warn('Clipboard API failed', err);
      }
      
      // Fallback for non-secure contexts HTTP / legacy browser
      try {
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.top = '0';
        textArea.style.left = '-9999px';
        textArea.style.opacity = '0';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        textArea.setSelectionRange(0, textArea.value.length);
        const didCopy = document.execCommand('copy');
        document.body.removeChild(textArea);
        return didCopy;
      } catch (err) {
        console.warn('Fallback copy failed', err);
        return false;
      }
    };

    const applyButtons = (container: HTMLDivElement) => {
      const blocks = container.querySelectorAll<HTMLElement>(selectors.join(','));

      blocks.forEach((block) => {
        if (block.querySelector(`:scope > .${copyButtonClassName}`)) {
          return;
        }

        const sourceNode = block.matches('.input_area')
          ? block.querySelector<HTMLElement>('.cm-content')
          : block.querySelector<HTMLElement>('code') ?? block;

        const rawText = sourceNode?.innerText?.replace(/\u00a0/g, ' ').trimEnd();

        if (!rawText) {
          return;
        }

        block.classList.add('jk-copy-target');

        const button = document.createElement('button');
        button.type = 'button';
        button.className = copyButtonClassName;
        button.textContent = 'Copy';
        button.setAttribute('aria-label', 'Copy code');
        button.addEventListener('click', async () => {
          const latestSourceNode = block.matches('.input_area')
            ? block.querySelector<HTMLElement>('.cm-content')
            : block.querySelector<HTMLElement>('code') ?? block;
          const latestText = latestSourceNode?.innerText?.replace(/\u00a0/g, ' ').trimEnd() ?? '';

          if (!latestText) {
            return;
          }

          const originalText = button.textContent;

          try {
            const success = await copyText(latestText);
            button.textContent = success ? 'Copied' : 'Failed';
          } catch {
            button.textContent = 'Failed';
          }

          window.setTimeout(() => {
            button.textContent = originalText;
          }, 1200);
        });

        block.prepend(button);
      });
    };

    const observers = containers.map((container) => {
      applyButtons(container);

      const observer = new MutationObserver(() => {
        applyButtons(container);
      });

      observer.observe(container, {
        childList: true,
        subtree: true,
      });

      return observer;
    });

    return () => {
      observers.forEach((observer) => observer.disconnect());
    };
  }, [pathname, ipynb, isExpanded]);

  useEffect(() => {
    if (!isExpanded) {
      return;
    }

    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';

    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        setIsExpanded(false);
      }
    };

    window.addEventListener('keydown', handleKeyDown);

    return () => {
      document.body.style.overflow = previousOverflow;
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [isExpanded]);

  const normalizedNotebook = normalizeNotebookLinks(ipynb, pathname || '/', routeIndex);

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

  const explicitMetadata = extractNotebookMetadata(normalizedNotebook);
  const youtubeUrl = explicitMetadata.video || extractFirstYouTubeLink(normalizedNotebook);
  
  let notebookResources = extractNotebookResources(normalizedNotebook);
  if (explicitMetadata.docs) {
    notebookResources.unshift({ label: 'Docs', url: explicitMetadata.docs });
  }
  if (explicitMetadata.paper) {
    notebookResources.unshift({ label: 'Paper', url: explicitMetadata.paper });
  }
  
  // Deduplicate resources from explicit metadata
  const seenResourceUrls = new Set<string>();
  notebookResources = notebookResources.filter(res => {
    if (seenResourceUrls.has(res.url)) return false;
    seenResourceUrls.add(res.url);
    return true;
  });

  const hasExtraResources = notebookResources.length > 2;
  const topResources = notebookResources.slice(0, 2);
  const dropdownResources = notebookResources.slice(2);

  const linkClass = "text-xs font-medium px-2.5 py-1.5 rounded border border-gray-200 dark:border-gray-700 bg-white dark:bg-[#111] text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors inline-flex items-center justify-center gap-1.5 shadow-sm";
  const buttonClass = `${linkClass} cursor-pointer`;

  return (
    <>
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
          {youtubeUrl ? (
            <a href={youtubeUrl} target="_blank" rel="noreferrer" className={linkClass}>
              <svg className="w-3.5 h-3.5 text-red-600" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M23.5 6.2a3.06 3.06 0 0 0-2.15-2.16C19.46 3.5 12 3.5 12 3.5s-7.46 0-9.35.54A3.06 3.06 0 0 0 .5 6.2 31.4 31.4 0 0 0 0 12a31.4 31.4 0 0 0 .5 5.8 3.06 3.06 0 0 0 2.15 2.16c1.89.54 9.35.54 9.35.54s7.46 0 9.35-.54a3.06 3.06 0 0 0 2.15-2.16A31.4 31.4 0 0 0 24 12a31.4 31.4 0 0 0-.5-5.8ZM9.6 15.78V8.22L16.06 12 9.6 15.78Z" />
              </svg>
              YouTube
            </a>
          ) : null}
          {topResources.map((resource) => (
            <a key={resource.url} href={resource.url} target="_blank" rel="noreferrer" className={linkClass}>
              <svg className="w-3.5 h-3.5 text-slate-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
                <path strokeLinecap="round" strokeLinejoin="round" d="M14 3h7v7" />
                <path strokeLinecap="round" strokeLinejoin="round" d="M10 14 21 3" />
                <path strokeLinecap="round" strokeLinejoin="round" d="M21 14v4a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3h4" />
              </svg>
              {resource.label}
            </a>
          ))}
          {hasExtraResources && (
            <div className="relative group inline-block">
              <button type="button" className={linkClass}>
                <span>Resources</span>
                <svg className="w-3.5 h-3.5 ml-0.5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path>
                </svg>
              </button>
              <div className="absolute right-0 mt-1 hidden group-hover:block w-48 bg-white dark:bg-[#1a1a1a] rounded shadow-lg border border-gray-200 dark:border-gray-800 z-10 py-1">
                {dropdownResources.map((resource) => (
                  <a key={resource.url} href={resource.url} target="_blank" rel="noreferrer" className="block px-4 py-2 text-xs text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800">
                    {resource.label}
                  </a>
                ))}
              </div>
            </div>
          )}
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
          <a href={githubUrl} target="_blank" rel="noreferrer" className={linkClass}>
             <svg className="w-3.5 h-3.5 text-gray-800 dark:text-gray-200" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
             GitHub
          </a>
            <button type="button" className={buttonClass} onClick={() => setIsExpanded(true)}>
              Maximize
            </button>
          </div>
        </div>
        
        {/* Internal Notebook Engine */}
        <div className="jk-notebook-container" ref={notebookContainerRef}>
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

      {isExpanded ? (
        <div className="fixed inset-0 z-[100] bg-black/70 px-3 py-3 backdrop-blur-sm sm:px-6 sm:py-6">
          <div className="mx-auto flex h-full w-full max-w-[1600px] flex-col overflow-hidden rounded-2xl border border-gray-200 dark:border-gray-800 bg-[var(--nextra-bg)] shadow-2xl">
            <div className="flex items-center justify-between gap-3 border-b border-gray-200 bg-gray-50/90 px-4 py-3 dark:border-gray-800 dark:bg-[#0a0a0a]">
              <div>
                <div className="text-sm font-semibold text-gray-800 dark:text-gray-100">Jupyter Notebook</div>
                <div className="text-xs text-gray-500 dark:text-gray-400">Expanded view. Press Esc to close.</div>
              </div>
              <button type="button" className={buttonClass} onClick={() => setIsExpanded(false)}>
                Close full screen
              </button>
            </div>
            <div className="min-h-0 flex-1 overflow-auto p-4 sm:p-6">
              <div className="jk-notebook-container jk-notebook-container--expanded" ref={expandedNotebookContainerRef}>
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
          </div>
        </div>
      ) : null}

      <style jsx global>{`
        .jk-notebook-container {
          --jk-gh-bg: rgb(255, 255, 255);
          --jk-gh-fg: rgb(36, 41, 47);
          --jk-gh-muted: rgb(101, 109, 118);
          --jk-gh-border: rgb(208, 215, 222);
          --jk-gh-cell-bg: rgb(246, 248, 250);
          --jk-gh-output-bg: rgb(255, 255, 255);
          --jk-gh-accent: rgb(9, 105, 218);
          --jk-gh-inline-code-bg: rgb(175, 184, 193, 0.2);
          --jk-gh-keyword: rgb(207, 34, 46);
          --jk-gh-string: rgb(11, 110, 153);
          --jk-gh-comment: rgb(87, 96, 106);
          --jk-gh-number: rgb(5, 80, 174);
          --jk-gh-function: rgb(130, 80, 223);
          --jk-gh-operator: rgb(36, 41, 47);
        }

        .dark .jk-notebook-container {
          --jk-gh-bg: rgb(13, 17, 23);
          --jk-gh-fg: rgb(230, 237, 243);
          --jk-gh-muted: rgb(139, 148, 158);
          --jk-gh-border: rgb(48, 54, 61);
          --jk-gh-cell-bg: rgb(22, 27, 34);
          --jk-gh-output-bg: rgb(13, 17, 23);
          --jk-gh-accent: rgb(47, 129, 247);
          --jk-gh-inline-code-bg: rgb(110, 118, 129, 0.4);
          --jk-gh-keyword: rgb(255, 123, 114);
          --jk-gh-string: rgb(121, 192, 255);
          --jk-gh-comment: rgb(139, 148, 158);
          --jk-gh-number: rgb(165, 214, 255);
          --jk-gh-function: rgb(210, 168, 255);
          --jk-gh-operator: rgb(230, 237, 243);
        }

        .jk-notebook-container .jupyter-kit-notebook {
          color: var(--jk-gh-fg);
          background: transparent;
        }

        .jk-notebook-container .cell {
          border: 1px solid var(--jk-gh-border);
          border-left: 3px solid var(--jk-gh-accent);
          border-radius: 0.5rem;
          background: var(--jk-gh-cell-bg);
          margin: 0.75rem 0;
          padding: 0.25rem 0.5rem;
        }

        .jk-notebook-container .text_cell_render,
        .jk-notebook-container .rendered,
        .jk-notebook-container .rendered_html {
          color: var(--jk-gh-fg);
        }

        .jk-notebook-container .input,
        .jk-notebook-container .input_area {
          background: var(--jk-gh-bg);
          border: 1px solid var(--jk-gh-border);
          border-radius: 0.375rem;
        }

        .jk-notebook-container .output,
        .jk-notebook-container .output_wrapper {
          background: var(--jk-gh-output-bg);
          border: 1px solid var(--jk-gh-border);
          border-radius: 0.375rem;
          color: var(--jk-gh-fg);
        }

        .jk-notebook-container .prompt,
        .jk-notebook-container .input_prompt {
          color: var(--jk-gh-muted);
          font-family: var(--font-mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace);
          font-size: 0.75rem;
        }

        .jk-notebook-container .text_cell_render code,
        .jk-notebook-container .rendered_html code {
          background: var(--jk-gh-inline-code-bg);
          border: 1px solid var(--jk-gh-border);
          border-radius: 0.25rem;
          color: var(--jk-gh-fg);
          padding: 0.1rem 0.3rem;
        }

        /* GitHub-like token colors for CodeMirror syntax highlighting. */
        .jk-notebook-container .cm-editor .cm-keyword {
          color: var(--jk-gh-keyword);
        }

        .jk-notebook-container .cm-editor .cm-string,
        .jk-notebook-container .cm-editor .cm-special {
          color: var(--jk-gh-string);
        }

        .jk-notebook-container .cm-editor .cm-comment {
          color: var(--jk-gh-comment);
        }

        .jk-notebook-container .cm-editor .cm-number,
        .jk-notebook-container .cm-editor .cm-bool,
        .jk-notebook-container .cm-editor .cm-atom {
          color: var(--jk-gh-number);
        }

        .jk-notebook-container .cm-editor .cm-def,
        .jk-notebook-container .cm-editor .cm-variableName,
        .jk-notebook-container .cm-editor .cm-propertyName {
          color: var(--jk-gh-function);
        }

        .jk-notebook-container .cm-editor .cm-operator,
        .jk-notebook-container .cm-editor .cm-punctuation {
          color: var(--jk-gh-operator);
        }

        /* Token fallbacks for Prism/Highlight.js/Pygments-like class names. */
        .jk-notebook-container .text_cell_render .token.keyword,
        .jk-notebook-container .text_cell_render .hljs-keyword,
        .jk-notebook-container .text_cell_render .k {
          color: var(--jk-gh-keyword);
        }

        .jk-notebook-container .text_cell_render .token.string,
        .jk-notebook-container .text_cell_render .hljs-string,
        .jk-notebook-container .text_cell_render .s {
          color: var(--jk-gh-string);
        }

        .jk-notebook-container .text_cell_render .token.comment,
        .jk-notebook-container .text_cell_render .hljs-comment,
        .jk-notebook-container .text_cell_render .c {
          color: var(--jk-gh-comment);
        }

        .jk-notebook-container .text_cell_render .token.number,
        .jk-notebook-container .text_cell_render .hljs-number,
        .jk-notebook-container .text_cell_render .m {
          color: var(--jk-gh-number);
        }

        .jk-notebook-container .text_cell_render .token.function,
        .jk-notebook-container .text_cell_render .hljs-title,
        .jk-notebook-container .text_cell_render .nf {
          color: var(--jk-gh-function);
        }

        .jk-notebook-container .jk-copy-target {
          position: relative;
        }

        .jk-notebook-container .jk-copy-button {
          position: absolute;
          top: 0.5rem;
          right: 0.5rem;
          z-index: 3;
          border: 1px solid rgba(148, 163, 184, 0.45);
          border-radius: 0.375rem;
          background: rgba(255, 255, 255, 0.94);
          color: rgb(51, 65, 85);
          padding: 0.2rem 0.55rem;
          font-size: 0.72rem;
          line-height: 1;
          cursor: pointer;
          opacity: 0;
          transition: opacity 120ms ease, background-color 120ms ease, border-color 120ms ease;
        }

        .dark .jk-notebook-container .jk-copy-button {
          background: rgba(15, 23, 42, 0.92);
          color: rgb(226, 232, 240);
          border-color: rgba(100, 116, 139, 0.55);
        }

        .jk-notebook-container .jk-copy-target:hover > .jk-copy-button,
        .jk-notebook-container .jk-copy-target:focus-within > .jk-copy-button {
          opacity: 1;
        }

        .jk-notebook-container .jk-copy-button:hover {
          background: rgba(241, 245, 249, 0.98);
          border-color: rgba(100, 116, 139, 0.7);
        }

        .dark .jk-notebook-container .jk-copy-button:hover {
          background: rgba(30, 41, 59, 0.96);
        }

        .jk-notebook-container .input_area {
          padding-top: 2rem;
        }

        .jk-notebook-container .text_cell_render pre {
          padding-top: 2.25rem;
        }

        .jk-notebook-container .jk-copy-target pre,
        .jk-notebook-container .text_cell_render pre {
          background: var(--jk-gh-cell-bg);
          border: 1px solid var(--jk-gh-border);
          border-radius: 0.375rem;
        }

        /* Improve code readability in light mode for notebook-rendered blocks. */
        .jk-notebook-container .jk-copy-target pre,
        .jk-notebook-container .jk-copy-target pre code,
        .jk-notebook-container .text_cell_render pre,
        .jk-notebook-container .text_cell_render pre code {
          color: rgb(31, 41, 55);
        }

        .dark .jk-notebook-container .jk-copy-target pre,
        .dark .jk-notebook-container .jk-copy-target pre code,
        .dark .jk-notebook-container .text_cell_render pre,
        .dark .jk-notebook-container .text_cell_render pre code {
          color: rgb(226, 232, 240);
        }

        .dark .jk-notebook-container .jk-copy-target pre,
        .dark .jk-notebook-container .text_cell_render pre {
          background: var(--jk-gh-cell-bg);
          border-color: var(--jk-gh-border);
        }

        .jk-notebook-container--expanded {
          min-height: 100%;
        }

        .jk-notebook-container--expanded .Notebook {
          max-width: none;
        }
      `}</style>
    </>
  );
}
