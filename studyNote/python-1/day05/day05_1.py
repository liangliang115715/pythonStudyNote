name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary= float(input("Salary:"))

msg='''
----------- info of %s ------------
Name: %s
Age : %d
Job : %s
Salary : %f
------------- end -------------------
'''%(name,name,age,job,salary)
print(msg)