import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

const SignInSchema = Yup.object().shape({
    email: Yup.string()
        .required("This field is required")
        .email("Must be a valid email"),
    password: Yup.string()
        .required("This field is required")
        .min(8, "Must be at least 8 characters long")
});

function App() {
    const handleSubmit = (values: any) => {
        console.log(`Email: ${values.email} Password: ${values.password}`);
    };

    return (
        <div className="App">
            <Formik
                initialValues={{ email: "", password: "" }}
                onSubmit={handleSubmit}
                validationSchema={SignInSchema}
            >
                {({ handleReset, isValid, dirty }) => (
                    <Form>
                        <div>
                            <label htmlFor="email">Email: </label>
                            <Field autoComplete="off" name="email" />
                            <ErrorMessage name="email" />
                        </div>
                        <div>
                            <label htmlFor="password">Password: </label>
                            <Field autoComplete="off" name="password" />
                            <ErrorMessage name="password" />
                        </div>
                        <button disabled={!isValid || !dirty} type="submit">
                            Submit
                        </button>
                        <button type="reset">Reset</button>
                        {/* <button onClick={handleReset} type="button">
                            Reset
                        </button> */}
                    </Form>
                )}
            </Formik>
        </div>
    );
}

export default App;
