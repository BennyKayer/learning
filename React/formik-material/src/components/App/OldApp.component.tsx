import React from "react";
import "./App.css";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

interface FormValues {
    name: string;
    position: string;
}

const initialValues: FormValues = {
    name: "",
    position: ""
};

const SignUpSchema = Yup.object().shape({
    name: Yup.string()
        .min(2, "Too Short")
        .required("required"),
    position: Yup.string().required("required")
});

const App: React.FC = () => {
    const handleSubmit = (values: FormValues): void => {
        alert(JSON.stringify(values));
    };

    return (
        <div className="app">
            <h1>Sign Up</h1>
            <Formik
                initialValues={initialValues}
                onSubmit={handleSubmit}
                validationSchema={SignUpSchema}
            >
                {({ dirty, isValid }) => {
                    return (
                        <Form>
                            <div>
                                <label htmlFor="name">Name: </label>
                                <Field
                                    autoComplete="off"
                                    name="name"
                                    as="input"
                                />
                                <ErrorMessage name="name" />
                            </div>
                            <div>
                                <label htmlFor="position">Position: </label>
                                <Field
                                    name="position"
                                    as="select"
                                    placeholder="Choose your position"
                                >
                                    <option value="">...</option>
                                    <option value="frontEnd">Front End</option>
                                    <option value="backEnd">Back End</option>
                                    <option value="devOps">Dev Ops</option>
                                </Field>
                                <ErrorMessage name="position" />
                            </div>

                            <button disabled={!isValid || !dirty} type="submit">
                                Submit
                            </button>
                        </Form>
                    );
                }}
            </Formik>
        </div>
    );
};

export default App;
