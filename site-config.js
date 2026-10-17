/**
 * Abhishek Wood Works - Central Site Configuration
 * 
 * Edit all business details, phone numbers, WhatsApp, categories, and copy here.
 * You do NOT need to touch HTML or CSS to update your business information.
 */
window.SITE_CONFIG = {
  business: {
    name: "Abhishek Wood Works",
    tagline: "Custom furniture and interiors, made to order.",
    description: "Handcrafted custom woodwork, bespoke furniture, and architectural interiors tailored to your space.",
    phone: "[TODO: Add your phone number, e.g. +91 98765 43210]",
    phoneClean: "919876543210", // Digits only with country code for tel: links
    whatsapp: "[TODO: Add your WhatsApp number, e.g. +91 98765 43210]",
    whatsappClean: "919876543210", // Digits only with country code for wa.me links
    email: "[TODO: Add your email, e.g. info@abhishekwoodworks.com]",
    address: "[TODO: Add workshop street address, city, pin code]",
    workingHours: "[TODO: Add working hours, e.g. Monday - Saturday: 9:00 AM - 7:30 PM]",
    mapEmbedUrl: "", // [TODO: Add Google Maps embed iframe URL if desired]
    formActionUrl: "https://api.web3forms.com/submit", // Form endpoint (Web3Forms / Formspree)
    formAccessKey: "[TODO: Add your Web3Forms or Formspree access key here]",
    social: {
      instagram: "[TODO: Add Instagram profile URL]",
      facebook: "[TODO: Add Facebook page URL]",
    }
  },

  hero: {
    heading: "Abhishek Wood Works",
    subheading: "Custom furniture and interiors, made to order.",
    ctaWork: "View Our Work",
    ctaQuote: "Get a Quote",
    image: "assets/optimized/hero_1400w.webp",
    imageSrcset: "assets/optimized/hero_800w.webp 800w, assets/optimized/hero_1400w.webp 1400w, assets/optimized/hero_2048w.webp 2048w"
  },

  categories: [
    { id: "Sofas & Seating", label: "Sofas & Seating", shortLabel: "Sofas", slug: "sofas" },
    { id: "Dining", label: "Dining", shortLabel: "Dining", slug: "dining" },
    { id: "Wardrobes", label: "Wardrobes", shortLabel: "Wardrobes", slug: "wardrobes" },
    { id: "Kitchens", label: "Kitchens", shortLabel: "Kitchens", slug: "kitchens" },
    { id: "Doors & Windows", label: "Doors & Windows", shortLabel: "Doors", slug: "doors" },
    { id: "TV Units & Partitions", label: "TV Units & Partitions", shortLabel: "TV Units", slug: "tv-units" },
    { id: "Beds & Bedroom", label: "Beds & Bedroom", shortLabel: "Beds", slug: "beds" }
  ],

  about: {
    heading: "Crafted by Hand, Built to Last",
    subheading: "Direct from the workshop to your home",
    founderPhotoPlaceholder: "[TODO: Insert Owner/Craftsman Workshop Photo]",
    timberPhoto: "assets/optimized/timber_1000w.webp",
    paragraphs: [
      "We make custom furniture the way it should be made: built to the exact dimensions of your home, using solid timber and quality fittings.",
      "Every piece you see in our gallery was commissioned by a client and crafted in our workshop. We do not sell mass-produced flat-pack furniture. When you work with us, you speak directly with the people shaping the wood.",
      "[TODO: Add your story here — when you started Abhishek Wood Works, your years of experience, and your background in carpentry.]",
      "[TODO: List the specific types of timber and board materials you specialize in, e.g. Seasoned Teak, Hardwood, Commercial/Marine Plywood, and selected veneers.]"
    ],
    materialsNotice: "All wood is inspected for grain, moisture, and structural stability before cutting begins."
  },

  process: {
    heading: "How We Work",
    subheading: "A straightforward, honest process from your first sketch to final installation.",
    steps: [
      {
        number: "01",
        title: "Share Your Idea",
        description: "Send us a photo, a rough sketch, or pick an item from our gallery. Tell us what space you have and what you need it to do."
      },
      {
        number: "02",
        title: "Site Visit & Measuring",
        description: "[TODO: Describe your measurement process] — We inspect the site, take accurate measurements of your space, and discuss suitable wood choices."
      },
      {
        number: "03",
        title: "Design & Estimate",
        description: "We provide design layouts, discuss timber and finish options, and give you an honest quote with clear material specifications."
      },
      {
        number: "04",
        title: "Build & Installation",
        description: "Your furniture is built in our workshop, pre-fitted to verify joinery, delivered to your site, and installed cleanly."
      }
    ]
  },

  enquiry: {
    heading: "Discuss Your Project",
    subheading: "Tell us what you want built. We'll review your dimensions and get back to you with an honest quote.",
    needOptions: [
      "Bed / Bedroom Set",
      "Wardrobe & Storage",
      "Sofa / Living Seating",
      "Dining Table & Chairs",
      "Modular Kitchen",
      "Doors & Architectural",
      "TV Unit / Room Partition",
      "Full Home Woodwork & Interiors",
      "Other Custom Woodwork"
    ],
    budgetOptions: [
      "Flexible / To be discussed based on design",
      "Under ₹50,000",
      "₹50,000 - ₹1,50,000",
      "₹1,50,000 - ₹3,00,000",
      "₹3,00,000+"
    ],
    timelineOptions: [
      "Immediately / As soon as possible",
      "Within 1 month",
      "Within 2 - 3 months",
      "Planning ahead / Just exploring ideas"
    ],
    photoNote: "Have reference photos or room sketches? Submit this form or click the WhatsApp button to send them directly to our chat."
  }
};
