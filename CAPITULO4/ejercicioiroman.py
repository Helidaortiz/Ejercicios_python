can_fly=(input('¿Puede volar?  '))
is_human=(input('¿Es humano? '))
has_a_mask=(input('¿Tiene mascara? ')) 

if can_fly=='si' and is_human=='si' and has_a_mask=='si': #iroman
        print("iroman")
elif can_fly=='si' and is_human=='si' and has_a_mask=='no':  #captain marvel
        print("captain marvel")
elif  can_fly=='si' and is_human=='no' and has_a_mask=='si': #ronan accuser
        print("ronan accuser")
elif can_fly=='si' and is_human=='no' and has_a_mask=='no': #vision
        print("vision")
elif can_fly=='no' and is_human=='si' and has_a_mask=='si': #spiderman
        print("spiderman")
elif  can_fly=='no' and is_human=='si' and has_a_mask=='no': #hulk
        print("hulk")
elif  can_fly=='no' and is_human=='no' and has_a_mask=='yes': #black bolt
        print("black bolt")
elif  can_fly=='no' and is_human=='no' and has_a_mask=='no': #Thanos
        print("Thanos")