import pandas as pd

#data importeren
df = pd.read_excel("B2C3-B2F2 data Hartaandoening.xlsx")
df = df.values.tolist()

header = ['Leeftijd', 'Geslacht', 'Type pijn op de borst',
'Bloeddruk in rust toestand', 'Cholesterol', 'nuchtere bloedsuikerspiegel',
'ECG in rust toestand', 'Maximale hartslag', 'Oefening geïnduceerde angina',
'ST-depressie veroorzaakt door inspanning ten opzichte van rust',
'Piektraining ST-segment', 'Aantal grote bloedvaten (0-3)',
'gekleurd door flourosopy', 'thalassemia', 'Diagnose van hartaandoening']

#telt het aantal van elk klassen in de dataset
def class_counts(rijen):
    counts = {}  
    for rij in rijen:
        #label is laatste kolom
        label = rij[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

#kijkt of value numeriek is
def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)

#een vraag wordt gebruikt om een ​​dataset te partitioneren
#deze klasse legt alleen een 'kolomnummer' vast
class Question:
    #de 'match'-methode wordt gebruikt om de kenmerkwaarde te vergelijken
    #in een voorbeeld naar de kenmerkwaarde die is opgeslagen in de vraag
    def __init__(self, kolom, value):
        self.kolom = kolom
        self.value = value

    def match(self, example):
        #vergelijk de feature value in een voorbeeld met de
        #feature value in deze vraag
        val = example[self.kolom]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

#deze functie kijkt naar elke rij in de dataset of ze de vraag matchen of niet
#als dat niet zo is worden ze in false_rijen gezet en als dat wel zo is in true_rijen
def partition(rijen, question):
    true_rijen = []
    false_rijen = []
    for rij in rijen:
        if question.match(rij):
            true_rijen.append(rij)
        else:
            false_rijen.append(rij)
    return true_rijen, false_rijen

#berekent de Gini Impurity voor de rijen
def gini(rijen):
    counts = class_counts(rijen)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rijen))
        impurity -= prob_of_lbl**2
    return impurity

#de uncertainty van de start node - de gemiddelde impurity van de child nodes
def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

#vind de beste vraag om te stellen door elke functie/waarde te herhalen en de informationgain te berekenen
def zoek_beste_optie(rijen):
    best_gain = 0  
    best_question = None  
    current_uncertainty = gini(rijen)
    #aantal kolommen
    n_features = len(rijen[0]) - 1

    for col in range(n_features):
        values = set([rij[col] for rij in rijen])

        for val in values:
            question = Question(col, val)
            #dataset splitsen
            true_rijen, false_rijen = partition(rijen, question)

            if len(true_rijen) == 0 or len(false_rijen) == 0:
                continue

            #berekent informationgain van deze split
            gain = info_gain(true_rijen, false_rijen, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question
    return best_gain, best_question

class Leaf:
    def __init__(self, rijen):
        self.predictions = class_counts(rijen)

class Decision_Node:
    #decision node stelt een vraag
    #dit bevat een verwijzing naar de vraag en naar de twee onderliggende knooppunten.
    def __init__(self,
                 question,
                 true_tak,
                 false_tak):
        self.question = question
        self.true_tak = true_tak
        self.false_tak = false_tak

#deze functie stelt de boom op
def tree_opstellen(rijen):
    gain, question = zoek_beste_optie(rijen)

    if gain == 0:
        return Leaf(rijen) 

    #als er een feature/value is gevonden wordt er nog een keer gesplitst
    true_rijen, false_rijen = partition(rijen, question)

    #de true_tak wordt recursief opgesteld
    true_tak = tree_opstellen(true_rijen)

    #de false_tak wordt recursief opgesteld
    false_tak = tree_opstellen(false_rijen)

    return Decision_Node(question, true_tak, false_tak)

def classify(rij, node):
    if isinstance(node, Leaf):
        return node.predictions

    #kiest true of false tak
    if node.question.match(rij):
        return classify(rij, node.true_tak)
    else:
        return classify(rij, node.false_tak)

def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs

if __name__ == '__main__':
    tree = tree_opstellen(df)

    #evalueren
    testing_data = df

    #Accuracy
    for rij in testing_data:
        #Actual = rij[-1]
        Pred = print_leaf(classify(rij, tree))       
    
    print(Pred)