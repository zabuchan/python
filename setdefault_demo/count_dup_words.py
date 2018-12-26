
import re
import sys

WORE_RE = re.compile(r'\w+')

index = {}
# with open(sys.argv[1], 'r') as fp:
# 	for line_no, line in enumerate(fp, 1):
# 		for match in WORE_RE.finditer(line):
# 			word = match.group()
# 			#print(match.start())
# 			# print(word)
# 			column_no = match.start()+1
# 			location = {line_no, column_no}
# 			occurences = index.get(word, [])
# 			occurences.append(location)
# 			index[word] = occurences
# 			# print(occurences)

with open(sys.argv[1], 'r') as fp:
	for line_no, line in enumerate(fp, 1):
		for match in WORE_RE.finditer(line):
			word = match.group()
			#print(match.start())
			# print(word)
			column_no = match.start()+1
			location = (line_no, column_no)
			index.setdefault(word, []).append(location)


for word in sorted(index,key=str.upper):
	print(word, index[word])