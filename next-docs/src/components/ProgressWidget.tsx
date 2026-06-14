'use client';

import React, { useEffect, useState } from 'react';
import { usePathname } from 'next/navigation';
import { createBrowserClient } from '@supabase/ssr';
import generatedRouteIndex from '@/generated/route-index';

type OAuthProvider = 'github' | 'google';

export default function ProgressWidget() {
  const pathname = usePathname();
  const [completedRoutes, setCompletedRoutes] = useState<Set<string>>(new Set());
  const [totalRoutes] = useState<number>(() => {
    return generatedRouteIndex.filter((route) => route !== '/' && !route.includes('/temp')).length;
  });
  const [mounted, setMounted] = useState(false);
  const [user, setUser] = useState<any>(null);
  const [syncError, setSyncError] = useState<string | null>(null);
  
  // Note: These env vars must be defined in your .env.local
  const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
  const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';
  
  // Only initialize supabase if both keys are present
  const [supabase] = useState(() => 
    supabaseUrl && supabaseAnonKey 
      ? createBrowserClient(supabaseUrl, supabaseAnonKey) 
      : null
  );

  useEffect(() => {
    setMounted(true);

    // 1. Evaluate Auth State
    if (supabase) {
      supabase.auth.getUser().then(({ data: { user } }) => {
        setUser(user);
        if (user) {
          fetchCloudProgress(user.id);
        } else {
          loadLocalProgress();
        }
      });

      const { data: authListener } = supabase.auth.onAuthStateChange(
        async (event, session) => {
          const currentUser = session?.user;
          setUser(currentUser ?? null);
          if (currentUser) {
            await fetchCloudProgress(currentUser.id);
          } else {
            loadLocalProgress();
          }
        }
      );
      
      return () => {
        authListener?.subscription.unsubscribe();
      };
    }

    loadLocalProgress();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [supabase]);
  
  const loadLocalProgress = () => {
    const stored = localStorage.getItem('curriculum-progress');
    if (stored) {
      try {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed)) setCompletedRoutes(new Set(parsed));
      } catch {}
    }
  };

  const fetchCloudProgress = async (userId: string) => {
    if (!supabase) return;
    
    // Attempt to migrate any unstored local progress
    const local = localStorage.getItem('curriculum-progress');
    if (local) {
      try {
        const parsed = JSON.parse(local);
        if (Array.isArray(parsed) && parsed.length > 0) {
          // Bulk upsert missing paths to supabase
          const rows = parsed.map((route: string) => ({ user_id: userId, route }));
          await supabase.from('learning_progress').upsert(rows, { onConflict: 'user_id, route' } as any);
          // Clear local storage after successful migration
          localStorage.removeItem('curriculum-progress');
        }
      } catch (e) {
        console.error("Migration error:", e)
      }
    }
    
    // Fetch from Supabase
    const { data, error } = await supabase
      .from('learning_progress')
      .select('route')
      .eq('user_id', userId);
      
    if (!error && data) {
      const routes = data.map((row: any) => row.route);
      setCompletedRoutes(new Set(routes));
    }
  };

  const handleLogin = async (provider: OAuthProvider) => {
    if (!supabase) {
      setSyncError('Supabase URL and Anon Key are missing in .env.local');
      return;
    }
    setSyncError(null);
    const callbackUrl = new URL('/auth/callback', location.origin);
    callbackUrl.searchParams.set('next', currentPath);

    await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: callbackUrl.toString(),
      }
    });
  };

  const handleLogout = async () => {
    if (!supabase) return;
    await supabase.auth.signOut();
    setCompletedRoutes(new Set());
    loadLocalProgress();
  };

  const currentPath = pathname || '/';
  const isHomepage = currentPath === '/';
  const isCompleted = completedRoutes.has(currentPath);

  const toggleCompletion = async () => {
    const next = new Set(completedRoutes);
    if (isCompleted) {
      next.delete(currentPath);
    } else {
      next.add(currentPath);
    }
    setCompletedRoutes(next);

    // Save state
    if (user && supabase) {
      if (isCompleted) {
        await supabase
          .from('learning_progress')
          .delete()
          .eq('user_id', user.id)
          .eq('route', currentPath);
      } else {
        await supabase
          .from('learning_progress')
          .insert([{ user_id: user.id, route: currentPath }]);
      }
    } else {
      localStorage.setItem('curriculum-progress', JSON.stringify(Array.from(next)));
    }
  };

  if (!mounted) return null;

  const validCompletedCount = Array.from(completedRoutes).length;
  const progressPercent = totalRoutes > 0 ? Math.round((validCompletedCount / totalRoutes) * 100) : 0;

  return (
    <div className="fixed bottom-6 right-6 z-50 flex flex-col items-end gap-2">
      {syncError && (
        <div className="bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-700 text-red-700 dark:text-red-300 text-xs rounded-lg px-3 py-2 max-w-[220px] shadow-md">
          {syncError}
          <button
            onClick={() => setSyncError(null)}
            className="ml-2 text-red-400 hover:text-red-600 dark:hover:text-red-200"
            aria-label="Dismiss"
          >
            ✕
          </button>
        </div>
      )}
      {/* Cloud Sync Status / Login Button */}
      {user ? (
        <div className="bg-white dark:bg-[#111] border border-gray-200 dark:border-gray-800 shadow-lg rounded-full px-3 py-1 flex items-center gap-2 text-xs font-medium text-gray-600 dark:text-gray-300">
          <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
          Synced
          <button onClick={handleLogout} className="ml-1 text-gray-400 hover:text-gray-700 dark:hover:text-white transition-colors">
            (Logout)
          </button>
        </div>
      ) : (
        <div className="flex flex-col items-end gap-2">
          <button 
            onClick={() => handleLogin('github')} 
            className="cursor-pointer bg-gray-900 text-white dark:bg-white dark:text-black border border-transparent shadow-lg rounded-full px-3 py-1.5 flex items-center gap-2 text-xs font-medium hover:opacity-90 transition-opacity"
          >
            <svg className="w-3.5 h-3.5" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            Sync with GitHub
          </button>
          <button 
            onClick={() => handleLogin('google')} 
            className="cursor-pointer bg-white text-gray-900 dark:bg-[#111] dark:text-white border border-gray-200 dark:border-gray-700 shadow-lg rounded-full px-3 py-1.5 flex items-center gap-2 text-xs font-medium hover:bg-gray-50 dark:hover:bg-[#1a1a1a] transition-colors"
          >
            <svg className="w-3.5 h-3.5" viewBox="0 0 24 24" aria-hidden="true">
              <path fill="#EA4335" d="M12 10.2v3.9h5.4c-.2 1.3-1.6 3.9-5.4 3.9-3.2 0-5.9-2.7-5.9-6s2.7-6 5.9-6c1.8 0 3 .8 3.7 1.5l2.5-2.4C16.6 3.6 14.5 2.7 12 2.7 6.9 2.7 2.8 6.8 2.8 12S6.9 21.3 12 21.3c6.8 0 9-4.8 9-7.3 0-.5-.1-.9-.1-1.3H12Z"/>
              <path fill="#34A853" d="M2.8 12c0 1.7.6 3.3 1.7 4.5l2.8-2.2c-.4-.6-.6-1.4-.6-2.3s.2-1.6.6-2.3L4.5 7.5C3.4 8.7 2.8 10.3 2.8 12Z"/>
              <path fill="#FBBC05" d="M12 21.3c2.4 0 4.5-.8 6-2.3l-2.9-2.2c-.8.6-1.8 1.1-3.1 1.1-2.5 0-4.7-1.7-5.4-3.9l-2.8 2.2c1.6 3.1 4.8 5.1 8.2 5.1Z"/>
              <path fill="#4285F4" d="M21 12.1c0-.7-.1-1.3-.2-1.9H12v3.9h5.4c-.3 1.3-1 2.3-2 3l2.9 2.2c1.7-1.6 2.7-4 2.7-7.2Z"/>
            </svg>
            Sync with Google
          </button>
        </div>
      )}

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
          className={`cursor-pointer flex items-center gap-2 px-4 py-2.5 rounded-full shadow-lg font-medium text-sm transition-all focus:outline-none focus:ring-2 focus:ring-offset-2 ${
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
