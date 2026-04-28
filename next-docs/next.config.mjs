import nextra from 'nextra';
import remarkStripMissingImages from './remark-strip-missing-images.mjs';
import { existsSync, writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';

const withNextra = nextra({
  latex: true,
  mdxOptions: {
    remarkPlugins: [remarkStripMissingImages]
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
    // Avoid using high concurrency that leads to Node OOMing inside GitHub runner
    cpus: 1,
    workerThreads: false,
    memoryBasedWorkersCount: false,
  },
  webpack(config, { webpack, isServer }) {
    if (!config.resolve.alias) {
      config.resolve.alias = {};
    }

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
