import actionTypes from "./actionTypes";
// redux-thunk
import {
    REQUEST_ROBOTS_PENDING,
    REQUEST_ROBOTS_SUCCESS,
    REQUEST_ROBOTS_FAIL,
} from "./constants";

export const setSearchField = (text) => ({
    type: actionTypes.CHANGE_SEARCH_FIELD,
    payload: text,
});

// redux-thunk
export const requestRobots = () => (dispatch) => {
    dispatch({ type: REQUEST_ROBOTS_PENDING });
    fetch("https://jsonplaceholder.typicode.com/users")
        .then((response) => response.json())
        .then((data) =>
            dispatch({ type: REQUEST_ROBOTS_SUCCESS, payload: data })
        )
        .catch((error) =>
            dispatch({ type: REQUEST_ROBOTS_FAIL, payload: error })
        );
};
