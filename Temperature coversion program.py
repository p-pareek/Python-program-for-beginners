print("Welcome to Temperature converter program")


temp_f=float(input("What is the temperature in degrees farhenheit: "))
#convert temperature:

temp_c=(5/9)*(temp_f-32)
temp_k=temp_c+273.15

#round the temps
temp_f=round(temp_f,4)
temp_c=round(temp_c,4)
temp_k=round(temp_k,4)

#summary table
print("\nDegrees farhenheit:\t"+str(temp_f))
print("\n Degress celcius:\t" +str(temp_c))
print("\n kelvin temperature:\t"+str(temp_k))

      
      
      
