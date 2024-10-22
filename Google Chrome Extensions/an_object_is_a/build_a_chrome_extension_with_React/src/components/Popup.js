import React from "react";
import HorizontalCarousel from "./HorizontalCarousel.js";

const App = () => {
    return (
        <div style={styles.main}>
            <h1>Chrome Ext - Popup</h1>
            <HorizontalCarousel />
        </div>
    );
};

const styles = {
    main: {
        width: "300px",
        height: "600px",
    },
};

export default App;
