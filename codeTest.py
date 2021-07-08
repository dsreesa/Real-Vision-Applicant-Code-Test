#by David Sreesangkom
#Tell Python to open and read alice_in_wonderland.txt file
f = open('alice_in_wonderland.txt', 'r')

textlist = []
#append text into a list using for loop
for line in f:
    Text = line.strip()
    textlist.append(Text)

#change the list to string
Text = str(textlist)

#tell Python to open and read 1-1000.txt file
f = open('1-1000.txt', 'r')

skiptextlist  = []
for line in f:
    Skiptext = line.strip()
    skiptextlist.append(Skiptext)

#change the list to string
SkipText = str(skiptextlist)

# remove the common words
for common in SkipText:
    Text = Text.replace(common, '', 1)

#use for-loop to clean each words
for char in '\\\\[]-.,\n!:`\"\"\'\';?':
    Text = Text.replace(char, '')
Text = Text.lower()

word_list = Text.split()
#Initializing Dictionary
word_count_dict = {}

#using for loops to counting number of times each word comes up in list of words(in dictionary)
for word in word_list:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

#set the key and value so they can be sorted
temp = [(value,key) for value,key in word_count_dict.items()]
temp.sort(key = lambda x:x[1], reverse = True)
result = temp[:]
print(result)