var webpack = require('webpack');
var clean = require('clean-webpack-plugin');
var autoprefixer = require('autoprefixer');


var path = require('path');

/**
 * Base configuration
 */
config = {

    entry: './assets/index.js',

    //devtool: 'source-map',

    output: {
        filename: 'js/bundle.js',
        path: path.resolve(__dirname, "dist"),
        publicPath: "/static/"
    },

    module: {
        loaders: [
            /// Collect all js files
            {
                test: /\.jsx?$/,
                loader: 'ng-annotate?add=true!babel',
                include: [
                    path.resolve(__dirname, "assets/")
                ]
            },
            // Collect all LESS files
            {
                test: /\.scss$/,
                loaders: ["style", "css", "sass"]
            },
            // Base64 encode images in less
            {
                test: /\.(png|jpg|jpeg|gif|woff)$/,
                loader: 'url-loader?limit=8192'
            }, {
                test: /\.html$/,
                exclude: /node_modules/,
                loader: 'raw'
            }
        ]
    },

    // Add autoprefixer
    postcss: [autoprefixer({
        browsers: ['last 2 versions']
    })],

    plugins: [
        // Clean all files from dist
        new clean(['dist']),

        // Shims
        new webpack.ProvidePlugin({
            $: "jquery",
        }),
    ],
};

module.exports = config;