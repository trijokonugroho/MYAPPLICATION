const path = require('path');

module.exports = {
    mode: 'development',
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'static/frontend'),
        filename: 'main.js',
    },
    watch: true,
    module: {
        rules: [
            {
                test: /\.(jsx|js)$/,
                include: path.resolve(__dirname, 'src'),
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            ['@babel/preset-env', { 'targets': 'defaults' }],
                            ['@babel/preset-react', { 'runtime': 'automatic' }]
                        ]
                    }
                }
            }
        ]
    }
}