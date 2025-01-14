import psycopg2

# Configuración de la conexión
DB_HOST = "localhost"       # Cambia a la IP o nombre del host donde se ejecuta PostgreSQL
DB_NAME = "postgres"        # Nombre de tu base de datos
DB_USER = "admin"           # Usuario de PostgreSQL
DB_PASSWORD = "admin"       # Contraseña del usuario
DB_PORT = 5432              # Puerto, por defecto es 5432

def connect_database():
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
    return cursor
  except Exception as e:
    print(f"Error al conectar o consultar la base de datos: {e}")


def close_connection(cursor):
  if 'cursor' in locals():
    cursor.close()
  if 'connection' in locals():
    connection.close()


def get_all_workers(cursor):
  # Consulta para obtener el contenido de la tabla
  query = "SELECT * FROM workers;"
  cursor.execute(query)

  # Recuperar y mostrar los resultados
  rows = cursor.fetchall()
  print("Contenido de la tabla 'workers':")
  for row in rows:
    print(row)
  
  return rows

def new_workers(cursor, rows):
      # Insertar un registro
    insert_query = """
        INSERT INTO workers (id, name, office, location, room, on_boarding, last_change)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    data_to_insert = ("001", "John Doe", "HQ", "New York", "A-101", "2025-01-10", "2025-01-11")
    cursor.execute(insert_query, data_to_insert)

    # Confirmar cambios
    connection.commit()