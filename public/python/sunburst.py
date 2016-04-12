import json
from pprint import pprint

# cat = [{ "name" : "Film & Animation", "children": []},
# { "name" : "Autos & Vehicles", "children": []},
# { "name" :  "Music", "children": []},
# { "name" : "Pets & Animals", "children": []},
# { "name" : "Sports", "children": []},
# { "name" : "Short Movies", "children": []},
# { "name" : "Travel & Events", "children": []},
# { "name" : "Gaming", "children": []},
# { "name" : "Videoblogging", "children": []},
# { "name" : "Comedy", "children": []},
# { "name" : "Entertainment", "children": []},
# { "name" : "News & Politics", "children": []},
# { "name" : "Howto & Style", "children": []},
# { "name" : "Science & Technology", "children": []},
# { "name" : "Nonprofits & Activism", "children": []},
# { "name" : "Movies", "children": []},
# { "name" : "Anime/Animation", "children": []},
# { "name" : "Action/Adventure", "children": []},
# { "name" : "Classics", "children": []},
# { "name" : "Comedy", "children": []},
# { "name" : "Documentary", "children": []},
# { "name" : "Drama", "children": []},
# { "name" : "Family", "children": []},
# { "name" : "Foreign", "children": []},
# { "name" : "Horror", "children": []},
# { "name" : "Sci-Fi/Fantasy", "children": []},
# { "name" : "Thriller", "children": []},
# { "name" : "Shorts", "children": []},
# { "name" : "Shows", "children": []},
# { "name" : "Trailers", "children": []}]


list = []
channels = []

with open('MyVideoData1.json') as data_file:
	data = json.load(data_file)


print len(data['data'])
for entry in data['data']:
	if entry['Channel'] not in list:
		channels.append({"name": entry['Channel'], "category": entry['category'], "children": []})
		list.append(entry['Channel'])

with open('temp.json', 'w') as write_file:
	for entry in data['data']:
		for channel in channels:
			if entry['Channel'] is channel['name']:
				entry['name'] = entry['title']
				entry['size'] = entry['duration']
				channel['children'].append(entry)


	print len(channels)
	#print json.dumps(channels, sort_keys=True, indent=4)
	json.dump(channels, write_file)


sunburst = []
list2 =[]

with open('temp.json') as data_file:
	data = json.load(data_file)

for entry in data:
	if entry['category'] not in list2:
		sunburst.append({"name": entry['category'], "children": []})
		list2.append(entry['category'])

i = 0
with open('sunburst.json', 'w') as write_file:
	for entry in data:
		#print entry['category']
		for cat in sunburst:
			if entry['category'] == cat['name']:
				i+=1	
				cat['children'].append(entry)

	print i
	#print json.dumps(sunburst, sort_keys=True, indent=4)
	json.dump(sunburst, write_file)
