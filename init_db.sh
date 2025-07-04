#!/bin/bash

# Function to check if psql is installed
command -v psql >/dev/null 2>&1 || { echo >&2 "psql is not installed. Please install PostgreSQL client tools."; exit 1; }

# Extract database connection details from database.py
DB_HOST=$(grep -E "^DB_HOST\s*=\s*" database.py | cut -d '"' -f2)
DB_NAME=$(grep -E "^DB_NAME\s*=\s*" database.py | cut -d '"' -f2)
DB_USER=$(grep -E "^DB_USER\s*=\s*" database.py | cut -d '"' -f2)
DB_PASSWORD=$(grep -E "^DB_PASSWORD\s*=\s*" database.py | cut -d '"' -f2)
DB_PORT=$(grep -E "^DB_PORT\s*=\s*" database.py | cut -d ' ' -f3)

# Export password to avoid psql prompt
export PGPASSWORD=$DB_PASSWORD

# Execute the SQL script
echo "Initializing database..."
psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -f "sql/create_tables.sql"

if [ $? -eq 0 ]; then
  echo "Database initialized successfully."
else
  echo "Error initializing database."
fi

# Unset the password
unset PGPASSWORD
