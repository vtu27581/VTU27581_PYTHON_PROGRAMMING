#word count analyzer

def analyze_file (filename):
  with open (filename, "r")as f:
    text=f.read()

#count lines, words, characters
 lines = text. Splitlines() 
words text.split()
characters = len (text)

#word frequency
freq = {}
for word in words:

word=cword.lower().strip(".,!?")
freq=(word)=freq.get(word, o) +1

#Display esults

print("Number of lines: "len (lines))
print ("Number of words: ", len(words))

print ("number of character:", char acters)

print ("\n word frequencies:")

for k,v in freq. items():

print (k,":",v)

#store in analysis.txt
with open ("analysis. txt", "w") as f:

f.write ("Number of lines: "+ strlen (lines))+"\n")

f.write ("Number of words:" + str(len (words)) + "\n")

f.write("Number of characters: "+str(characters)+"\n")

f-write("\n word frequencies: \n")
for k,v in freq.items():

f. write (k+ ":" + str (v)+ "\n")

#Run the program

file name = input("Enter filename to analyze:")

analyze_file (filename).
