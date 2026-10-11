import nextra from 'nextra';
import { existsSync, writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';

const withNextra = nextra({
  latex: true,
  defaultShowCopyCode: true,
  mdxOptions: {
    remarkPlugins: []
  }
});

const outputMode = process.env.NEXT_OUTPUT_MODE ?? 'export';

const nextConfig = withNextra({
  ...(outputMode === 'export' ? { output: 'export' } : {}),
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

    // Fix: Next.js 14 server builds write chunks to server/chunks/{name}.js
    // (chunk names include the "chunks/" prefix), but webpack-runtime's u()
    // resolves using numeric chunk IDs without any path prefix → require("./N.js")
    // fails because the file is at ./chunks/N.js. Pinning the server chunkFilename
    // to "chunks/[id].js" aligns the runtime path template with the actual files.
    if (isServer) {
      config.output = config.output ?? {};
      config.output.chunkFilename = 'chunks/[id].js';
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

const nextraLoaderPath = join(process.cwd(), 'node_modules/nextra/loader.cjs');
const serializableLoaderPath = join(process.cwd(), 'turbopack-nextra-loader.cjs');
const remarkPluginPaths = [
  './remark-normalize-doc-links.mjs',
  './remark-fix-missing-refs.mjs',
];

nextConfig.turbopack ??= {};
nextConfig.turbopack.root = process.cwd();
nextConfig.turbopack.rules ??= {};
nextConfig.turbopack.rules['**/*.ipynb'] = {
  type: 'json',
};

for (const rule of Object.values(nextConfig.turbopack?.rules ?? {})) {
  if (!Array.isArray(rule.loaders)) continue;

  rule.loaders = rule.loaders.map((loader) => {
    if (loader.loader !== nextraLoaderPath || !loader.options.mdxOptions) {
      return loader;
    }

    return {
      loader: serializableLoaderPath,
      options: {
        ...loader.options,
        remarkPluginPaths,
      },
    };
  });
}

export default nextConfig;
