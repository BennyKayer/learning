import React from "react";
import { render, screen } from "@testing-library/react";

import StateEventProps from "./state-event-props.component";

describe("StateEventProps", () => {
    test("renders without error", async () => {
        render(<StateEventProps />);

        // screen.debug();
        expect(screen.getByRole("textbox")).toBeInTheDocument();
    });
    test("Search text present", async () => {
        render(<StateEventProps />);
        //Explicit
        // expect(screen.getByText("Search:")).toBeInTheDocument();
        // Implicit
        // screen.getByText("Search:");
        //REgex
        //expect(screen.getByText("/Search/")).toBeInTheDocument();

        // screen.debug();
        expect(screen.getByText("Search:")).toBeInTheDocument();
    });
    test("Shouldn't be there", async () => {
        render(<StateEventProps />);

        expect(screen.queryByRole("fuckbox")).toBeNull();
    });
    test("Async component", async () => {
        render(<StateEventProps />);

        expect(screen.queryByText(/Signed in as/)).toBeNull();
        expect(await screen.findByText(/Signed in as/)).toBeInTheDocument();
    });
});
