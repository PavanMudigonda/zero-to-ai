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
  transpilePackages: ['@theguild/remark-mermaid'],
  webpack(config, { webpack }) {
    if (!config.resolve.alias) {
      config.resolve.alias = {};
    }
    
    // Deep override @theguild/remark-mermaid import injection
    // to map to our custom ZoomableMermaid instead.
    // Using the 'webpack' object provided by next.js options.
    config.plugins.push(
      new webpack.NormalModuleReplacementPlugin(
        /@theguild\/remark-mermaid\/mermaid/,
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
