lst=[1,2,3,5,5]
lst_1=[(lst.count(x),x) for x in set(lst)]
max_count=max(lst_1)[0]
for ele in lst_1:
   if ele[0]==max_count:
       print(ele[1])
