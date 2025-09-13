ma_liste = []

while True:  #répète a l'infini jusqu'a break
    choix = input("""
Choisissez parmi les 5 options suivantes:
1: Ajouter un élément à la liste 
2: Retirer un élément de la liste 
3: Afficher les éléments de la liste 
4: Vider la liste de courses
5: Quitter 
Votre choix : """)

    if choix == "1":
        element = input("Entrez l'élément à ajouter : ")
        ma_liste.append(element)
        print(f"✅ L'élément '{element}' a été ajouté à la liste.")
    
    elif choix == "2":
        element = input("Entrez l'élément à retirer : ")
        if element in ma_liste:
            ma_liste.remove(element)
            print(f"✅ L'élément '{element}' a été retiré de la liste.")
        else:
            print(f"⚠️ L'élément '{element}' n'est pas dans la liste.")
    
    elif choix == "3":
        print(f"""Voici le contenu de la liste :
              {ma_liste}""")
    
    elif choix == "4":
        ma_liste.clear()
        print("La liste a été vidée de son contenu.")
        
    elif choix == "5":
        print("👋 Au revoir !")
        break #sort du programme

    else:
        print("⚠️ Choix invalide, réessayez !")
    
    