import React, { useState } from "react";
import "./App.css";

import Page1 from "./componenets/Page1";

const App = () => {
    const [route, setRoute] = useState("page1");
    const [Component, setComponent] = useState("");

    const onRouteChange = (route) => {
        if (route === "page1") {
            import("./componenets/Page1").then((Page1) => {
                setComponent(Page1.default);
                setRoute(route);
            });
        } else if (route === "page2") {
            // Dynamic import that works bcs of how webpack is set up in CRA
            // Well it doesn't anyway
            // But it should as it's build in
            import("./componenets/Page2").then((Page2) => {
                setComponent(Page2.default);
                setRoute(route);
            });
        } else if (route === "page3") {
            import("./componenets/Page3").then((Page3) => {
                setComponent(Page3.default);
                setRoute(route);
            });
        }
    };

    // return route === "page1" ? (
    //     <Page1 onRouteChange={onRouteChange} />
    // ) : route === "page2" ? (
    //     <Page2 onRouteChange={onRouteChange} />
    // ) : (
    //     <Page3 onRouteChange={onRouteChange} />
    // );
    return route === "page1" ? (
        <Page1 onRouteChange={onRouteChange} />
    ) : (
        <Component onRouteChange={onRouteChange} />
    );
};

// His shitty codesplitting with class component didn't work with hooks

export default App;
