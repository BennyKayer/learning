The problem ⚡
There are two use cases, the "data-fetching" and "displaying breadcrumbs". Both are updated with an useEffect hook. This single useEffect hooks will run when the fetchData and updateBreadcrumbs functions or the location changes. The main problem is now, we also call the fetchData function when the location changes. This might be a side effect we haven't thought of.

The solution ✅
Splitting up the effect makes sure, they are only used for one effect and the unexpected side effects are gone.
