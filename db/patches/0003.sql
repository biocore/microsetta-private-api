/*
17 December 2014
---------------
Move the settings table to the ag schema.
*/
DO
$do$
BEGIN
IF EXISTS (SELECT 1
           FROM   pg_catalog.pg_class c
           JOIN   pg_catalog.pg_namespace n ON n.oid = c.relnamespace
           WHERE  n.nspname = 'public'
           AND    c.relname = 'settings') THEN
  ALTER TABLE public.settings SET SCHEMA ag;
END IF;
END
$do$
