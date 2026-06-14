// Ambient declarations for CSS side-effect imports.
// TypeScript 6 no longer implicitly resolves bare `.css` imports, so declare
// them as side-effect-only modules to keep `tsc --noEmit` clean.
declare module '*.css';
