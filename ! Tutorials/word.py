#  details, originally stored in word

Python 

INPUT 

a = input (“Enter something here:”)

a = int (“Enter a number:”)

print (“Enter a name”)
nameIn = input()



VARIABLES

var1, var2, var3 = exp1, exp2, exp3



LISTS

Methods on list s:

	s.append()
	extend()
	insert(i,x)
	remove(x)
	pop()		removes last item
	pop(i)		removes indexed item
	clear()		same as del a[:]
	index(‘ant’)	returns index of string
	count(x)	returns number of x’s
	sort(key)	sort on key, e glen
	sort(reverse = True)
	reverse()
	copy()		shallow copy; same as a[:]
	
	
Functions on list:
	len(s)
	list()
	min()		or min(key)
	max()
	eg print(list(range()))

	del list[i]
(‘dog’) is a string; (‘dog’,) is a tuple

 

Enumerate 

(given list_3 containing 1 to 6)

for index, value in enumerate(list_3):
    print("Element",index,"->",value)
Element 0 -> 1
Element 1 -> 2
Element 2 -> 3
Element 3 -> 4
Element 4 -> 5
Element 5 -> 6



DICTIONARIES                    note ‘ for all strings ‘

>>> animals = {'dogs' : ['Robbie', 'Tess', 'Lily', 'Merle', 'Robin'], 'cats' : ['Jake', 'Katie', 'Ben', 'Thomas', 'Molly']}

access data: either

   animals [‘dogs’]				# error if not in dict
or
   animals.get (‘dogs’)				# None, but no error
   animals.get ('birds', 'No birds here')		# default message if fails

access data in (list in dict):

>>> animals ['dogs'][2]
'Lily'
>>> animals ['cats'][1]
'Katie'

ie dict [key] [index in list]			[]
or
    dict.get (key)				()

Change dict contents:

dd[‘age’] = 35		update existing key ‘age’
dd[‘weight’] = 179    	add a new key:value pair

del dd[‘age’]		delete a key:value pair
del dd			delete entire dict
dict.keys(),  .values(),  items()     # returns tuples; can do list (dict.keys())

dict.items()     returns tuples containing key and value;
	can iterate like so:
	for k, v in dd.items()
	    print(k,v)
or, can leave tuples as single var,
	for x in dd.items()
  	    print(x)          prints tuple pairs

Can use in, not in:
	‘name’ in dict – or in dict.keys()        key True for both expressions
	‘Bob’ in dict.values()    		must specify value() 

In place of:
“
if height not in dd:
    dd [‘height’] = 5 	“	indexing on key ‘height’

dd.setdefault (‘height’, 5)	note ()




SEE ALSO dict.update 

>>> d = {1:'one', 2:'two'}
>>> d2={3:'three'}			# from another dictionary
>>> d.update(d2)
>>> d
{1: 'one', 2: 'two', 3: 'three'}


or ….

dd = {‘one’ : 1}

dd.update (two = 2, three = 3)	# an iterable object of key/value pairs  # #(generally tuples).
					# note NO ‘  ‘


or …

dd.update ({“four” : 4})	# key/value pair in dict format, not previously defined
