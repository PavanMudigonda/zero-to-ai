import type { MetadataRoute } from 'next';

import { getStaticSiteRoutes } from '@/lib/site-routes';

export default function sitemap(): MetadataRoute.Sitemap {
  const buildDate = new Date(process.env.BUILD_DATE ?? Date.now()).toISOString();

  return getStaticSiteRoutes().map((routePath) => ({
    url: new URL(routePath, 'https://zero-to-ai.dev').toString(),
    lastModified: buildDate,
    changeFrequency: routePath === '/' || routePath.startsWith('/curriculum') ? 'weekly' : 'monthly',
    priority: routePath === '/' ? 1 : routePath.startsWith('/curriculum') ? 0.8 : 0.7,
  }));
}