import psycopg2
import os
import csv

# Configuración de la conexión
DB_HOST = "localhost"       # Cambia a la IP o nombre del host donde se ejecuta PostgreSQL
DB_NAME = "postgres"        # Nombre de tu base de datos
DB_USER = "admin"           # Usuario de PostgreSQL
DB_PASSWORD = "admin"       # Contraseña del usuario
DB_PORT = 5432              # Puerto, por defecto es 5432

def convertir_csv(datos):
    with open('out.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(datos) 

def main():
    try:
        # Conectar a la base de datos
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )

        # Crear un cursor
        cursor = connection.cursor()

        # Consulta para obtener el contenido de la tabla
        query = "SELECT * FROM workers;"
        cursor.execute(query)

        # Recuperar y mostrar los resultados
        rows = cursor.fetchall()
        print("Contenido de la tabla 'workers':")
        for row in rows:
            print(row)

        convertir_csv(rows)

    except Exception as e:
        print(f"Error al conectar o consultar la base de datos: {e}")
    finally:
        # Cerrar la conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    main()
