'use client';

import { usePathname, useRouter } from 'next/navigation';
import { useEffect, useMemo, useRef, useState } from 'react';

type SearchItem = {
  title: string;
  route: string;
  breadcrumb: string;
};

type FuzzySearchProps = {
  items: SearchItem[];
};

type ScoredItem = SearchItem & {
  score: number;
};

function normalize(value: string) {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
}

function subsequenceScore(query: string, candidate: string) {
  if (!query) return 0;

  let queryIndex = 0;
  let lastMatch = -1;
  let score = 0;

  for (let candidateIndex = 0; candidateIndex < candidate.length && queryIndex < query.length; candidateIndex += 1) {
    if (candidate[candidateIndex] !== query[queryIndex]) {
      continue;
    }

    score += lastMatch === -1 ? 4 : Math.max(1, 4 - (candidateIndex - lastMatch - 1));
    lastMatch = candidateIndex;
    queryIndex += 1;
  }

  return queryIndex === query.length ? score : -1;
}

function scoreItem(query: string, item: SearchItem) {
  const normalizedQuery = normalize(query);
  if (!normalizedQuery) return -1;

  const normalizedTitle = normalize(item.title);
  const normalizedBreadcrumb = normalize(item.breadcrumb);
  const normalizedRoute = normalize(item.route.replaceAll('/', ' '));

  let score = 0;

  if (normalizedTitle === normalizedQuery) score += 140;
  if (normalizedTitle.startsWith(normalizedQuery)) score += 90;
  if (normalizedTitle.includes(normalizedQuery)) score += 65;
  if (normalizedBreadcrumb.includes(normalizedQuery)) score += 35;
  if (normalizedRoute.includes(normalizedQuery)) score += 25;

  const titleSubsequence = subsequenceScore(normalizedQuery.replaceAll(' ', ''), normalizedTitle.replaceAll(' ', ''));
  if (titleSubsequence > 0) score += titleSubsequence;

  const breadcrumbSubsequence = subsequenceScore(
    normalizedQuery.replaceAll(' ', ''),
    normalizedBreadcrumb.replaceAll(' ', ''),
  );
  if (breadcrumbSubsequence > 0) score += Math.floor(breadcrumbSubsequence / 2);

  return score;
}

export default function FuzzySearch({ items }: FuzzySearchProps) {
  const router = useRouter();
  const pathname = usePathname();
  const containerRef = useRef<HTMLDivElement>(null);
  const activeIndexRef = useRef(0);
  const [query, setQuery] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const [activeIndex, setActiveIndex] = useState(0);

  const results = useMemo(() => {
    const trimmedQuery = query.trim();
    if (!trimmedQuery) return [];

    return items
      .map<ScoredItem>((item) => ({ ...item, score: scoreItem(trimmedQuery, item) }))
      .filter((item) => item.score > 0)
      .sort((left, right) => right.score - left.score || left.breadcrumb.localeCompare(right.breadcrumb))
      .slice(0, 8);
  }, [items, query]);

  useEffect(() => {
    activeIndexRef.current = 0;
    setActiveIndex(0);
  }, [query]);

  useEffect(() => {
    const handlePointerDown = (event: MouseEvent) => {
      if (!containerRef.current?.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };

    document.addEventListener('mousedown', handlePointerDown);
    return () => document.removeEventListener('mousedown', handlePointerDown);
  }, []);

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
        event.preventDefault();
        const input = containerRef.current?.querySelector('input');
        input?.focus();
        setIsOpen(true);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const navigateTo = (route: string) => {
    setIsOpen(false);
    setQuery('');
    if (route !== pathname) {
      router.push(route);
    }
  };

  return (
    <div ref={containerRef} className="relative w-full max-w-md">
      <div className="flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-3 py-2 shadow-sm dark:border-gray-800 dark:bg-neutral-900">
        <svg
          aria-hidden="true"
          viewBox="0 0 20 20"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.8"
          className="h-4 w-4 shrink-0 text-gray-400"
        >
          <circle cx="8.5" cy="8.5" r="5.5" />
          <path d="M12.5 12.5L17 17" strokeLinecap="round" />
        </svg>
        <input
          type="search"
          value={query}
          onChange={(event) => {
            setQuery(event.target.value);
            setIsOpen(true);
          }}
          onFocus={() => setIsOpen(true)}
          onKeyDown={(event) => {
            if (event.key === 'ArrowDown') {
              event.preventDefault();
              setIsOpen(true);
              setActiveIndex((current) => {
                const next = Math.min(current + 1, Math.max(results.length - 1, 0));
                activeIndexRef.current = next;
                return next;
              });
            } else if (event.key === 'ArrowUp') {
              event.preventDefault();
              setActiveIndex((current) => {
                const next = Math.max(current - 1, 0);
                activeIndexRef.current = next;
                return next;
              });
            } else if (event.key === 'Enter' && results[activeIndexRef.current]) {
              event.preventDefault();
              navigateTo(results[activeIndexRef.current].route);
            } else if (event.key === 'Escape') {
              setIsOpen(false);
            }
          }}
          placeholder="Search documentation..."
          aria-label="Search documentation"
          className="min-w-0 flex-1 bg-transparent text-sm outline-none placeholder:text-gray-400"
        />
        <span className="hidden rounded-md border border-gray-200 px-1.5 py-0.5 text-[11px] text-gray-400 md:inline dark:border-gray-700">Ctrl K</span>
      </div>

      {isOpen && query.trim() && (
        <div className="absolute left-0 right-0 top-[calc(100%+0.5rem)] z-40 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-2xl dark:border-gray-800 dark:bg-neutral-900">
          {results.length > 0 ? (
            <ul role="listbox" className="max-h-[24rem] overflow-y-auto py-2">
              {results.map((item, index) => (
                <li key={item.route}>
                  <button
                    type="button"
                    onMouseDown={(event) => event.preventDefault()}
                    onClick={() => navigateTo(item.route)}
                    className={`flex w-full flex-col items-start px-4 py-3 text-left transition ${
                      index === activeIndex
                        ? 'bg-sky-50 dark:bg-slate-800'
                        : 'hover:bg-gray-50 dark:hover:bg-slate-800/70'
                    }`}
                  >
                    <span className="text-sm font-medium text-slate-900 dark:text-slate-100">{item.title}</span>
                    <span className="mt-1 text-xs text-slate-500 dark:text-slate-400">{item.breadcrumb}</span>
                  </button>
                </li>
              ))}
            </ul>
          ) : (
            <div className="px-4 py-4 text-sm text-slate-500 dark:text-slate-400">No matching pages</div>
          )}
        </div>
      )}
    </div>
  );
}