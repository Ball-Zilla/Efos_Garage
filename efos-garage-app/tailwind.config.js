/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}", "./public/**/*.{html,js}"],
  theme: {
    extend: {
      base: {
        'font-family': 'Inter, sans-serif',
      },
      krona: {
        'font-family': 'Krona One, sans-serif',
      },
    },
  },
  plugins: [],
}

