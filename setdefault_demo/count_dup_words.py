
import re
import os

WORE_RE = re.compile(r'\w+')
file_name = os.path.join(os.path.dirname(__file__),
                        "harry_potter_sorcerer's_stone_1st_chapter.txt")
index = {}

# with open(file_name, 'r') as fp:
# 	for line_no, line in enumerate(fp, 1):
# 		for match in WORE_RE.finditer(line):
# 			word = match.group()
# 			column_no = match.start()+1
# 			location = (line_no, column_no)
# 			occurences = index.get(word, [])
# 			occurences.append(location)
# 			index[word] = occurences
# 			# print(occurences)
# #
with open(file_name, 'r') as fp:
	for line_no, line in enumerate(fp, 1):
		for match in WORE_RE.finditer(line):
			word = match.group()
			column_no = match.start()+1
			location = (line_no, column_no)
			index.setdefault(word, []).append(location)

for word in sorted(index,key=str.upper):
	print("Word: {}, Word Count: {}, Location: {}".format(word, len(index[word]), index[word]))