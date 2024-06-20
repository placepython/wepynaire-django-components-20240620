import { defineConfig } from "vite";
import path from "path";
import { glob } from "glob";

/**
 * Return an objet for vite rollup$Options input to detect files
 * to process.
 */
function getInputFiles(pattern) {
  return glob.sync(pattern).reduce((entries, file) => {
    const entry = path.basename(file, path.extname(file));
    // Ajoutez l'entrée au tableau des entrées
    entries[entry] = file;
    return entries;
  }, {});
}

// Collection of input files
const applicationFiles = getInputFiles("src/application/**/*.{js,ts}")
const styleFiles = getInputFiles("src/styles/*.{css,scss}");
const componentFiles = getInputFiles("../components/**/*.{js,ts,css,scss}")

const input = {
  ...applicationFiles,
  ...styleFiles,
  ...componentFiles,
};

console.log(input);

// Configuration entry point
export default defineConfig({
  plugins: [],
  base: "/static/",
  server: {
    open: false,
  },
  build: {
    outDir: path.resolve(__dirname, "../example/static/"),
    manifest: true,
    emptyOutDir: true,
    target: "modules",
    rollupOptions: {
      input,
      output: {
        entryFileNames: assetInfo => {
          if (assetInfo.facadeModuleId.includes('components')) {
            return 'components/[name].js';
          }
          return 'js/[name].js';
        },
        chunkFileNames: assetInfo => {
          if (assetInfo.facadeModuleId.includes('components')) {
            return 'components/chuncks/[name]-[hash].js';
          }
          return 'chunks/[name].js';
        },
        assetFileNames: assetInfo => {
          if (/\.(css|scss)$/i.test(assetInfo.facadeModuleId)) {
            if (assetInfo.facadeModuleId.includes('components')) {
              return 'components/css/[name][extname]';
            }
            return 'css/[name][extname]';
          }
          if (/\.(woff2?|ttf|eot|otf)$/i.test(assetInfo.facadeModuleId)) {
            return 'fonts/[name][extname]';
          }
          if (/\.(png|jpe?g|gif|svg|webp)$/i.test(assetInfo.facadeModuleId)) {
            return 'images/[name][extname]';
          }
          // Default fallback
          return '[name][extname]';
        }
      }
    },
  },
});
