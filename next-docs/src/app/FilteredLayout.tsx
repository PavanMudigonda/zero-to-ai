"use client";

import React from 'react';
import { usePathname } from 'next/navigation';
import { Layout } from 'nextra-theme-docs';

export default function FilteredLayout({ pageMap, children, ...props }: any) {
  const pathname = usePathname();
  const isHomePage = pathname === '/';

  return (
    <Layout
      pageMap={pageMap}
      {...props}
      editLink={isHomePage ? null : props.editLink}
      feedback={isHomePage ? { content: null, labels: 'feedback' } : props.feedback}
    >
      {children}
    </Layout>
  );
}
