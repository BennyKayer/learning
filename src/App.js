import React from "react";
import "./App.css";
import Content from "./Content";
import { Route, Switch, Link } from "react-router-dom";

const SomePage = () => {
    return (
        <div>
            <h1>Welcome to some page</h1>
            <Link to="/">
                <span>Go back</span>
            </Link>
        </div>
    );
};

const App = () => {
    return (
        <Switch>
            <Route exact path="/" component={Content} />
            <Route exact path="/some_page" component={SomePage} />
        </Switch>
    );
};

export default App;
