# Oefening 1
# Print de volgende zin "Hello World"

print("Hello World")



# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Tami"
leeftijd = 18
woonstad = "Vianen"

print(naam)
print(leeftijd)
print(woonstad)



# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")

print(f"Hallo mijn naam is {naam}")
print(f"Ik ben {leeftijd} jaar oud" )
print(f"Ik woon in {woonstad}")
# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"

Game = "Mobile Legends"
Uren = 200
Cijfer = 8.5

print(f"Mijn favorite game is {Game}" )
print(f"Ik heb deze game {Uren} uren gespeeld")
print(f"Ik geef deze game een {Cijfer}")



# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit

Number1 = 10
Number2 = 5

Som = Number1 + Number2
Verschil = Number1 - Number2
Product = Number1 * Number2

print(f"{Number1}+{Number2}={Som}")
print(f"{Number1}-{Number2}={Verschil}")
print(f"{Number1}*{Number2}={Product}")


# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit

name="Silly"
health= 100
level= 20
damage= 20

print(f"Naam: {naam}")
print(f"Health: {health}")
print(f"Level: {level}")
print(f"Damage: {damage}")
health = health - damage
print(f"New health: {health}")

# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 

weapon= "Blade"
damage= damage + 1
level= level + 1

print(f"Weapon: {weapon}")
print(f"Damage: {damage}")
print(f"Level: {level}")



# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe

name= "Billy"
age= 19
favoriteGame= "League of Legends"
hoursPlayed= "350"
level= 100
score= 300
land= "Verenigde staten"


print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Game: {favoriteGame}")
print(f"Hours Played: {hoursPlayed}")
print(f"Level: {level}")
print(f"Score: {score}")
print(f"Land: {land}")



score= score + 250

print(f"New score: {score}")



