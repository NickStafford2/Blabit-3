'use strict'
const { VueLoaderPlugin } = require('vue-loader')
module.exports = {
  mode: 'production',
  entry: [
    './src/index.js'
  ],
  module: {
    rules: [
      {
          test: /\.vue$/,
          exclude: /node_modules/,
          loader: 'vue-loader'
      },
      {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
          loader: 'babel-loader'
          }
      }
    ],
  },
  plugins: [
    new VueLoaderPlugin()
  ]
}
