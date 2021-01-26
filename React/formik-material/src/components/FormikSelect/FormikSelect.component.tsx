import React, { ReactNode } from "react";
import { Field, ErrorMessage, FieldInputProps } from "formik";
import { makeStyles } from "@material-ui/core/styles";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";

export interface FormikSelectItems {
    label: string;
    value: string;
}

interface FormikSelectProps {
    items: FormikSelectItems[];
    label: string;
    name: string;
    required: boolean;
}

interface MaterialUISelectFieldProps extends FieldInputProps<string> {
    errorString?: string;
    children: ReactNode;
    label: string;
    required?: boolean;
}

const MaterialUISelectField: React.FC<MaterialUISelectFieldProps> = ({
    errorString,
    label,
    children,
    value,
    name,
    onChange,
    onBlur,
    required,
}) => {
    return (
        <FormControl variant="outlined" fullWidth>
            <InputLabel required={required}>{label}</InputLabel>
            <Select
                name={name}
                onChange={onChange}
                onBlur={onBlur}
                value={value}
            >
                {children}
            </Select>
            <FormHelperText>{errorString}</FormHelperText>
        </FormControl>
    );
};

const FormikSelect: React.FC<FormikSelectProps> = ({
    name,
    items,
    label,
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
                name={name}
                as={MaterialUISelectField}
                label={label}
                errorString={<ErrorMessage name={name} />}
                required={required}
            >
                {items.map((item) => (
                    <MenuItem value={item.value} key={item.value}>
                        {item.label}
                    </MenuItem>
                ))}
            </Field>
            {/* <MaterialUISelectField errorString="Incorrect!" label={label}>
                {items.map((item) => (
                    <MenuItem value={item.value} key={item.value}>
                        {item.label}
                    </MenuItem>
                ))}
            </MaterialUISelectField> */}
        </div>
    );
};

export default FormikSelect;
