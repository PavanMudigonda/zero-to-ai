'use client';

// Bypass alias by directly referencing the exact file
import { Mermaid as BaseMermaid } from '../../node_modules/@theguild/remark-mermaid/dist/mermaid.js';
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

export function Mermaid({ chart }: ZoomableMermaidProps) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [zoom, setZoom] = useState(1);

  useEffect(() => {
    if (!isExpanded) {
      setZoom(1);
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
            zIndex: 1000,
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center'
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
              height: '90vh',
              width: '90vw',
              overflow: 'hidden',
              position: 'relative'
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
                padding: '1rem',
                zIndex: 10
              }}
            >
              <button
                type="button"
                style={{ ...toolbarButtonStyle, opacity: zoomOutDisabled ? 0.5 : 1 }}
                disabled={zoomOutDisabled}
                onClick={() => setZoom((z) => Math.max(0.2, z - 0.2))}
              >
                -
              </button>
              <button
                type="button"
                style={toolbarButtonStyle}
                onClick={() => setZoom(1)}
              >
                Reset
              </button>
              <button
                type="button"
                style={{ ...toolbarButtonStyle, opacity: zoomInDisabled ? 0.5 : 1 }}
                disabled={zoomInDisabled}
                onClick={() => setZoom((z) => Math.min(3, z + 0.2))}
              >
                +
              </button>
              <div style={{ width: '1rem' }} />
              <button
                type="button"
                style={toolbarButtonStyle}
                onClick={() => setIsExpanded(false)}
              >
                Close
              </button>
            </div>
            
            <div
              style={{
                flex: 1,
                overflow: 'auto',
                padding: '2rem',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'flex-start'
              }}
            >
              <div
                style={{
                  transform: `scale(${zoom})`,
                  transformOrigin: 'top center',
                  transition: 'transform 0.2s ease-out'
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

// Preserve backwards default export just in case
export default Mermaid;
