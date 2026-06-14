import Link from 'next/link';

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4 px-4 text-center">
      <h1 className="text-6xl font-bold text-gray-300 dark:text-gray-600">404</h1>
      <h2 className="text-2xl font-semibold">Page Not Found</h2>
      <p className="text-gray-500 dark:text-gray-400 max-w-md">
        The page you&apos;re looking for doesn&apos;t exist or has been moved.
      </p>
      <Link
        href="/"
        className="mt-2 px-5 py-2.5 rounded-lg bg-blue-600 text-white font-medium hover:bg-blue-700 transition-colors"
      >
        Back to Home
      </Link>
    </div>
  );
}
