"use client";

import React, { useEffect, useMemo, useState } from 'react';
import { usePathname } from 'next/navigation';
import { Layout, Navbar } from 'nextra-theme-docs';
import FuzzySearch from '@/components/FuzzySearch';
import ThemeSwitchHotkey from '@/components/ThemeSwitchHotkey';

export default function FilteredLayout({ pageMap, children, searchItems, ...props }: any) {
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
    <Layout
      pageMap={filteredPageMap}
      navbar={navbar}
      footer={footer}
      {...props}
      sidebar={sidebar}
      editLink={isHomePage ? null : props.editLink}
      feedback={isHomePage ? { content: null, labels: 'feedback' } : props.feedback}
      search={<FuzzySearch items={searchItems} />}
    >
      {children}
    </Layout>
  );
}
