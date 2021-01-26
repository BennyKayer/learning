getBy - when elements should be there
queryBy - when elements shouldn't be there
findBy - when elements will be there eventually

What about multiple elements?
You have learned about the three search variants getBy, queryBy and findBy; which all can be associated with the search types (e.g. Text, Role, PlaceholderText, DisplayValue). If all of these search functions return only one element, how to assert if there are multiple elements (e.g. a list in a React component). All search variants can be extended with the All word:

getAllBy
queryAllBy
findAllBy

Assertive Functions
Assertive functions happen on the right hand-side of your assertion. In the previous tests, you have used two assertive functions: toBeNull and toBeInTheDocument. Both are primarily used in React Testing Library to check whether an element is present or not.

Usually all these assertive functions origin from Jest. However, React Testing Library extends this API with its own assertive functions like toBeInTheDocument. All these assertive functions come in an extra package which are already set up for you when using create-react-app.

toBeDisabled
toBeEnabled
toBeEmpty
toBeEmptyDOMElement
toBeInTheDocument
toBeInvalid
toBeRequired
toBeValid
toBeVisible
toContainElement
toContainHTML
toHaveAttribute
toHaveClass
toHaveFocus
toHaveFormValues
toHaveStyle
toHaveTextContent
toHaveValue
toHaveDisplayValue
toBeChecked
toBePartiallyChecked
toHaveDescription
