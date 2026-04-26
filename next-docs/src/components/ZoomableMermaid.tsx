'use client';

import { Mermaid as BaseMermaid } from 'nextra/components';
import { useEffect, useState } from 'react';

type ZoomableMermaidProps = {
  chart: string;
};

const toolbarButtonStyle = {
  border: '1px solid var(--nextra-border, rgba(0,0,0,0.12))',
  borderRadius: '0.5rem',
  background: 'var(--nextra-bg, #fff)',
  color: 'var(--nextra-text, inherit)',
  cursor: 'pointer',
  fontSize: '0.875rem',
  lineHeight: 1,
  padding: '0.45rem 0.65rem'
} as const;

export default function ZoomableMermaid({ chart }: ZoomableMermaidProps) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [zoom, setZoom] = useState(1);

  useEffect(() => {
    if (!isExpanded) {
      return;
    }

    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';

    return () => {
      document.body.style.overflow = previousOverflow;
    };
  }, [isExpanded]);

  const zoomOutDisabled = zoom <= 0.6;
  const zoomInDisabled = zoom >= 2.4;

  return (
    <>
      <div
        style={{
          border: '1px solid var(--nextra-border, rgba(0,0,0,0.12))',
          borderRadius: '0.75rem',
          margin: '1.5rem 0',
          overflow: 'hidden'
        }}
      >
        <div
          style={{
            alignItems: 'center',
            background: 'var(--nextra-bg, #fff)',
            borderBottom: '1px solid var(--nextra-border, rgba(0,0,0,0.12))',
            display: 'flex',
            gap: '0.5rem',
            justifyContent: 'flex-end',
            padding: '0.75rem'
          }}
        >
          <button type="button" style={toolbarButtonStyle} onClick={() => setIsExpanded(true)}>
            Maximize
          </button>
        </div>
        <div
          className="zoomable-mermaid-render"
          style={{
            overflowX: 'auto',
            padding: '1rem'
          }}
        >
          <BaseMermaid chart={chart} />
        </div>
      </div>

      {isExpanded ? (
        <div
          onClick={() => setIsExpanded(false)}
          style={{
            background: 'rgba(15, 23, 42, 0.72)',
            inset: 0,
            padding: '2rem',
            position: 'fixed',
            zIndex: 1000
          }}
        >
          <div
            onClick={(event) => event.stopPropagation()}
            style={{
              background: 'var(--nextra-bg, #fff)',
              borderRadius: '1rem',
              boxShadow: '0 24px 80px rgba(0,0,0,0.35)',
              display: 'flex',
              flexDirection: 'column',
              height: '100%',
              margin: '0 auto',
              maxWidth: 'min(96vw, 1400px)'
            }}
          >
            <div
              style={{
                alignItems: 'center',
                borderBottom: '1px solid var(--nextra-border, rgba(0,0,0,0.12))',
                display: 'flex',
                gap: '0.5rem',
                justifyContent: 'space-between',
                padding: '1rem'
              }}
            >
              <strong style={{ fontSize: '0.95rem' }}>Mermaid diagram</strong>
              <div style={{ alignItems: 'center', display: 'flex', gap: '0.5rem' }}>
                <button
                  type="button"
                  style={toolbarButtonStyle}
                  onClick={() => setZoom((value) => Math.max(0.6, value - 0.2))}
                  disabled={zoomOutDisabled}
                >
                  -
                </button>
                <span style={{ fontSize: '0.9rem', minWidth: '4.5rem', textAlign: 'center' }}>
                  {Math.round(zoom * 100)}%
                </span>
                <button
                  type="button"
                  style={toolbarButtonStyle}
                  onClick={() => setZoom((value) => Math.min(2.4, value + 0.2))}
                  disabled={zoomInDisabled}
                >
                  +
                </button>
                <button type="button" style={toolbarButtonStyle} onClick={() => setZoom(1)}>
                  Reset
                </button>
                <button type="button" style={toolbarButtonStyle} onClick={() => setIsExpanded(false)}>
                  Close
                </button>
              </div>
            </div>
            <div
              className="zoomable-mermaid-render"
              style={{
                flex: 1,
                overflow: 'auto',
                padding: '1.5rem'
              }}
            >
              <div
                style={{
                  minHeight: '100%',
                  transform: `scale(${zoom})`,
                  transformOrigin: 'top center',
                  width: zoom > 1 ? `${100 / zoom}%` : '100%'
                }}
              >
                <BaseMermaid chart={chart} />
              </div>
            </div>
          </div>
        </div>
      ) : null}
    </>
  );
}