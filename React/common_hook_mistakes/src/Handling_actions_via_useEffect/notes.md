The problem ⚡
There are two useEffect hooks, the first one is handling the api call on the initial render and the second one will call the onSuccess function, by assuming when there is no loading, no error, but data in the state, it must have been a successful call. Makes sense right?

Sure for the first call this is true and probably will never fail. But you also loose the direct connection between the action and the function that needs to be called. There is no guarantee that this case will only happen if the fetch action has succeeded and this is something we as developers really don't like.

The solution ✅
A straight forward solution would be to set the "onSuccess" function to the actual place where the call was successful:
