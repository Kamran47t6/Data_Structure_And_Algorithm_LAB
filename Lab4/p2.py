import time
import math
import matplotlib.pyplot as plt 
import pandas as pd

def Euclidean_distance(x,y):
    return math.sqrt(sum((xi-yi)**2 for xi,yi in zip(x,y)))

df = pd.read_csv('Train.csv' )
symptoms=['COUGH','MUSCLE_ACHES','TIREDNESS','SORE_THROAT', 'RUNNY_NOSE',
    'STUFFY_NOSE', 'FEVER', 'NAUSEA', 'VOMITING', 'DIARRHEA',
    'SHORTNESS_OF_BREATH', 'DIFFICULTY_BREATHING', 'LOSS_OF_TASTE',
    'LOSS_OF_SMELL', 'ITCHY_NOSE', 'ITCHY_EYES', 'ITCHY_MOUTH',
    'ITCHY_INNER_EAR', 'SNEEZING', 'PINK_EYE'] 
for symptom in symptoms:
    plt.figure(figsize=(8,4))
    plt.scatter(df['TYPE'],df[symptom],alpha=0.5)
    plt.xlabel('Disease Type')
    plt.ylabel(symptom)
    plt.title(f'Scatter Plot of {symptom} vs. Disease Type')
    plt.show()
    time.sleep(1.5)
        