import csv, random, math
trabajador=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","MiguelSánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def asignar_sueldos_aleatorios(diccionario_trabajadores):
    for trabajador in diccionario_trabajadores:
        SUELDO = random.randit(300000,250000)
        trabajador['sueldo'] = SUELDO
        return diccionario_trabajadores
    
def clasificar_Sueldos(diccionario_trabajadores):
    try:
        print("Sueldo menores a 800.000:\n")
        for trabajador in diccionario_trabajadores:
            
            if trabajador ['sueldo'] < 8000000:
                print(f"Nombre: {trabajador['nombre']} || cargo:  {trabajador['cargo']} || sueldo: {trabajador['Sueldo']}\n")
                
        print("Sueldos entre 800000 y 2.000.000")
        for trabajador in diccionario_trabajadores:
            
            if trabajador['sueldo'] > 800000 and trabajador['sueldo'] < 2000000:
                print(f"Nombre: {trabajador['nombre']} || cargo:  {trabajador['cargo']} || sueldo:{trabajador['Sueldo']}\n")
                 
        print("Sueldo superiores a 2.000.000:\n")
        for trabajador in diccionario_trabajadores:
            if trabajador ['sueldo'] > 2000000:
                 print(f"Nombre: {trabajador['nombre']} || cargo: {trabajador['cargo']} || sueldo:{trabajador['Sueldo']}\n")
    except KeyError:
        print("¡Aun no hay sueldos registrados!")
        
def estadisticas(diccionario_trabajadores):
    try:
        sueldos= []
        for trabajador in diccionario_trabajadores:
            sueldos.append(trabajador['sueldo'])
    except KeyError:
        print("Aun no hay sueldos registrados")
    else:
        sueldo_max = max(sueldos)
        sueldo_min= min(sueldos)
        sueldo_promedio= sum(sueldos) / len(sueldos)
        sueldo_geom= math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
        print(f"sueldos mas alto: ${sueldo_max}")
        print(f"sueldo mas bajo: ${sueldo_min}")
        print(f"Promedio de sueldos: $ {sueldo_promedio:.2f}")
        print(f"media geometrica de sueldos:${sueldo_geom:.2f}")
        
        
def generar_reporte_sueldos(diccionario_trabajadores):
    try:
        campos=['nombre empleado', 'sueldo base', 'descuento salud', 'descuento AFP', 'sueldo liquido']
        with open('reporte_sueldos.csv', 'w', newline='.') as archivo:
            escritor= csv.DictWriter(archivo,fieldnames=campos)
            escritor.writeheader()
            for trabajador in diccionario_trabajadores:
                sueldo_base = trabajador['sueldo']
                descuento_afp= sueldo_base*0.12
                descuento_salud= sueldo_base*0.07
                sueldo_liquido = sueldo_base-descuento_afp-descuento_salud
                
                fila ={'nombre empleado': trabajador['nombre'], 'sueldo base': sueldo_base ,
                       'descuento salud': descuento_salud, 'descuento afp': descuento_afp, 
                       'sueldo liquido': sueldo_liquido
                }
                
    except KeyError:
        print("Aaun no hay sueldos registados") 
        
                 

print("1.-Asignar sueldos aleatorios ")  
print("2.-Clasificar sueldos ") 
print("3.-Ver estadisticas ") 
print("4.-Reporte de sueldos ")
opcion=int(input("Bienvenido al sistema, por favor, escoge alguna de estas opciones"))

if opcion==1:
    print(asignar_sueldos_aleatorios) 
elif opcion==2:
    print(clasificar_Sueldos)
        
          
            
                  
                    
            
                
             
                        
                        
                        
                           
        
        
    
    