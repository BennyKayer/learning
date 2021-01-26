import React from "react";
import { useHistory, Link } from "react-router-dom";

export const RouterDangerous = () => {
    const history = useHistory();

    const handleRedirect = () => {
        history.push("/some_page");
    };

    return (
        <button onClick={handleRedirect}>Go to next page - dangerous</button>
    );
};

export const RouterSolution = () => {
    return (
        <Link to="/some_page">
            <span>Go to next page - solution</span>
        </Link>
    );
};
