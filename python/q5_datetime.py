# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

from datetime import date

date_diff1 = date(2015, 7, 28) - date(2013, 1, 2)
print(date_diff1)

date_diff2 = date(2015, 5, 28) - date(2013, 12, 31)
print(date_diff2)

date_diff3 = date(2015, 7, 14) - date(1994, 1, 15)
print(date_diff3)
