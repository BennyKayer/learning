import React from "react";
import { render, screen } from "@testing-library/react";

import Content from "./Content";

describe("Content", () => {
    test("renders without error", () => {
        render(<Content />);

        // screen.debug();
    });
});
