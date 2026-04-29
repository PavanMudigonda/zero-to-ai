import React from 'react';
import { Navbar, ThemeSwitch } from "nextra-theme-docs";
import FilteredLayout from "./FilteredLayout";
import { Head, Search } from 'nextra/components';
import 'nextra-theme-docs/style.css';
import './globals.css';
import { Metadata, Viewport } from 'next';
import { getStaticSiteRoutes } from '@/lib/site-routes';

type NavNode = {
  name: string;
  route: string;
  title: string;
  children: Map<string, NavNode>;
};

function segmentToTitle(segment: string): string {
  if (segment === 'index') {
    return 'Home';
  }

  return segment
    .replace(/[-_]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .replace(/\b\w/g, (character) => character.toUpperCase());
}

function createNavNode(name: string, route: string): NavNode {
  return {
    name,
    route,
    title: segmentToTitle(name),
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

    currentNodes = currentNodes.get(segment)!.children;
  }
}

function compareNavNodes(left: NavNode, right: NavNode): number {
  return left.route.localeCompare(right.route);
}

function materializePageMap(nodes: Map<string, NavNode>): any[] {
  return Array.from(nodes.values())
    .sort(compareNavNodes)
    .map((node) => {
      if (node.children.size > 0) {
        return {
          name: node.name,
          route: node.route,
          title: node.title,
          children: materializePageMap(node.children),
        };
      }

      return {
        name: node.name,
        route: node.route,
        title: node.title,
      };
    });
}

function buildLightweightPageMap(routes: string[]): any[] {
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
    },
    ...materializePageMap(rootNodes),
  ];
}

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  viewportFit: 'cover',
};

export const metadata: Metadata = {
  metadataBase: new URL('https://zero-to-ai.dev'),
  title: {
    template: '%s | Zero to AI',
    default: 'Zero to AI - Master Artificial Intelligence'
  },
  description: 'A comprehensive, open-source curriculum covering Python, Data Science, Machine Learning, Neural Networks, LLMs, and AI Agentic Frameworks.',
  keywords: ['AI', 'Artificial Intelligence', 'Machine Learning', 'Data Science', 'Python', 'LLM', 'Neural Networks', 'LangChain', 'Prompt Engineering'],
  applicationName: 'Zero to AI',
  generator: 'Next.js',
  authors: [{ name: 'Zero to AI Contributors' }],
  creator: 'Zero to AI Project',
  publisher: 'Zero to AI',
  alternates: {
    canonical: '/',
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
        url: '/social-preview.svg',
        width: 1200,
        height: 630,
        alt: 'Zero to AI open-source curriculum',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Zero to AI - Master Artificial Intelligence',
    description: 'An open-source roadmap & curriculum for learning Data Science, Machine Learning, LLMs, and AI Agents from scratch.',
    images: ['/social-preview.svg'],
  },
  appleWebApp: {
    title: 'Zero to AI',
    statusBarStyle: 'default',
  }
};

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const routeIndex = getStaticSiteRoutes();
  const pageMap = buildLightweightPageMap(routeIndex);
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
      <ThemeSwitch />
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
          search={<Search />}
        >
          {children}
        </FilteredLayout>
      </body>
    </html>
  );
}
