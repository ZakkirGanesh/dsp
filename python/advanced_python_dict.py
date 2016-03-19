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

both_names_list = []
for name in faculty_list[1:]:
    each_name = name[0].split(" ")
    name_tuple = [each_name[0], each_name[-1]]
    both_names_list += [name_tuple]
both_names_tuple = tuple(tuple(entry) for entry in both_names_list)
#print(both_names_tuple)

first_faculty_dict = {}
info_only_list = [info[1:] for info in faculty_list[1:]]
#print(info_only_list)
#print(faculty_list)
i = 0
while i < len(info_only_list):
    if last_names_list[i] in first_faculty_dict:
        first_faculty_dict[last_names_list[i]] += [info_only_list[i]]
    else:
        first_faculty_dict[last_names_list[i]] = []
        first_faculty_dict[last_names_list[i]] += [info_only_list[i]]
    i += 1
#print(first_faculty_dict)

second_faculty_dict = {}

for j in range(len(info_only_list)):
    second_faculty_dict[both_names_tuple[j]] = info_only_list[j]
    j += 1
print(second_faculty_dict)
