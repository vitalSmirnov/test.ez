import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import { quasar, transformAssetUrls } from "@quasar/vite-plugin"
import { fileURLToPath } from "url"
// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue({
      template: { transformAssetUrls },
    }),
    quasar({
      autoImportComponentCase: "kebab",
      sassVariables: fileURLToPath(new URL("./src/quasar-variables.sass", import.meta.url)),
    }),
  ],
    server: {
    proxy: {
      "/api": "http://localhost:3000",
      "/media": "http://localhost:3000",
    },
  },
},
)
