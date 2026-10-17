# Implementation Plan: Abhishek Wood Works Website

> **Status:** Plan Phase — No implementation code will be written until explicit approval is given by the user.

---

## 1. Project Overview & Aesthetic Direction

### Goal
Build an ultra-fast, mobile-first, high-converting portfolio website for **Abhishek Wood Works**—a bespoke custom woodwork, furniture, and interiors studio. 

### Core Principles
1. **Gallery First:** Finished, tangible woodwork is visible immediately within the first viewport. No long corporate introductions or marketing buzzwords.
2. **Information Gathering:** Every interaction leads effortlessly to project enquiry (Name, Phone/WhatsApp, Project Type, Budget, Timeline, Reference Photos) or instant direct WhatsApp chat.
3. **No AI Slop & No Generic SaaS Look:**
   - **No** purple/blue gradients, no neon glows, no glassmorphism, no gradient text.
   - **No** three-identical-card layouts repeated down the page. Layouts vary between editorial splits, asymmetric masonry, and vertical numbered timelines.
   - **No** emoji or generic icon-in-circle cards. Clean, thin architectural line vectors only if needed.
   - **No** hollow filler slogans ("Crafting dreams into reality"). Honest, plain-spoken craftsman copy written in the first person.
   - **No** fake stats, fake client testimonials, or invented 5-star ratings. Genuine workshop milestones and explicit `[TODO]` placeholders for the owner's story.
   - **No** pill-shaped rounded-2xl buttons with massive fuzzy drop shadows. Crisp or softly rounded corners (rounded-sm/md), hairline borders (`border-[#2B1A12]/15`), and subtle natural wood grain textures.
   - **Asymmetric, editorial layouts** with generous whitespace, alternating warm cream and deep walnut sections like walking through rooms in a luxury showroom.

---

## 2. Palette & Typography System

### Color Palette (Extracted directly from `/assets/logo.jpg`)
| Token Name | Hex Code | Role & Usage |
| :--- | :--- | :--- |
| **Deep Walnut** | `#2B1A12` | Primary dark tone, high-contrast dark section backgrounds, primary text in cream sections |
| **Rich Mahogany** | `#4A2C1A` | Secondary wood tone, card surfaces in dark mode, borders, deep accents |
| **Warm Cream / Maple** | `#F1E3C8` | Primary light background, soft paper texture feel, text color in dark sections |
| **Soft Sand / Linen** | `#F9F5EE` | Off-white canvas background for gallery whitespace and high readability |
| **Amber Glow** | `#D98B2B` | Single accent color (sparingly used for active tab underlines, quote badges, focus rings) |
| **Showroom Off-Black** | `#0E0A08` | Deepest contrast background for the Hero / Dark showroom transition sections |
| **WhatsApp Emerald** | `#25D366` | Discreetly utilized for the floating chat button and WhatsApp enquiry trigger |

### Typography
- **Headings & Display:** `Cormorant Garamond` (Google Font) – Elegant serif with classical proportion, high contrast serifs, and timeless artisanal heritage.
- **Body & Controls:** `DM Sans` (Google Font) – Geometric yet warm sans-serif with high legibility on mobile screens, clean numerals, and spacious letterforms.
- **Eyebrows & Labels:** Small uppercase tracking (`tracking-[0.2em] uppercase text-xs font-medium`).

---

## 3. Asset Audit & Gallery Categorization

A scan of `/assets` identified **33 real image assets** (no stock photos will ever be used). All images have been inspected and cataloged:

