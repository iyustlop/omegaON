import os
import csv

def flatten(xss):
    return [x for xs in xss for x in xs]

def convertir_csv(datos):
    with open('out.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(datos) 

def open_csv(directorio, archivos):
  datos = []
  for archivo in archivos:
    nombre_archivo = "{}/{}".format(directorio, archivo)
    with open(nombre_archivo, 'r') as archivo:
      datos.append(list(csv.reader(archivo)))
  
  salida = flatten(datos)
  return salida

def listar_archivos(directorio, prefijo=None):
    """
    Lista todos los archivos en un directorio y, si se especifica un prefijo, filtra los que lo tienen.
    
    :param directorio: Ruta del directorio a listar.
    :param prefijo: (Opcional) Prefijo por el que filtrar los archivos.
    :return: Lista de archivos (opcionalmente filtrados).
    """
    try:
        # Lista todos los archivos en el directorio
        archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
        
        # Si se especifica un prefijo, filtra los archivos
        if prefijo:
            archivos = [f for f in archivos if f.startswith(prefijo)]
        
        return archivos
    except FileNotFoundError:
        print(f"El directorio '{directorio}' no existe.")
        return []
    except PermissionError:
        print(f"No tienes permisos para acceder al directorio '{directorio}'.")
        return []


