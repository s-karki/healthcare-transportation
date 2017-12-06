import os
from generate import create_dict_list
from invertedindex import create_inverted_index, IndexHolder


def main():
    dir_ = os.getcwd()
    l = create_dict_list(dir_ + "/data/Complaints.csv") # create a list of objects from CSV
    print("Completed object list creation")
    indexes = create_inverted_index(l)

    '''now generate files for 2 folder
        folder 'counts': For each inverted index, generate a
        a file that contains mappings between words and number of
        complaints they appear in

        folder 'index': For each inverted index, list the tuples
        these are mappings between a word, and a list of all the Complaints
        they appear in
    '''

    complaints = indexes.complaint_index
    actions = indexes.action_index
    investigators = indexes.investigator_index

    xs = {'Complaints': complaints, 'Actions': actions,
     'Investigators':investigators}

    for key in xs.keys():
        print ("Starting to write counts for " + key)
        counts = open(dir_ + "/output/counts/count" + key + ".txt", mode='w')

        for entry in xs[key]: # iterate through the index
            counts.write(entry[0] + " " + str(len(entry[1])) +  "\n")
        counts.close()

        print ("Finished writing counts for " + key)

    for key in xs.keys():
        print ("Starting to write index for " + key)
        write_index = open(dir_ + "/output/indexes/indexes" + key + ".txt", mode='w')

        for entry in xs[key]:
            write_index.write(entry[0] + " " + " ".join(entry[1]) + "\n")
     
	write_index.close()
	print("Finished writing index for " + key) 

main()
