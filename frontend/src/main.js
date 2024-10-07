import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import {DefaultConfig} from "http-client";

DefaultConfig.config = {
    basePath: import.meta.env.VITE_API_URL
};

const app = createApp(App)

app.use(router)

app.mount('#app')
