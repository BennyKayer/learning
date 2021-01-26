import React, { Fragment } from "react";
import {
    UnnecesaryRerender,
    NoRerender,
} from "./Using_useState_when_no_rerender_is_needed/no_rerender.component";
import {
    RouterDangerous,
    RouterSolution,
} from "./Using_router.push_instead_of_link/router_issues.component";

const Content = () => {
    return (
        <Fragment>
            <h1>{"Unnecessary re-render"}</h1>
            <UnnecesaryRerender />
            <br />
            <h1>{"Preventing re-render by using ref"}</h1>
            <NoRerender />
            <br />
            <RouterDangerous />
            <br />
            <RouterSolution />
            <br />
        </Fragment>
    );
};

export default Content;
