<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useData } from 'vitepress'

const { page } = useData()

// Module definitions matching the learning roadmap
const modules = [
  { id: '01-slash-commands', title: 'Slash Commands', path: '/01-slash-commands/' },
  { id: '02-memory', title: 'Memory', path: '/02-memory/' },
  { id: '03-skills', title: 'Skills', path: '/03-skills/' },
  { id: '04-subagents', title: 'Subagents', path: '/04-subagents/' },
  { id: '05-mcp', title: 'MCP', path: '/05-mcp/' },
  { id: '06-hooks', title: 'Hooks', path: '/06-hooks/' },
  { id: '07-plugins', title: 'Plugins', path: '/07-plugins/' },
  { id: '08-checkpoints', title: 'Checkpoints', path: '/08-checkpoints/' },
  { id: '09-advanced-features', title: '高级功能', path: '/09-advanced-features/' },
  { id: '10-cli', title: 'CLI', path: '/10-cli/' },
]

// Storage key
const STORAGE_KEY = 'claude-howto-progress'

// Reactive state
const completedModules = ref<Set<string>>(new Set())
const visitedPages = ref<Set<string>>(new Set())
const isLoaded = ref(false)

// Load progress from localStorage
const loadProgress = () => {
  if (typeof window === 'undefined') return

  try {
    const stored = localStorage.getItem(STORAGE_KEY)
    if (stored) {
      const data = JSON.parse(stored)
      completedModules.value = new Set(data.completed || [])
      visitedPages.value = new Set(data.visited || [])
    }
  } catch (e) {
    console.warn('Failed to load progress:', e)
  }
  isLoaded.value = true
}

// Save progress to localStorage
const saveProgress = () => {
  if (typeof window === 'undefined') return

  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      completed: [...completedModules.value],
      visited: [...visitedPages.value],
      lastUpdated: new Date().toISOString()
    }))
  } catch (e) {
    console.warn('Failed to save progress:', e)
  }
}

// Track page visit
const trackVisit = (path: string) => {
  // Normalize path
  const normalizedPath = path.replace(/\.html$/, '').replace(/\/$/, '')
  if (!visitedPages.value.has(normalizedPath)) {
    visitedPages.value.add(normalizedPath)
    saveProgress()
  }
}

// Toggle module completion
const toggleComplete = (moduleId: string) => {
  if (completedModules.value.has(moduleId)) {
    completedModules.value.delete(moduleId)
  } else {
    completedModules.value.add(moduleId)
  }
  saveProgress()
}

// Check if current page is completed
const isCurrentModuleCompleted = computed(() => {
  const currentModule = modules.find(m => page.value.relativePath.startsWith(m.id))
  return currentModule ? completedModules.value.has(currentModule.id) : false
})

// Calculate overall progress percentage
const progressPercentage = computed(() => {
  const total = modules.length
  const completed = completedModules.value.size
  return Math.round((completed / total) * 100)
})

// Get current module
const currentModule = computed(() => {
  return modules.find(m => page.value.relativePath.startsWith(m.id))
})

// Track page visits on route change
watch(() => page.value.relativePath, (newPath) => {
  if (newPath && isLoaded.value) {
    trackVisit(newPath)
  }
}, { immediate: true })

// Load on mount
onMounted(() => {
  loadProgress()
  trackVisit(page.value.relativePath)
})

// Expose for template
defineExpose({
  modules,
  completedModules,
  visitedPages,
  progressPercentage,
  currentModule,
  isCurrentModuleCompleted,
  toggleComplete
})
</script>

<template>
  <div class="progress-tracker" v-if="isLoaded">
    <div class="progress-header">
      <span class="progress-title">学习进度</span>
      <span class="progress-percentage">{{ progressPercentage }}%</span>
    </div>

    <div class="progress-bar">
      <div
        class="progress-fill"
        :style="{ width: `${progressPercentage}%` }"
      ></div>
    </div>

    <div class="module-list">
      <div
        v-for="module in modules"
        :key="module.id"
        class="module-item"
        :class="{
          completed: completedModules.has(module.id),
          active: currentModule?.id === module.id
        }"
      >
        <span class="status-icon">
          {{ completedModules.has(module.id) ? '✓' : '○' }}
        </span>
        <a :href="module.path" class="module-link">
          {{ module.id }}. {{ module.title }}
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.progress-tracker {
  background: var(--vp-c-bg-soft);
  border-radius: 12px;
  padding: 1rem 1.25rem;
  margin: 1rem 0;
  border: 1px solid var(--vp-c-divider);
}

.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.progress-title {
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--vp-c-text-1);
}

.progress-percentage {
  font-weight: 700;
  color: var(--vp-c-brand-1);
  font-size: 1.1rem;
}

.progress-bar {
  height: 8px;
  background: var(--vp-c-bg-mute);
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 1rem;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--vp-c-brand-1), #16A34A);
  border-radius: 4px;
  transition: width 0.4s ease;
}

.module-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.module-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  font-size: 0.875rem;
  transition: background-color 0.2s;
}

.module-item:hover {
  background: var(--vp-c-bg-mute);
}

.module-item.completed {
  color: var(--vp-c-brand-1);
}

.module-item.completed .status-icon {
  color: var(--vp-c-brand-1);
}

.module-item.active {
  background: var(--vp-c-brand-soft);
  font-weight: 500;
}

.status-icon {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.875rem;
  color: var(--vp-c-text-2);
}

.module-link {
  color: inherit;
  text-decoration: none;
}

.module-link:hover {
  color: var(--vp-c-brand-1);
}
</style>