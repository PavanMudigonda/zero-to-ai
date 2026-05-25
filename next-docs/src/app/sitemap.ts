import type { MetadataRoute } from 'next';

import { getStaticSiteRoutes } from '@/lib/site-routes';

export default function sitemap(): MetadataRoute.Sitemap {
  const lastModified = new Date();

  return getStaticSiteRoutes().map((routePath) => ({
    url: new URL(routePath, 'https://zero-to-ai.dev').toString(),
    lastModified,
    changeFrequency: routePath === '/' || routePath.startsWith('/curriculum') ? 'weekly' : 'monthly',
    priority: routePath === '/' ? 1 : routePath.startsWith('/curriculum') ? 0.8 : 0.7,
  }));
}