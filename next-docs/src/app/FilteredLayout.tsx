"use client";

import React, { useMemo } from 'react';
import { usePathname } from 'next/navigation';
import { Layout } from 'nextra-theme-docs';

export default function FilteredLayout({ pageMap, children, ...props }: any) {
  const pathname = usePathname();
  const isHomePage = pathname === '/';
  const filteredPageMap = useMemo(() => {
    if (isHomePage) {
      return pageMap;
    }

    const topLevelSection = pathname.split('/').filter(Boolean)[0];

    return pageMap.map((item: any) => {
      if (item && item.children && item.name !== topLevelSection) {
        return {
          ...item,
          children: [],
        };
      }

      return item;
    });
  }, [isHomePage, pageMap, pathname]);

  return (
    <Layout
      pageMap={filteredPageMap}
      {...props}
      editLink={isHomePage ? null : props.editLink}
      feedback={isHomePage ? { content: null, labels: 'feedback' } : props.feedback}
    >
      {children}
    </Layout>
  );
}
