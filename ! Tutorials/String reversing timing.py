




$ python3.7 -m timeit --number 100000 --unit usec 'import string_reverse' 'string_reverse.reverse_slicing("ABç∂EF"*10)'
100000 loops, best of 5: 0.449 usec per loop

$ python3.7 -m timeit --number 100000 --unit usec 'import string_reverse' 'string_reverse.reverse_list("ABç∂EF"*10)'
100000 loops, best of 5: 2.46 usec per loop

$ python3.7 -m timeit --number 100000 --unit usec 'import string_reverse' 'string_reverse.reverse_join_reversed_iter("ABç∂EF"*10)'
100000 loops, best of 5: 2.49 usec per loop

$ python3.7 -m timeit --number 100000 --unit usec 'import string_reverse' 'string_reverse.reverse_for_loop("ABç∂EF"*10)'
100000 loops, best of 5: 5.5 usec per loop

$ python3.7 -m timeit --number 100000 --unit usec 'import string_reverse' 'string_reverse.reverse_while_loop("ABç∂EF"*10)'
100000 loops, best of 5: 9.4 usec per loop

$ python3.7 -m timeit --number 100000 --unit usec 'import string_reverse' 'string_reverse.reverse_recursion("ABç∂EF"*10)'
100000 loops, best of 5: 24.3 usec per loop
