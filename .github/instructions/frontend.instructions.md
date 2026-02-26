---
applies_to:
  - "**/*.html"
  - "**/*.css"
  - "**/*.js"
  - "manifest.json"
---

# Frontend Instructions for Lord'Os AI System

## Overview

This file contains instructions specific to the Lord'Os PWA (Progressive Web App) frontend, which includes HTML, CSS, JavaScript, and PWA configuration.

## Technology Stack

- **Architecture**: Pure HTML/CSS/JavaScript (No frameworks)
- **Type**: Progressive Web App (PWA)
- **Design**: Dark Mode + Glassmorphism
- **Language Support**: Arabic (RTL) with bilingual content
- **Deployment**: Netlify, GitHub Pages, or Vercel

## Core Files

1. **index.html**: Main interface (desktop + mobile)
2. **style.css**: Styling (Dark mode, Glassmorphism effects)
3. **brain.js**: AI agent logic and interaction
4. **manifest.json**: PWA configuration

## Design Guidelines

### Color Scheme
- **Primary Background**: `#0a0a0a` (very dark)
- **Secondary Background**: `#1a1a1a` (dark gray)
- **Accent Colors**: Purple shades (`#9c27b0`, `#4a148c`, `#311b92`)
- **Text**: White (`#ffffff`) with proper contrast

### Visual Style
- **Dark Mode**: Always-on dark theme
- **Glassmorphism**: Frosted glass effects with backdrop-filter
- **Shadows**: Subtle shadows for depth
- **Borders**: Rounded corners (`border-radius: 10px-20px`)
- **Transparency**: Semi-transparent overlays (`rgba()`)

### Example CSS Pattern:
\`\`\`css
.glass-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
\`\`\`

## HTML Guidelines

### Structure
- Use semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<article>`)
- Keep markup clean and minimal
- Ensure proper heading hierarchy (h1 → h2 → h3)

### Arabic Text Support
- Always include `dir="rtl"` for Arabic text containers
- Use `lang="ar"` attribute where appropriate
- Test text alignment and rendering

### Example:
\`\`\`html
<div class="arabic-content" dir="rtl" lang="ar">
    <h2>مروى مسلم الدوسري</h2>
    <p>وكيلة ذكية بلهجة نجدية بيضاء</p>
</div>
\`\`\`

### Accessibility
- Include `alt` attributes for images
- Use proper ARIA labels when needed
- Ensure keyboard navigation works
- Maintain color contrast ratios

## CSS Guidelines

### Organization
- Group related styles together
- Use comments to separate sections
- Follow mobile-first approach

### RTL Support
\`\`\`css
body {
    direction: rtl; /* For Arabic content */
    text-align: right;
}

/* Use logical properties when possible */
.element {
    margin-inline-start: 10px; /* Instead of margin-left */
    padding-inline-end: 20px;  /* Instead of padding-right */
}
\`\`\`

### Responsive Design
- Mobile-first: Start with mobile styles, add desktop with media queries
- Breakpoints: 
  - Mobile: default (< 768px)
  - Tablet: `@media (min-width: 768px)`
  - Desktop: `@media (min-width: 1024px)`

### Example:
\`\`\`css
/* Mobile first */
.container {
    padding: 10px;
    font-size: 14px;
}

/* Desktop */
@media (min-width: 1024px) {
    .container {
        padding: 20px;
        font-size: 16px;
    }
}
\`\`\`

### Dark Mode Best Practices
- Use dark backgrounds with light text
- Reduce brightness for white elements
- Test eye comfort in dark environments
- Avoid pure white (`#ffffff`) for large areas, prefer `#f0f0f0` or less

## JavaScript Guidelines

### Code Style
- Use modern ES6+ syntax
- Use `const` and `let`, avoid `var`
- Use arrow functions for callbacks
- Use template literals for strings

