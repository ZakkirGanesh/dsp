import csv

faculty_list = list(csv.reader(open
            ("/Users/azg/ds/metis/dsp/python/faculty.csv")))
degrees_list = []
degree_counts = {}
title_counts = {}
email_domain_counts = {}

for name in faculty_list[1:]:
    name_degree = name[1].split(" ")
    for degree in name_degree:
        if degree != " " and degree != "":
            degrees_list.append(degree)

degrees_list = [degree.replace("Ph.D.","PhD").replace("Ph.D",
                "PhD").replace("Sc.D.","ScD").replace("M.S.",
                "MS") for degree in degrees_list]

for degree in degrees_list:
    if degree in degree_counts:
        degree_counts[degree] += 1
    else:
        degree_counts[degree] = 1

title_list = [name[2].replace( " is ", " of ") for name in faculty_list[1:]]

for title in title_list:
    if title in title_counts:
        title_counts[title] += 1
    else:
        title_counts[title] = 1

email_list = [name[3] for name in faculty_list[1:]]

email_domain_list = []
for email in email_list:
    domain = email.split("@")[1]
    email_domain_list.append(domain)

for domain in email_domain_list:
    if domain in email_domain_counts:
        email_domain_counts[domain] += 1
    else:
        email_domain_counts[domain] = 1

