# Chrome extensions with React

`@babel/core` translates into plain JS.
`@babel/preset-react` is for transpiring JSX to normal JS.
`@babel/preset-env` transpiring ES6 into ES5 etc.
`babel-loader` allows webpack to use Babel core.
`@babel/plugin-proposal-class-properties` how to transpire class components.
`clean-webpack-plugin` deletes before building (no duplicates etc.).
`copy-webpack-plugin` copy stuff as it is, don't minify etc. needed for manifest `inject_script` and `index-popup`.
`html-loader` tells `babel-loader` how to deal with HTML files.
`html-webpack-plugin` export HTML files.

## In Google Docs, they call foreground script a content script

## Commands

`npm run build` — build and starts development server
