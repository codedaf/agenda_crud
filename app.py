import os

CARPETA='contactos/'
EXTENSION= '.txt'


#contacto
class Contacto:
    def __init__(self,name,phone,category):
        self.name=name
        self.phone=phone
        self.category=category




def app():
    crear_directorio()

    mostrar_menu()

    user_options()



def user_options():
    question = True
    while question:
        option = input('Select option: \r\n')
        option=int(option)

        if option==1:
            add_contact()
            question=False
        elif option==2:
            edit_contact()
            question=False
        elif option==3:
            read_contact()
            question=False
        elif option==4:
            search_contact()
            question=False
        elif option==5:
            delete_contact()
            question=False
        elif option==6:
             
            question=False  
        else:
            print('Opcion invalida')




def read_contact():
    #print ('Add contact')
    archivos=os.listdir(CARPETA) 

    #Valido que sean los txt
    archivos_txt= [i for i  in archivos if  i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA+archivo) as contactos:
            for linea in contactos:
                #Imprime contendios
                print(linea.rstrip())
            #Imprime separadores
            print('------------------\r\n')

        










  
            
def add_contact():
    print ('___Add contact___')
    name_contact = input('Name Contact: \n\r')

    #Revisar si existe
    existe= existe_contacto(name_contact)

    if not existe:
    
        with open (CARPETA+name_contact+EXTENSION, 'w') as archivo:
            phone_contact = input('Phone Contact: \n\r')
            category_contact = input('Category Contact: \n\r')
            #Instanciar la clase
            contacto= Contacto(name_contact,phone_contact,category_contact)

            #Escriir en el archivo
            archivo.write('Name: ' + contacto.name  +  '\n\r' )
            archivo.write('Phone: ' + contacto.phone  +  '\n\r' )
            archivo.write('Category: ' + contacto.category  +  '\n\r' )
            print ('Add contact ok !')
    else: 
        print ('Contact exist')

    #reinicar la APP
    app()

        
   
    
def edit_contact():
    nombre_anterior = input('Name to edit:\n')

    # Suponiendo que existe_contacto() es una función definida en otra parte del código
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            name_contact = input('Add new name contact: \n')
            phone_contact = input('Add new phone contact: \n')
            category_contact = input('Add new category contact: \n')
            
            # Suponiendo que Contacto es una clase definida en otra parte del código
            contacto = Contacto(name_contact, phone_contact, category_contact)

            # Escribir en el archivo
            archivo.write('Name: ' + contacto.name + '\n')
            archivo.write('Phone: ' + contacto.phone + '\n')
            archivo.write('Category: ' + contacto.category + '\n')
            print('Add contact ok !')

        # Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + name_contact + EXTENSION)
        
        print('Edit contact correct!')
    else: 
        print('Contact does not exist')






def existe_contacto(nombre):
    #Valida que la caperta exista 
    return os.path.isfile(CARPETA+nombre+EXTENSION)




def search_contact():
    #print ('Add contact')
    names = input('Select Name: \r\n')

    try:
        with open(CARPETA+names+EXTENSION) as contacto:
            print('<<<<  Information >>>>> \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')


    except IOError:
        print('Not Exists') 
        print(IOError)
    
    #reinicial la app
    app()


def delete_contact():
    name = input('Select Name to delete: \r\n')

    try:
         os.remove(CARPETA+name+ EXTENSION)
         print('Delect Correct \r\n') 
    except IOError:
        print('Not Exists \r\n') 
        print(IOError)
    
    #reinicial la app
    app()













def mostrar_menu():
    print('Select option:')
    print('(1) Add contact')
    print('(2) Edit contact')
    print('(3) Read contact')
    print('(4) Search contact')
    print('(5) Delete contact')
    print('(6) Exit')
    
    


def crear_directorio():
    if not os.path.exists(CARPETA):
    #crear carpeta
        os.makedirs(CARPETA)


app()