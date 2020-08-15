import actionTypes from './actionTypes'

export const setSearchField = text => ({
    type: actionTypes.CHANGE_SEARCH_FIELD,
    payload: text
})
