"use client";
import React, { useMemo } from 'react';
import { usePathname } from 'next/navigation';
import { Layout } from 'nextra-theme-docs';

export default function FilteredLayout({ pageMap, children, ...props }: any) {
  const pathname = usePathname();

  const filteredPageMap = useMemo(() => {
    if (!pathname) return pageMap;
    const parts = pathname.split('/').filter(Boolean);
    const topLevel = parts[0];
    
    if (!topLevel) return pageMap;

    return pageMap.map((item: any) => {
      if (item && item.kind === 'Folder' && item.name !== topLevel) {
        return { ...item, children: [] };
      }
      if (item && item.children && item.name !== topLevel && topLevel !== "demo") {
        return { ...item, children: [] };
      }
      return item;
    });
  }, [pageMap, pathname]);

  return <Layout pageMap={filteredPageMap} {...props}>{children}</Layout>;
}
