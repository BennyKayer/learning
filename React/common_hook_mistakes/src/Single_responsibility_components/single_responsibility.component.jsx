import React from "react";

export const HeaderDangerous = ({ menuItems }) => {
    return (
        <header>
            <HeaderInner menuItems={menuItems} />
        </header>
    );
};

export const HeaderInnerDangerous = ({ menuItems }) => {
    return isMobile() ? (
        <BurgerButton menuItems={menuItems} />
    ) : (
        <Tabs tabData={menuItems} />
    );
};

export const HeaderSolution = (props) => {
    return (
        <header>
            {isMobile() ? (
                <BurgerButton menuItems={menuItems} />
            ) : (
                <Tabs tabData={menuItems} />
            )}
        </header>
    );
};
