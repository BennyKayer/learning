The problem ⚡
At first sight, you might ask what exactly is the problem with that? Isn't that what state was made for? Sure you are right, this will work just fine and probably there will never be a problem with that. However in react every state change will force a rerender for that component and most likely its children. But in the above example since we never use that state in our render part, this will end up being an unnecessary render every time we set the counter, which can impact the performance or could have unexpected side effects.

The solution ✅
If you want to use a variable inside your component which should keep its value between rendering but also don't force a rerender, you can use the useRef hook. It will keep the value, but doesn't force the component to rerender.
