import { useMDXComponents as getNextraComponents } from 'nextra-theme-docs';
import ZoomableMermaid from './components/ZoomableMermaid';

export function useMDXComponents(components: any) {
  return {
    ...getNextraComponents(),
    Mermaid: ZoomableMermaid,
    ...components
  };
}
