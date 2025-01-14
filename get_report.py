import psycopg2
import os
from manage_csv import convertir_csv
from database import get_all_workers, connect_database, close_connection


def main():
  cursor = connect_database()
  rows = get_all_workers(cursor[1])
  convertir_csv(rows)
  close_connection(cursor)
    

if __name__ == "__main__":
  main()
