const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: './static/scss/index.scss',
    module: {
        rules: [
            {
                test: /\.scss$/i,
                use: [
                MiniCssExtractPlugin.loader,
                'css-loader',
                'sass-loader',
                ],
            },
        ],
    },
    
    plugins: [
        new MiniCssExtractPlugin({
        filename: 'index.css',
        }),
    ],
    output: {
        path: path.resolve(__dirname, 'static', 'css')
    },
    optimization: {
        minimize: false,
        splitChunks: false
    },
    devServer: {
        static: {
            directory: path.join(__dirname, 'static', 'css')
        },
        compress: true,
        port: 8081
    }
};