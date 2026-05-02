'use client';

import React, { useEffect, useState } from 'react';
import { usePathname } from 'next/navigation';

export default function ProgressWidget() {
  const pathname = usePathname();
  const [completedRoutes, setCompletedRoutes] = useState<Set<string>>(new Set());
  const [totalRoutes, setTotalRoutes] = useState<number>(0);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    // Load from local storage
    const stored = localStorage.getItem('curriculum-progress');
    if (stored) {
      try {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed)) {
          setCompletedRoutes(new Set(parsed));
        }
      } catch {
        // Ignore
      }
    }

    // Load total routes length from route index
    fetch('/route-index.json')
      .then(res => res.json())
      .then((routes: string[]) => {
        // Filter out root index and demo pages if needed
        const validRoutes = routes.filter(r => r !== '/' && !r.includes('/temp'));
        setTotalRoutes(validRoutes.length);
      })
      .catch(() => {});

    setMounted(true);
  }, []);

  const currentPath = pathname || '/';
  
  // Don't show the mark complete button on the actual homepage
  const isHomepage = currentPath === '/';

  const isCompleted = completedRoutes.has(currentPath);

  const toggleCompletion = () => {
    const next = new Set(completedRoutes);
    if (isCompleted) {
      next.delete(currentPath);
    } else {
      next.add(currentPath);
    }
    setCompletedRoutes(next);
    localStorage.setItem('curriculum-progress', JSON.stringify(Array.from(next)));
  };

  if (!mounted) return null;

  const validCompletedCount = Array.from(completedRoutes).length; // simple approximation
  const progressPercent = totalRoutes > 0 ? Math.round((validCompletedCount / totalRoutes) * 100) : 0;

  return (
    <div className="fixed bottom-6 right-6 z-50 flex flex-col items-end gap-2">
      {/* Progress Bar popout */}
      {totalRoutes > 0 && (
        <div className="bg-white dark:bg-[#111] border border-gray-200 dark:border-gray-800 shadow-lg rounded-lg p-3 w-48 text-xs relative overflow-hidden">
          <div className="flex justify-between items-center mb-1 text-gray-700 dark:text-gray-300 font-medium">
            <span>Course Progress</span>
            <span>{progressPercent}%</span>
          </div>
          <div className="w-full bg-gray-100 dark:bg-gray-800 rounded-full h-1.5 mb-1">
            <div 
              className="bg-blue-500 h-1.5 rounded-full transition-all duration-500" 
              style={{ width: `${progressPercent}%` }}
            ></div>
          </div>
          <div className="text-gray-500 dark:text-gray-400 text-[10px] text-right">
            {validCompletedCount} of {totalRoutes} modules
          </div>
        </div>
      )}

      {/* Action Button */}
      {!isHomepage && (
        <button
          onClick={toggleCompletion}
          className={`flex items-center gap-2 px-4 py-2.5 rounded-full shadow-lg font-medium text-sm transition-all focus:outline-none focus:ring-2 focus:ring-offset-2 ${
            isCompleted 
              ? 'bg-green-500 text-white hover:bg-green-600 focus:ring-green-500' 
              : 'bg-white dark:bg-[#111] border border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-[#1a1a1a] focus:ring-gray-200'
          }`}
        >
          {isCompleted ? (
            <>
              <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
              </svg>
              <span>Completed</span>
            </>
          ) : (
            <>
              <svg className="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
              </svg>
              <span>Mark Complete</span>
            </>
          )}
        </button>
      )}
    </div>
  );
}