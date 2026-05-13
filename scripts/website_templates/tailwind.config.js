/** @type {import('tailwindcss').Config} */
//
// Used by the Tailwind standalone CLI (invoked from scripts/vendor_assets.py).
// The `content` globs are passed as absolute paths via env vars so the build
// works from any cwd.
//
const path = require('path');
const siteDir = process.env.TAILWIND_SITE_DIR || path.join(__dirname, '..', '..', 'site');
const templateDir = process.env.TAILWIND_TEMPLATE_DIR || __dirname;

module.exports = {
  content: [
    path.join(siteDir, '**/*.html'),
    path.join(templateDir, '**/*.j2'),
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      colors: {
        brand: {
          50: '#eef2ff',
          100: '#e0e7ff',
          500: '#6366f1',
          600: '#4f46e5',
          700: '#4338ca',
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
