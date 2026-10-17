/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./site-config.js",
    "./js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        walnut: {
          50: '#FDF9F6',
          100: '#F8EFE9',
          200: '#EED9CC',
          300: '#DEC0AA',
          700: '#5E3822',
          800: '#4A2C1A',
          900: '#382115',
          950: '#2B1A12',
        },
        cream: {
          50: '#FCF9F3',
          100: '#FAF5EC',
          200: '#F1E3C8',
          300: '#E4CFAB',
          400: '#D5BC8F',
        },
        amber: {
          accent: '#D98B2B',
          hover: '#C2761B',
          subtle: '#F6E6D0',
        },
        wood: {
          black: '#0E0A08',
          dark: '#17110E',
          card: '#1F1713',
        }
      },
      fontFamily: {
        serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        sans: ['"DM Sans"', 'system-ui', '-apple-system', 'sans-serif'],
      },
      letterSpacing: {
        widest: '.2em',
      }
    },
  },
  plugins: [],
}
