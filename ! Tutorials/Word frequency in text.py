# Word frequency in text

#============================ *
# this clip from
#           https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php
#     using dictionary  (working)

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

# print(char_frequency('google.com'))


sample = """
Technical Note: In this form of the bytes() function, the <encoding> argument is required.
“Encoding” refers to the manner in which characters are translated to integer values.
A value of "utf8" indicates Unicode Transformation Format UTF-8, which is an encoding
that can handle every possible Unicode character. UTF-8 can also be indicated by
specifying "UTF8", "utf-8", or "UTF-8" for <encoding>.

See the Unicode documentation for more information. As long as you are
dealing with common Latin-based characters, UTF-8 will serve you fine."""

print(char_frequency(sample))

#=============================

# modify to count words; working.
# string --> list of strings with string.split(' ')
#  results --> dictionary

def word_frequency(str1):
    dict = {}
    lstr1=str1.split(' ')
    
    for n in lstr1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

 


sample = """
The number π is a mathematical constant. Originally defined as the ratio of a circle's circumference to its diameter, it now has various equivalent definitions and appears in many formulas in all areas of mathematics and physics. It is approximately equal to 3.14159. It has been represented by the Greek letter "π" since the mid-18th century, though it is also sometimes spelled out as "pi". It is also called Archimedes' constant.

Being an irrational number, π cannot be expressed as a common fraction (equivalently, its decimal representation never ends and never settles into a permanently repeating pattern). Still, fractions such as 22/7 and other rational numbers are commonly used to approximate π. The digits appear to be randomly distributed. In particular, the digit sequence of π is conjectured to satisfy a specific kind of statistical randomness, but to date, no proof of this has been discovered. Also, π is a transcendental number; that is, it is not the root of any polynomial having rational coefficients. This transcendence of π implies that it is impossible to solve the ancient challenge of squaring the circle with a compass and straightedge.

Ancient civilizations required fairly accurate computed values to approximate π for practical reasons, including the Egyptians and Babylonians. Around 250 BC the Greek mathematician Archimedes created an algorithm for calculating it. In the 5th century AD Chinese mathematics approximated π to seven digits, while Indian mathematics made a five-digit approximation, both using geometrical techniques. The historically first exact formula for π, based on infinite series, was not available until a millennium later, when in the 14th century the Madhava–Leibniz series was discovered in Indian mathematics.[1][2] In the 20th and 21st centuries, mathematicians and computer scientists discovered new approaches that, when combined with increasing computational power, extended the decimal representation of π to many trillions of digits after the decimal point.[3][4] Practically all scientific applications require no more than a few hundred digits of π, and many substantially fewer, so the primary motivation for these computations is the quest to find more efficient algorithms for calculating lengthy numeric series, as well as the desire to break records.[5][6] The extensive calculations involved have also been used to test supercomputers and high-precision multiplication algorithms.

Because its most elementary definition relates to the circle, π is found in many formulae in trigonometry and geometry, especially those concerning circles, ellipses, and spheres. In more modern mathematical analysis, the number is instead defined using the spectral properties of the real number system, as an eigenvalue or a period, without any reference to geometry. It appears therefore in areas of mathematics and the sciences having little to do with the geometry of circles, such as number theory and statistics, as well as in almost all areas of physics. The ubiquity of π makes it one of the most widely known mathematical constants both inside and outside the scientific community. Several books devoted to π have been published, and record-setting calculations of the digits of π often result in news headlines. Attempts to memorize the value of π with increasing precision have led to records of over 70,000 digits. """

print(word_frequency(sample))

# see https://www.sanfoundry.com/python-program-calculate-number-words-characters-string/
# if needed

# now try >ordering output by number of uses
#                > pprint


#=============================
# https://codereview.stackexchange.com/questions/27781/counting-letters-in-a-string
## This is called Dictionary comprehension, which is an efficient way to get
##  the count of each alphabet in the string as a letter(key):count(value) pair.

str = """
Technical Note: In this form of the bytes() function, the <encoding> argument is required.
“Encoding” refers to the manner in which characters are translated to integer values.
A value of "utf8" indicates Unicode Transformation Format UTF-8, which is an encoding
that can handle every possible Unicode character. UTF-8 can also be indicated by
specifying "UTF8", "utf-8", or "UTF-8" for <encoding>.

See the Unicode documentation for more information. As long as you are
dealing with common Latin-based characters, UTF-8 will serve you fine."""
 
{i:str.count(i) for i in str}

# doesn't work as a script (no output); does in REPL

## >>> {i:str.count(i) for i in str}
##{'\n': 8, 'T': 7, 'e': 46, 'c': 25, 'h': 16, 'n': 39, 'i': 33, 'a': 32, 'l': 11, ' ': 75, 'N': 1, 'o': 32, 't': 30, ':': 1,
## 'I': 1, 's': 19, 'f': 13, 'r': 27, 'm': 10, 'b': 5, 'y': 6, '(': 1, ')': 1, 'u': 10, ',': 5, '<': 2, 'd': 16, 'g': 9, '>': 2,
## 'q': 1, '.': 6, '“': 1, 'E': 1, '”': 1, 'w': 4, 'v': 4, 'A': 2, '"': 8, '8': 7, 'U': 8, 'F': 6, '-': 6, 'p': 2, 'S': 1, 'L': 1}
##>>>

#=============================
#     using regex

import re
import string
frequency = {}
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print words, frequency[words]

##Let's write our regular expression that would return all the words
##with the number of characters in the range [3-15]. Starting from 3
##will help in avoiding words that we may not be interested in counting
##their frequency like if, of, in, etc., and words having a length larger
##than 15 might not be correct words. The regular expression for such
##a pattern looks as follows:
## 
	
#              \b[a-z]{3,15}\b

##\b is related to word boundary.

##The above regular expression can be written as follows:
 	
##match_pattern = re.search(r'\b[a-z]{3,15}\b', text_string)    
 
