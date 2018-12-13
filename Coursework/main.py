
import csv
import random as r

def series_score(t):
	t[1].pop(t[1].index(max(t[1])))
	print(t)

def sort_series(t):
	print(sorted(t, key=lambda x: x[0]))
	#Add the draw

def importing_csv_file(filename):
	with open(filename+'.csv') as f:
		reader = csv.reader(f)
		raw_data = [r for r in reader]
	return raw_data[1:]

def read_sailor_data():
	where_is_data = 'sailor_performances'
	raw_data = importing_csv_file(where_is_data)
	sailors = {}
	for people in raw_data:
		sailors.update({people[0]:(float(people[1]),float(people[2]))})
	return(sailors)

def generate_performances(sailors):
	scores = {}
	for person in sailors:
		score = r.normal(sailors[person][0],sailors[person][1])
		scores.update({person : score})
	return scores

def calculate_finishing_order(sailor_scores):
	win_order = []
	for people in (sorted(sailor_scores.items(), key = lambda x: x[1], reverse=True)):
		win_order.append(people[0])
	return win_order

def simulate_the_races(races=6):
	results = {'Bob':[], 'Alice':[], 'Clare':[], 'Dennis':[], 'Eva':[]}
	for i in range(races):
		r = (calculate_finishing_order(generate_performances(read_sailor_data())))
		for person in r:
			results[person].append(r.index(person)+1)
	return results

def main():
	results = simulate_the_races()
	print(results)

if __name__ == '__main__':
	main()
