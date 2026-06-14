import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

/**
 * Zero to AI — Docusaurus configuration (migration demo).
 *
 * This mirrors the information architecture of the original Nextra site:
 *  - the sidebar order/titles come from the migrated chapters (see sidebars.ts)
 *  - LaTeX is enabled via remark-math + rehype-katex (Nextra used `latex: true`)
 *  - Mermaid is enabled via @docusaurus/theme-mermaid (Nextra used a custom
 *    ZoomableMermaid component)
 */
const config: Config = {
  title: 'Zero to AI',
  tagline:
    'An open-source roadmap & curriculum for learning Data Science, ML, LLMs, and AI Agents from scratch.',
  favicon: 'img/logo.svg',

  url: 'https://zero-to-ai.dev',
  baseUrl: '/',

  organizationName: 'PavanMudigonda',
  projectName: 'zero-to-ai',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  markdown: {
    // 'detect' => .md files parse as CommonMark, .mdx as MDX. Notebook-derived
    // prose often contains bare `<` / `{`, which would break the MDX compiler.
    format: 'detect',
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/', // docs at the site root, like the Nextra site
          sidebarPath: './sidebars.ts',
          // Ordering/labels come from sidebar_position + _category_.json that the
          // migration script writes, so we keep numeric filename prefixes intact
          // (disabling the parser avoids doc-id collisions like 06_/12_advanced_retrieval).
          numberPrefixParser: false,
          editUrl:
            'https://github.com/PavanMudigonda/zero-to-ai/tree/main/docusaurus-site/',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  // KaTeX stylesheet (required for rehype-katex rendering).
  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css',
      type: 'text/css',
      integrity:
        'sha384-nB0miv6/jRmo5UMMR1wu3Gz6NLsoTkbqJghGIsx//Rlm+ZU03BU6SQNC66uf4l5+',
      crossorigin: 'anonymous',
    },
  ],

  themeConfig: {
    image: 'img/logo.svg',
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Zero to AI',
      logo: {
        alt: 'Zero to AI',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'curriculumSidebar',
          position: 'left',
          label: 'Curriculum',
        },
        {
          href: 'https://github.com/PavanMudigonda/zero-to-ai',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Learn',
          items: [
            { label: 'Course Setup', to: '/00-course-setup' },
            { label: 'Python', to: '/01-python' },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/PavanMudigonda/zero-to-ai',
            },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} Zero to AI Curriculum.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'bash', 'json'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
