import React from 'react';
import { Layout } from 'nextra-theme-docs';
import { Head } from 'nextra/components';
import { getPageMap } from 'nextra/page-map';
import 'nextra-theme-docs/style.css';
import './globals.css';

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const pageMap = await getPageMap();
  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head />
      <body>
        <Layout
          pageMap={pageMap}
          docsRepositoryBase="https://github.com/PavanMudigonda/zero-to-ai/blob/main/docs"
          footer={<div>Zero to AI - Open Source Curriculum</div>}
          sidebar={{ defaultMenuCollapseLevel: 1, autoCollapse: true }}
        >
          {children}
        </Layout>
      </body>
    </html>
  );
}
