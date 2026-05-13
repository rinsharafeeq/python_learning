my_set={1,2,3,4.9,4,5,'s',4,4,5 } #set ennath oru keyword aan . athinaal oru variable name kodukkumbool underscore kodukkunnath nallathaan (my_set)
# print(type(my_set))  # o/p=> set
# print(my_set)  #o/p=> {1,2,3,...,5}
# print(len(my_set))  # oru set-inullil number,letter.. onnilathikam pravashyam vannaal oru pravashyam maathram print cheyyukayullu .
#                     # eg :-  {1,2,3,4,2,2,1,3,5} o/p => {1,2,3,4,5} . len(my_set) => 5  *//* len 9 enn varilla
# my_set.add(44)  # add(num) enn koduthaal oru number maathram cheerkkaan pattullu
# print(my_set)


my_set.update({45,65})  # update koduthaal onnilathikam numbers cheerkkaam . ath kramathil aavillaa print cheyyuka
print(my_set)
my_set.pop()
print(my_set)
my_set.remove(2)
# print(set)

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9,0}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))


lst=[1,2,2,1,1,1,1,3,3,3,3,4,4,4,4,1]
set1=set(lst)
print(set1)