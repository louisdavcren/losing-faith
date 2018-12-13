import matplotlib.pyplot as plt
import csv
from numpy import random as r
from random import randint
from collections import Counter
from Q1 import generate_performances

def import_csv_file(filename):
    with open(filename) as csvfile:
        rdr = csv.reader(csvfile)
        raw_data = [r for r in rdr]
    return raw_data[1:]

def read_sailor_data():
    raw_data = import_csv_file("sailors4graph.csv")
    global sailors
    sailors = {}
    for people in raw_data:
        if people != "":
            sailors.update({people[0]: (float(people[1]),float(people[2]))})
    return(sailors)

def gen_counts(race_standing):
    count = []
    count_output = []
    for s in race_standing:
        count.append(int(race_standing[s]))
    data = (Counter(count))
    for numbers in data:
        count_output.append([numbers,data[numbers]])
    return count_output


def add_sailor_to_graph(loops):
    with open('sailors4graph.csv', mode = 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(loops):
            writer.writerow(['Example'+str(i), randint(0,100),20])

def plot():
    race_standing = (generate_performances(read_sailor_data()))
    sailors = read_sailor_data()
    x = []; y = []
    standing_count = sorted(gen_counts(race_standing))
    print(standing_count)
    for items in standing_count:
        x.append(items[0])
        y.append(items[1])

    plt.plot(x, y, 'ro')
    plt.axis([min(x),max(x)*1.1, min(y),max(y)*1.1])
    plt.xlabel('Skill')
    plt.ylabel('Amount of people that got the race score')
    plt.title('Score')
    plt.show()

add_sailor_to_graph(100)
plot()

def graph1():
    plt.plot([2,4,5,8], [1,4,9,16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()

# results = run_races(x)
def graph2(x):
    for key,val in results.item():
        plt.plot(val,label = key)

    plt.ylabel("Position")
    plt.xlabel("Races")
    plt.legend()

    plt.show()
