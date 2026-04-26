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
    config.module.rules.push({
      test: /\.ipynb$/,
      type: 'json',
    });
    return config;
  },
  reactStrictMode: true,
});
