import csv

faculty_list = list(csv.reader(open
            ("/Users/azg/ds/metis/dsp/python/faculty.csv")))

email_csv_list = csv.writer(open("/Users/azg/ds/metis/dsp/python/emails.csv", 
                                 "w"), delimiter=",")

email_list = [name[3] for name in faculty_list[1:]]                                 

nested_email_list = []
for email in email_list:
    nested_email_list.append([email])
    
print(nested_email_list)
for email in nested_email_list:
    email_csv_list.writerows(email)
