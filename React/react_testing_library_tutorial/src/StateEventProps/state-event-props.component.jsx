import React, { useState, useEffect } from "react";

const StateEventProps = () => {
    const [search, setSearch] = useState("");
    const [user, setUser] = useState(null);

    useEffect(() => {
        const loadUser = async () => {
            const user = await getUser();
            setUser(user);
        };
        loadUser();
    }, []);

    const getUser = () => {
        return Promise.resolve({ id: "1", name: "Robin" });
    };
    const handleChange = (event) => {
        setSearch(event.target.value);
    };

    return (
        <div>
            {user ? <p>Signed in as {user.name}</p> : null}
            <Search value={search} onChange={handleChange}>
                {"Search:"}
            </Search>
            <p>Searches for {search ? search : "..."}</p>
        </div>
    );
};

export const Search = ({ value, onChange, children }) => {
    return (
        <div>
            <label htmlFor="search">{children}</label>
            <input id="search" type="text" value={value} onChange={onChange} />
        </div>
    );
};

export default StateEventProps;
