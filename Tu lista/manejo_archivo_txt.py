




print("------------------------------")
print("Bienvenido \n")
aux = False         ### variable auxiliar cambia su valor si hay una lista 
while(True):
    print("1-Elegir lista de compras")
    print("2-agregar producto")
    print("3-Mostar la lista de los productos")
    print("4-Eliminar algún producto de la lista")
    print("5-Guardar lista en un archivo de texto")
    print("6-Salir del programa \n")
    print("------------------------------")
    opcion = input("¿Qué deseas hacer? ")
    print()
    
    #Modulo 1  elige la lista
    if opcion == "1":
        print("Desea una lista nueva(n) o desea usar la lista anterior(a)\n")           ###pide al usuario usar la lista anterior o una nueva
        eleccion_lista = input("").lower()
        
        if eleccion_lista == "n":       ### crea lista nueva
            compras = [] 
            aux = True                  ### cambia su valor
            print("Lista nueva creada...\n")
            
            
            
        elif eleccion_lista == "a":             ### abre la lista anterior, y si no hay la crea
            
            try:
                archivo = open("lista_de_compras.txt", "r")
                compras = archivo.read()            ### carga la lista en la variable
                archivo.close()
                compras = compras.split()           ### convierte el string en una lista, usando los espacios
                print("se cargó la lista anterior...\n")    
                aux = True                          ###cambia su valor
                print(compras)
                print()
            
            except FileNotFoundError:
                print("no hay lista que cargar, se creara una nueva \n")    ### si no hay lista crea una nueva
                compras = []
                aux = True                          ### cambia su valor
        
            
    
    

    #Modulo 2 agrega productos a la lista
    elif opcion == "2" :
                
            while True:
                
                if aux == False:                ### si sigue siendo false, significa que no ha creado una lista 
                    print("primero elija una lista... \n")
                    break
                    
                print("Agregar productos a la lista de compras... \n")
                producto = input("Escribe el nombre del producto: ")
                compras.append(producto)        ### metodo para agregar un valor a la lista
                
                print("Producto agregado correctamente \n")
                opcion2 = input("Escribe 'V' para volver al menú principal o 'A' para agregar otro producto: ") ### le pregunta al usuario si desea seguir agregando elementos
                opcion2.lower()

                if opcion2 == 'v':              
                        break
                elif opcion2 == 'a':
                        continue
                else:
                    print("Opción incorrecta saliendo del menú \n")
                    break
            continue    

    #Módulo 3 muestra la lista del usuario
    elif opcion == "3":
    
        if aux == False:                        ### si no hay lista, entonces no hay nada que ver
            print("primero elija una lista... \n")
            continue
            
        print("------Lista de productos------")

        for producto in compras:                ### recorre la lista y la muestra con un salto de linea

            print(producto)

        print("------------------------------")

        continue

    #Módulo 4 elimina un producto de la lista
    elif opcion == "4":
        
        if aux == False:                       ### si no hay lista no hay nada que borrar
            print("primero elija una lista... \n")
            continue
        
        elif compras == []:                    ### si la lista esta vacia, no hay nada que borrar
            
            print("no hay nada en la lista...\n")
            continue

        print("----Eliminar producto----")

        for i in range(0, len(compras)):       ### recorre la lista y muestra al usuario la posicion de los productos en ella

            print(str(i) + "-" + compras[i])
        
        
        while(True):
            
            try:
                opcion_borrar = int(input("¿Cuál desea borrar? : "))    ### le pide el indice del elemento a borrar de la lista
            except ValueError:
                print("ingrese una opción valida...")                   ### si ingresa un dato no requerido y un indice fuera de rango le avisa al usuario
                                                                             
            if(opcion_borrar > len(compras)-1):                        
                print("Escribe una opción válida...")
                continue

            else:

                compras.remove(compras[opcion_borrar])#Funcion para eliminar un elemento de la lista con el nombre
                print("Producto eliminado correctamente... \n")
                break

        continue

    #Módulo 5 guarda la lista en un archivo de texto
    elif opcion == "5" :
        
        if aux == False:                        ### si no hay lista no hay nada que guardar
            print("primero elija una lista... \n")
            continue
        
        archivo = open("Lista_de_compras.txt", "w") ### abre el archivo en modo escritura
        
        for i in compras:
            espacio = " "
            archivo.write(i + espacio)  ###recorremos y guardames elementos uno por uno con un espacio 
            
        
       
        
        
        archivo.close()
        
        
        
        
        print("Se guardo correctamente.")
        
    
    #Pendiente...

    #Módulo 6

    elif opcion == "6":
        break

    else:
        print("Escribe un número válido patacón...")
        continue    

   

            

opinion_usuario = input("ayudenos a mejorar, deja tu comentario: ")
print("Fin del programa...")


