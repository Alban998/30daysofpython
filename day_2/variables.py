# Day 2: 30 Days of python programming – Level 2

# Variables du niveau 1 (rappel)
first_name = "Henovi"
last_name = "Komla"
full_name = first_name + " " + last_name
country = "Togo"
city = "Kohe"
age = 28
year = 2025
is_married = False
is_true = True
is_light_on = True
school, level, language = "Université de Lomé", "Master", "Python"

# 1. Vérification des types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(school), type(level), type(language))

# 2. Longueur du prénom
print("Longueur du prénom:", len(first_name))

# 3. Comparaison des longueurs
print("Prénom plus long que nom ?", len(first_name) > len(last_name))

# 4 à 11. Calculs avec num_one et num_two
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Addition:", total)
print("Soustraction:", diff)
print("Multiplication:", product)
print("Division:", division)
print("Modulo:", remainder)
print("Exponentielle:", exp)
print("Floor division:", floor_division)

# 12. Calculs liés au cercle
radius = 30
pi = 3.14159

area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Aire du cercle (r=30):", area_of_circle)
print("Circonférence:", circum_of_circle)

# Aire avec saisie utilisateur
r = float(input("Entrez un rayon : "))
print("Aire du cercle (r saisi):", pi * r ** 2)

# 13. Saisie utilisateur de données personnelles
user_firstname = input("Votre prénom : ")
user_lastname = input("Votre nom : ")
user_country = input("Votre pays : ")
user_age = int(input("Votre âge : "))

print("Bonjour", user_firstname, user_lastname, "de", user_country, "âgé(e) de", user_age, "ans.")

# 14. Mots clés Python
# (À exécuter uniquement dans le shell ou en dernier dans le script)
help('keywords')
