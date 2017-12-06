
import csv, os
from datetime import datetime


def get_date_diff(date1, date2):
    try:
        dateObj1 = datetime.strptime(date1, '%m/%d/%Y')
        dateObj2 = datetime.strptime(date2, '%m/%d/%Y')
    except ValueError:
        return None

    return (dateObj1 - dateObj2).days

def alter_fields(complaint):
     complaint['ServiceType'] = complaint.pop('Service Type')
     complaint['MARTAction'] = complaint.pop('MART Action')
     complaint['ComplaintNumber'] = complaint.pop('\xef\xbb\xbfS.No')
     complaint['InvestigatorResponse'] = complaint.pop('InvestigatorResposeMemo')
     complaint['DateReceived'] = complaint.pop('DateRecieved')
     complaint['ResponseDueDate'] = complaint.pop('ResponseDue Date')
     complaint['DateOfIncident'] = complaint.pop('Date Of Incident')

def create_dict_list(x):
    dict_list = []
    with open(x, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for obj in reader:

            alter_fields(obj) # fix typos and bad field formats
            if obj['ComplaintNumber'] == 'S.No':
                continue  # ignore duplicated field lines

            else:
                Received_Delay = get_date_diff(obj['DateReceived'],
                    obj['DateOfIncident']) # typo in the csv file
                Response_Delay = get_date_diff(obj['ResponseDueDate'],
                    obj['DateReceived'])


                obj['ReceivedDelay'] = Received_Delay
                obj['ResponseDelay'] = Response_Delay

                dict_list.append(obj)

    return dict_list
