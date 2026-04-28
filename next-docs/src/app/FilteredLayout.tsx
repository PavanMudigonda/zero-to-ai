"use client";

import React from 'react';
import { Layout } from 'nextra-theme-docs';

export default function FilteredLayout({ pageMap, children, ...props }: any) {
  return <Layout pageMap={pageMap} {...props}>{children}</Layout>;
}
