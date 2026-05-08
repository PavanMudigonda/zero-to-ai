'use client';

import Link from 'next/link';
import { useRouter, useSearchParams } from 'next/navigation';
import { useEffect, useMemo, useState } from 'react';

import { createClient } from '@/utils/supabase/client';

function normalizeNextPath(value: string | null) {
  if (!value || !value.startsWith('/')) {
    return '/';
  }

  try {
    const url = new URL(value, 'http://localhost');
    return `${url.pathname}${url.search}${url.hash}`;
  } catch {
    return '/';
  }
}

export default function AuthCallbackPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const nextPath = useMemo(
    () => normalizeNextPath(searchParams.get('next')),
    [searchParams],
  );
  const authError = useMemo(
    () => searchParams.get('error_description') ?? searchParams.get('error'),
    [searchParams],
  );

  useEffect(() => {
    const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
    const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';

    if (!supabaseUrl || !supabaseAnonKey) {
      setErrorMessage('Supabase URL and anon key are missing in .env.local.');
      return;
    }

    if (authError) {
      setErrorMessage(authError);
      return;
    }

    const supabase = createClient();
    let cancelled = false;

    const timeoutId = window.setTimeout(() => {
      if (!cancelled) {
        setErrorMessage('GitHub sign-in did not finish in time. Please try again.');
      }
    }, 8000);

    const { data: authListener } = supabase.auth.onAuthStateChange((_event, session) => {
      if (cancelled || !session) {
        return;
      }

      window.clearTimeout(timeoutId);
      router.replace(nextPath);
    });

    supabase.auth.getSession().then(({ data, error }) => {
      if (cancelled) {
        return;
      }

      if (error) {
        window.clearTimeout(timeoutId);
        setErrorMessage(error.message);
        return;
      }

      if (data.session) {
        window.clearTimeout(timeoutId);
        router.replace(nextPath);
      }
    });

    return () => {
      cancelled = true;
      window.clearTimeout(timeoutId);
      authListener.subscription.unsubscribe();
    };
  }, [authError, nextPath, router]);

  return (
    <main className="mx-auto flex min-h-[60vh] max-w-xl flex-col items-center justify-center px-6 py-16 text-center">
      <div className="w-full rounded-2xl border border-gray-200 bg-white p-8 shadow-sm dark:border-gray-800 dark:bg-[#111]">
        <h1 className="text-2xl font-semibold text-gray-900 dark:text-white">Complete GitHub sign-in</h1>
        {errorMessage ? (
          <>
            <p className="mt-3 text-sm text-red-600 dark:text-red-400">{errorMessage}</p>
            <div className="mt-6 flex items-center justify-center gap-3">
              <Link
                href={nextPath}
                className="rounded-full bg-gray-900 px-4 py-2 text-sm font-medium text-white dark:bg-white dark:text-black"
              >
                Return to site
              </Link>
            </div>
          </>
        ) : (
          <>
            <p className="mt-3 text-sm text-gray-600 dark:text-gray-300">
              Finalizing your GitHub login and syncing your course progress.
            </p>
            <div className="mt-6 flex items-center justify-center gap-2 text-sm text-gray-500 dark:text-gray-400">
              <span className="inline-block h-2.5 w-2.5 animate-pulse rounded-full bg-green-500" />
              Waiting for Supabase session...
            </div>
          </>
        )}
      </div>
    </main>
  );
}