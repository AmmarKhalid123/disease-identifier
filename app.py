import flask
import numpy as np
from flask import jsonify, request
from main import DecisionTree
from maintwo import NaiveBayes

app = flask.Flask(__name__)
app.config["DEBUG"] = True

d = DecisionTree()
d.read_all_symptoms('Symptom-severity.csv')
d.read_file('dataset.csv')
d.read_precautions('symptom_precaution.csv')
d.read_description('symptom_Description.csv')
d.makeTree(d.root, d)

nb = NaiveBayes()
nb.learn_and_test()

@app.route('/', methods=['POST'])
def index():
    a = request.get_json(force=True)
    print(a)
    dt_disease = d.predict(a["symptoms"], d.root)
    nb_disease = nb.predict(a["symptoms"])

    result = {"dt": {"disease": dt_disease, "prec": d.precautions[dt_disease], "desc": d.description[dt_disease]}, "nb": {"disease": nb_disease, "prec": d.precautions[nb_disease], "desc": d.description[nb_disease]}}
    print(result)
    return jsonify({"result": result})
app.run()