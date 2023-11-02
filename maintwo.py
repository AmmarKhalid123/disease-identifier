import numpy as np
import pandas as pd
from sklearn import preprocessing
import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix


class NaiveBayes:
    def __init__(self):
        self.dictionary = {}
        self.model = GaussianNB()

        with open('final.csv') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for i in fields:
                self.dictionary[i] = []

            for i in csvreader:
                j = 0
                while j < len(i):
                    if j == 0:
                        self.dictionary['Disease'].append(i[j])
                    else:
                        self.dictionary[fields[j]].append(i[j])
                    j += 1
        le = preprocessing.LabelEncoder()
        self.encoded_dict = {}
        for key, val in self.dictionary.items():
            self.encoded_dict[key] = le.fit_transform(val)
        self.decode_disease = {}
        encoded = list(self.encoded_dict['Disease'])
        decoded = list(self.dictionary['Disease'])
        for i in range(4920):
            if len(self.decode_disease) == 41:
                break
            if encoded[i] not in list(self.decode_disease.keys()):
                self.decode_disease[encoded[i]] = decoded[i]
    def learn_and_test(self):

        features = zip(self.encoded_dict['itching'], self.encoded_dict['skin_rash'], self.encoded_dict['nodal_skin_eruptions'], self.encoded_dict['continuous_sneezing'], self.encoded_dict['shivering'], self.encoded_dict['chills'], self.encoded_dict['joint_pain'], self.encoded_dict['stomach_pain'], self.encoded_dict['acidity'], self.encoded_dict['ulcers_on_tongue'], self.encoded_dict['muscle_wasting'], self.encoded_dict['vomiting'], self.encoded_dict['burning_micturition'], self.encoded_dict['spotting_urination'], self.encoded_dict['fatigue'], self.encoded_dict['weight_gain'], self.encoded_dict['anxiety'], self.encoded_dict['cold_hands_and_feets'], self.encoded_dict['mood_swings'], self.encoded_dict['weight_loss'], self.encoded_dict['restlessness'], self.encoded_dict['lethargy'], self.encoded_dict['patches_in_throat'], self.encoded_dict['irregular_sugar_level'], self.encoded_dict['cough'], self.encoded_dict['high_fever'], self.encoded_dict['sunken_eyes'], self.encoded_dict['breathlessness'], self.encoded_dict['sweating'], self.encoded_dict['dehydration'], self.encoded_dict['indigestion'], self.encoded_dict['headache'], self.encoded_dict['yellowish_skin'], self.encoded_dict['dark_urine'], self.encoded_dict['nausea'], self.encoded_dict['loss_of_appetite'], self.encoded_dict['pain_behind_the_eyes'], self.encoded_dict['back_pain'], self.encoded_dict['constipation'], self.encoded_dict['abdominal_pain'], self.encoded_dict['diarrhoea'], self.encoded_dict['mild_fever'], self.encoded_dict['yellow_urine'], self.encoded_dict['yellowing_of_eyes'], self.encoded_dict['acute_liver_failure'], self.encoded_dict['fluid_overload'], self.encoded_dict['swelling_of_stomach'], self.encoded_dict['swelled_lymph_nodes'], self.encoded_dict['malaise'], self.encoded_dict['blurred_and_distorted_vision'], self.encoded_dict['phlegm'], self.encoded_dict['throat_irritation'], self.encoded_dict['redness_of_eyes'], self.encoded_dict['sinus_pressure'], self.encoded_dict['runny_nose'], self.encoded_dict['congestion'], self.encoded_dict['chest_pain'], self.encoded_dict['weakness_in_limbs'], self.encoded_dict['fast_heart_rate'], self.encoded_dict['pain_during_bowel_movements'], self.encoded_dict['pain_in_anal_region'], self.encoded_dict['bloody_stool'], self.encoded_dict['irritation_in_anus'], self.encoded_dict['neck_pain'], self.encoded_dict['dizziness'], self.encoded_dict['cramps'], self.encoded_dict['bruising'], self.encoded_dict['obesity'], self.encoded_dict['swollen_legs'], self.encoded_dict['swollen_blood_vessels'], self.encoded_dict['puffy_face_and_eyes'], self.encoded_dict['enlarged_thyroid'], self.encoded_dict['brittle_nails'], self.encoded_dict['swollen_extremeties'], self.encoded_dict['excessive_hunger'], self.encoded_dict['extra_marital_contacts'], self.encoded_dict['drying_and_tingling_lips'], self.encoded_dict['slurred_speech'], self.encoded_dict['knee_pain'], self.encoded_dict['hip_joint_pain'], self.encoded_dict['muscle_weakness'], self.encoded_dict['stiff_neck'], self.encoded_dict['swelling_joints'], self.encoded_dict['movement_stiffness'], self.encoded_dict['spinning_movements'], self.encoded_dict['loss_of_balance'], self.encoded_dict['unsteadiness'], self.encoded_dict['weakness_of_one_body_side'], self.encoded_dict['loss_of_smell'], self.encoded_dict['bladder_discomfort'], self.encoded_dict['foul_smell_of_urine'], self.encoded_dict['continuous_feel_of_urine'], self.encoded_dict['passage_of_gases'], self.encoded_dict['internal_itching'], self.encoded_dict['toxic_look_(typhos)'], self.encoded_dict['depression'], self.encoded_dict['irritability'], self.encoded_dict['muscle_pain'], self.encoded_dict['altered_sensorium'], self.encoded_dict['red_spots_over_body'], self.encoded_dict['belly_pain'], self.encoded_dict['abnormal_menstruation'], self.encoded_dict['dischromic_patches'], self.encoded_dict['watering_from_eyes'], self.encoded_dict['increased_appetite'], self.encoded_dict['polyuria'], self.encoded_dict['family_history'], self.encoded_dict['mucoid_sputum'], self.encoded_dict['rusty_sputum'], self.encoded_dict['lack_of_concentration'], self.encoded_dict['visual_disturbances'], self.encoded_dict['receiving_blood_transfusion'], self.encoded_dict['receiving_unsterile_injections'], self.encoded_dict['coma'], self.encoded_dict['stomach_bleeding'], self.encoded_dict['distention_of_abdomen'], self.encoded_dict['history_of_alcohol_consumption'], self.encoded_dict['blood_in_sputum'], self.encoded_dict['prominent_veins_on_calf'], self.encoded_dict['palpitations'], self.encoded_dict['painful_walking'], self.encoded_dict['pus_filled_pimples'], self.encoded_dict['blackheads'], self.encoded_dict['scurring'], self.encoded_dict['skin_peeling'], self.encoded_dict['silver_like_dusting'], self.encoded_dict['small_dents_in_nails'], self.encoded_dict['inflammatory_nails'], self.encoded_dict['blister'], self.encoded_dict['red_sore_around_nose'], self.encoded_dict['yellow_crust_ooze'], self.encoded_dict['prognosis'])

        features = np.array(list(features))

        label = zip(self.encoded_dict['Disease'])
        label = np.array(list(label))

        X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=1/3, shuffle=False) # 70% training and 30% test
        y_tr = []
        for i in y_train:
            y_tr.append((i[0], ))
        self.model.fit(X_train, y_tr)
        preds = []

        for i in X_test:
            xx = np.array(i)
            xx = xx.reshape(1, -1)
            dd = self.model.predict(xx)
            preds.append((dd[0],))
        print("Accuracy of Naive Bayes model:",accuracy_score(y_test, preds)*100,'\n')

    def predict(self, arr):
        pp = 0
        final = {}
        for i in self.dictionary.keys():
            if pp > 0:
                if i in arr:
                    final[i] = 1
                else:
                    final[i] = 0
            pp+=1
        xx = np.array(list(final.values()))
        xx = xx.reshape(1, -1)
        dd = self.model.predict(xx)
        return self.decode_disease[dd[0]]
