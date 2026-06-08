/** @type {import('tailwindcss').Config} */
const path = require('path')
module.exports = {
  content: [
    path.join(__dirname, '../../**/templates/**/*.html'),
    path.join(__dirname, '../../**/templates/*.html'),
    path.join(__dirname, '../../**/*.html'),
    path.join(__dirname, '../../**/*.py'),
  ],

  theme: {
    extend: {},
  },

  plugins: [],
}