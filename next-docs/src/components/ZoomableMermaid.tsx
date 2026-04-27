'use client';

// Bypass alias by directly referencing the exact file
import { Mermaid as BaseMermaid } from '../../node_modules/@theguild/remark-mermaid/dist/mermaid.js';
import { useCallback, useEffect, useRef, useState } from 'react';

type ZoomableMermaidProps = {
  chart: string;
};

/* ── constants ────────────────────────────────────────────── */
const MIN_SCALE = 0.1;
const MAX_SCALE = 5;
const ZOOM_STEP = 0.15;
const PAN_STEP = 40;
const DRAG_THRESHOLD = 3;

/* ── shared button style ──────────────────────────────────── */
const btnBase = {
  border: '1px solid var(--nextra-border, rgba(0,0,0,0.12))',
  borderRadius: '0.5rem',
  background: 'var(--nextra-bg, #fff)',
  color: 'var(--nextra-text, inherit)',
  cursor: 'pointer',
  fontSize: '0.875rem',
  lineHeight: 1,
  padding: '0.45rem 0.65rem',
} as const;

/* ── helpers ──────────────────────────────────────────────── */
function clamp(v: number, lo: number, hi: number) {
  return Math.min(hi, Math.max(lo, v));
}

/* ══════════════════════════════════════════════════════════════
   Pan + Zoom viewer rendered inside the expanded modal.
   Inspired by svg-toolbelt (zakaria.dev/svg-toolbelt) and
   BookStack's Mermaid Viewer.

   Features:
     • Mouse-wheel zoom to cursor
     • Click-drag pan
     • Pinch-to-zoom (touch)
     • One-finger drag (touch)
     • Keyboard: +/− zoom, 0 reset, arrows pan, Esc close
     • Zoom-level % indicator
   ══════════════════════════════════════════════════════════════ */
