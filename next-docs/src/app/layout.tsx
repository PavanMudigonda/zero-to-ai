import React from 'react';
import { Navbar } from "nextra-theme-docs";
import FilteredLayout from "./FilteredLayout";
import ProgressWidget from "@/components/ProgressWidget";
import FuzzySearch from '@/components/FuzzySearch';
import ThemeSwitchHotkey from '@/components/ThemeSwitchHotkey';
import { Head } from 'nextra/components';
import 'nextra-theme-docs/style.css';
import './globals.css';
import { Metadata, Viewport } from 'next';
import { getStaticSiteRoutes } from '@/lib/site-routes';
import { buildSearchItems } from '@/lib/search-items';

type NavNode = {
  name: string;
  route: string;
  title: string;
  hasPage: boolean;
  children: Map<string, NavNode>;
};

const TITLE_OVERRIDES: Record<string, string> = {
  ai: 'AI',
  ml: 'ML',
  llm: 'LLM',
  llms: 'LLMs',
  rag: 'RAG',
  mlops: 'MLOps',
  nlp: 'NLP',
  api: 'API',
  apis: 'APIs',
  sdk: 'SDK',
  mcp: 'MCP',
  rl: 'RL',
  lora: 'LoRA',
  qlora: 'QLoRA',
  vscode: 'VS Code',
  openai: 'OpenAI',
  ide: 'IDE',
  ides: 'IDEs',
};

const PHRASE_OVERRIDES: Record<string, string> = {
  'Devops Interviews': 'Cheatsheets',
  'Debugging Troubleshooting': 'Debugging & Troubleshooting',
  'AI Safety Redteaming': 'AI Safety & Red Teaming',
  'AI Powered Dev Tools': 'AI-Powered Dev Tools',
  'AI Hardware LLM Validation': 'AI Hardware & LLM Validation',
  'Low Code AI Tools': 'Low-Code AI Tools',
  'Real Time Streaming': 'Real-Time Streaming',
  'Time Series Analysis': 'Time-Series Analysis',
};

function extractNumericPrefix(value: string): number | null {
  const match = value.match(/^(\d+)/);
  return match ? Number(match[1]) : null;
}

function getSiblingPriority(name: string): number {
  const normalized = name.toLowerCase();

  if (normalized.includes('start_here') || normalized.includes('start-here')) {
    return 0;
  }

  if (normalized.includes('pre-quiz') || normalized.includes('pre_quiz')) {
    return 2;
  }

  if (normalized.includes('post-quiz') || normalized.includes('post_quiz')) {
    return 3;
  }

  return 1;
}

function segmentToTitle(segment: string): string {
  if (segment === 'index') {
    return 'Home';
  }

  const cleaned = segment
    .replace(/[-_]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();

  const words = cleaned.split(' ').filter(Boolean).map((word) => {
    const override = TITLE_OVERRIDES[word.toLowerCase()];
    if (override) {
      return override;
    }

    return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
  });

  const title = words.join(' ');
  const numberPrefixMatch = title.match(/^(\d+)\s+(.*)$/);

  if (!numberPrefixMatch) {
    return PHRASE_OVERRIDES[title] ?? title;
  }

  const [, numberPrefix, remainder] = numberPrefixMatch;
  return `${numberPrefix} ${PHRASE_OVERRIDES[remainder] ?? remainder}`;
}

function createNavNode(name: string, route: string): NavNode {
  return {
    name,
    route,
    title: segmentToTitle(name),
    hasPage: false,
    children: new Map<string, NavNode>(),
  };
}

function insertRoute(nodes: Map<string, NavNode>, route: string) {
  const segments = route.split('/').filter(Boolean);
  let currentNodes = nodes;
  let currentRoute = '';

  for (const segment of segments) {
    currentRoute += `/${segment}`;

    if (!currentNodes.has(segment)) {
      currentNodes.set(segment, createNavNode(segment, currentRoute));
    }

    const currentNode = currentNodes.get(segment)!;

    if (currentRoute === route) {
      currentNode.hasPage = true;
    }

    currentNodes = currentNode.children;
  }
}

function compareNavNodes(left: NavNode, right: NavNode): number {
  const leftPriority = getSiblingPriority(left.name);
  const rightPriority = getSiblingPriority(right.name);

  if (leftPriority !== rightPriority) {
    return leftPriority - rightPriority;
  }

  const leftNumber = extractNumericPrefix(left.name);
  const rightNumber = extractNumericPrefix(right.name);

  if (leftNumber !== null && rightNumber !== null && leftNumber !== rightNumber) {
    return leftNumber - rightNumber;
  }

  return left.route.localeCompare(right.route);
}

function resolveSidebarRoute(node: NavNode): string {
  if (node.hasPage) {
    return node.route;
  }

  const firstChild = Array.from(node.children.values()).sort(compareNavNodes)[0];

  return firstChild ? resolveSidebarRoute(firstChild) : node.route;
}

function canFlattenLeafWrapper(node: NavNode): boolean {
  if (node.hasPage || node.children.size !== 1) {
    return false;
  }

  const onlyChild = Array.from(node.children.values())[0];
  return onlyChild.hasPage && onlyChild.children.size === 0;
}

function materializeNode(node: NavNode): unknown {
  if (canFlattenLeafWrapper(node)) {
    const onlyChild = Array.from(node.children.values())[0];

    return {
      name: onlyChild.name,
      title: `${node.title} / ${onlyChild.title}`,
      frontMatter: {},
      route: onlyChild.route,
    };
  }

  const baseItem = {
    name: node.name,
    title: node.title,
    frontMatter: {},
    route: resolveSidebarRoute(node),
  };

  if (node.children.size > 0) {
    return {
      ...baseItem,
      children: materializePageMap(node.children),
    };
  }

  return baseItem;
}

function materializePageMap(nodes: Map<string, NavNode>): unknown[] {
  return Array.from(nodes.values())
    .sort(compareNavNodes)
    .map((node) => materializeNode(node));
}

function buildLightweightPageMap(routes: string[]): unknown[] {
  const rootNodes = new Map<string, NavNode>();

  for (const route of routes) {
    if (route === '/') {
      continue;
    }

    insertRoute(rootNodes, route);
  }

  return [
    {
      name: 'index',
      route: '/',
      title: 'Home',
      frontMatter: {},
    },
    ...materializePageMap(rootNodes),
  ];
}

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  viewportFit: 'cover',
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: '#ffffff' },
    { media: '(prefers-color-scheme: dark)', color: '#0a0a0a' },
  ],
};

