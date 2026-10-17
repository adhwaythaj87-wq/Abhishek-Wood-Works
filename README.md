# Abhishek Wood Works — Portfolio & Custom Interiors

> High-end, bespoke custom woodwork, furniture, and interior solutions.

A gallery-first portfolio website crafted for **Abhishek Wood Works**, showcasing real bespoke woodwork with an editorial aesthetic, responsive design, and zero AI-slop design tropes.

---

## Features

- **Hero Showcase**:
  - Full-bleed ambient photography with real furniture pieces.
  - 6-second crossfade rotation with subtle hardware-accelerated zoom (`scale(1.00)` to `scale(1.05)`).
  - Soft dark-walnut gradient at the bottom 45% ensuring text readability with **15.5:1** contrast ratio.
  - Interactive caption linking directly to corresponding gallery categories.
  - Desktop right-edge indicator dots and mobile-optimized touch controls.
  - Complete `prefers-reduced-motion` accessibility support.

- **Refined Catalogue Gallery**:
  - 7 curated categories: *Sofas*, *Dining*, *Wardrobes*, *Kitchens*, *Doors*, *TV Units*, *Beds*.
  - Clean wrapping category tabs on mobile (zero horizontal scroll) and sticky navigation.
  - Natural aspect-ratio masonry grid with lazy loading and blur-up placeholders.
  - Density toggle on desktop (*Comfortable* vs *Compact*).
  - Deep linking support with URL hashes (e.g., `#kitchens`, `#dining`).

- **Full-Featured Lightbox**:
  - Split-view detail interaction on desktop; touch-friendly bottom sheet on mobile.
  - Double-tap and pinch-to-zoom support for examining fine wood joinery details.
  - Category-scoped filmstrip thumbnail navigation.
  - Direct *"Enquire about this piece"* button pre-filling the enquiry form.

- **Information Gathering & Enquiries**:
  - Project enquiry form with project type, timeline, and requirements.
  - Instant WhatsApp direct submission button.
  - Pinned, quiet cream-outline floating WhatsApp pill with anti-collision geometry.

---

## Tech Stack

- **HTML5 & Vanilla JavaScript**: Zero heavy runtime dependencies, native DOM performance.
- **Tailwind CSS v3**: Compiled production CSS with custom walnut, cream, and amber color palette.
- **Typography**: Cormorant Garamond (Serif headings) and DM Sans (Body / UI labels).
- **Responsive Images**: Optimized WebP formats with multi-resolution `srcset` support.

---

## Project Structure

```text
├── assets/                 # Raw and optimized WebP furniture photography
│   └── optimized/          # Multi-resolution responsive image assets
├── dist/
│   └── output.css          # Compiled and minified Tailwind CSS
├── js/
│   ├── gallery-data.js     # Furniture catalog dataset
│   └── main.js             # Interactive behavior (Hero, Gallery, Lightbox, Form)
├── src/
│   └── input.css           # Tailwind base styles and custom utility classes
├── site-config.js          # Business details, categories, and contact info
├── index.html              # Main portfolio landing page
├── tailwind.config.js      # Tailwind configuration and design tokens
└── package.json            # Build scripts and development dependencies
```

---

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adhwaythaj87-wq/Abhishek-Wood-Works.git
   cd Abhishek-Wood-Works
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Build styles**:
   ```bash
   npm run build:css
   ```

4. **Serve locally**:
   ```bash
   # Using Python
   python -m http.server 3000

   # Or using Node
   npx serve .
   ```
   Open `http://localhost:3000` in your browser.
