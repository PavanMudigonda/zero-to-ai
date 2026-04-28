"use client";

import React, { useMemo } from 'react';
import { usePathname } from 'next/navigation';
import { Layout } from 'nextra-theme-docs';

export function FilteredPageMapLayout({ pageMap, children, ...props }: any) {
  const pathname = usePathname();

  const filteredPageMap = useMemo(() => {
    // pathname might be "/01-python", "/01-python/01-python.ipynb", etc.
    const parts = pathname.split('/').filter(Boolean);
    const topLevelSection = parts[0];

    // the pageMap is an array of items for the root level.
    // we want to keep all non-folder items (like 'index', 'demo' etc if any)
    // and ONLY the folder that matches topLevelSection.
    // However, top level items might be hidden or just normal pages.
    // Wait, if we filter out other top level folders, we WILL LOSE THEM from the Sidebar Top Level list!
    // We WANT them in the Sidebar Top Level list, but we just don't want their CHILDREN to render.
    // To achieve this, we can deep clone the pageMap, and for any top-level folder that is NOT topLevelSection,
    // we clear its `children` array!
    
    return pageMap.map((item: any) => {
      // If it's a folder/route with children at the root level
      if (item && item.children && item.name !== topLevelSection) {
        // Strip the children so they aren't rendered!
        return {
          ...item,
          children: []
        };
      }
      return item; // return as-is (this includes the active section and its full children tree)
    });
  }, [pageMap, pathname]);

  return (
    <Layout
      pageMap={filteredPageMap}
      {...props}
    >
      {children}
    </Layout>
  );
}
