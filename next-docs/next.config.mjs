import nextra from 'nextra';
import remarkNormalizeDocLinks from './remark-normalize-doc-links.mjs';
import remarkStripMissingImages from './remark-strip-missing-images.mjs';
import { existsSync, writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';

const withNextra = nextra({
  latex: true,
  defaultShowCopyCode: true,
  mdxOptions: {
    remarkPlugins: [remarkNormalizeDocLinks, remarkStripMissingImages]
  }
});

export default withNextra({
  output: 'export',
  eslint: {
    ignoreDuringBuilds: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    unoptimized: true,
  },
  transpilePackages: ['@theguild/remark-mermaid'],
  experimental: {
    // Enable memory-based worker caps instead of forcing 1 cpu
    memoryBasedWorkersCount: true,
  },
  webpack(config, { webpack, isServer, dev }) {
    if (!config.resolve.alias) {
      config.resolve.alias = {};
    }

    // Rely on Next.js default caching mechanism. 
    // Do NOT disable cache here; caching speeds up subsequent builds tremendously.

    // Workaround: Next.js 14.2.x export crashes with ENOENT on
    // pages-manifest.json in app-router-only projects. Ensure the
    // empty manifest exists after the server compilation emits.
    if (isServer) {
      config.plugins.push({
        apply(compiler) {
          compiler.hooks.afterEmit.tapAsync(
            'EnsurePagesManifest',
            (_compilation, callback) => {
              const manifestPath = join(
                compiler.outputPath,
                'pages-manifest.json',
              );
              if (!existsSync(manifestPath)) {
                mkdirSync(compiler.outputPath, { recursive: true });
                writeFileSync(manifestPath, '{}');
              }
              callback();
            },
          );
        },
      });
    }
    
    config.plugins.push(
      new webpack.NormalModuleReplacementPlugin(
        /^@theguild\/remark-mermaid\/mermaid$/,
        new URL('./src/components/ZoomableMermaid.tsx', import.meta.url).pathname
      )
    );

    config.module.rules.push({
      test: /\.ipynb$/,
      type: 'json',
    });
    return config;
  },
  reactStrictMode: true,
});
