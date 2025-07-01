# omegaON
Project for OmegaON, resources and more

# Persistance layer.

The command docker compose up start a postgres database. create_table.sql creates the schema and some data.

```bash
docker run -d \
--name postgres-container \
-e POSTGRES_USER=mi_usuario \
-e POSTGRES_PASSWORD=mi_contraseña \
-e POSTGRES_DB=mi_base_de_datos \
-v /sql/create-tables.sql:/docker-entrypoint-initdb.d/create-tables.sql \
-v /postgres-data:/var/lib/postgresql/data \
-p 5432:5432 \
postgres
```

## Database Initialization (for local, non-Docker deployments)

To initialize or reset the database for local development (when not using Docker), you can use the `init_db.sh` script.

**Prerequisites:**
- Make sure you have the PostgreSQL client tools installed (specifically `psql`). If not, you'll need to install them for your operating system.
- Ensure your PostgreSQL server is running and accessible with the credentials specified in `database.py` (host: `localhost`, user: `admin`, password: `admin`, database: `postgres`, port: `5432`).

**Usage:**
1. Open your terminal.
2. Navigate to the root directory of this project.
3. Make sure the script is executable: `chmod +x init_db.sh` (this only needs to be done once).
4. Run the script:
   ```bash
   ./init_db.sh
   ```
This script will connect to the PostgreSQL database using the details found in `database.py` and execute the `sql/create_tables.sql` file to set up the necessary tables and initial data.

**Note for Docker users:** If you are using Docker Compose (`docker-compose up`), the database is automatically initialized when the `postgres` service starts for the first time using the `sql/create_tables.sql` script. You do **not** need to run `init_db.sh` separately in that case. This script is intended for non-Dockerized local setups or for manually resetting the database if needed.