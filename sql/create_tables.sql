DROP TABLE IF EXISTS workers;

-- Crear la tabla 'workers'
CREATE TABLE workers(
    id VARCHAR(50) PRIMARY KEY,      -- Identificador único como string
    name VARCHAR(100) NOT NULL,      -- Nombre del trabajador
    office VARCHAR(50),              -- Oficina del trabajador
    location VARCHAR(100),           -- Ubicación del trabajador
    room VARCHAR(100),               -- Sala
    on_boarding DATE,                -- Fecha de incorporación
    last_change DATE                 -- Última modificación, con valor por defecto
);

-- Insertar dos registros de ejemplo
INSERT INTO workers (id, name, office, location, room, on_boarding, last_change)
VALUES ('T1000','Alice Johnson', 'London', 'ShortForm', 'Alpha', '2023-05-01', '2025-01-01');
INSERT INTO workers (id, name, office, location, room, on_boarding, last_change)
VALUES ('T1001','Bob Smith', 'Madrid', 'LongForm', 'Kappa', '2022-11-15', '2025-01-01');

-- Seleccionar datos para confirmar inserciones (opcional)
SELECT * FROM workers;