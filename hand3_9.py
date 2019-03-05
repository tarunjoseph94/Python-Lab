def uniq(lst):
     ndlst=[]
     for i in lst:
         if i not in ndlst:
             ndlst.append(i)

     return ndlst
lst=[1,2,3,3,4,5,4,5]
print(uniq(lst))
