import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import ProgressTracker from './components/ProgressTracker.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // Register global components
    app.component('ProgressTracker', ProgressTracker)
  }
} satisfies Theme