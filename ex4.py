#NUMERO DE CARROS
cars = 100
#QUANTIDADE DE LUGARES EM UM CARRO
space_in_a_car = 4.0
#QUANTIDADE DE MOTORISTAS
drivers = 30
#QUANTIDADE DE PASSAGEIROS
passengers = 90

#CALCULO DE CARROS SEM MOTORISTAS
cars_not_driven = cars - drivers

#CARROS COM MOTORISTAS = QUANTIDADE DE MOTORISTAS
#CONSIDERANDO QUE HÁ MAIS MOTORISTAS QUE CARROS DISPONIVEIS
cars_driven = drivers
#QUANTIDADE DE CAPACIDADE DE TRANSPORTE DE PASSAGEIROS
carpool_capacity = cars_driven * space_in_a_car
#MEDIA DE PASSAGEIROS POR CARRO
average_passengers_per_car = passengers / cars_driven


print("There are", cars , "cars avaiable.")
print("There are only", drivers, "drivers avaiable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