function PanZoomViewer({
  svgHtml,
  onClose,
}: {
  svgHtml: string;
  onClose: () => void;
}) {
  const viewportRef = useRef<HTMLDivElement>(null);
  const contentRef = useRef<HTMLDivElement>(null);

  // Transform state kept in a ref so event handlers never go stale.
  const tf = useRef({ scale: 1, tx: 0, ty: 0 });
  // Only used for the zoom % badge – updated sparingly.
  const [displayScale, setDisplayScale] = useState(1);

  /* ── apply transform to DOM ──────────────────────────────── */
  const apply = useCallback((animate = false) => {
    const el = contentRef.current;
    if (!el) return;
    const { scale, tx, ty } = tf.current;
    el.style.transition = animate ? 'transform 0.25s ease-out' : 'none';
    el.style.transform = `translate(${tx}px, ${ty}px) scale(${scale})`;
    setDisplayScale(scale);
  }, []);

  /* ── zoom to a point (clientX/Y) ─────────────────────────── */
  const zoomTo = useCallback(
    (dir: number, clientX: number, clientY: number, animate = false) => {
      const vp = viewportRef.current;
      if (!vp) return;
      const rect = vp.getBoundingClientRect();
      const { scale: oldScale, tx, ty } = tf.current;
      const newScale = clamp(oldScale * (1 + dir * ZOOM_STEP), MIN_SCALE, MAX_SCALE);
      if (newScale === oldScale) return;

      // Keep the point under the cursor fixed.
      const cx = clientX - rect.left;
      const cy = clientY - rect.top;
      const ratio = newScale / oldScale;
      tf.current = {
        scale: newScale,
        tx: cx - ratio * (cx - tx),
        ty: cy - ratio * (cy - ty),
      };
      apply(animate);
    },
    [apply],
  );

  /* ── zoom to viewport centre (for buttons / keyboard) ───── */
  const zoomCentre = useCallback(
    (dir: number) => {
      const vp = viewportRef.current;
      if (!vp) return;
      const r = vp.getBoundingClientRect();
      zoomTo(dir, r.left + r.width / 2, r.top + r.height / 2, true);
    },
    [zoomTo],
  );

  /* ── reset: fit + centre ─────────────────────────────────── */
  const reset = useCallback(() => {
    tf.current = { scale: 1, tx: 0, ty: 0 };
    apply(true);
  }, [apply]);

  /* ── centre the diagram on first render ──────────────────── */
  useEffect(() => {
    const vp = viewportRef.current;
    const ct = contentRef.current;
    if (!vp || !ct) return;
    // Wait one frame so the SVG has layout dimensions.
    requestAnimationFrame(() => {
      const svg = ct.querySelector('svg');
      if (!svg) return;
      const vr = vp.getBoundingClientRect();
      const sr = svg.getBoundingClientRect();
      // Fit the diagram inside the viewport with some padding.
      const pad = 32;
      const fitScale = Math.min(
        (vr.width - pad * 2) / sr.width,
        (vr.height - pad * 2) / sr.height,
        1, // don't upscale beyond 100 %
      );
      const scaledW = sr.width * fitScale;
      const scaledH = sr.height * fitScale;
      tf.current = {
        scale: fitScale,
        tx: (vr.width - scaledW) / 2,
        ty: (vr.height - scaledH) / 2,
      };
      apply(false);
    });
  }, [svgHtml, apply]);

  /* ── mouse-wheel zoom ────────────────────────────────────── */
  useEffect(() => {
    const vp = viewportRef.current;
    if (!vp) return;
    const onWheel = (e: WheelEvent) => {
      e.preventDefault();
      const dir = e.deltaY < 0 ? 1 : -1;
      zoomTo(dir, e.clientX, e.clientY);
    };
    vp.addEventListener('wheel', onWheel, { passive: false });
    return () => vp.removeEventListener('wheel', onWheel);
  }, [zoomTo]);

  /* ── mouse drag pan ──────────────────────────────────────── */
  useEffect(() => {
    const vp = viewportRef.current;
    if (!vp) return;
    let dragging = false;
    let dragStarted = false;
    let sx = 0;
    let sy = 0;
    let baseTx = 0;
    let baseTy = 0;

    const onDown = (e: MouseEvent) => {
      if (e.button !== 0) return;
      dragging = true;
      dragStarted = false;
      sx = e.clientX;
      sy = e.clientY;
      baseTx = tf.current.tx;
      baseTy = tf.current.ty;
      vp.style.cursor = 'grabbing';
    };
    const onMove = (e: MouseEvent) => {
      if (!dragging) return;
      const dx = e.clientX - sx;
      const dy = e.clientY - sy;
      if (!dragStarted && Math.abs(dx) < DRAG_THRESHOLD && Math.abs(dy) < DRAG_THRESHOLD) return;
      dragStarted = true;
      e.preventDefault();
      tf.current.tx = baseTx + dx;
      tf.current.ty = baseTy + dy;
      apply();
    };
    const onUp = () => {
      dragging = false;
      dragStarted = false;
      vp.style.cursor = 'grab';
    };

    vp.addEventListener('mousedown', onDown);
    document.addEventListener('mousemove', onMove);
    window.addEventListener('mouseup', onUp);
    return () => {
      vp.removeEventListener('mousedown', onDown);
      document.removeEventListener('mousemove', onMove);
      window.removeEventListener('mouseup', onUp);
    };
  }, [apply]);

  /* ── touch: pinch-to-zoom + one-finger drag ─────────────── */
  useEffect(() => {
    const vp = viewportRef.current;
    if (!vp) return;
    let lastDist = 0;
    let lastMidX = 0;
    let lastMidY = 0;
    let singleTouch = false;
    let stx = 0;
    let sty = 0;
    let baseTx = 0;
    let baseTy = 0;

    const dist = (a: Touch, b: Touch) =>
      Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY);

    const onTouchStart = (e: TouchEvent) => {
      if (e.touches.length === 2) {
        e.preventDefault();
        lastDist = dist(e.touches[0], e.touches[1]);
        lastMidX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
        lastMidY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
        singleTouch = false;
      } else if (e.touches.length === 1) {
        singleTouch = true;
        stx = e.touches[0].clientX;
        sty = e.touches[0].clientY;
        baseTx = tf.current.tx;
        baseTy = tf.current.ty;
      }
    };

    const onTouchMove = (e: TouchEvent) => {
      if (e.touches.length === 2) {
        e.preventDefault();
        const d = dist(e.touches[0], e.touches[1]);
        const midX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
        const midY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
        const ratio = d / lastDist;
        const oldScale = tf.current.scale;
        const newScale = clamp(oldScale * ratio, MIN_SCALE, MAX_SCALE);
        const rect = vp.getBoundingClientRect();
        const cx = midX - rect.left;
        const cy = midY - rect.top;
        const r = newScale / oldScale;
        tf.current = {
          scale: newScale,
          tx: cx - r * (cx - tf.current.tx) + (midX - lastMidX),
          ty: cy - r * (cy - tf.current.ty) + (midY - lastMidY),
        };
        lastDist = d;
        lastMidX = midX;
        lastMidY = midY;
        apply();
      } else if (e.touches.length === 1 && singleTouch) {
        e.preventDefault();
        tf.current.tx = baseTx + (e.touches[0].clientX - stx);
        tf.current.ty = baseTy + (e.touches[0].clientY - sty);
        apply();
      }
    };

    vp.addEventListener('touchstart', onTouchStart, { passive: false });
    vp.addEventListener('touchmove', onTouchMove, { passive: false });
    return () => {
      vp.removeEventListener('touchstart', onTouchStart);
      vp.removeEventListener('touchmove', onTouchMove);
    };
  }, [apply]);

  /* ── keyboard shortcuts ──────────────────────────────────── */
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      switch (e.key) {
        case 'Escape':
          onClose();
          break;
        case '+':
        case '=':
          zoomCentre(1);
          break;
        case '-':
          zoomCentre(-1);
          break;
        case '0':
          reset();
          break;
        case 'ArrowUp':
          e.preventDefault();
          tf.current.ty += PAN_STEP;
          apply(true);
          break;
        case 'ArrowDown':
          e.preventDefault();
          tf.current.ty -= PAN_STEP;
          apply(true);
          break;
        case 'ArrowLeft':
          e.preventDefault();
          tf.current.tx += PAN_STEP;
          apply(true);
          break;
        case 'ArrowRight':
          e.preventDefault();
          tf.current.tx -= PAN_STEP;
          apply(true);
          break;
        default:
          return;
      }
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, [onClose, zoomCentre, reset, apply]);

  /* ── lock body scroll ────────────────────────────────────── */
  useEffect(() => {
    const prev = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = prev;
    };
  }, []);

  const pct = Math.round(displayScale * 100);

  return (
    <div
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-label="Mermaid diagram viewer"
      style={{
        background: 'rgba(15,23,42,0.72)',
        inset: 0,
        position: 'fixed',
        zIndex: 1000,
        display: 'flex',
        flexDirection: 'column',
      }}
    >
      {/* ── toolbar ──────────────────────────────────────────── */}
      <div
        onClick={(e) => e.stopPropagation()}
        style={{
          alignItems: 'center',
          background: 'var(--nextra-bg, #fff)',
          borderBottom: '1px solid var(--nextra-border, rgba(0,0,0,0.12))',
          display: 'flex',
          gap: '0.5rem',
          justifyContent: 'center',
          padding: '0.6rem 1rem',
          zIndex: 10,
          flexShrink: 0,
        }}
      >
        <button type="button" style={btnBase} onClick={() => zoomCentre(-1)} title="Zoom out (−)">
          −
        </button>
        <span
          style={{
            fontSize: '0.8rem',
            fontVariantNumeric: 'tabular-nums',
            minWidth: '3.2rem',
            textAlign: 'center',
            userSelect: 'none',
          }}
        >
          {pct}%
        </span>
        <button type="button" style={btnBase} onClick={() => zoomCentre(1)} title="Zoom in (+)">
          +
        </button>
        <button type="button" style={btnBase} onClick={reset} title="Reset zoom (0)">
          Reset
        </button>
        <div style={{ width: '1rem' }} />
        <button type="button" style={btnBase} onClick={onClose} title="Close (Esc)">
          ✕ Close
        </button>
      </div>

      {/* ── viewport (pan + zoom area) ───────────────────────── */}
      <div
        ref={viewportRef}
        onClick={(e) => e.stopPropagation()}
        style={{
          flex: 1,
          overflow: 'hidden',
          cursor: 'grab',
          position: 'relative',
          touchAction: 'none',
        }}
      >
        <div
          ref={contentRef}
          style={{ transformOrigin: '0 0', willChange: 'transform' }}
          dangerouslySetInnerHTML={{ __html: svgHtml }}
        />

        {/* ── floating hint ─────────────────────────────────── */}
        <div
          style={{
            position: 'absolute',
            bottom: '0.75rem',
            left: '50%',
            transform: 'translateX(-50%)',
            background: 'rgba(0,0,0,0.55)',
            color: '#fff',
            fontSize: '0.7rem',
            borderRadius: '0.4rem',
            padding: '0.3rem 0.6rem',
            pointerEvents: 'none',
            userSelect: 'none',
          }}
        >
          Scroll to zoom · Drag to pan · +/− · 0 reset · Esc close
        </div>
      </div>
    </div>
  );
}

