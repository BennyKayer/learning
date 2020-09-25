import React from "react";
import { render, screen } from "@testing-library/react";

import StateEventProps from "./state-event-props.component";

describe("StateEventProps", () => {
    test("renders without error", () => {
        render(<StateEventProps />);

        screen.debug();
    });
});
