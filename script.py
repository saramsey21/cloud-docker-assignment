import functions

# setting variables
path = 'home/data'
topWordFile = 'IF.txt'

filesInDirectory = functions.find_txt_files(path)

# creating / overwriting new txt file
f = open("home/output/result.txt", "w")

# printing out text files from path
f.write('Text files in ' + path + ' are: \n')
grandTotal = 0
for file in filesInDirectory:
    f.write(file + '\n')

f.write('\n')

# initialize grand total at 0
grandTotal = 0

# find word count for each individual file + grand total
for file in filesInDirectory:
    wordCount = functions.read_individual_word_count(file, path)
    f.write('The number of words in ' + file + ' are: ')
    f.write(str(wordCount) + '\n\n')
    grandTotal += wordCount

# display grand total
f.write('The grand total number of words in all files are: ')
f.write(str(grandTotal) + '\n\n')

# find top 3 words
topWords = functions.top_three_words( topWordFile, path )
f.write('The top words in ' + topWordFile + ' are: \n')
for word in topWords:
    f.write('Word: ' + word[0] + '\nFrequency: ' + str(word[1]) + '\n')

# return machine ip address
ipAddress = functions.find_ip()
f.write('\n' + 'Your IP address is: ' + str(ipAddress))
