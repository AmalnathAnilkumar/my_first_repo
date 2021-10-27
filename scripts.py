#!/usr/bin/env python
# coding: utf-8

# # DATA SCIENCE (ADM)
# # HOMEWORK 1

# ## Amalnath Anilkumar

# # --------

# # PROBLEM 1

# ## 1. Introduction

# ###  Say "Hello, World!" With Python

# In[ ]:


str="Hello, World!"
print(str)


# ###  Python If-Else

# In[ ]:


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2 == 0:
        if n>1 and n<6:
            print('Not Weird')
        elif n>6 and n<21:
            print('Weird')
        else:
            print('Not Weird')        
    else:
        print('Weird')


# ### Arithmetic Operators

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# ### Python Division

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# ### Loops

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    i=0
    while i<n:
        print(i*i)
        i=i+1


# ### Write a function

# In[ ]:


def is_leap(year):
    if year%4 == 0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))


# ### Print Function

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    i=1
    list=[]
    for i in range(i,n+1):
        list.append(i)
    print(list,end='',sep='')    


# ## 2. Data Type

# ### List Comprehension

# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k==n:
                    continue
                else:
                    list.append([i,j,k])
    print(list)


# ### Find the Runner up score

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    x = max(arr)
    y = -9999999
    for i in range(0,n):
        if arr[i]<x and arr[i] > y:
            y = arr[i]
    
    print(y)


# ### nested list

# In[ ]:


if __name__ == '__main__':
    record=[]
    grade=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
        grade.append(score)
    
    grade=list(set(grade))
    grade=sorted(grade)
    record=sorted(record)
    second_lowest = grade[1]
    for name,score in record:
        if score==second_lowest:
            print(name)


# ### find the percentage

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total_mark=[]
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total_mark = sum(student_marks[query_name])
    average = total_mark/3 
    print("%.2f"%(average))


# ## Lists

# In[ ]:


if __name__ == '__main__':
    N = int(input())
    list=[]
    command=[]
    for i in range(0,N):
        command=input().split();
        if command[0] == "insert":
            list.insert(int(command[1]),int(command[2]))
        elif command[0] == "append":
            list.append(int(command[1]))
        elif command[0] == "pop":
            list.pop();
        elif command[0] == "print":
            print(list)
        elif command[0] == "remove":
            list.remove(int(command[1]))
        elif command[0] == "sort":
            list.sort();
        else:
            list.reverse();


# ## tuples

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list=tuple(integer_list)
    print(hash(integer_list))


# ## 3. String

# ### swap case

# In[ ]:


def swap_case(s):
    s1=''
    for ch in s:
        if ch.isupper():
            s1=s1+ch.lower()
        else:
            s1=s1+ch.upper()    
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print (result)


# ### string split and join

# In[ ]:


def split_and_join(line):
    # write your code here
    b=line.split(" ")
    b="-".join(b)
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print (result)


# ### Whats your name

# In[ ]:


