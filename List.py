# LIST
'''


append()
extend()
insert()
remove()
index()
count()


copy()
copy.deepcopy()

clear()


# Dictionary
clear()
copy()
fromkeys()
get()
items()
keys()
values()

popitem()
setdefault()
pop()
update()

# String
capitalize()
center()
casefold()
count()
endswith()
expandtabs()
encode()
find(),rfind()
format()
index(),rindex()

isalnum()
isalpha()
isdecimal()
isdigit()
isidentifier()
islower()
isnumeric()
isprintable()
isspace()
istitle()
isupper()

join()
split(),rsplit(),splitlines()


ljust(), rjust()
upper(), lower()

swapcase()
lstrip(), rstrip(), strip()

partition(), rpartition()
maketrans()

translate(), replace()
startswith()

title()
zfill()
format_map()


#  Set
add()
remove()

copy()
clear()

difference(), difference_update()
intersection(), intersection_update()

isdisjoin()
issubset(), issuperset()


discard()






# General
any()
all()
ascii()

int(), bool(), float()
max() min() sum()
filter()
enumerate()

len()
reversed()
slice()

sorted()
reversed()

zip()
unzip()

'''

p = [x for x in range(5) if x%2==0]
#p = (x if x%2==0 else 0 for x in range(5))
#p.append([5])
#p.extend([5])
#p = p+ [5]
'''
for i in p:
    print(i)
'''

x = [[0 for y in range(5)] for i in range(5)]
print(x)

