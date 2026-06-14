'use client';

import Link from 'next/link';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4 px-4 text-center">
      <h1 className="text-6xl font-bold text-gray-300 dark:text-gray-600">500</h1>
      <h2 className="text-2xl font-semibold">Something went wrong</h2>
      <p className="text-gray-500 dark:text-gray-400 max-w-md">
        {error.message || 'An unexpected error occurred.'}
      </p>
      <div className="flex gap-3 mt-2">
        <button
          onClick={reset}
          className="px-5 py-2.5 rounded-lg bg-blue-600 text-white font-medium hover:bg-blue-700 transition-colors"
        >
          Try again
        </button>
        <Link
          href="/"
          className="px-5 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 font-medium hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
        >
          Back to Home
        </Link>
      </div>
    </div>
  );
}
