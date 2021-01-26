The problem ⚡
With this approach the component HeaderInner is trying to be two different things at once and we all learned from Mr. Jekyll, being more than one thing at a time isn't really ideal. Also it makes it even harder to test or to reuse the component in other places.

The solution ✅
Bringing the condition one level up, makes it easier to see what the components are made for and that they only have one responsibility, being a Header, Tabs or a BurgerButton and not trying to be two things at once.
