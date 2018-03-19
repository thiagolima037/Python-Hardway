name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let´s talk about {name}.")
print(f"He´s {height} inches tall.")
print(f"He´s {weight} pounds heavy.")
print("Actually that´s not too heavy.")
print(f"He´s got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffe.")

#this line is a tricky, try to get it exactly right
total = age + weight + height
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#calculo do peso em kg
weight_kg = weight * 0.45359237
#calculo da altura em cm
height_cm = height * 2.54

#Altura em cm
print(f"My height is {height} inches or {height_cm} cm")
#Peso em Kg
print(f"My weight is {weight} lbs or {weight_kg} kg")

#Teste função round
print(round(weight_kg))
