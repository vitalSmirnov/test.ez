import vue from "eslint-plugin-vue"
import vueParser from "vue-eslint-parser"
import tsParser from "@typescript-eslint/parser"
import globals from "globals"

export default [
  ...vue.configs["flat/recommended"],
  {
    files: ["**/*.{ts,vue}", "**/*.js"],
    languageOptions: {
      parser: vueParser,
      parserOptions: {
        parser: tsParser,
        ecmaVersion: "latest",
        sourceType: "module",
        extraFileExtensions: [".vue"],
      },
      globals: {
        ...globals.browser,
        ...globals.node,
      },
    },
    rules: {
      "vue/multi-word-component-names": "off",
    },
  },
]
