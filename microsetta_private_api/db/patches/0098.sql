ALTER TABLE ag.account DROP COLUMN cannot_geocode;
ALTER TABLE ag.account ADD COLUMN address_verified boolean NOT NULL DEFAULT FALSE;
ALTER TABLE ag.account ADD COLUMN cannot_geocode boolean NOT NULL DEFAULT FALSE;
