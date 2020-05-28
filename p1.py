import json
import nltk.data
import os

def Capitalise_Name(string):
	capitalized_str = " ".join([word.capitalize() for word in string.split(" ")])
	return capitalized_str

def Capitalise_Paragraph(string):
	sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	sentences = sent_tokenizer.tokenize(string)
	sentences = [sent.capitalize() for sent in sentences]

	out = ""
	for sent in sentences:
		out = out + " " + sent

	return out

def makeJsonFile(keys, values, file):

	if len(keys) == len(values):
		size =len(keys)
		json_dict = {}
		for i in range(size):
			json_dict[keys[i]] = values[i]
	else:
		return None

	filename = file.split(".")
	filename[0] = filename[0] + "_o"
	file = filename[0] + "." + filename[1]

	with open(file, 'w') as json_file:
		json.dump(json_dict, json_file)

	return 1

def main():
	path2dir = str(input("Enter path to directory containing files : "))
	print(path2dir)
	filenames = []
	data = []

	for file in os.listdir(path2dir):
		if os.path.isfile(os.path.join(path2dir, file)):
			#print(file)

			if file != ".DS_Store":
				filenames.append(file)

				f = open(file)
				d = json.load(f)
				data.append(d)
				f.close()

	# print(data)
	# print(len(data))
	i = 0
	for d in data:
		keys = []
		values = []

		for (k,v) in d.items():
			keys.append(k)
			values.append(v)

		index = 0

		for k in keys:
			if "name" in k:
				#Capitalise the name
				values[index] = Capitalise_Name(values[index])
			elif "comment" in k or "note" in k:
				#Capitalise the paragraph
				values[index] = Capitalise_Paragraph(values[index])
			index += 1

		if makeJsonFile(keys,values,filenames[i]) != None:
			print("File succesfully updated.")
		else:
			print("Error updating file.")

		i += 1


if __name__ == '__main__':
	main()
	