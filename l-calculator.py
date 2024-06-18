name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")

name1 = name1.lower()
name2 = name2.lower()

t = 0
l = 0

t += name1.count('t')
t += name1.count('r')
t += name1.count('u')
t += name1.count('e')
l += name1.count('l')
l += name1.count('o')
l += name1.count('v')
l += name1.count('e')
t += name2.count('t')
t += name2.count('r')
t += name2.count('u')
t += name2.count('e')
l += name2.count('l')
l += name2.count('o')
l += name2.count('v')
l += name2.count('e')

print(str(t)+str(l)+"%")

