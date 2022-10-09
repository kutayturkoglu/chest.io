const colors = require('tailwindcss/colors')

module.exports = {
    content: ["../templates/*.html","../templates/**/*.html"],
    theme: {
        colors: {
          transparent: 'transparent',
          current: 'currentColor',
          black: colors.black,
          white: colors.white,
          gray: colors.gray,
          emerald: colors.emerald,
          indigo: colors.indigo,
          yellow: colors.yellow,
          red: colors.red,
          blue: colors.blue,
          sky: colors.sky,
          green: colors.green
        },
        container: {
          center: true,
        },
      },
    plugins: [],
  }