import csv
import random

class Node:
    def __init__(self, name=""):
        self.name = name
        self.yes = None
        self.no = None
        self.yes_gini = -1
        self.no_gini = -1
        self.rec_to_include = {}
        self.disease = False

    def setName(self, name):
        self.name = name

    def setYesGini(self, g):
        self.yes_gini = g
    
    def setNoGini(self, g):
        self.no_gini = g

    def setYes(self, name=""):
        self.yes = Node(name)
    def setNo(self, name=""):
        self.no = Node(name)
    def setRecToInclude(self, key, val):
        self.rec_to_include[key] = val
    def setDisease(self, name):
        self.name = name
        self.disease = True

def shouldAdd(record, records_to_not_inclcude):
    for symp, ins in records_to_not_inclcude.items():
        if ins == "no":
            if symp in record:
                return False
        if ins == "yes":
            if symp not in record:
                return False
    return True

def returnKeyWithMaxLenVal(diseases):
    a = -10
    dis = ""
    for dise, lst in diseases.items():
        if len(lst) > a:
            a = len(lst)
            dis = dise
    return dis

def printDT(d):
    if d == None:
        return
    if (not(d.disease)):
        print(d.name)
    prrr(d.yes)
    if (d.disease):
        print("leaf: ", d.name)
        return
    prrr(d.no)

