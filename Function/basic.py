#required thinks 
'''def function(name,age):
    print(f"My name is {name} and age is {age}.")

function("Abhay",35)
'''
# optional and required parameters
# there is no relation with the name parameter to this optional parameter 
def fun(eng,hin = 0,sst=0,comp=0,pt=0):
    total = eng+sst+hin+comp+pt
    print(f"Total marks are {total}.")
fun(20,30,40,90,80)
# there should be in the sequence of "required parameter should be in left and optional should be in right it will also show the error"