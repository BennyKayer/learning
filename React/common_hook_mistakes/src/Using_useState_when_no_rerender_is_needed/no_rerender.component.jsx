import React, { useState, useRef } from "react";

export const UnnecesaryRerender = () => {
    const [count, setCount] = useState(0);

    const handleCounter = () => {
        setCount(count + 1);
    };

    const handleRequest = () => {
        console.log("Faking api call: ", count);
    };

    return (
        <div>
            <button onClick={handleCounter}>Counter</button>
            <button onClick={handleRequest}>Submit</button>
        </div>
    );
};

export const NoRerender = () => {
    const count = useRef(0);

    const handleCounter = () => {
        count.current++;
    };

    const handleRequest = () => {
        console.log("Faking api call: ", count.current);
    };

    return (
        <div>
            <button onClick={handleCounter}>Counter</button>
            <button onClick={handleRequest}>Submit</button>
        </div>
    );
};