/* ══════════════════════════════════════════════════════════════
   Main export – inline card + maximize → PanZoomViewer
   ══════════════════════════════════════════════════════════════ */
export function Mermaid({ chart }: ZoomableMermaidProps) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [capturedSvg, setCapturedSvg] = useState('');
  const inlineRef = useRef<HTMLDivElement>(null);

  const handleMaximize = useCallback(() => {
    if (inlineRef.current) {
      setCapturedSvg(inlineRef.current.innerHTML);
    }
    setIsExpanded(true);
  }, []);

  const handleClose = useCallback(() => setIsExpanded(false), []);

  return (
    <>
      {/* ── inline card ──────────────────────────────────────── */}
      <div
        style={{
          border: '1px solid var(--nextra-border, rgba(0,0,0,0.12))',
          borderRadius: '0.75rem',
          margin: '1.5rem 0',
          overflow: 'hidden',
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
            padding: '0.75rem',
          }}
        >
          <button type="button" style={btnBase} onClick={handleMaximize}>
            Maximize
          </button>
        </div>
        <div
          ref={inlineRef}
          className="zoomable-mermaid-render"
          style={{ overflowX: 'auto', padding: '1rem' }}
        >
          <BaseMermaid chart={chart} />
        </div>
      </div>

      {/* ── expanded pan-zoom viewer ─────────────────────────── */}
      {isExpanded && <PanZoomViewer svgHtml={capturedSvg} onClose={handleClose} />}
    </>
  );
}

export default Mermaid;
