const path = require('node:path');
const { pathToFileURL } = require('node:url');

module.exports = async function turbopackNextraLoader(source) {
  const callback = this.async();

  try {
    const options = this.getOptions();
    const remarkPlugins = await Promise.all(
      options.remarkPluginPaths.map(async (pluginPath) => {
        const modulePath = path.resolve(process.cwd(), pluginPath);
        const pluginModule = await import(pathToFileURL(modulePath).href);
        return pluginModule.default;
      }),
    );
    const loaderOptions = {
      ...options,
      mdxOptions: {
        ...options.mdxOptions,
        remarkPlugins,
      },
    };
    const loaderContext = Object.create(this);
    Object.defineProperty(loaderContext, 'getOptions', {
      value: () => loaderOptions,
    });
    const nextraLoaderPath = path.resolve(
      process.cwd(),
      'node_modules/nextra/dist/server/loader.js',
    );
    const { loader } = await import(pathToFileURL(nextraLoaderPath).href);
    const output = await loader.call(loaderContext, source);
    const relativeImport = (modulePath) => {
      const relativePath = path
        .relative(path.dirname(this.resourcePath), modulePath)
        .split(path.sep)
        .join('/');
      return relativePath.startsWith('.') ? relativePath : `./${relativePath}`;
    };
    const outputWithImports = output
      .replaceAll(
        '"nextra/setup-page"',
        JSON.stringify(
          relativeImport(path.resolve(process.cwd(), 'turbopack-setup-page.mjs')),
        ),
      )
      .replaceAll(
        '"next-mdx-import-source-file"',
        JSON.stringify(relativeImport(path.resolve(process.cwd(), 'src/mdx-components.tsx'))),
      );

    callback(null, outputWithImports);
  } catch (error) {
    callback(error);
  }
};
