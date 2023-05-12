# QUESTION 1:
# 1. Afficher les éléments de la liste
my_list = ['orange', 'banana', 'apple', 'pear', 'kiwi', 'peach', 'grape', 'mango', 'pineapple', 'plume']
print(my_list)

# 2. Changer le contenu de l'élément numéro 5
my_list[4] = 'cherry'
print(my_list)

# 3. Créer une nouvelle liste en la remplissant avec les éléments de la liste précédente contenant la lettre "a"
new_list = [elem for elem in my_list if 'a' in elem]
print(new_list)

# 4. Ajouter un élément à la fin de la liste
my_list.append('watermelon')
print(my_list)

# 5. Ajouter un élément à l’index numéro 2
my_list.insert(1, 'grapefruit')
print(my_list)

# 6. Supprimer l'élément numéro 3
del my_list[2]
print(my_list)

# 7. Supprimer l'élément à l’index numéro 2
my_list.pop(1)
print(my_list)

# 8. Ordonner la liste
my_list.sort()
print(my_list)

# 9. Afficher la sens au sens inverse
my_list.reverse()
print(my_list)

# 10. Vider la liste
my_list.clear()
print(my_list)

# 11. Supprimer la liste
del my_list


# Question 2: 
# 2.0 Créer une tuple de 10 éléments de type entier
t = (2, 5, 3, 8, 1, 6, 4, 7, 9, 3)

# 2.1 Afficher les éléments de la tuple
print(t)


