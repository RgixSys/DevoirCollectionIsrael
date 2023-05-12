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