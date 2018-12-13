        # SAMPLE DATA
import random
import math
import csv

example1 = [("Alice", [1, 2, 1, 1, 1,]), ("Bob", [2, 4, 1, 1, 2, 5]), ("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]), ("Eva", [4, 5, 3, 5, 5, 3])]

example2 =("bob", [2,4,1,1,2,5])

        # QUESTION 1.A
def series_score(sailor, discard=1):
    for i in range(0, discard):
        deleted_score = max(sailor[1])
        sailor[1].remove(deleted_score)
    total = sum(sailor[1])
    return total


        # QUESTION 1.B
def sort_series():
    print(sorted(example1, key=lambda x: x[0]))


        # QUESTION 1.C
import csv

def import_csv_file(filename):
    with open(filename) as csvfile:
        rdr = csv.reader(csvfile)
        raw_data = [r for r in rdr]
    return raw_data[1:]

def read_sailor_data():
    raw_data = import_csv_file("sailors.csv")
    global sailors
    sailors = {}
    for people in raw_data:
        if people != "":
            sailors.update({people[0]: (float(people[1]),float(people[2]))})
    return(sailors)

        # EXPECTED RESULT:
        # {'Dennis': (90.0, 0.0), 'Clare':(100.0, 10.0), 'Eva': (90.0, 5.0), 'Bob': (100.0, 5.0), 'Alice':(100.0, 0.0)}


        # QUESTION 1.D
def generate_performances():
    # random.seed(57)
    global performance
    performance = {}
    read_sailor_data()
    for key in sailors:
        mu = float(sailors[key][0])
        sigma = float(sailors[key][1])
        performance[key] = random.normalvariate(mu, sigma)
    return(performance)


        # QUESTION 1.E
def calculate_finishing_order():
    generate_performances()
    # sorted(performance.items(), key=lambda x: x[1], reverse=True))
    return [sailor_names for sailor_names, sailorValues in sorted(performance.items(), key=lambda y: y[1], reverse=True)]


        # QUESTION 1.F
# results = {'Dennis': [4, 4, 4, 4, 4, 5], 'Alice': [2, 2, 2, 1, 1, 2], 'Bob': [3, 3, 3, 3, 2, 1], 'Eva': [5, 5, 5, 5, 3, 3], 'Clare': [1, 1, 1, 2, 5, 4]}
# Expected order
# ['Alice', 'Clare', 'Bob', 'Dennis', 'Eva']

def run_races(x=6):
    results = {'Eva':[], 'Dennis':[], 'Clare':[], 'Bob':[], 'Alice':[]} # the results format
    for i in range(x):
        r = (calculate_finishing_order())
        print(r)
        for people in r:
            results[people].append(r.index(people)+1)
    return(results)


    
    
    
    
