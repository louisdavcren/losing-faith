
import csv
from collections import OrderedDict
from numpy import random as r
#1a
# test = ("bob",[2,4,1,1,2,5])
def series_score(person, worst=1):
    for i in range(1, worst+1):
        largest = max(person[1])
        found = person[1].index(largest)
        person[1].pop(found)
    return sum(person[1])
# print(series_score(test))
#1b
# testing = [('Alice',[1,2,1,1,1,1]), ('Bob',[3,1,5,3,2,5]), ('Clare', [2,3,2,2,4,2]), ('Dennis', [5,4,4,4,3,4]), ('Eva', [4,5,3,5,5,3])]
def sort_series(sailors):
    unordered = []
    for s in sailors:
        unordered.append((s[0],series_score(s)))
    order = sorted(unordered, key=lambda x: x[1])
    print(order)
# sort_series(testing)
#1c
def import_file(filename):
    with open(filename+'.csv') as f:
        reader = csv.reader(f)
        raw = [r for r in reader]
    return raw[1:]

def read_sailor_data():
    data = 'sailor_performances'
    raw = import_file(data)
    sailors = {}
    for people in raw:
        if people !="":
            sailors.update({people[0]:(float(people[1]),float(people[2]))})
    return(sailors)
    print(people)
read_sailor_data()
#1d
def generate_performances(sailors):
    d = OrderedDict()
    for person in sailors:
        score = r.normal(sailors[person][0],sailors[person][1])
        d.update({person : score})
    return d
#1e
def calculate_final_order(sailor_scores):
    final_order = []
    for people in (sorted(sailor_scores.items(),key = lambda x: x[1], reverse=True)):
        final_order.append(people[0])
    return final_order
#1f
def simulation_races(races=6):
    results = {'Eva':[], 'Dennis':[], 'Clare':[], 'Bob':[], 'Alice':[]}
    for i in range(races):
        r = (calculate_final_order(generate_performances(read_sailor_data())))
        for people in r:
            results[people].append(r.index(people)+1)
    return results

def main():
	results = simulation_races()
	print(results)

if __name__ == '__main__':
	main()
