-- language is a reserved keyword in some variants of sql, (but not Postgres)
-- so we use preferred_language at the DB layer.
ALTER TABLE account ADD COLUMN preferred_language VARCHAR;
UPDATE account SET preferred_language='en_US';
ALTER TABLE account ALTER COLUMN preferred_language SET NOT NULL;