class DecisionTree:
    def __init__(self):
        self.records = {}
        self.test = {}
        self.all_symptoms = {}
        self.root = None
        self.precautions = {}
        self.description = {}
    def read_all_symptoms(self, dataset):
        with open(dataset) as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for i in csvreader:
                a = i[0].strip()
                self.all_symptoms[a] = int(i[1])
    def read_precautions(self, dataset):
        with open(dataset) as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for i in csvreader:
                a = i[0].strip()
                self.precautions[a] = []
                for j in range(1,5):
                    x = i[j].strip()
                    if x != "":
                        self.precautions[a].append(x)
    def read_description(self, dataset):
        with open(dataset) as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for i in csvreader:
                a = i[0].strip()
                self.description[a] = []
                self.description[a].append(i[1].strip())

    def read_file(self, dataset):
        with open(dataset) as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for i in csvreader:
                r = random.randint(1,10)
                if r <= 6:
                    j = 0
                    disease = i[j].strip()
                    try:
                        if len(self.records[disease][-1]) != 0:
                            self.records[disease].append([])
                    except:
                        self.records[disease] = [[]]
                    j += 1
                    lst = []
                    while j <= 17:
                        if i[j] == '':
                            break
                        
                        lst.append(i[j].strip())
                        j += 1
                    try:
                        if lst not in self.test[disease]:
                            # print("ayaa test", lst, self.test[disease])
                            for m in lst:
                                self.records[disease][-1].append(m)
                    except:
                        for m in lst:
                            self.records[disease][-1].append(m)

                else:
                    j = 0
                    disease = i[j].strip()
                    try:
                        if len(self.test[disease][-1]) != 0:
                            self.test[disease].append([])
                    except:
                        self.test[disease] = [[]]
                    j += 1
                    lst = []
                    while j <= 17:
                        if i[j] == '':
                            break
                        lst.append(i[j].strip())
                        j += 1
                    try:
                        if lst not in self.records[disease]:
                            # print("ayaa train", lst, self.records[disease])
                            for m in lst:
                                self.test[disease][-1].append(m)
                    except:
                        for m in lst:
                            self.test[disease][-1].append(m)

    def calculate_gini(self, symp, total_rec, records_to_see):
        divide_if_yes = {}
        divide_if_no = {}
        gini_yes = 1
        gini_no = 1
        yes_rec_count = 0
        no_rec_count = 0
        t = 0
        for disease, recs in records_to_see.items():
            for rec in recs:
                t+=1
                if symp in rec:
                    try:
                        divide_if_yes[disease] += 1
                    except:
                        divide_if_yes[disease] = 1
                    yes_rec_count += 1
                else:
                    try:
                        divide_if_no[disease] += 1
                    except:
                        divide_if_no[disease] = 1
                    no_rec_count += 1
        for dis, count in divide_if_yes.items():
            gini_yes -= (count/yes_rec_count)**2
        for dis, count in divide_if_no.items():
            gini_no -= (count/no_rec_count)**2
        total_gini = (gini_no*(no_rec_count/t)) + (gini_yes*(yes_rec_count/t))
        return (total_gini, gini_no, gini_yes)

    def select_split_node(self, records_to_not_inclcude):
        gini_all_symptoms = {} # gini val of all the symptoms
        gini_no_all_symptoms = {} # gini val of all the symptoms
        gini_yes_all_symptoms = {} # gini val of all the symptoms
        if len(records_to_not_inclcude) == 0:
            for symptom in self.all_symptoms.keys():
                ginis = self.calculate_gini(symptom, 4920, self.records)
                gini_all_symptoms[symptom], gini_no_all_symptoms[symptom], gini_yes_all_symptoms[symptom] = ginis
            symptom = min(gini_all_symptoms, key=gini_all_symptoms.get)
            return symptom, gini_no_all_symptoms[symptom], gini_yes_all_symptoms[symptom], gini_all_symptoms[symptom], self.records
        else:
            recs = {}
            for disease, records in self.records.items():
                recs[disease] = []
                for record in records:
                    if shouldAdd(record, records_to_not_inclcude):
                        recs[disease].append(record)
            for symptom in self.all_symptoms.keys():
                if symptom not in records_to_not_inclcude.keys():
                    ginis = self.calculate_gini(symptom, len(recs), recs)
                    gini_all_symptoms[symptom], gini_no_all_symptoms[symptom], gini_yes_all_symptoms[symptom] = ginis
            symptom = min(gini_all_symptoms, key=gini_all_symptoms.get)
            
            return symptom, gini_no_all_symptoms[symptom], gini_yes_all_symptoms[symptom], gini_all_symptoms[symptom], recs

    def makeTree(self, node, diseasess={}, root = True, gini = -1):
        if root:
            symptom, no, yes, trash, diseases = self.select_split_node({})
            self.root = Node(symptom)
            self.root.setNoGini(no)
            self.root.setYesGini(yes)
            self.root.setNo()
            self.root.setYes()
            self.root.yes.setRecToInclude(symptom, "yes")
            self.root.no.setRecToInclude(symptom, "no")
            self.makeTree(self.root.yes, diseases, False, self.root.yes_gini)
            self.makeTree(self.root.no, diseases, False, self.root.no_gini)
        else:
            if len(node.rec_to_include) == len(self.all_symptoms):
                recs = {}
                for disease, records in self.records.items():
                    recs[disease] = []
                    for record in records:
                        if shouldAdd(record, node.rec_to_include):
                            recs[disease].append(record)
                final_dis = returnKeyWithMaxLenVal(recs)
                node.setDisease(final_dis)
                return
            symptom, no, yes, trash, diseases = self.select_split_node(node.rec_to_include)
            if gini <= trash:
                final_dis = returnKeyWithMaxLenVal(diseases)
                node.setDisease(final_dis)
                return
            else:
                node.setName(symptom)
                node.setNoGini(no)
                node.setYesGini(yes)
                node.setNo()
                node.setYes()
                for i, j in node.rec_to_include.items():
                    node.yes.setRecToInclude(i, j)
                    node.no.setRecToInclude(i, j)
                node.yes.setRecToInclude(symptom, "yes")
                node.no.setRecToInclude(symptom, "no")
                # print("passing",diseases)
                self.makeTree(node.yes, diseases, False, node.yes_gini)
                self.makeTree(node.no, diseases, False, node.no_gini)
                return
        
    def predict(self, rec, node):
        while not(node.disease):
            if node.name in rec:
                node = node.yes
            else:
                node = node.no
        return node.name

    def accuracy(self):
        total = 0
        correct = 0
        for disease, recs in self.test.items():
            for rec in recs:
                total += 1
                a = self.predict(rec, self.root)
                if a == disease:
                    correct += 1
        print("The accuracy of the Decision Tree is: ", correct/total)
