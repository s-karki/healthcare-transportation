
import re, operator
''' Input: A list of complaint objects (as dictionaries)
    Output: Three inverted indexes of the major text field
            in each object (ComplaintMemo, MARTAction, InvestigatorResponse)
            The indexes map to a ComplaintID(s)
'''

class IndexHolder:

        def __init__(self, Complaint, MARTAction,
            InvestigatorResponse):
            self.complaint_index = Complaint
            self.action_index = MARTAction
            self.investigator_index = InvestigatorResponse


def create_inverted_index(dicts):
    dict_list = dicts # avoid changing the original dict list
    text_fields = ['ComplaintMemo', 'InvestigatorResponse', 'MARTAction', 'ComplaintID']

    complaint_index = {}
    investigator_index = {}
    MART_index = {}

    for each_dict in dict_list:
        for key in each_dict.keys():
            if (key in text_fields) is False:
                del each_dict[key]

    text_fields.remove('ComplaintID')

    # now build each index
    for field in text_fields:
        print("Starting: ", field)
        index = build_index(field, dict_list)
        index = sort_index(index)

        if field == "ComplaintMemo":
            complaint_index = index
            print("Completed Complaints")
        if field == "InvestigatorResponse":
            investigator_index = index
            print("Completed Investigator")
        if field == "MARTAction":
            MART_index = index
            print("Completed MART")


    i = IndexHolder(complaint_index, MART_index, investigator_index)
    return i

def build_index(field, dicts):
    dict_list = dicts
    index = {}

    for each_dict in dict_list:

        text = each_dict[field] # text for a given field in each dict
        current_id = each_dict['ComplaintID']
        words_only = re.compile('\w+').findall(text)

        for word in words_only:
            if (word in index.keys()):
                 if (current_id in index[word]) == False: # add ID to existing index entry
                    index[word].append(current_id)
                    # do nothing if ID already account for

            else: # add a new entry
                index[word] = [current_id]


    # index is now a dictionary of words mapped to IDs in which they are found
    # But we're interested in the most common words. We sort by value length.
    return index

def sort_index(index):
    tuples = index.items()
    return sorted(tuples, key=lambda t: len(t[1]), reverse=True)