| Asset Filename | Dimensions | Aspect / Type | Identified Subject & Category | Proposed Caption & Tag |
| :--- | :--- | :--- | :--- | :--- |
| `logo.jpg` | 1024x1024 | Square / Brand | Official 3D carved circular wooden emblem | Brand Logo & Favicon Source |
| `777189214_1772764893764912_6432006908235877688_n.webp` | 2048x1152 | Wide Landscape (16:9) | Hand-carved workshop sign with plane, saw, wood shavings | Banner / Hero / About Feature |
| `1790507733748.jpg.jpeg` | 1364x768 | Landscape | Handcrafted solid teak slat bench & cabriole-leg coffee table | Hero Candidate / Seating |
| `1790495440438.jpg.jpeg` | 896x1200 | Portrait | 4-door natural teak wardrobe with dressing mirror & drawers | Wardrobes & Storage |
| `1790495660941.jpg.jpeg` | 768x1364 | Portrait | Full-height teak wardrobe with integrated vanity & mirror | Wardrobes & Storage |
| `1790495791951.jpg.jpeg` | 768x1364 | Portrait | Matte slate grey modular wardrobe with floating vanity unit | Wardrobes & Storage |
| `1790496338473.jpg.jpeg` | 768x1364 | Portrait | Floor-to-ceiling champagne acrylic wardrobe with black pulls | Wardrobes & Storage |
| `1790496822199.jpg.jpeg` | 768x1364 | Portrait | Dual-tone teak & grey wardrobe with overhead lofts & bench vanity | Wardrobes & Storage |
| `1790495521516.jpg.jpeg` | 768x1364 | Portrait | Teak slatted back accent chair with terracotta bolster cushion | Seating & Chairs |
| `1790495655377.jpg.jpeg` | 768x1364 | Portrait | Row of 5 dining chairs in workshop with "Abhishek Wood Works" sign | Dining & Chairs |
| `1790496564042.jpg.jpeg` | 768x1364 | Portrait | Round space-saving dining table with 4 nesting tuck-in slat chairs | Dining |
| `1790506933257.jpg.jpeg` | 768x1364 | Portrait | Solid wood X-frame upholstered dining bench next to marble table | Dining & Seating |
| `1790506973624.jpg.jpeg` | 768x1364 | Portrait | Pair of sculptural wood breakfast counter barstools in sky blue | Chairs & Barstools |
| `1790507134383.jpg.jpeg` | 768x1364 | Portrait | Curved high-back teak dining chair with cabriole legs | Dining & Chairs |
| `1790495728758.jpg.jpeg` | 768x1364 | Portrait | Detail shot: "SKU: WF-SOFA-A1 \| Premium Teak Wood \| Artisan Crafted" | Sofas & Living |
| `1790496663240.jpg.jpeg` | 768x1364 | Portrait | Solid teak L-shaped corner sectional sofa with carved coffee table | Sofas & Living |
| `1790507013071.jpg.jpeg` | 768x1364 | Portrait | 3-seater living room sofa with fluted dark walnut timber armrests | Sofas & Living |
| `1790495975706.jpg.jpeg` | 768x1376 | Portrait | L-shaped gloss cream modular kitchen with glass crockery cabinet | Kitchens |
| `1790496145559.jpg.jpeg` | 768x1364 | Portrait | Modular kitchen cooking zone with built-in gas hob & pan drawers | Kitchens |
| `1790496266825.jpg.jpeg` | 768x1364 | Portrait | Full perspective modular kitchen with black granite countertop | Kitchens |
| `1790496500474 (1).jpg.jpeg` | 768x1364 | Portrait | Modern powder blue & white modular kitchen with corner sink | Kitchens |
| `1790506776206.jpg.jpeg` | 768x1364 | Portrait | Solid teak entry door with coffered relief panels & fluted glass | Doors & Architectural |
| `1790506884483.jpg.jpeg` | 768x1364 | Portrait | 3-panel wooden casement window with frosted geometric art glass | Windows & Architectural |
| `1790507090416.jpg.jpeg` | 768x1364 | Portrait | Custom walnut & teak entrance door with geometric glass inserts | Doors & Architectural |
| `1790507286793.jpg.jpeg` | 768x1364 | Portrait | Teak interior flush door with curved hand-routed grain arcs | Doors & Architectural |
| `1790507674542.jpg.jpeg` | 768x1364 | Portrait | Hand-carved heritage entrance / pooja door with floral filigree frame | Doors & Heritage |
| `1790506845672.jpg.jpeg` | 768x1364 | Portrait | Minimalist cream bedside nightstand with brass knobs & bedframe | Beds & Bedroom |
| `1790507405276.jpg.jpeg` | 768x1364 | Portrait | Solid raw teak daybed / diwan with hand-carved lion-paw feet | Beds & Daybeds |
| `1790496739030.jpg.jpeg` | 768x1376 | Portrait | Walnut open display bookshelf & entertainment console with X-brace | Living & Display |
| `1790507330037.jpg.jpeg` | 768x1364 | Portrait | Floor-to-ceiling modular TV unit and decorative partition grid | TV Units & Living |
| `1790507453367.jpg.jpeg` | 768x1364 | Portrait | 5-tier pyramid corner display etagere stand with curved base | Living & Display |
| `1790507499478.jpg.jpeg` | 768x1364 | Portrait | Custom timber partition archway with built-in low book ledge | Interiors & Partitions |
| `1790495923428.jpg.jpeg` | 768x1376 | Portrait | Raw teak wood timber planks with fresh wood curls ("PREMIUM TEAK") | Materials & Workshop |

