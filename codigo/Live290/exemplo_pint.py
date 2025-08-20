from pint import Quantity

kms = Quantity(45, 'kilometer')
miles = kms.to('miles')
print(kms, miles)
# 45 kilometer 27.96170365068003 mile

temp_c = Quantity(30, 'celsius')
temp_f = temp_c.to('fahrenheit')
print(temp_c, temp_f)
# 30 degree_Celsius 85.99999999999993 degree_Fahrenheit

peso_kg = Quantity(70, 'kilogram')
peso_lb = peso_kg.to('pound')
print(peso_kg, peso_lb)
# 70 kilogram 154.3235835294143 pound
