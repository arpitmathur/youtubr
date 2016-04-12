import json

categoriesList = []
categories = []
counter = 0
matrix = [[0 for i in xrange(len(categories))] for j in xrange(892)]

with open('MyVideoData.json') as data_file:
	data = json.load(data_file)

for video in data['data']:
	if video['category'] not in categoriesList:
		categories.append({"category": video['category'], "videos": []})
		categoriesList.append(video['category'])


for category in categories:
	for video in data['data']:
		if video['category'] == category['category']:
			rank = int(video['Number'])+891
			category['videos'].append({"name":video['title'], "channel": video['Channel'], "duration": video['duration'], "rank": rank}) 
			counter+=1

for category in categories:
	for video in category['videos']:
		index = int(categoriesList.index(category['category']))
		duration = video['duration']
		rank = int(video['rank'])
		matrix[rank][index] = duration

with open('categories.json', 'w') as write_file:
	json.dump(categoriesList, write_file, sort_keys=True, indent=4)

with open('matrix.json', 'w') as write_file:
	json.dump(matrix, write_file, sort_keys=True, indent=4)

with open('streamgraphData.json', 'w') as write_file:
	json.dump(categories, write_file, sort_keys=True, indent=4)

