import React from "react";
import "./App.css";
import { Formik, Form } from "formik";
import * as Yup from "yup";
import Button from "@material-ui/core/Button";
// Components
import FormikField from "../FormikField/FormikField.component";
import FormikSelect, {
    FormikSelectItems,
} from "../FormikSelect/FormikSelect.component";

interface FormValues {
    name: string;
    position: string;
    email: string;
    password: string;
    passwordConfirm: string;
}

const initialValues: FormValues = {
    name: "",
    position: "",
    email: "",
    password: "",
    passwordConfirm: "",
};

const positionItems: FormikSelectItems[] = [
    {
        label: "Front End",
        value: "front_end",
    },
    {
        label: "Back End",
        value: "back_end",
    },
    {
        label: "Dev Ops",
        value: "dev_ops",
    },
    {
        label: "UX Designer",
        value: "ux_designer",
    },
];

const emailAdresses = ["test@gmail.com", "test2@gmail.com"];

const lowercaseRegex = /(?=.*[a-z])/;
const uppercaseRegex = /(?=.*[A-Z])/;
const numericRegex = /(?=.*[0-9])/;

const SignUpSchema = Yup.object().shape({
    name: Yup.string().min(2, "Too Short").required("Required"),
    position: Yup.string().required("Required"),
    email: Yup.string()
        .lowercase()
        .email("Must be a valid email")
        .notOneOf(emailAdresses, "Email already taken")
        .required("Required"),
    password: Yup.string()
        .matches(lowercaseRegex, "Must include lowercase letter")
        .matches(uppercaseRegex, "Must include UPPERCASE letter")
        .matches(numericRegex, "Must include at least 1 number")
        .min(8, "Minimum 8 characters")
        .required("Required"),
    passwordConfirm: Yup.string()
        .oneOf([Yup.ref("password")], "Passwords must match")
        .required("Required"),
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
                        <Form autoComplete="off">
                            <FormikField label="Name" name="name" required />
                            <FormikField
                                label="Email"
                                name="email"
                                type="email"
                                required
                            />
                            <FormikField
                                label="Password"
                                name="password"
                                type="password"
                                required
                            />

                            <FormikField
                                label="Confirm Password"
                                name="passwordConfirm"
                                type="password"
                                required
                            />

                            <FormikSelect
                                items={positionItems}
                                label="Position"
                                name="position"
                                required
                            />

                            <Button
                                disabled={!isValid || !dirty}
                                type="submit"
                                variant="outlined"
                            >
                                Submit
                            </Button>
                        </Form>
                    );
                }}
            </Formik>
        </div>
    );
};

export default App;
