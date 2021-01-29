import React, { useState, useEffect } from "react";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import SpeechRecognition, { useSpeechRecognition } from "react-speech-recognition";
import Fab from "@material-ui/core/Fab";
import MicOffIcon from "@material-ui/icons/MicOff";
import MicIcon from "@material-ui/icons/Mic";
import FormHelperText from "@material-ui/core/FormHelperText";
import Checkbox from "@material-ui/core/Checkbox";
import FormGroup from "@material-ui/core/FormGroup";

const Dictaphone = () => {
    const [value, setValue] = useState("female");
    const [state, setState] = React.useState({
        gilad: true,
        jason: false,
        antoine: false,
    });

    const handleVoiceValueChange = (gender) => {
        const acceptedGenders = ["female", "male", "other"];
        if (acceptedGenders.includes(gender.toLowerCase())) {
            setValue(gender);
        }
    };

    const handleVoiceChangeBox = (command, spokenPhrase, similarityRatio) => {
        console.log("command", command);
        console.log("spokenPhrase", spokenPhrase);
        console.log("similarityRatio", similarityRatio);
    };

    const commands = [
        {
            command: "gender *",
            callback: (gender) => handleVoiceValueChange(gender),
        },
        {
            command: "assign *",
            callback: (command, spokenPhrase, similarityRatio) =>
                handleVoiceChangeBox(command, spokenPhrase, similarityRatio),
            isFuzzyMatch: true,
            fuzzyMatchingThreshold: 0.2,
        },
        {
            command: "Stop listening",
            callback: () => SpeechRecognition.abortListening(),
        },
        {
            command: "reset",
            callback: () => resetTranscript(),
        },
    ];

    const { transcript, resetTranscript, listening, interimTranscript } = useSpeechRecognition({
        commands,
    });

    const browserSupported = SpeechRecognition.browserSupportsSpeechRecognition();

    const handleChange = (event) => {
        setValue(event.target.value);
    };

    const handleChangeCheckbox = (event) => {
        setState({ ...state, [event.target.name]: event.target.checked });
    };

    useEffect(() => {
        SpeechRecognition.startListening({
            continuous: true,
            language: "en-US",
        });
    }, []);

    useEffect(() => {
        console.log(interimTranscript);
    }, [interimTranscript]);
    const { gilad, jason, antoine } = state;
    return browserSupported ? (
        <div>
            <Fab
                color="primary"
                aria-label="add"
                onClick={
                    listening
                        ? SpeechRecognition.stopListening
                        : () =>
                              SpeechRecognition.startListening({
                                  continuous: true,
                                  language: "en-US",
                              })
                }
            >
                {listening ? <MicOffIcon /> : <MicIcon />}
            </Fab>
            <p>{transcript}</p>
            <FormControl component="fieldset">
                <FormLabel component="legend">Assign responsibility</FormLabel>
                <FormGroup>
                    <FormControlLabel
                        control={
                            <Checkbox
                                checked={gilad}
                                onChange={handleChangeCheckbox}
                                name="gilad"
                            />
                        }
                        label="Gilad Gray"
                    />
                    <FormControlLabel
                        control={
                            <Checkbox
                                checked={jason}
                                onChange={handleChangeCheckbox}
                                name="jason"
                            />
                        }
                        label="Jason Killian"
                    />
                    <FormControlLabel
                        control={
                            <Checkbox
                                checked={antoine}
                                onChange={handleChangeCheckbox}
                                name="antoine"
                            />
                        }
                        label="Antoine Llorca"
                    />
                </FormGroup>
            </FormControl>
            <FormControl component="fieldset">
                <FormLabel component="legend">Gender</FormLabel>
                <RadioGroup
                    aria-label="gender"
                    name="gender1"
                    value={value}
                    onChange={handleChange}
                >
                    <FormControlLabel value="female" control={<Radio />} label="Female" />
                    <FormControlLabel value="male" control={<Radio />} label="Male" />
                    <FormControlLabel value="other" control={<Radio />} label="Other" />
                </RadioGroup>
            </FormControl>
        </div>
    ) : (
        <div>
            <p>{"Your browser does not support web speech api"}</p>
        </div>
    );
};
export default Dictaphone;
