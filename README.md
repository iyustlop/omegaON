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