export const metadata: Metadata = {
  metadataBase: new URL('https://zero-to-ai.dev'),
  title: {
    template: '%s | Zero to AI',
    default: 'Zero to AI - Master Artificial Intelligence'
  },
  description: 'A comprehensive, open-source curriculum covering Python, Data Science, Machine Learning, Neural Networks, LLMs, and AI Agentic Frameworks.',
  manifest: '/manifest.webmanifest',
  icons: {
    icon: '/favicon.ico',
    shortcut: '/favicon.ico',
    apple: '/apple-touch-icon.png',
  },
  keywords: ['AI', 'Artificial Intelligence', 'Machine Learning', 'Data Science', 'Python', 'LLM', 'Neural Networks', 'LangChain', 'Prompt Engineering'],
  applicationName: 'Zero to AI',
  generator: 'Next.js',
  authors: [{ name: 'Zero to AI Contributors' }],
  creator: 'Zero to AI Project',
  publisher: 'Zero to AI',
  alternates: {
    canonical: './',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-image-preview': 'large',
      'max-snippet': -1,
      'max-video-preview': -1,
    },
  },
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  openGraph: {
    title: 'Zero to AI - Master Artificial Intelligence',
    description: 'An open-source roadmap & curriculum for learning Data Science, Machine Learning, LLMs, and AI Agents from scratch.',
    url: 'https://zero-to-ai.dev',
    siteName: 'Zero to AI',
    locale: 'en_US',
    type: 'website',
    images: [
      {
        url: '/social-preview.png',
        width: 1200,
        height: 630,
        type: 'image/png',
        alt: 'Zero to AI open-source curriculum',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Zero to AI - Master Artificial Intelligence',
    description: 'An open-source roadmap & curriculum for learning Data Science, Machine Learning, LLMs, and AI Agents from scratch.',
    images: ['/social-preview.png'],
  },
  appleWebApp: {
    title: 'Zero to AI',
    statusBarStyle: 'default',
  }
};

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const canonicalRoutes = getStaticSiteRoutes();
  const pageMap = buildLightweightPageMap(canonicalRoutes);
  const searchItems = buildSearchItems(buildLightweightPageMap(canonicalRoutes) as any);
  const websiteStructuredData = {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: 'Zero to AI',
    url: 'https://zero-to-ai.dev',
    description: 'Open-source curriculum for learning Python, machine learning, LLMs, AI agents, evaluation, and MLOps.',
    inLanguage: 'en-US',
    publisher: {
      '@type': 'Organization',
      name: 'Zero to AI',
      url: 'https://zero-to-ai.dev',
    },
  };
  
  const navbar = (
    <Navbar
      logo={
        <span className="site-logo">
          <span className="site-logo-mark" aria-hidden="true">🚀</span>
          <span className="site-logo-text">Zero to AI</span>
        </span>
      }
      projectLink="https://github.com/PavanMudigonda/zero-to-ai"
    >
      <ThemeSwitchHotkey />
    </Navbar>
  );
  
  const footer = (
    <footer style={{ background: 'var(--nextra-bg)', borderTop: '1px solid rgba(0,0,0,0.1)', padding: '2rem 1rem', textAlign: 'center', fontSize: '0.875rem' }}>
      © {new Date().getFullYear()} Zero to AI Curriculum.
    </footer>
  );

  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head>
      </Head>
      <body>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteStructuredData) }}
        />
        <FilteredLayout
          pageMap={pageMap}
          navbar={navbar}
          footer={footer}
          nextThemes={{ defaultTheme: 'light' }}
          docsRepositoryBase="https://github.com/PavanMudigonda/zero-to-ai/tree/main/next-docs/src/app"
          editLink="Edit this page on GitHub"
          sidebar={{ defaultMenuCollapseLevel: 1, autoCollapse: true }}
          feedback={{ content: 'Question? Give us feedback →', labels: 'feedback' }}
          search={<FuzzySearch items={searchItems} />}
        >
          {children}
          <ProgressWidget />
        </FilteredLayout>
      </body>
    </html>
  );
}
