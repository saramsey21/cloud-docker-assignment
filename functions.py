import os
import socket

def find_txt_files(path):
    txtFiles = []
    for x in os.listdir(path):
        if x.endswith(".txt"):
            txtFiles.append(x)

    return txtFiles

def read_individual_word_count(file, path):
    grandTotal = 0
    currFile = path + '/' + file
    num_words = 0
    with open(currFile, 'r' ) as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    grandTotal += num_words
    return num_words

def top_three_words( file, path):
    word_freq = {}
    currFile = path + '/' + file
    with open(currFile, 'r' ) as f:
        for line in f:
            for word in line.split():
                if word.lower() in word_freq:
                    word_freq[word.lower()] += 1
                else:
                    word_freq[word.lower()] = 1
        
    sorted_freq = sorted(word_freq.items(), key=lambda x: x[1])
    top_three = [sorted_freq[-1], sorted_freq[-2], sorted_freq[-3]]
    return top_three

def find_ip():
    hostname=socket.gethostname()  
    IPAddr=socket.gethostbyname(hostname)
    return IPAddr