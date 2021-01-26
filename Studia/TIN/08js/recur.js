const cached = (cache, fun) => {
    return n => {
        if (n in cache) {
            return cache[n];
        } else {
            let result = fun(n);
            cache[n] = result;
            return result;
        }
    };
};
