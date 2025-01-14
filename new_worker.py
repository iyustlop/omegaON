import psycopg2
import os
from manage_csv import convertir_csv, listar_archivos, open_csv
from database import connect_database, close_connection, new_workers


def main():
  cursor = connect_database()
  archivos = listar_archivos("./new", "new")
  rows = open_csv("./new", archivos)
  new_workers(cursor[0], cursor[1], rows)
  
  close_connection(cursor)
    
if __name__ == "__main__":
  main()
