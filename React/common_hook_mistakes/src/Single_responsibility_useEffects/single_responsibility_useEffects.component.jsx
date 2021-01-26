import React from "react";

export const ExampleDangerous = (props) => {
    const location = useLocation();

    const fetchData = () => {
        /*  Calling the api */
    };

    const updateBreadcrumbs = () => {
        /* Updating the breadcrumbs*/
    };

    useEffect(() => {
        fetchData();
        updateBreadcrumbs();
    }, [location.pathname]);

    return (
        <div>
            <BreadCrumbs />
        </div>
    );
};

export const ExampleSolution = (props) => {
    const location = useLocation();

    const updateBreadcrumbs = () => {
        /* Updating the breadcrumbs*/
    };

    useEffect(() => {
        updateBreadcrumbs();
    }, [location.pathname]);

    const fetchData = () => {
        /*  Calling the api */
    };

    useEffect(() => {
        fetchData();
    }, []);

    return (
        <div>
            <BreadCrumbs />
        </div>
    );
};
