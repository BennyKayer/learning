module.exports = {
    extends: [
        "react-app",
        "prettier",
        "plugin:testing-library/react",
        "plugin:jest-dom/recommended",
        "plugin:prettier/recommended",
        "prettier/react",
    ],
    plugins: ["prettier", "testing-library", "jest-dom", "simple-import-sort"],
    rules: {
        "prettier/prettier": "error",
        "sort-imports": "off",
        "import/order": "off",
        "simple-import-sort/sort": [
            "error",
            {
                groups: [
                    ["^\\u0000", "^react", "^\\w", "^@?\\w", "^[^.]", "^\\."],
                ],
            },
        ],
        "import/prefer-default-export": "error",
        "no-unused-vars": [
            "error",
            {
                argsIgnorePattern: "^_",
            },
        ],
        "no-console": [
            "error",
            {
                allow: ["info", "warn", "error"],
            },
        ],
        "react/prop-types": [
            "error",
            {
                skipUndeclared: true,
            },
        ],
    },
};
