import os, re
import json
import pdb
import collections
from bs4 import BeautifulSoup
from django.utils.text import slugify

sourceLink = 'https://sa.wikipedia.org/wiki/मुख्यपृष्ठम्',
source = 'Sanskrit Wikipedia'

works = [{
	'originalTitle': "आयुर्वेद",
	'englishTitle': "Ayurveda",
	'author': "Not available",
	'dirname': "ayurveds",
	'source': source,
	'sourceLink': sourceLink,
	'language': 'sanskrit',
	'text': {},
}, {
	'originalTitle': "पुराण",
	'englishTitle': "Puranas",
	'author': "Not available",
	'dirname': "puranas",
	'source': source,
	'sourceLink': sourceLink,
	'language': 'sanskrit',
	'text': {},
}]

ayurvedsTexts = ["ashta", "chikitsa", "chikitsasathanam__", "nidin_", "sutar", "viman_"]
puranasTexts = []

def jaggedListToDict(text):
	node = { str(i): t for i, t in enumerate(text) }
	node = collections.OrderedDict(sorted(node.items(), key=lambda k: int(k[0])))
	for child in node:
		if isinstance(node[child], list):
			if len(node[child]) == 1:
				node[child] = node[child][0]
			else:
				node[child] = jaggedListToDict(node[child])
	return node

def fileToLines(root, fname):
	with open(os.path.join(root, fname)) as f:
		lines = f.read().splitlines()

	text = []
	for line in lines:
		if len(line.strip()):
			text.append(line)

	return text

def main():
	if not os.path.exists('cltk_json'):
		os.makedirs('cltk_json')
	# Build json docs from txt files
	for root, dirs, files in os.walk("."):
		path = root.split('/')
		print((len(path) - 1) * '---', os.path.basename(root))

		for fname in files:
			if fname.endswith('.txt'):
				print((len(path)) * '---', fname)

				for work in works:
					if path[2] == work['dirname']:

						if work['dirname'] == 'ayurveds':
							chapter = str(ayurvedsTexts.index(fname.replace(".txt", "")))
							text = fileToLines(root, fname)
							work['text'][str(chapter)] = jaggedListToDict(text)
							work['text'] = collections.OrderedDict(sorted(work['text'].items(), key=lambda k: int(k[0])))

						elif work['dirname'] == 'puranas':

							text = fileToLines(root, fname)
							chapters = os.listdir('/'.join(path[0:3]))
							chapter = str(chapters.index(path[3]))

							if chapter not in work['text']:
								work['text'][chapter] = {}

							if len(path) == 4:
								quarters = os.listdir('/'.join(path[0:4]))
								quarter = str(quarters.index(fname))
								if quarter not in work['text'][chapter]:
									work['text'][chapter][quarter] = {}
								work['text'][chapter][quarter] = jaggedListToDict(text)

							elif len(path) == 5:
								quarters = os.listdir('/'.join(path[0:4]))
								quarter = str(quarters.index(path[4]))
								sections = os.listdir('/'.join(path[0:5]))
								section = str(sections.index(fname))

								if quarter not in work['text'][chapter]:
									work['text'][chapter][quarter] = {}
								if section not in work['text'][chapter][quarter]:
									work['text'][chapter][quarter][section] = {}
								work['text'][chapter][quarter][section] = jaggedListToDict(text)

								work['text'][chapter][quarter][section] = collections.OrderedDict(sorted(work['text'][chapter][quarter][section].items(), key=lambda k: int(k[0])))

							work['text'] = collections.OrderedDict(sorted(work['text'].items(), key=lambda k: int(k[0])))
							work['text'][chapter] = collections.OrderedDict(sorted(work['text'][chapter].items(), key=lambda k: int(k[0])))
							work['text'][chapter][quarter] = collections.OrderedDict(sorted(work['text'][chapter][quarter].items(), key=lambda k: int(k[0])))

	for work in works:
		fname = slugify(work['source']) + '__' + slugify(work['englishTitle'][0:100]) + '__' + slugify(work['language']) + '.json'
		fname = fname.replace(" ", "")
		with open('cltk_json/' + fname, 'w') as f:
			json.dump(work, f)

if __name__ == '__main__':
	main()
