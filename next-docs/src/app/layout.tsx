import React from 'react';
import { Layout, Navbar } from 'nextra-theme-docs';
import { Head, Search } from 'nextra/components';
import { getPageMap } from 'nextra/page-map';
import 'nextra-theme-docs/style.css';
import './globals.css';
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: {
    template: '%s | Zero to AI',
    default: 'Zero to AI - Master Artificial Intelligence'
  },
  description: 'An open source curriculum covering Python, Data Science, Neural Networks, Agentic Frameworks and more.',
  applicationName: 'Zero to AI',
  generator: 'Next.js',
  appleWebApp: {
    title: 'Zero to AI',
  }
};

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const pageMap = await getPageMap();
  
  const navbar = (
    <Navbar
      logo={<b style={{ fontSize: '1.2rem', letterSpacing: '-0.02em' }}>🚀 Zero to AI</b>}
      projectLink="https://github.com/PavanMudigonda/zero-to-ai"
    />
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
        <Layout
          pageMap={pageMap}
          navbar={navbar}
          footer={footer}
          docsRepositoryBase="https://github.com/PavanMudigonda/zero-to-ai/tree/main/next-docs/src/app"
          editLink="Edit this page on GitHub"
          sidebar={{ defaultMenuCollapseLevel: 1, autoCollapse: true }}
          feedback={{ content: 'Question? Give us feedback →', labels: 'feedback' }}
          search={<Search />}
        >
          {children}
        </Layout>
      </body>
    </html>
  );
}
