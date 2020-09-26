import React from "react";
import userEvent from "@testing-library/user-event";
import { render, screen, fireEvent } from "@testing-library/react";

import StateEventProps from "./state-event-props.component";

describe("StateEventProps", () => {
    test("renders without error", async () => {
        render(<StateEventProps />);

        await screen.findByText(/Signed in as/);
        // expect(screen.getByRole("textbox")).toBeInTheDocument();

        expect(screen.queryByText(/Searches for JavaScript/)).toBeNull();

        screen.debug();

        fireEvent.change(screen.getByRole("textbox"), {
            target: { value: "JavaScript" },
        });

        expect(
            screen.queryByText(/Searches for JavaScript/),
        ).toBeInTheDocument();

        screen.debug();
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
    test("User Event Example", async () => {
        render(<StateEventProps />);

        await screen.findByText(/Signed in as/);

        expect(screen.queryByText(/Searches for JavaScript/)).toBeNull();

        await userEvent.type(screen.getByRole("textbox"), "JavaScript");

        expect(screen.getByText(/Searches for JavaScript/)).toBeInTheDocument();
    });
});
