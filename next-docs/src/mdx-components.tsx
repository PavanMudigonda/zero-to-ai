import { useMDXComponents as getNextraComponents } from 'nextra-theme-docs';

export function useMDXComponents(components: any) {
  return {
    ...getNextraComponents(),
    ...components
  };
}
