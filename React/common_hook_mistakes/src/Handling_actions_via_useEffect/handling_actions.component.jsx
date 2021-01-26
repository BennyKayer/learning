import React from "react";

export const DataListDangerous = ({ onSuccess }) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [data, setData] = useState(null);

    const fetchData = () => {
        setLoading(true);
        callApi()
            .then((res) => setData(res))
            .catch((err) => setError(err))
            .finally(() => setLoading(false));
    };

    useEffect(() => {
        fetchData();
    }, []);

    useEffect(() => {
        if (!loading && !error && data) {
            onSuccess();
        }
    }, [loading, error, data, onSuccess]);

    return <div>Data: {data}</div>;
};

export const DataListSolution = ({ onSuccess }) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [data, setData] = useState(null);

    const fetchData = () => {
        setLoading(true);
        callApi()
            .then((fetchedData) => {
                setData(fetchedData);
                onSuccess();
            })
            .catch((err) => setError(err))
            .finally(() => setLoading(false));
    };

    useEffect(() => {
        fetchData();
    }, []);

    return <div>{data}</div>;
};
