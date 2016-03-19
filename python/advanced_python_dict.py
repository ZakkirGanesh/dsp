import csv

faculty_list = list(csv.reader(open
            ("/Users/azg/ds/metis/dsp/python/faculty.csv")))
degrees_list = []
degree_counts = {}
title_counts = {}
email_domain_counts = {}

last_names_list = []
for name in faculty_list[1:]:
    last_name = name[0].split(" ")[-1]
    last_names_list.append(last_name)

first_faculty_dict = {}
info_only_list = [info[1:] for info in faculty_list[1:]]

print(faculty_list)
i = 0
while i < len(info_only_list):
    if last_names_list[i] in first_faculty_dict:
        first_faculty_dict[last_names_list[i]] += [info_only_list[i]]
    else:
        first_faculty_dict[last_names_list[i]] = []
        first_faculty_dict[last_names_list[i]] += [info_only_list[i]]
    i += 1
print(first_faculty_dict)
