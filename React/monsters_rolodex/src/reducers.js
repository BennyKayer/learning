import {
    actionTypes,
    REQUEST_ROBOTS_PENDING,
    REQUEST_ROBOTS_SUCCESS,
    REQUEST_ROBOTS_FAIL,
} from "./constants";

const initialState = {
    searchField: "",
};

export const searchRobots = (state = initialState, action = {}) => {
    switch (action.type) {
        case actionTypes.CHANGE_SEARCH_FIELD:
            return Object.assign({}, state, { searchField: action.payload });
        default:
            return { ...state };
    }
};

const initialStateRequest = {
    isPending: false,
    robots: [],
    error: "",
};

export const requestRobots = (state = initialStateRequest, action = {}) => {
    switch (action.type) {
        case REQUEST_ROBOTS_PENDING:
            return Object.assign({}, state, { isPending: true });
        case REQUEST_ROBOTS_SUCCESS:
            return Object.assign({}, state, {
                robots: action.payload,
                isPending: false,
            });
        case REQUEST_ROBOTS_FAIL:
            return Object.assign({}, state, {
                error: action.payload,
                isPend: false,
            });
        default:
            return state;
    }
};
