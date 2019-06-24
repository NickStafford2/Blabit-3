//'use strict'
const { VueLoaderPlugin } = require('vue-loader')
module.exports = {
  mode: 'development',
  entry: [
    './src/index.js'
  ],

  module: {
    rules: [
      {
          test: /\.vue$/,
          //exclude: /node_modules/,
          loader: 'vue-loader'
      },
      /*{
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
          loader: 'babel-loader'
          }
      }*/
      {
        test: /\/client\/.*\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              ['env']
            ]
          }
        }
      },
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      }
    ],
  },
  resolve: {
    alias: {
      vue: 'vue/dist/vue.js'
    }
  },
  plugins: [
    new VueLoaderPlugin()
  ]
}