### Example:
\`\`\`javascript
const greetUser = (name) => {
    return `مرحباً ${name}، كيف حالك؟`;
};

// Use descriptive variable names
const userMessage = document.getElementById('user-input');
const sendButton = document.querySelector('.send-btn');
\`\`\`

### Event Handling
- Use event delegation when possible
- Remove event listeners when not needed
- Handle mobile touch events

### Example:
\`\`\`javascript
// Good: Event delegation
document.addEventListener('click', (e) => {
    if (e.target.matches('.button')) {
        handleClick(e.target);
    }
});

// Touch support
element.addEventListener('touchstart', handleTouch);
\`\`\`

### مروى AI Character Logic
The `brain.js` file contains the AI agent's personality:
- **Character**: مروى مسلم الدوسري (Najdi dialect)
- **Traits**: Authentic Najdi expressions, helpful, warm
- **Vocabulary**: "سمّ"، "أبشر بعزك"، "يا بعد حيّي"

**Maintain character consistency** when adding responses or dialog.

## PWA Configuration (manifest.json)

### Required Fields
\`\`\`json
{
  "name": "Lord'Os AI",
  "short_name": "Lord'Os",
  "start_url": "index.html",
  "display": "standalone",
  "background_color": "#0a0a0a",
  "theme_color": "#0a0a0a",
  "orientation": "portrait"
}
\`\`\`

### Icons
- Provide 192x192 and 512x512 PNG icons
- Use high-quality, recognizable icons
- Test on both Android and iOS

### Testing PWA
1. Serve locally: `python3 -m http.server 8080`
2. Open Chrome DevTools → Application → Manifest
3. Check "Add to Home Screen" functionality
4. Test offline capabilities

## Performance Optimization

### File Size
- Minimize CSS/JS files for production
- Optimize images (use WebP when possible)
- Lazy load non-critical resources

### Loading Speed
- Inline critical CSS
- Defer non-critical JavaScript
- Use `async` or `defer` for script tags

### Example:
\`\`\`html
<link rel="preload" href="style.css" as="style">
<script src="brain.js" defer></script>
\`\`\`

## Common Tasks

### Adding New Features
1. Update HTML structure
2. Add corresponding styles in `style.css`
3. Implement logic in `brain.js`
4. Test on mobile and desktop
5. Verify Arabic text rendering

### Modifying مروى's Responses
Edit the response logic in `brain.js`:
\`\`\`javascript
const responses = {
    greeting: "سمّ، أبشر بعزك! كيف أقدر أساعدك؟",
    farewell: "يسعد مساك، يا بعد حيّي 💜"
};
\`\`\`

### Changing Theme Colors
Update CSS variables or direct color values:
\`\`\`css
:root {
    --primary-bg: #0a0a0a;
    --accent-color: #9c27b0;
    --text-color: #ffffff;
}
\`\`\`

## Testing Checklist

### Visual Testing
- [ ] Dark mode looks good in low light
- [ ] Glassmorphism effects render correctly
- [ ] Arabic text is properly aligned (RTL)
- [ ] Mobile responsive design works
- [ ] Colors have sufficient contrast

### Functional Testing
- [ ] PWA installs correctly on mobile
- [ ] Touch interactions work on mobile
- [ ] Keyboard navigation works on desktop
- [ ] AI responses display correctly
- [ ] All buttons and links work

### Browser Testing
- Test on Chrome/Edge (Chromium)
- Test on Safari (iOS)
- Test on Firefox
- Verify PWA functionality on Android

## Deployment

### Netlify
\`\`\`bash
# Drag and drop these files:
# - index.html
# - style.css
# - brain.js
# - manifest.json
\`\`\`

### GitHub Pages
\`\`\`bash
# Enable in repository settings
# Access at: https://username.github.io/RawanAI
\`\`\`

### Vercel
\`\`\`bash
npm i -g vercel
vercel --prod
\`\`\`

## Security Considerations

### Content Security
- Sanitize user input before displaying
- Avoid `eval()` or `innerHTML` with user content
- Use `textContent` for displaying user data

### Example:
\`\`\`javascript
// Good: Safe
element.textContent = userInput;

// Bad: Vulnerable to XSS
element.innerHTML = userInput;
\`\`\`

### External Resources
- Use HTTPS for all external resources
- Verify integrity of CDN resources
- Consider self-hosting critical dependencies

## Boundaries

### Do Not Change
- Core character personality (مروى مسلم الدوسري)
- Dark theme aesthetic
- Najdi dialect expressions
- PWA offline functionality
- Copyright statements

### Always Maintain
- RTL support for Arabic text
- Mobile-first responsive design
- Glassmorphism visual effects
- Dark mode consistency
- Touch-friendly interface

## Questions Before Making Changes

1. Does this maintain the dark theme aesthetic?
2. Is Arabic text properly rendered with RTL support?
3. Does this work on mobile devices (touch-friendly)?
4. Are Glassmorphism effects preserved?
5. Is مروى's Najdi dialect character maintained?
6. Does the PWA still install and work offline?
7. Is the interface still accessible?

## Additional Notes

- Lord'Os is designed for both **web and mobile** (PWA)
- **No backend required** - all logic runs client-side
- **Offline-first** approach - works without internet
- Respects **Saudi Arabian Najdi dialect** cultural context
- Maintains **professional yet warm** interaction style
