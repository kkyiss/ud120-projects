#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

POI = 0
for key in enron_data:
    if enron_data[key]["poi"] == 1:
        POI+=1

print "Enron email has %s people." % (len(enron_data.keys()))
print "For each person there are %s features." % (len(enron_data["SKILLING JEFFREY K"]))
print "There are %s POI in E+F datasets" % (POI)

POI_TEST = "../final_project/poi_names.txt"
POI_TXT = open(POI_TEST,'r')

rl = POI_TXT.readlines()
print "There are %s POIs exists." % (len(rl[2:]))
print "James Prentice has stock belonging %s." % (enron_data["PRENTICE JAMES"]["total_stock_value"])
print "Wesley Colwell has %s persons of interest." % (enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print "Jeffrey K Skilling has %s value of stock options." % (enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

TOTAL_PAY = 0
for key in enron_data:
    if enron_data[key]["total_payments"] == 'NaN':
        TOTAL_PAY +=1
print "There are %.5s percentage of people in the dataset have NaN for their total payments." % (float(TOTAL_PAY)/len(enron_data.keys()))
print "Total payment is %s." % (float(TOTAL_PAY))

TOTAL_PAY_DATASET = 0
for key in enron_data:
    if enron_data[key]["total_payments"] == 'NaN' and enron_data[key]["poi"] == True:
        TOTAL_PAY_DATASET +=1
print "There are %s percentage of POI in the dataset have NaN for their total payments" % (float(TOTAL_PAY_DATASET)/len(enron_data.keys()))

print "\nAfter add 10 more data points which were all POI's"
print "The new number of people in the dataset %s" % (len(enron_data.keys())+10)
print "NaN for total_payments %s" % (TOTAL_PAY+10)
print "\nNew number of POIs in the dataset %s" % (POI+10)
print "New number of POIs with NaN %s" % (TOTAL_PAY_DATASET+10)


