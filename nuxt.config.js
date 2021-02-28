export default {
  mode: 'spa',
  target: 'server',
  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || 'Botimzozli',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || '',
      },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: [],
  /*
   ** Plugins to load before mounting the App
   */

  plugins: [{ src: '~/plugins/lingallery', ssr: false }],
  /*
   ** Nuxt.js modules
   */
  modules: [ "@nuxtjs/axios", "@nuxtjs/cloudinary"  ],

  cloudinary: {
    cloudName: process.env.CLOUDNAME,
    /* all other options */
  },

  env: {
    CLOUDNAME: process.env.CLOUDNAME,
    API_KEY: process.env.API_KEY,
    API_SECRET: process.env.API_SECRET
  },


  axios: {
    credentials: false
  },
  /*
   ** Build configuration
   */
  build: {
    babel: {
      presets({isServer}) {
        const targets = isServer ? { node: 'current' } : { ie: 11 }
        return [
          [ require.resolve("@babel/preset-env"), { targets }  ]
        ]
      },
      plugins: [
        "@babel/syntax-dynamic-import",
        "@babel/transform-runtime",
        "@babel/transform-async-to-generator"
      ]

    // extend(config, ctx) {}
  }
}
}