### Gallery Filter Categories
1. **All Work** (Complete catalogue of 31 showcase items)
2. **Sofas & Seating** (Sectional sofas, bench seating, barstools, armchairs, diwan)
3. **Dining** (Nesting round dining table, dining chairs, dining bench)
4. **Wardrobes** (Teak wardrobes, dual-tone laminate, champagne acrylic, vanities)
5. **Kitchens** (Modular kitchens in cream, powder blue, granite countertops)
6. **Doors & Windows** (Hand-carved heritage pooja door, designer entrance doors, geometric windows)
7. **TV Units & Partitions** (Wall entertainment centers, display etagere, partition archways)

---

## 4. Architecture & Technical Stack

### Clean, High-Performance Static Setup (No framework overhead)
- **HTML5:** Semantic, accessible markup (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<dialog>`, `<footer>`).
- **Tailwind CSS (v3 / standalone CDN or compiled build):** Customized with exact palette tokens, serif typography, custom container widths, and micro-interaction utilities.
- **Zero-Dependency Vanilla JavaScript:**
  - Lightweight, modular structure (~12KB total).
  - Fast mobile touch gestures for the Lightbox (touchstartX, touchmove, touchend swipe).
  - Keyboard navigation (`Escape` closes lightbox, `ArrowLeft` / `ArrowRight` cycles through items).
  - Dynamic category filtering with smooth fade/scale transitions.
  - Interactive WhatsApp URL builder encoding form parameters.
  - Sticky header scroll observer via `IntersectionObserver` or scroll throttle.
- **Single Source of Truth Configuration (`site-config.js`):**
  - All editable business info (business name, phone, WhatsApp number, email, address, working hours, form endpoint, gallery items metadata) is defined in one clean configuration file so the owner never has to touch HTML markup to update details.
- **Target Hosting:** 100% compatible with GitHub Pages, Netlify, Vercel, or standard cPanel/Apache/Nginx servers.

---

## 5. Page Layout & Section-by-Section Plan

### Section 1: Header (Sticky Navigation)
- **Left:** Real logo image (`/assets/logo.jpg`, 48px height, rounded-full border with subtle amber ring).
- **Center / Right Nav:** Minimal links: *Work*, *About*, *Process*, *Contact*.
- **Right CTA:** "Get a Quote" solid button (`#2B1A12` with hover state to `#D98B2B`).
- **Mobile Menu:** Discreet hamburger toggle opening a clean, full-screen slide-down drawer with large typography and phone CTA.
- **Scroll Behavior:** Starts transparent over hero, transitions smoothly to solid background (`bg-[#F9F5EE]/95 backdrop-blur-md` with subtle bottom border) when scrolled past 60px.

### Section 2: Hero (Gallery First, High Impact)
- **Visual:** Full-bleed presentation using the high-resolution landscape asset (`777189214_1772764893764912_6432006908235877688_n.webp` or `1790507733748.jpg.jpeg`) with a dark walnut gradient scrim.
- **Badge:** Small letterspaced label: `HANDCRAFTED IN INDIA • CUSTOM ORDER ONLY`.
- **Title:** `Abhishek Wood Works` in regal Cormorant Garamond serif.
- **Subline:** Exactly as requested: `"Custom furniture and interiors, made to order."`
- **Actions:**
  - Primary button: `"View Our Work"` (smooth scrolls directly into the gallery grid).
  - Secondary button: `"Get a Quote"` (smooth scrolls to the enquiry form).
- **Hero-to-Gallery Flow:** The hero is tight and impactful (~75-80vh on desktop, compact on mobile) so the top of the gallery grid is peeked/visible without excessive scrolling.

### Section 3: Gallery (The Hero Feature)
- **Category Filter Tabs:** Horizontally scrollable on mobile with pill indicators (All, Sofas & Seating, Dining, Wardrobes, Kitchens, Doors & Windows, TV Units & Partitions).
- **Editorial Masonry Layout:**
  - CSS Columns or responsive CSS Grid preserving the natural aspect ratio of every photograph (no artificial square cropping).
  - Gentle hover zoom (`scale-102`) with subtle caption overlay appearing on hover / tap.
  - Each item card shows: title, timber/material tag, and a subtle "Tap to inspect" prompt.
- **Full-Screen Lightbox Experience:**
  - Triggered by clicking any photo.
  - Native `<dialog>` or accessible modal with `role="dialog"` and `aria-modal="true"`.
  - Full-resolution image display with natural aspect preservation.
  - Title, category, and descriptive caption.
  - Keyboard controls: `Esc` to close, `←` / `→` arrows to navigate previous/next.
  - Mobile touch gestures: left/right swipe detection for smooth photo browsing.
  - **Conversion Hook:** Prominent `"Like this? Enquire about it"` button inside the lightbox modal that closes the modal, smoothly scrolls to the Enquiry Form, and auto-selects the category and prefills the message field with: *"I am interested in custom-making something like [Item Name] seen in your gallery."*

### Section 4: About Us (Honest Craftsman Voice)
- **Palette Shift:** Warm cream background (`#F1E3C8`) with deep walnut text.
- **Layout:** Asymmetric 2-column layout.
  - Column 1: Editorial photography showcase utilizing `1790495923428.jpg.jpeg` (the real raw teak timber planks with wood shavings) and a framed placeholder for the founder/workshop master.
  - Column 2: First-person carpenter statement:
    - Honest craftsman philosophy: *"We don't sell flat-pack boards from factories. Every bed, wardrobe, and door that leaves our workshop is measured to the millimeter for your room and built out of solid seasoned wood and premium hardware."*
    - Clearly marked `[TODO: Insert Owner Name & Years in Business]` and `[TODO: List your local workshop address/city]`.
    - Material commitments: Solid Teak, Rosewood, Marine Plywood, Acrylic Laminates, and Blum/Hettich precision hardware.

### Section 5: How We Work (4-Step Timeline, Not Generic Cards)
- **Design:** Vertical editorial timeline with connecting hairline borders and large numeral markers (`01`, `02`, `03`, `04`) in serif italics.
- **Steps:**
  1. **01. Share Your Idea** — Send us a rough sketch, an Instagram reference, or select an item from our gallery.
  2. **02. Visit & Measure** — We visit your space, take precise laser measurements, inspect wall alignments, and discuss wood choices.
  3. **03. Design & Quote** — Detailed layout drawings with material specs and an honest, transparent estimate without hidden charges.
  4. **04. Build & Install** — Handcrafted in our workshop, pre-assembled to verify tolerances, and cleanly installed at your premises.

### Section 6: Enquiry Form (Primary Conversion Point)
- **Palette Shift:** Showroom dark section (`#0E0A08` to `#2B1A12`) with warm cream text and amber accents for maximum focus.
- **Fields:**
  - `Name` (Required)
  - `Phone / WhatsApp Number` (Required, with validation pattern)
  - `Email Address` (Optional)
  - `What do you need?` (Dropdown: *Bed & Bedroom*, *Wardrobe & Storage*, *Sofa & Living Seating*, *Dining Table & Chairs*, *Modular Kitchen*, *Custom Doors & Windows*, *Full Home Interiors*, *Other Custom Woodwork*)
  - `Estimated Budget` (Optional dropdown: *Under ₹50,000*, *₹50,000 - ₹1,50,000*, *₹1,50,000 - ₹3,00,000*, *₹3,00,000+*, *Need guidance*)
  - `Timeline` (Dropdown: *Immediately / This Month*, *1 to 2 Months*, *Planning Ahead*)
  - `Upload Reference Photo` (File input with preview / WhatsApp helper note)
  - `Project Details / Notes` (Textarea, auto-prefilled when clicked from Gallery)
- **Dual Conversion Pathways:**
  1. **Standard Form Submission:** Connects to Web3Forms / Formspree (configured via `site-config.js` with friendly inline validation, spinner state, and custom success confirmation screen).
  2. **"Send on WhatsApp Instead" Button:** Prominent alternative CTA. A live script compiles all filled form values into an elegant, formatted message and opens `https://wa.me/{phone}?text={encoded_message}` directly.

### Section 7: Contact & Local Footer
- **Layout:** Multi-column asymmetric footer.
  - Column 1: Official Logo (`/assets/logo.jpg`), business name, and licensing tag.
  - Column 2: Direct contact details (Click-to-call Phone, WhatsApp link, Email, Workshop Address, Working Hours: Mon-Sat 9:00 AM - 8:00 PM).
  - Column 3: Workshop location with interactive Google Maps embed iframe placeholder `[TODO: Insert Google Maps Embed URL]`.
  - Column 4: Social media handles `[TODO: Add your Instagram & Facebook links]`.
- **Copyright & Transparency:** Clean footer notice, no third-party branding.

### Section 8: Floating WhatsApp Button
- Positioned fixed at bottom-right (`bottom-6 right-6 z-50`).
- Subtle, quiet, non-distracting pill or circular button with WhatsApp icon and tooltip: *"Chat with Abhishek Wood Works"*.
- Strictly **no bouncing or annoying AI animations**. Respects user reading focus.

---

## 6. Performance, SEO & Accessibility (WCAG 2.2 AA)

1. **Performance (Target 90+ Lighthouse):**
   - Native lazy loading (`loading="lazy"`) and `decoding="async"` on all gallery images below the fold.
   - High-priority `fetchpriority="high"` for the Hero image.
   - Clean responsive image markup (`srcset` or optimized dimensions).
   - Zero heavy JavaScript frameworks; total JS bundle < 15KB.
2. **SEO & Structured Data:**
   - Accurate `<title>`: `Abhishek Wood Works | Custom Handcrafted Furniture & Interiors`
   - Meta description highlighting bespoke furniture, modular kitchens, wardrobes, and solid wood craftsmanship.
   - Open Graph tags (`og:title`, `og:description`, `og:image` pointing to `/assets/logo.jpg`).
   - Valid **Schema.org `LocalBusiness` / `HomeAndConstructionBusiness`** JSON-LD snippet with name, logo, telephone, address, and opening hours.
3. **Accessibility:**
   - Color contrast ratio exceeding 4.5:1 across all sections.
   - Distinct, visible `:focus-visible` styling with amber outline ring.
   - Meaningful, descriptive `alt` attributes on all 31 furniture images (no generic "image1.jpg" or blank alts).
   - Lightbox modal traps focus, manages `aria-expanded` and `aria-hidden`, and restores focus upon exit.
   - Full support for `@media (prefers-reduced-motion: reduce)`.

---

## 7. Assumptions & Clarifications for the User

1. **Contact Details:** Currently placeholder numbers (`+91 98765 43210`) are set in the configuration. The user can simply update `site-config.js` with their real phone number and WhatsApp number.
2. **Categories:** The 31 images were categorized into:
   - *Sofas & Seating*
   - *Dining*
   - *Wardrobes*
   - *Kitchens*
   - *Doors & Windows*
   - *TV Units & Partitions*
   - *Beds & Bedroom*
   These can be renamed or regrouped at any time via `site-config.js`.
3. **Hero Image Selection:** We propose using either the wide cinematic craftsman banner `777189214_1772764893764912_6432006908235877688_n.webp` or the landscape solid teak bench `1790507733748.jpg.jpeg` for the desktop hero background.
4. **Form Backend:** Default placeholder configured for Web3Forms/Formspree access key; the direct WhatsApp button works out of the box with zero external backend.

---

## 8. Implementation Phases (Will execute ONLY upon your signal)

- **Phase 1: Project Setup & Central Configuration**
  - Create `site-config.js` containing all metadata, phone/WhatsApp numbers, address, and the complete 31-item photo registry with titles and categories.
  - Create web-standard responsive favicon from `logo.jpg`.
- **Phase 2: HTML Skeleton & Styling Framework**
  - Scaffold semantic `index.html` with Tailwind setup, Google Fonts (`Cormorant Garamond` + `DM Sans`), and design tokens matching the logo palette.
- **Phase 3: Hero & Header Implementation**
  - Build transparent-to-solid sticky header with logo and mobile drawer.
  - Build high-impact hero section with direct gallery jump CTA.
- **Phase 4: Gallery & Interactive Lightbox**
  - Build category filter bar and natural aspect ratio masonry grid for all 31 images.
  - Implement full-screen lightbox with keyboard navigation, swipe gestures, and "Enquire about this piece" prefill trigger.
- **Phase 5: Story, Process, Form & Footer**
  - Craft the About section (first-person honest craftsman tone with workshop timber imagery).
  - Build the 4-step vertical timeline.
  - Implement the smart Enquiry Form (validation + Formspree/Web3Forms + direct WhatsApp builder).
  - Build Contact Footer and subtle floating WhatsApp trigger.
- **Phase 6: Quality Audit, Accessibility & Documentation**
  - Test responsive breakpoints (360px mobile, 768px tablet, 1440px desktop).
  - Verify WCAG 2.2 AA contrast and keyboard accessibility.
  - Create comprehensive `README.md` with instructions on customizing content, adding new photos, and deploying for free.