def print_full_name(first, last):
    # Write your code here
    print("Hello "+first+" "+last+"! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# ### Mutation

# In[ ]:


def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string="".join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print (s_new)


# ### Find a string

# In[ ]:


def count_substring(string, sub_string):
    count1=0
    for i in range(0,len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            count1=count1+1

    return count1

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count


# ### String validators

# In[ ]:


if __name__ == '__main__':
    s = raw_input()
    #Alphanumeric
    f=0
    for i in range(len(s)):
        if(s[i].isalnum()):
            f=1
            break
    if f==1:
        print(True)
    else:
        print(False)
      #Character  
    f=0
    for i in range(len(s)):
        if(s[i].isalpha()):
            f=1
            break
    if f==1:
        print(True)
    else:
        print(False) 
        
        #Digit
    f=0
    for i in range(len(s)):
        if(s[i].isdigit()):
            f=1
            break
    if f==1:
        print(True)
    else:
        print(False)
  
  
        #Lower case     
    f=0
    for i in range(len(s)):
        if(s[i].islower()):
            f=1
            break
    if f==1:
        print(True)
    else:
        print(False)
    
        #uppercase
    f=0
    for i in range(len(s)):
        if(s[i].isupper()):
            f=1
            break
    if f==1:
        print(True)
    else:
        print(False)
   


# ### text alignment

# In[ ]:


width = int(input()) #This must be an odd number
ch = 'H'

#Top Cone
# replace  ______ To rjust |  ______ To  ljust
for i in range(width):
    print((ch*i).rjust(width-1)+ch+(ch*i).ljust(width-1))

#Top Pillars

for i in range(width+1):
    print((ch*width).center(width*2)+(ch*width).center(width*6))
    
#Middle Belt

for i in range((width+1)//2):
    print((ch*width*5).center(width*6))    

#Bottom Pillars

for i in range(width+1):
    print((ch*width).center(width*2)+(ch*width).center(width*6))    

#Bottom Cone

for i in range(width):
    print(((ch*(width-i-1)).rjust(width)+ch+(ch*(width-i-1)).ljust(width)).rjust(width*6))


# ### text wrap

# In[ ]:


import textwrap

def wrap(string, max_width):
    l= list()
    for i in range(0,len(string),max_width):
         l.append(string[i:i+max_width])
    return "\n".join(l)

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result


# ### designer door mat

# In[ ]:


N,M=map(int,input().split())

for i in range(1,N,2): 
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))


# ### string formatting

# In[ ]:


def print_formatted(number):
    length = len(bin(number)[2:])
   
    for i in range(1,number+1):
        print(str(i).rjust(length,' '),end=" ")
        print(oct(i)[2:].rjust(length,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(length,' '),end=" ")
        print(bin(i)[2:].rjust(length,' '),end=" ")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# ### alphabet rangoli

# In[ ]:


def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    data=[alpha[i] for i in range(n)]
        
    items = list(range(n))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-")) 

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# ### Capitalize

# In[ ]:


def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# ### Minion game

# In[ ]:


def minion_game(string):
    stuart=0;
    kevin=0;
    str_len = len(string)
    for i in range(str_len):
        if string[i] in "AEIOU":
            kevin=kevin + (str_len)-i
        else :
            stuart = stuart + (str_len)-i
    
    if stuart < kevin:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart",stuart)
    elif stuart == kevin:
        print("Draw")
    else :
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)


# ### Merge the tools

# In[ ]:


def merge_the_tools(string, k):
      
      i = 0
      while i < len(string):
        a = string[i:i+k]
        sub_str = ""
        for ch in a:
            if ch not in sub_str:
                sub_str += ch
        print(sub_str)
        i=i+k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# ## 4. SETS

# ### introduction to set

# In[ ]:


def average(array):
    s=0
    array=set(array)
    return (sum(array)/len(array))
    


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# ### No idea

# In[ ]:


n,m =map(int,input().split())
storage=list()
count = 0

storage=list(map(int, input().strip().split()))

A=set(map(int, input().strip().split()))
B=set(map(int, input().strip().split()))

for i in storage:
    if i in A:
        count=count+1
    if i in B:
        count=count-1

print(count)


# ### Symmetric difference

# In[ ]:


m=int(input())
a=set()
a=set(map(int, input().split()))
n=int(input())
b=set()
b=set(map(int, input().split()))
c=a.union(b)
d=a.intersection(b)
e=c.difference(d)
for i in sorted(list(e)):
    print(i)


# ### set add()

# In[ ]:


n=int(input())

country=set()

for i in range(n):
    country.add(input())

print(len(country))


# ### set discard() remove() pop()

# In[ ]:


n = int(input())
s = set(map(int, input().split()))
number=int(input())
for i in range(number):
    command = input().split()
    if command[0]=="remove":
        s.remove(int(command[1]))
    elif command[0]=="discard":
        s.discard(int(command[1]))
    else :
        s.pop()
print(sum(list(s)))


# ### set union()

# In[ ]:


n=int(input())
Estud=set(map(int,input().split()))
n=int(input())
Fstud=set(map(int,input().split()))
c=Estud.union(Fstud)
print(len(c))


# ### set intersection()

# In[ ]:


n=int(input())
Estud=set(map(int,input().split()))
n=int(input())
Fstud=set(map(int,input().split()))
c=Estud.intersection(Fstud)
print(len(c))


# ### set difference()

# In[ ]:


n=int(input())
Estud=set(map(int,input().split()))
n=int(input())
Fstud=set(map(int,input().split()))
c=Estud.difference(Fstud)
print(len(c))


# ### set symmetric difference()

# In[ ]:


n=int(input())
a=set(map(int,input().split()))
m=int(input())
for i in range(m):
    command=input().split()
    if command[0] == 'intersection_update':
        temp_a = set(map(int, input().split()))
        a.intersection_update(temp_a)
    elif command[0] == 'update':
        temp_a = set(map(int, input().split()))
        a.update(temp_a)
    elif command[0] == 'symmetric_difference_update':
        temp_a = set(map(int, input().split()))
        a.symmetric_difference_update(temp_a)
    elif command[0] == 'difference_update':
        temp_a = set(map(int, input().split()))
        a.difference_update(temp_a)
    else :
        assert False

print(sum(a))


# ### set mutation()

# In[ ]:


n=int(input())
a=set(map(int,input().split()))
m=int(input())
for i in range(m):
    command=input().split()
    if command[0] == 'intersection_update':
        temp_a = set(map(int, input().split()))
        a.intersection_update(temp_a)
    elif command[0] == 'update':
        temp_a = set(map(int, input().split()))
        a.update(temp_a)
    elif command[0] == 'symmetric_difference_update':
        temp_a = set(map(int, input().split()))
        a.symmetric_difference_update(temp_a)
    elif command[0] == 'difference_update':
        temp_a = set(map(int, input().split()))
        a.difference_update(temp_a)
    else :
        assert False

print(sum(a))


# ### The captains room

# In[ ]:


n=int(input())
a=map(int, input().split())
a=sorted(a)
for i in range(len(a)):
    if(i!=len(a)-1):
        if(a[i]!=a[i-1] and a[i]!=a[i+1]):
            print(a[i])
            break;
    else:
        print(a[i])


# ### check subset

# In[ ]:


no_test=int(input())

for i in range(no_test):
    n = input()
    a = set(input().split())
    m = int(input())
    b = set(input().split())
    print(a.issubset(b)


# ### check strict superset

# In[ ]:


a=set(input().split())
no_sets=int(input())
output = True

for i in range(no_sets):
    b = set(input().split())
    if not b.issubset(a):
        output = False
    if len(b) >= len(a):
        output = False

print(output)


# ## 5. collection

# ### collections.Counter()

# In[ ]:


from collections import Counter
x=int(input())
slist=Counter(map(int,input().split()))
y=int(input())
sum=0

for i in range(y):
    shoeno ,shoeprice = map(int,input().split())
    if(slist[shoeno]>0):
        sum = sum+shoeprice
        slist[shoeno] -= 1

print(sum)


# ### default dict tutorial

# In[ ]:


n,m=map(int,input().split())
from collections import defaultdict
d = defaultdict(list)
i=0
for i in range(n):
    d[input()].append(i+1)
    
for j in range(m):
    item = input()
    if len(d[item]) == 0:
        print(-1)
    else:
        print(*d[item])


# ### collections.namedtuple()

# In[ ]:


import collections
from collections import namedtuple
n = int(input())
colname = ','.join(input().split())
stud =namedtuple('stud',colname)
sum = 0
for i in range(n):
    row = input().split()
    student = stud(*row)
    sum += int(student.MARKS)
print(sum/n)


# ### collections orderdict

# In[ ]:


from collections import OrderedDict
n=int(input())
d=OrderedDict()
for i in range(n):
    item, space, price = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(price)
for item, price in d.items():
    print(item, price)


# ### word order

# In[ ]:


from collections import OrderedDict
n =int(input())

d = OrderedDict()
list_words = []
for i in range(n):
    list_words.append(input())

for s in list_words:
    if s not in d:
        d[s] = 1
    else:
        d[s] = d[s] + 1    
answer = ""
for i in d:
    answer = answer + str(d[i]) + " "
    
print(len(d))
print(answer)


# ### collection.deque()

# In[ ]:


from collections import deque

n=int(input())
d = deque()
for i in range(n):
    cmd=list(input().split())
    if cmd[0]=='append':
        d.append(int(cmd[1]))
    elif cmd[0]=='appendleft':
        d.appendleft(int(cmd[1]))
    elif cmd[0]=='pop':
        d.pop()
    elif cmd[0]=='popleft':
        d.popleft()
    else:
        print("Invalid command")    
for i in range(len(d)):
    print(d.popleft(),end =' ')


# ### company logo

# In[ ]:


import math
import os
import random
import re
import sys


from collections import Counter
if __name__ == '__main__':
    s=sorted(input().strip())
    s_counter =Counter(s).most_common(3)    
    for i in range(3):
        print(s_counter[i][0], s_counter[i][1])


# ### piling up

# In[ ]:


Tests=int(input())
for i in range(Tests):
    input()
    list1 =[int(i) for i in input().split()]
    min_list =list1.index(min(list1))
    left = list1[:min_list]
    right = list1[min_list+1:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")


# ## 6. Date and time

# ### calendar module

# In[ ]:


import calendar
import datetime


m, d, y = map(int, input().split())
date = datetime.date(y, m, d)
print(calendar.day_name[date.weekday()].upper())


# ### Time Delta exit full screen view

# In[ ]:


import math
import os
import random
import re
import sys
import calendar
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    d1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z') 
    d2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z') 
    tdiff = abs(int((d2-d1).total_seconds()))  
    return tdiff
if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)


# ## 7. Exception

# In[ ]:


t=int(input())

for i in range(t):
    try:
        a, b = input().split()
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)


# ## 8. Builts in

# ### Zipped!

# In[ ]:


st , sub =map(int, input().strip().split())
marks = []
for i in range(sub):
    marks.append(map(float, input().strip().split()))
        
for i in zip(*marks):
    print(sum(i)/sub)


# ### Athlete sort

# In[ ]:


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr=sorted(arr,key=lambda row:row[k])
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()


# ### ginorts

# In[ ]:


s=str(input())
s=list(s)
d=[]
l=[]
u=[]
o=[]
e=[]
for i in range(len(s)):
    if s[i].isdigit():
        d=d+list(s[i] )
    elif s[i].islower():
        l=l+list(s[i] )
    elif s[i].isupper():
        u=u+list(s[i] )   
l=sorted(l)
u=sorted(u)
for i in range(len(d)):
    if int(d[i])%2==0:
        e=e+list(d[i])
    else:
       o=o+list(d[i])
e=sorted(e)
o=sorted(o)
l=l+u+o+e
for i in l:
    print(i,end="") 


# ## 9. Python Functionals

# ### map and lambda functions

# In[ ]:


cube = lambda x: x*x*x 

def fibonacci(n):
    l=[]
    l[0]=0
    l[1]=1
    i=2
    for i in range(n):
        temp=l[i]+l[i+1]
        l.append(temp)
        l[i]=l[i+1]
        l[i+1]=l[i+2]
    return l    
        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# ## 10. Regex and parsing

# ### detect floating point number

# In[ ]:


t=int(input())
import re
for i in range(t):
    print(bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$', input())))


# ### re.split()

# In[ ]:


regex_pattern = r'[.,]+'

import re
print("\n".join(re.split(regex_pattern, input())))


# ### group()

# In[ ]:


import re
m = re.search(r'([a-zA-Z0-9])\1', input().strip())
print(m.group(1) if m else -1)


# ### re.findall

# In[ ]:


import re

s=re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if s:
    for i in s:
        print(i)
else:
    print(-1)


# ### re.start and re.end

# In[ ]:


import re
text, pattern = input(), input()
m=list(re.finditer("(?=(%s))"%pattern,text))
if not m:
    print((-1,-1))
for i in m:
    print((i.start(1),i.end(1)-1))


# ### re.substitution

# In[ ]:


import re

def change(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

for i in range(int(input())):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", change,input()))


# ### validating roman numerals

# In[ ]:


thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)

import re
print(str(bool(re.match(regex_pattern, input()))))


# ### validating phone numbers

# In[ ]:


import re
n=int(input())
for i in range(n):
    ph_no=input().strip()
    if (len(re.findall(r'^[7-9]\d{9}$',ph_no)) != 0):
        print("YES")
    else:
        print("NO")    
        


# ### validating and parsing email address

# In[ ]:


import re
n = int(input())
for i in range(n):
    name, email = input().split()
    pattern=r"<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name,email)


# ### Hex color code

# In[ ]:


import re
n=int(input())
for i in range(n):
    s=input()
    x=s.split()
    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
        for  i in x:
            print(i)


# ### HTML Parser 1

# In[ ]:


from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for a in attrs:
            print ('->',a[0],'>',a[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for a in attrs:
            print ('->',a[0],'>',a[1])
            
MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for i in range(int(input()))]))


# ### HTML Parser 2

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data != '\n':
            if '\n' not in data:
                print(">>> Single-line Comment")
                print(data)
            else:
                print(">>> Multi-line Comment")
                print(data)
                    
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()            


# ### Detect HTML tag attribute and values

# In[ ]:


from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        for a in attrs:
            print("-> {} > {}".format(a[0],a[1]))
    
    def handle_startendtag(self,tag,attrs):
        print(tag)
        for a in attrs:
            print("-> {} > {}".format(a[0],a[1]))
                   
html=""
t=int(input())
for i in range(t):
    html+=input().rstrip()
    html+='\n'     
    
parser=MyHtmlParser()    
parser.feed(html)
parser.close()


# ### Validating UID

# In[ ]:


import re

for i in range(int(input())):
    uid=''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', uid)
        assert re.search(r'\d\d\d', uid)
        assert not re.search(r'[^a-zA-Z0-9]', uid)
        assert not re.search(r'(.)\1', uid)
        assert len(uid) == 10
    except:
        print('Invalid')
    else:
        print('Valid')


# ### Validating credit card

# In[ ]:


import re
tests=re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for i in range(int(input().strip())):
    print("Valid" if tests.search(input().strip()) else "Invalid")


# ### Validating postal codes

# In[ ]:


import re
tests=re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for i in range(int(input().strip())):
    print("Valid" if tests.search(input().strip()) else "Invalid")


# ### matrix script

# In[ ]:


import math
import os
import random
import re
import sys
n,m=map(int,input().split())

matrix = []

for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrix=list(zip(*matrix))
s=''
for i in matrix:
    s+=''.join(i)
s=re.sub(r'\b[^a-zA-z0-9]+\b',r' ',s)
print(s)


# ## 11. XML

# ### XML find the score

# In[ ]:


import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    count = 0
    for tag in node.iter():
        count+=len(tag.attrib)    
    return count    

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# ### XML Find the maximum depth

# In[ ]:


import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level==maxdepth:
        maxdepth+=1
    for tag in elem:
        depth(tag,level+1)
            
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# ## 12. Closures and Decorators

# ### Standardize mobile number

# In[ ]:


def wrapper(f):
    def fun(l):
        output=[]
        for ph_no in l:
            s=""
            s=ph_no[::-1][0:10][::-1]
            s=" ".join(["+91"] + [s[0:5],s[5:]])  
            output.append(s) 
        f(output)         
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# ### Name Directory

# In[ ]:


import operator

def person_lister(f):
    def inner(people):
        people=sorted(people,key= lambda x: int(x[2]))
        output=[]
        for i in people:
            output.append(f(i))
        return output
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# ## 13. NUMPY

# ### Array

# In[ ]:


import numpy

def arrays(arr):
    arr=numpy.array(arr,float)
    
    return arr[::-1]
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# ### shape and reshape

# In[ ]:


import numpy

ar=list(map(int,input().split()))
array=numpy.array(ar)
print (numpy.reshape(array,(3,3)))


# ### Transpose and flatten

# In[ ]:


import numpy

n,m=map(int,input().split())
arr = numpy.array([input().strip().split() for _ in range(n)], int)
print (arr.transpose())
print (arr.flatten())


# ### Concatenate### 

# In[ ]:


import numpy
n,m,p=map(int,input().split())
arr=numpy.array([input().strip().split() for i in range(n)],int)
arr1=numpy.array([input().strip().split() for i in range(m)],int)
print (numpy.array(numpy.concatenate((arr, arr1), axis=0)))


# ### Zeroes and Ones

# In[ ]:


import numpy
n=tuple(map(int,input().split()))
print(numpy.zeros(n, dtype = numpy.int))
print(numpy.ones(n, dtype = numpy.int))


# ### Eye  and Identity

# In[ ]:


import numpy
numpy.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
print(numpy.eye(n, m, k = 0))


# ### Array Mathematics

# In[ ]:


import numpy
n,m=map(int,input().split())
arr=numpy.array([list(map(int, input().split())) for n in range(n)])
arr1=numpy.array([list(map(int, input().split())) for n in range(n)])
print(arr+arr1)
print(arr-arr1)
print(arr*arr1)
print(arr//arr1)
print(arr%arr1)
print(arr**arr1)


# ### Floor ceil and rint

# In[ ]:


import numpy
numpy.set_printoptions(legacy='1.13')

arr = numpy.array(input().split(),float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))


# ### Sum and product

# In[ ]:


import numpy
n,m=map(int,input().split())
arr = numpy.array([input().split() for i in range(n)], int)
print(numpy.prod(numpy.sum(arr, axis=0), axis=0))


# ### Min And Max

# In[ ]:


import numpy
n,m=map(int, input().split())
arr=numpy.array([input().split() for i in range(n)],int)
print(numpy.max(numpy.min(arr,axis=1), axis=0))


# ### Mean Variance and std

# In[ ]:


import numpy
numpy.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
a=numpy.array([input().split() for i in range(n)],dtype=numpy.float)
print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
print(numpy.std(a,axis=None))


# ### Dot and cross

# In[ ]:


import numpy
n=int(input())
arr=numpy.array([input().split() for _ in range(n)], dtype=int)
arr1=numpy.array([input().split() for _ in range(n)], dtype=int)
print (numpy.dot(arr,arr1))


# ### Inner and outer

# In[ ]:


import numpy
arr=numpy.array(input().split(), int)
arr1=numpy.array(input().split(), int)
print(numpy.inner(arr, arr1))
print(numpy.outer(arr, arr1))



# ### Polynomials

# In[ ]:


import numpy
n = list(map(float,input().split()))
m = input()
print(numpy.polyval(n,int(m)))


# ### Linear Algebra

# In[ ]:


import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
print(round(numpy.linalg.det(a),2))


# # Problem 2

# ## Algorithms

# ### 1. Birthday Cake Candles

# In[ ]:


import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# ### 2. Kangaroo

# In[ ]:


import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# ### 3. Strange Advertising

# In[ ]:


mport math
import os
import random
import re
import sys


def viralAdvertising(n):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# ### 4. Recursive Digit Sum

# In[ ]:



import math
import os
import random
import re
import sys

def superDigit(n, k):
    def sum_digit(sm):
        if sm<10:
            return sm
        s=sum(int(i) for i in str(sm))
        return sum_digit(s)
    p=sum_digit(int(n))
    return sum_digit(p*k)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# ### 5. Insertion Sort 1

# In[ ]:


import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    temp=arr[-1]
    i=n-1
    while i>0 and arr[i-1]>temp:
        arr[i]=arr[i-1]
        print(*arr)
        i=i-1
    arr[i]=temp
    print(*arr)    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# ### 6. Insertion sort 2

# In[ ]:


import math
import os
import random
import re
import sys


def insertionSort2(n, arr):
    for i in range(1,n):
        temp=arr[i]
        j=i
        while j>0 and arr[j-1]>temp:
            arr[j]=arr[j-1]
            j=j-1
        arr[j]=temp
        print(*arr)    
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

