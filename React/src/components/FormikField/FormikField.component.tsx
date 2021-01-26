import React from "react";
// Formik
import { Field, ErrorMessage } from "formik";
// UI Core
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";

interface FormikFieldProps {
    name: string;
    label: string;
    type?: string;
    required?: boolean;
}

const FormikField: React.FC<FormikFieldProps> = ({
    name,
    label,
    type = "text",
    required = false,
}) => {
    const useStyles = makeStyles({
        root: {
            margin: "10px 0px",
        },
    });
    const classes = useStyles();

    return (
        <div className={classes.root}>
            <Field
                required={required}
                autoComplete={`new-${label}`}
                as={TextField}
                label={label}
                fullWidth
                name={name}
                type={type}
                helperText={<ErrorMessage name={name} />}
            />
        </div>
    );
};

export default FormikField;
