import { createApp } from "vue"
import { createPinia } from "pinia"
import "./style.scss"

import "quasar/src/css/index.sass"

import App from "./App.vue"
import { Quasar } from "quasar"

const myApp = createApp(App)

myApp.use(createPinia())
myApp.use(Quasar, {
  plugins: {}, // import Quasar plugins and add here
})

myApp.mount("#app")
