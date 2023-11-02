import React, { useEffect, useState } from 'react';
import Page from './page';
import { MDBBtn } from 'mdbreact';
import { Card, Col, Container, Row } from 'react-bootstrap';


export default function Main({displays, setDisp, setShowResult, showResult}){
    const symp =  {'itching': '1', 'skin_rash': '1', 'nodal_skin_eruptions': '1', 'continuous_sneezing': '1', 'shivering': '1', 'chills': '1', 'joint_pain': '1', 'stomach_pain': '1', 'acidity': '1', 'ulcers_on_tongue': '1', 'muscle_wasting': '1', 'vomiting': '1', 'burning_micturition': '1', 'spotting_urination': '1', 'fatigue': '1', 'weight_gain': '1', 'anxiety': '1', 'cold_hands_and_feets': '1', 'mood_swings': '1', 'weight_loss': '1', 'restlessness': '1', 'lethargy': '1', 'patches_in_throat': '1', 'irregular_sugar_level': '1', 'cough': '1', 'high_fever': '1', 'sunken_eyes': '1', 'breathlessness': '1', 'sweating': '1', 'dehydration': '1', 'indigestion': '1', 'headache': '1', 'yellowish_skin': '1', 'dark_urine': '1', 'nausea': '1', 'loss_of_appetite': '1', 'pain_behind_the_eyes': '1', 'back_pain': '1', 'constipation': '1', 'abdominal_pain': '1', 'diarrhoea': '1', 'mild_fever': '1', 'yellow_urine': '1', 'yellowing_of_eyes': '1', 'acute_liver_failure': '1', 'swelling_of_stomach': '1', 'swelled_lymph_nodes': '1', 'malaise': '1', 'blurred_and_distorted_vision': '1', 'phlegm': '1', 'throat_irritation': '1', 'redness_of_eyes': '1', 'sinus_pressure': '1', 'runny_nose': '1', 'congestion': '1', 'chest_pain': '1', 'weakness_in_limbs': '1', 'fast_heart_rate': '1', 'pain_during_bowel_movements': '1', 'pain_in_anal_region': '1', 'bloody_stool': '1', 'irritation_in_anus': '1', 'neck_pain': '1', 'dizziness': '1', 'cramps': '1', 'bruising': '1', 'obesity': '1', 'swollen_legs': '1', 'swollen_blood_vessels': '1', 'puffy_face_and_eyes': '1', 'enlarged_thyroid': '1', 'brittle_nails': '1', 'swollen_extremeties': '1', 'excessive_hunger': '1', 'extra_marital_contacts': '1', 'drying_and_tingling_lips': '1', 'slurred_speech': '1', 'knee_pain': '1', 'hip_joint_pain': '1', 'muscle_weakness': '1', 'stiff_neck': '1', 'swelling_joints': '1', 'movement_stiffness': '1', 'spinning_movements': '1', 'loss_of_balance': '1', 'unsteadiness': '1', 'weakness_of_one_body_side': '1', 'loss_of_smell': '1', 'bladder_discomfort': '1', 'foul_smell_of_urine': '1', 'continuous_feel_of_urine': '1', 'passage_of_gases': '1', 'internal_itching': '1', 'toxic_look_(typhos)': '1', 'depression': '1', 'irritability': '1', 'muscle_pain': '1', 'altered_sensorium': '1', 'red_spots_over_body': '1', 'belly_pain': '1', 'abnormal_menstruation': '1', 'dischromic_patches': '1', 'watering_from_eyes': '1', 'increased_appetite': '1', 'polyuria': '1', 'family_history': '1', 'mucoid_sputum': '1', 'rusty_sputum': '1', 'lack_of_concentration': '1', 'visual_disturbances': '1', 'receiving_blood_transfusion': '1', 'receiving_unsterile_injections': '1', 'coma': '1', 'stomach_bleeding': '1', 'distention_of_abdomen': '1', 'history_of_alcohol_consumption': '1', 'fluid_overload': '1', 'blood_in_sputum': '1', 'prominent_veins_on_calf': '1', 'palpitations': '1', 'painful_walking': '1', 'pus_filled_pimples': '1', 'blackheads': '1', 'scurring': '1', 'skin_peeling': '1', 'silver_like_dusting': '1', 'small_dents_in_nails': '1', 'inflammatory_nails': '1', 'blister': '1', 'red_sore_around_nose': '1', 'yellow_crust_ooze': '1', 'prognosis': '1'}
    const [symptoms, setSymptoms] = useState([]);
    const [resultant, setResult] = useState({});
    const nextClicked = () => {
        var a = [];
        var b = false;
        for (var i = 0; i < 13; i++){
            if (displays[i] === "block"){
                a[i] = "none";
                b = true;
            }
            else if (b){
                b = false;
                a[i] = "block";
            }
            else{
                a[i] = displays[i];
            }
        }
        console.log(displays);
        console.log(a);
        setDisp(a);
    }
    const backClicked = () => {
        var a = [];
        var b = false;
        for (var i = 0; i < 13; i++){
            if (displays[i] === "block"){
                a[i] = "none";
                a[i-1] = "block";
            }
            else{
                a[i] = displays[i];
            }
        }
        // print(a);
        setDisp(a);
    }
    const submit = () => {
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var dict = {"symptoms": symptoms};

        fetch('/', {
                method: 'POST', // or 'PUT'
                headers: {
                    'Content-Type': 'application/json',
            },
                body: JSON.stringify(dict),
                mode:"no-cors"
        })
        .then(response => {
            console.log(response);
            return response.json()
        })
        .then((data) => {
            console.log(data);
            setResult(data);
            setShowResult(true);
        })
            .catch((error) => {
            console.log("Error")
            console.log(error)
        })
    }
    if (showResult){
        return(
            <>
            <div style={{float: 'left', marginRight: '100px', "height": '500px', visibility: 'hidden'}}>abcd</div>
            <Container>
                <Row>
                    <Col xs="6">
                        <Card >
                            <Card.Body>
                                <Card.Title>{resultant.result.dt.disease}</Card.Title>
                                <Card.Subtitle className="mb-2 text-muted">Decision Tree Result</Card.Subtitle>
                                <Card.Text>{resultant.result.dt.desc}</Card.Text>
                                <Card.Text>
                                    <h4>Precautions:</h4>
                                    <ul>
                                    {resultant.result.dt.prec.map(val => <li key={val}>{val}</li>)}
                                    </ul>
                                </Card.Text>
                                <Card.Link href="/">Check for other symptoms!</Card.Link>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col xs="6">
                        <Card >
                            <Card.Body>
                                <Card.Title>{resultant.result.nb.disease}</Card.Title>
                                <Card.Subtitle className="mb-2 text-muted">Naive Bayes Result</Card.Subtitle>
                                <Card.Text>{resultant.result.nb.desc}</Card.Text>
                                <Card.Text>
                                    <h4>Precautions:</h4>
                                    <ul>
                                        {resultant.result.nb.prec.map(val => <li key={val}>{val}</li>)}
                                    </ul>
                                </Card.Text>
                                <Card.Link href="/">Check for other symptoms!</Card.Link>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
            </>
        );
    }
    else{
        return(
            <>
            <div style={{float: 'left', marginRight: '100px', "height": '500px', visibility: 'hidden'}}>Page No. {symptoms.indexOf("block")+1}/ 13</div>
            <div className="text-white">
                {displays.map((v, inn) => <Page symptoms={symp} display={displays[inn]} pageNum={inn} selectedSymp={symptoms} setSymptoms={setSymptoms} />)}

                <div style={{marginLeft: "390px"}}>
                    <MDBBtn className="mr-2"  color="dark" disabled={displays[0] === "block"} onClick={() =>  backClicked()}>Back</MDBBtn>
                    <MDBBtn className="mr-4" color="dark" disabled={displays[12] === "block"} onClick={() =>  nextClicked()}>Next</MDBBtn>
                    <MDBBtn  color="dark" disabled={symptoms.length === 0} onClick={() =>  submit()}>Submit</MDBBtn>
                </div>
            </div>
            
            </>
        );
    }
}