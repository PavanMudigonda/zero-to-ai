'use client';
import dynamic from 'next/dynamic';

function NotebookSkeleton() {
  return (
    <div
      className="jk-notebook-skeleton"
      role="status"
      aria-live="polite"
      aria-busy="true"
    >
      <span className="jk-notebook-skeleton__sr">Loading interactive notebook…</span>

      <div className="jk-notebook-skeleton__toolbar" aria-hidden="true">
        <span className="jk-notebook-skeleton__pill" />
        <span className="jk-notebook-skeleton__pill" />
        <span className="jk-notebook-skeleton__pill jk-notebook-skeleton__pill--wide" />
      </div>

      <div className="jk-notebook-skeleton__cells" aria-hidden="true">
        <div className="jk-notebook-skeleton__line jk-notebook-skeleton__line--title" />
        <div className="jk-notebook-skeleton__line" />
        <div className="jk-notebook-skeleton__line jk-notebook-skeleton__line--short" />
        <div className="jk-notebook-skeleton__code">
          <div className="jk-notebook-skeleton__line jk-notebook-skeleton__line--code" />
          <div className="jk-notebook-skeleton__line jk-notebook-skeleton__line--code jk-notebook-skeleton__line--short" />
          <div className="jk-notebook-skeleton__line jk-notebook-skeleton__line--code" />
        </div>
        <div className="jk-notebook-skeleton__line" />
        <div className="jk-notebook-skeleton__line jk-notebook-skeleton__line--short" />
      </div>

      <style jsx>{`
        .jk-notebook-skeleton {
          border: 1px solid rgba(127, 127, 127, 0.18);
          border-radius: 0.75rem;
          padding: 1rem;
          background: var(--nextra-bg, #fff);
        }
        .jk-notebook-skeleton__sr {
          position: absolute;
          width: 1px;
          height: 1px;
          padding: 0;
          margin: -1px;
          overflow: hidden;
          clip: rect(0, 0, 0, 0);
          white-space: nowrap;
          border: 0;
        }
        .jk-notebook-skeleton__toolbar {
          display: flex;
          gap: 0.5rem;
          margin-bottom: 1.25rem;
        }
        .jk-notebook-skeleton__pill {
          width: 4.5rem;
          height: 1.6rem;
          border-radius: 9999px;
        }
        .jk-notebook-skeleton__pill--wide {
          width: 6rem;
          margin-left: auto;
        }
        .jk-notebook-skeleton__cells {
          display: flex;
          flex-direction: column;
          gap: 0.75rem;
        }
        .jk-notebook-skeleton__code {
          display: flex;
          flex-direction: column;
          gap: 0.6rem;
          padding: 1rem;
          border-radius: 0.5rem;
          background: rgba(127, 127, 127, 0.06);
          margin: 0.5rem 0;
        }
        .jk-notebook-skeleton__line {
          height: 0.85rem;
          width: 100%;
          border-radius: 0.3rem;
        }
        .jk-notebook-skeleton__line--title {
          height: 1.4rem;
          width: 45%;
        }
        .jk-notebook-skeleton__line--short {
          width: 60%;
        }
        .jk-notebook-skeleton__line--code {
          height: 0.75rem;
        }
        .jk-notebook-skeleton__pill,
        .jk-notebook-skeleton__line {
          background: linear-gradient(
            90deg,
            rgba(127, 127, 127, 0.1) 25%,
            rgba(127, 127, 127, 0.2) 37%,
            rgba(127, 127, 127, 0.1) 63%
          );
          background-size: 400% 100%;
          animation: jk-notebook-skeleton-shimmer 1.4s ease infinite;
        }
        @keyframes jk-notebook-skeleton-shimmer {
          0% {
            background-position: 100% 50%;
          }
          100% {
            background-position: 0 50%;
          }
        }
        @media (prefers-reduced-motion: reduce) {
          .jk-notebook-skeleton__pill,
          .jk-notebook-skeleton__line {
            animation: none;
          }
        }
      `}</style>
    </div>
  );
}

const NotebookViewer = dynamic(() => import('./NotebookViewer'), {
  ssr: false,
  loading: () => <NotebookSkeleton />,
});

export default function DynamicNotebook(props: any) {
  return <NotebookViewer {...props} />;
}
