import matplotlib.pyplot as plt
import csv
from numpy import random as r
from random import randint
from collections import Counter
from harryQ1 import *

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
    with open('sailor_performances.csv', mode = 'w') as f:
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
