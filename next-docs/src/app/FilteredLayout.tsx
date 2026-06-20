"use client";

import React, { useEffect, useMemo, useState } from 'react';
import { usePathname } from 'next/navigation';
import { Layout } from 'nextra-theme-docs';

export default function FilteredLayout({ pageMap, children, ...props }: any) {
  const pathname = usePathname();
  const isHomePage = pathname === '/';
  const [isDesktop, setIsDesktop] = useState(false);

  useEffect(() => {
    const mediaQuery = window.matchMedia('(min-width: 1024px)');
    const updateIsDesktop = () => setIsDesktop(mediaQuery.matches);

    updateIsDesktop();

    mediaQuery.addEventListener('change', updateIsDesktop);
    return () => mediaQuery.removeEventListener('change', updateIsDesktop);
  }, []);

  const filteredPageMap = useMemo(() => {
    if (isHomePage) {
      return pageMap;
    }

    const topLevelSection = pathname.split('/').filter(Boolean)[0];

    return pageMap.map((item: any) => {
      if (item && item.children && item.name !== topLevelSection) {
        const { children, ...rest } = item;
        return {
          ...rest,
        };
      }

      return item;
    });
  }, [isHomePage, pageMap, pathname]);

  const sidebar = useMemo(() => {
    const baseSidebar = props.sidebar ?? {};

    if (!isDesktop) {
      return baseSidebar;
    }

    return {
      ...baseSidebar,
      autoCollapse: false,
      defaultMenuCollapseLevel: baseSidebar.defaultMenuCollapseLevel ?? 1,
    };
  }, [isDesktop, props.sidebar]);

  return (
    <Layout
      pageMap={filteredPageMap}
      {...props}
      sidebar={sidebar}
      editLink={isHomePage ? null : props.editLink}
      feedback={isHomePage ? { content: null, labels: 'feedback' } : props.feedback}
    >
      {children}
    </Layout>
  );
}
