import nextra from 'nextra';
import remarkStripMissingImages from './remark-strip-missing-images.mjs';

const withNextra = nextra({
  latex: true,
  mdxOptions: {
    remarkPlugins: [remarkStripMissingImages]
  }
});

export default withNextra({
  output: 'export',
  images: {
    unoptimized: true,
  },
  webpack(config) {
    if (!config.resolve.alias) {
      config.resolve.alias = {};
    }
    // Deep override Nextra & @theguild/remark-mermaid import injection
    // to map to our custom ZoomableMermaid instead
    config.resolve.alias['@theguild/remark-mermaid/mermaid$'] = new URL(
      './src/components/ZoomableMermaid.tsx',
      import.meta.url
    ).pathname;

    config.module.rules.push({
      test: /\.ipynb$/,
      type: 'json',
    });
    return config;
  },
  reactStrictMode: true,
});
