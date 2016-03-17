# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences of values, indexed and accessible by integers. However, only tuples will work as keys in dictionaries, because dictionaries require immutable keys, and tuples are immutable unlike lists, which can be changed.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python lists and sets are both ways of storing multiple values. However, Python lists are ordered, indexed by integers, and can be iterated or sliced. Python sets are an unordered collection of objects that cannot appear in the set more than once. A Python set would be more helpful if you wanted to keep track of what items were at a grocery store, while a list would be more helpful if you wanted to keep track if the prices of items in different stores. Lists are faster to iterate through to find an element, but sets are faster to simply ask "if x in set" to find an element, since they are unordered and therefore would not have to iterate through the entire set to find element x.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The 'lambda' function is a construct in Python that allows for simple in-line programming. You could assign 'lambda x: x + 3' to a variable 'art', then call it saying 'art(3)', which would return 6; or, you could just write '(lambda x: x + 3)(3)' without assigning it to a variable, and it would still automatically return 6. This construct can be used in the 'key' argument in 'sorted' functions. If you wanted to sort a list of nested elements by a specific element within each element, you could write 'key=lambda x: x[i]'; or, if you had a set of temperatures in Celsius you wanted to sort from low to high in Fahrenheit, you could write 'key=lambda x: 1.8x + 32'.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are methods you can use to create lists quickly and easily. It usually consists of expressions involving "for" and "if" clauses. If you want to quickly create a list of squares, simply write '[x^2 for x in range(11)]', and you'll immediately have a list '[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'. If you use the 'map' function to accomplish the same thing, you would write a function 'def square(x): x^2' and then 'map(square, range(11))'. If you want squares that are only odd, with list comprehension you can just write '[x^2 for x in range(11) if (x^2) % 2 == 1]', which gives you '[1, 9, 25, 49, 81]'. Using 'filter', you would first have to have a preexisting list of squares 'squares', a preexisting function to specify odd numbers 'odd', then use 'filter(odd, squares)'. The performance speeds for 'map' and 'filter' versus list comprehensions are only marginally faster in cases where you are using a pre-existing function. Otherwise, list comprehensions are more often recommended for being simpler and easier to read. Set comprehension follows a similar pattern, with slight modifications: to make a set of squares, write '{x^2 for x in range(11)}'. To create a dictionary of squares (keys are the numbers, values are their squares) using dictionary comprehension, you can write 'x: x^2 for x in range(11)}'.
(Note: I'm using the caret instead of ** so the formatting is not bolded randomly.)

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





