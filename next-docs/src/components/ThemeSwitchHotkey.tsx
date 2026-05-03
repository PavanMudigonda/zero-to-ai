'use client';

import { ThemeSwitch } from 'nextra-theme-docs';
import { useTheme } from 'next-themes';
import { useEffect } from 'react';

function isEditableTarget(target: EventTarget | null) {
  if (!(target instanceof HTMLElement)) {
    return false;
  }

  const tagName = target.tagName;
  return target.isContentEditable || tagName === 'INPUT' || tagName === 'TEXTAREA' || tagName === 'SELECT';
}

export default function ThemeSwitchHotkey() {
  const { resolvedTheme, setTheme } = useTheme();

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.defaultPrevented || event.metaKey || event.ctrlKey || event.altKey) {
        return;
      }

      if (event.key.toLowerCase() !== 't' || isEditableTarget(event.target)) {
        return;
      }

      event.preventDefault();
      setTheme(resolvedTheme === 'dark' ? 'light' : 'dark');
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [resolvedTheme, setTheme]);

  return <ThemeSwitch />;
}