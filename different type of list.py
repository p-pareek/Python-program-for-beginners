#list challenge:different type of list program


#defining my list
num_strings=['15','100','55','42']
num_ints=[15,100,55,42]
num_floats=[20.256,5.0,1.245,0.142857]
num_list=[[1,2,3],[4,5,6],[7,8,9]]
#summary table
print("\n Summary table")
print("\n the variable num strings is a "+ str(type(num_strings)))
print("it contains the elements"+ str(num_strings))
print(" the elemets "+ num_strings[0]+" is a "+str(type(num_strings[0])))

print("\n the variable num strings is a "+ str(type(num_ints)))
print("it contains the elements "+ str(num_ints))
print(" the elemets "+ str(num_ints[0])+" is a "+str(type(num_ints[0])))

print("\n the variable num strings is a "+ str(type(num_floats)))
print("it contains the elements "+ str(num_floats))
print(" the elemets "+ str(num_floats[0])+" is a "+str(type(num_floats[0])))

print("\n the variable num strings is a "+ str(type(num_list)))
print("it contains the elements "+ str(num_list))
print(" the elemets "+ str(num_list[0])+" is a "+str(type(num_list[0])))

#sorting the list
num_strings.sort()
num_ints.sort()
num_floats.sort()
num_list.sort()
print(num_strings, num_ints, num_floats, num_list)

      
                
