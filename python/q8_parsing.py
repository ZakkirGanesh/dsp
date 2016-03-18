#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

  def read_data(data):
   # COMPLETE THIS FUNCTION

  def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

  def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION

import csv

football_file = list(csv.reader(open("/Users/azg/ds/metis/dsp/python/football.csv")))

goals_list = [int(team[5]) for team in football_file[1:]]
goals_allowed_list = [int(team[6]) for team in football_file[1:]]
team_names_list = [team[0] for team in football_file[1:]]
goal_diff = []
for i in range(len(football_file[1:])):
    goal_diff.append(abs(goals_list[i] - goals_allowed_list[i]))
    i += 1

smallest_diff = None
sd_index = None
for diff in goal_diff:
    if smallest_diff is None or diff < smallest_diff:
        smallest_diff = diff
        sd_index = goal_diff.index(diff)
print(smallest_diff)
print(team_names_list)
