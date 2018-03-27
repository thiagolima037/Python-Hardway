#CRIANDO UMA STRING COM UMA VARIAVEL
types_of_people = 10
x = f"There are {types_of_people} types of people."

#CRIANDO UMA STRING UTILIZANDO DUAS VARIAVEIS STRINGS
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

#ALTERANDO A STRING A SER IMPRESSA DENTRO DA FUNÇÃO PRINT
print(f"I said: {x}")
print(f"I also said: '{y}'")

#UTILIZANDO A FUNÇÃO FORMAT PARA "PASSAR" UMA VARIAVEL
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

#MANIPULANDO DUAS STRING PARA FORMAR UMA NOVA
w = "This is the left side of ..."
e = "a string with a right side."

print(w+e)
