# dic={'name':'rinsha','roll no':1,'place':'parappanangadi'}
# print(dic)
# print(type(dic))
# print(dic['name'])
# dic['city']='malappuram'
# print(dic)
# dic['roll no']=dic['roll no']+5
# print(dic)
# dic={'emp_id':1008,'emp_name':'rahul','salary':30000}
# print(dic)
# print(dic['salary'],dic['emp_name'])
# dic['company']='tcs'
# print(dic)
# dic['salary']=dic['salary']+5000
# print(dic)
lst=['hello','hai','orange','hello','orange','hello']
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)




