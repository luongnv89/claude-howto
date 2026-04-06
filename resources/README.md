<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

> 🌐 [中文版本](README.zh.md) | [English Version](README.md)

# Claude How To - Brand Assets

Complete collection of logos, icons, and favicons for the Claude How To project. All assets use the V3.0 design: a compass with code bracket (`>`) symbol, representing guided navigation through code — using a Black/White/Gray palette with Bright Green (#22C55E) accent.

## Directory Structure

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # Main logo - Light mode (520×120px)
│   └── claude-howto-logo-dark.svg  # Main logo - Dark mode (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # App icon - Light mode (256×256px)
│   └── claude-howto-icon-dark.svg  # App icon - Dark mode (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px (primary)
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

Additional assets in `assets/logo/`:
```
assets/logo/
├── logo-full.svg       # Mark + wordmark (horizontal)
├── logo-mark.svg       # Compass symbol only (120×120px)
├── logo-wordmark.svg   # Text only
├── logo-icon.svg       # App icon (512×512, rounded)
├── favicon.svg         # 16×16 optimized
├── logo-white.svg      # White version for dark backgrounds
└── logo-black.svg      # Black monochrome version
```

## Assets Overview

### Design Concept (V3.0)

**Compass with Code Bracket** — guidance meets code:
- **Compass Ring** = Navigation, finding your way
- **North Needle (Green)** = Direction, progress on the learning path
- **South Needle (Black)** = Grounding, solid foundation
- **`>` Bracket** = Terminal prompt, code, CLI context
- **Tick Marks** = Precision, structured learning

### Logos

**Files**:
- `logos/claude-howto-logo.svg` (Light mode)
- `logos/claude-howto-logo-dark.svg` (Dark mode)

**Specifications**:
- **Size**: 520×120 px
- **Purpose**: Main header/branding logo with wordmark
- **Usage**:
  - Website headers
  - README badges
  - Marketing materials
  - Print materials
- **Format**: SVG (fully scalable)
- **Modes**: Light (white background) & Dark (#0A0A0A background)

### Icons

**Files**:
- `icons/claude-howto-icon.svg` (Light mode)
- `icons/claude-howto-icon-dark.svg` (Dark mode)

**Specifications**:
- **Size**: 256×256 px
- **Purpose**: Application icon, avatars, thumbnails
- **Usage**:
  - App icons
  - Profile avatars
  - Social media thumbnails
  - Documentation headers
- **Format**: SVG (fully scalable)
- **Modes**: Light (white background) & Dark (#0A0A0A background)

**Design Elements**:
- Compass ring with cardinal and intercardinal tick marks
- Green north needle (direction/guidance)
- Black south needle (foundation)
- `>` code bracket at center (terminal/CLI)
- Green center dot accent

### Favicons

Optimized versions at multiple sizes for web use:

| File | Size | DPI | Usage |
|------|------|-----|-------|
| `favicon-16.svg` | 16×16 px | 1x | Browser tabs (older browsers) |
| `favicon-32.svg` | 32×32 px | 1x | Standard browser favicon |
| `favicon-64.svg` | 64×64 px | 1x-2x | High-DPI displays |
| `favicon-128.svg` | 128×128 px | 2x | Apple touch icon, bookmarks |
| `favicon-256.svg` | 256×256 px | 4x | Modern browsers, PWA icons |

**Optimization Notes**:
- 16px: Minimal geometry — ring, needles, chevron only
- 32px: Adds cardinal tick marks
- 64px+: Full detail with intercardinal ticks
- All maintain visual consistency with main icon
- SVG format ensures crisp display at any size

## HTML Integration

### Basic Favicon Setup

```html
<!-- Browser favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple touch icon (mobile home screen) -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA & modern browsers -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### Complete Setup

```html
<head>
  <!-- Primary favicon -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Apple touch icon -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- PWA icons -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- PWA manifest reference (if using manifest.json) -->
  <meta name="theme-color" content="#000000">
</head>
```

## Color Palette

### Primary Colors
- **Black**: `#000000` (Primary text, strokes, south needle)
- **White**: `#FFFFFF` (Light backgrounds)
- **Gray**: `#6B7280` (Secondary text, minor tick marks)

### Accent Color
- **Bright Green**: `#22C55E` (North needle, center dot, accent lines — highlights only, never as background)

### Dark Mode
- **Background**: `#0A0A0A` (Near-black)

### CSS Variables
```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Tailwind Config
```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### Usage Guidelines
- Use black for primary text and structural elements
- Use gray for secondary/supporting elements
- Use green **only** for highlights — needle, dots, accent lines
- Never use green as a background color
- Maintain WCAG AA contrast (4.5:1 minimum)

## Design Guidelines

### Logo Usage
- Use on white or dark (#0A0A0A) backgrounds
- Scale proportionally
- Include clear space around logo (minimum: logo height / 2)
- Use provided light/dark variants for appropriate backgrounds

### Icon Usage
- Use at standard sizes: 16, 32, 64, 128, 256px
- Maintain the compass proportions
- Scale proportionally

### Favicon Usage
- Use appropriate size for context
- 16-32px: Browser tabs, bookmarks
- 64px: Favicon site icons
- 128px+: Apple/Android home screens

## SVG Optimization

All SVG files are flat design with no gradients or filters:
- Clean stroke-based geometry
- No embedded rasters
- Optimized paths
- Responsive viewBox

For web optimization:
```bash
# Compress SVG while maintaining quality
svgo --config='{
  "js2svg": {
    "indent": 2
  },
  "plugins": [
    "convertStyleToAttrs",
    "removeRasterImages"
  ]
}' input.svg -o output.svg
```

## PNG Conversion

To convert SVG to PNG for older browser support:

```bash
# Using ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# Using Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## Accessibility

- High contrast color ratios (WCAG AA compliant — 4.5:1 minimum)
- Clean geometric shapes recognizable at all sizes
- Scalable vector format
- No text in icons (text added separately in wordmark)
- No red-green color dependency for meaning

## Attribution

These assets are part of the Claude How To project.

**License**: MIT (see project LICENSE file)

## Version History

- **v3.0** (February 2026): Compass-bracket design with Black/White/Gray + Green accent palette
- **v2.0** (January 2026): Claude-inspired 12-ray starburst design with emerald palette
- **v1.0** (January 2026): Original hexagon-based progression icon design

---

**Last Updated**: February 2026
**Current Version**: 3.0 (Compass-Bracket)
**All Assets**: Production-ready SVG, fully scalable, WCAG AA accessible
