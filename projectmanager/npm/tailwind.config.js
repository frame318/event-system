/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  content: [
    "../templates/**/*.{html,js,css}",
    "../templates/*.{html,js,css}",
    "./templates/**/*.{html,js,css}",
    "./templates/*.{html,js,css}",
    "./node_modules/flowbite/**/*.js",
    '../node_modules/flowbite/**/*.js'
    // "../member/forms.py",
  ],
  theme: {
    
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('flowbite-typography'),
    require('flowbite/plugin'),
  ],
}
