can_fly=bool(int(input('¿Puede volar? 1:true 0:false :')))
is_human=bool(input('¿Es humano? 1:true 0:false : '))
has_a_mask=bool(input('¿Tiene mascara?1:true 0:false:'))
#iroman
if is_human is True:    #si es humano
    print("Es iroman")
    if has_a_mask is True:  #si usa mascara
        print("Es iroman")
        if can_fly is True:  #puede volar  
                print("es iroman ")                         
#captain marvel
        else:
            if can_fly is True:  #puede volar  
                print("captain marvel ")
                if is_human is False:   #no humano
                    print("Captain marvel")      
        if has_a_mask is False:  #no usa mascara
            print("Capitan Marvel" )
#Ronan accuser
        else:
            if can_fly is True:  #puede volar
                print("Ronan Accuser")
                if is_human is False:   #no humano
                    print("Ronan Accuser")  
                    if has_a_mask is True:  #tiene mascara  
                        print("Ronan Accuser ") 
#Vision
                    else:
                        if can_fly is True:  #puede volar
                            print("vision")
                            if is_human is False:   #no humano
                                print("Vision")
                                if has_a_mask is False:  #no usa mascara  
                                    print("vision")
#spiderman
else:
    if can_fly is False:  #No puede volar
        print("spiderman")
    if is_human is True:   #Si humano
        print("spiderman")
        if has_a_mask is True:  #Usa mascara  
            print("spiderman")
#Hulk
    else:
        if can_fly is False:  #No puede volar
            print("Hulk")
            if is_human is True:   #Si humano
                print("Hulk")
                if has_a_mask is False:  #No Usa mascara  
                    print("Hulk")
                else:
                    if can_fly is False:
                        print("Black Bolt")
        if is_human is False:
            print("Black Bolt")
            if has_a_mask is True:
                print("Black Bolt")
            else:
                if can_fly is False:
                    print("Thanos")
            if is_human is False:
                print("Thanos")
                if has_a_mask is False:
                    print("Thanos")