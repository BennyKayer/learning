const createBuffer = () => {
    // String też jest obiektem
    let buff = "";
    const buffer = (text = "") => {
        if (text.length === 0) {
            return buff;
        }
        buff += text;
    };
    return buffer;
};
