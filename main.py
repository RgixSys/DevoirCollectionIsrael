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

# 2.2 Afficher le contenu de l'élément numéro 5
print(t[4])

# 2.3 Ordonner la tuple
t = tuple(sorted(t))
print(t)

# 2.4 Ajouter un élément à la fin de la tuple
t = t + (10,)
print(t)

# 2.5 Ajouter un élément à l’index numéro 3
t = t[:3] + (11,) + t[3:]

# 2.6 Afficher la nouvelle tuple
print(t)


# QUESTION 3 :
# 3.0 Créer un set de 10 éléments de type chaîne de caractères
my_set = {"chat", "chien", "oiseau", "souris", "poisson", "serpent", "grenouille", "lapin", "écureuil", "hamster"}

# 3.1 Afficher le set
print("Le set avant l'ajout : ", my_set)

# 3.2 Ajouter un élément
my_set.add("tortue")

# 3.3 Afficher le set après l'ajout
print("Le set après l'ajout : ", my_set)

# 3.4 Supprimer un élément
my_set.remove("souris")

# 3.5 Afficher le set après la suppression
print("Le set après la suppression : ", my_set)

# 3.6. Supprimer le set
my_set.clear()

# 3.7 Afficher le set après la suppression
print("Le set après la suppression totale : ", my_set)


#QUESTION 4 : 
# 4.1 Création du dictionnaire
dictionnaire = {"fruit": "pomme", "couleur": "rouge", "animal": "chat", "pays": "France", "ville": "Paris", "sport": "football", "instrument": "guitare", "plat": "pizza", "film": "Star Wars", "livre": "Harry Potter"}

# 4.2 Affichage du dictionnaire
print(dictionnaire)

# 4.3 Affichage des clés
print(dictionnaire.keys())

# 4.4 Affichage des valeurs
print(dictionnaire.values())

# 4.5 Affichage des clés et des valeurs
for cle, valeur in dictionnaire.items():
    print(cle, ":", valeur)
    

# 4.6 Supprimer l'élément à la clé numéro 2 
print("\n IV.5 ----la suppression de l'element numero 2 :")  
supprimer = dictionnaire.pop("python")
print(dictionnaire) 

# 4.7 Afficher l'élément de la clé numéro 5 
print("\n IV.6 ---l'affichage de l'element numero 5 de la dictionnaire:")
for cle, valeur in dictionnaire.items():
        if cle == "velo":
            print(cle,":",valeur)

# 4.8 Ajouter un nouvel élément   
print("\n IV.7 ---ajout d'un nouvel element dans un dictionnaire:")  
dictionnaire.update({"voiture":"vehicule","Ajax":"langage"}) 
print(dictionnaire)