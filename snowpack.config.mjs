/** @type {import("snowpack").SnowpackUserConfig } */
export default {
  mount: {
    public: { url: '/', static: true },
    src: { url: '/dist' },
  },
  plugins: [
    '@snowpack/plugin-react-refresh',
    '@snowpack/plugin-postcss',
    '@snowpack/plugin-dotenv',
  ],
  alias: {
    'components': './src/components',
    'images': './src/assets/images',
    'sections': './src/sections',
    'styles': './src/styles',
  },
  exclude: [
    '**/node_modules/**/*',
    'src/assets/images/design/*',
    'src/assets/images/unused/*',
  ],
  routes: [
    /* Enable an SPA Fallback in development: */
    // {"match": "routes", "src": ".*", "dest": "/index.html"},
  ],
  optimize: {
    /* Bundle the final build: */
    bundle: true,
    minify: true,
    target: 'es2018',
  },
  packageOptions: {
    /* ... */
  },
  devOptions: {
    /* Don't automatically open the browser */
    open: 'none',
    tailwindConfig: './tailwind.config.js',
  },
  buildOptions: {
    /* This feature is experimental */
    sourcemap: true,
  },
};
