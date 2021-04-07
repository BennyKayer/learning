# Code Splitting

https://reactjs.org/docs/code-splitting.html

## PAGE BASED CHUNKING

Route based easy stuff

## COMPONENT BASED CHUNKING

Homepage huge delay slides that are unlikely to show

## React Lazy

Does not work in SSR  
Does not work with Named Exports — you'll have to do the re-export

## React Performance

AVOID BLOCKING MAIN THREAD
type ?react_perf after URL note that production is always faster  
Basic stuff split into components
if shouldComponentUpdate on class components always returns false it WON'T EVER RE-RENDER
extending PureComponent will cause component to only re-render if the props have changed, it uses shallow comparison
`https://www.npmjs.com/package/@welldone-software/why-did-you-render` — shows why stuff re-rendered

## React Dev Tools

The more component re-renders the more it's frame turns RED  
The less = they are closer to blue

# Tree Shaking

Removing unnecessary code — mainly done by webpack, importing huge library only using 1 function will probably remove 999 other functions from the library though it is not 100% accurate

# Other stuff

Avoid Memory Leaks — cleanup event listeners that aren't hooked up etc.
Avoid Multiple re-rendering — shouldComponentUpdate would help with that, but I actually think that by using hooks this have been mostly mitigated
