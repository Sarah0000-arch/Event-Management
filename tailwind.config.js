/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",//template at project level 
    "./**/templates/**/*.html" //template at app level 
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

