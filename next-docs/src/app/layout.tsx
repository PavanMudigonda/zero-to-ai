import React from 'react';
import { Navbar, ThemeSwitch } from "nextra-theme-docs";
import FilteredLayout from "./FilteredLayout";
import { Head, Search } from 'nextra/components';
import { getPageMap } from 'nextra/page-map';
import 'nextra-theme-docs/style.css';
import './globals.css';
import { Metadata, Viewport } from 'next';
import { headers } from 'next/headers';
import { getStaticSiteRoutes } from '@/lib/site-routes';

function collapseInactiveSections(items: any[], activeSection?: string): any[] {
  return items.map((item) => {
    if (!item || !Array.isArray(item.children)) {
      return item;
    }

    if (!activeSection || item.name !== activeSection) {
      return {
        ...item,
        children: [],
      };
    }

    return item;
  });
}

async function getSerializedPageMap(): Promise<any[]> {
  const requestPath = headers().get('Next-Url')?.split('?')[0] || '/';
  const topLevelSection = requestPath.split('/').filter(Boolean)[0];
  const rootPageMap = await getPageMap('/');

  if (!topLevelSection) {
    return collapseInactiveSections(rootPageMap);
  }

  let sectionPageMap: any[] | null = null;

  try {
    sectionPageMap = await getPageMap(`/${topLevelSection}`);
  } catch {
    sectionPageMap = null;
  }

  return collapseInactiveSections(rootPageMap, topLevelSection).map((item) => {
    if (
      sectionPageMap &&
      item &&
      item.name === topLevelSection &&
      Array.isArray(item.children)
    ) {
      return {
        ...item,
        children: sectionPageMap,
      };
    }

    return item;
  });
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
  const pageMap = await getSerializedPageMap();
  const routeIndex = getStaticSiteRoutes();
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
        <script
          dangerouslySetInnerHTML={{
            __html: `window.__ZERO_TO_AI_ROUTE_INDEX__ = ${JSON.stringify(routeIndex)};`,
          }}
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
