-- August 24, 2015
-- add country column to zipcode table
ALTER TABLE ag.zipcodes ADD COLUMN country varchar NOT NULL DEFAULT '';
ALTER TABLE ag.zipcodes ALTER COLUMN country DROP DEFAULT;
ALTER TABLE ag.zipcodes DROP CONSTRAINT zipcodes_pkey;
ALTER TABLE ag.zipcodes ADD CONSTRAINT idx_zipcodes PRIMARY KEY ( zipcode, country );

UPDATE ag.zipcodes SET country = 'United States' WHERE state IN ('AL','AK','AZ','AR','CA','CO','CT','DC','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY');
UPDATE ag.zipcodes SET country = 'Canada' WHERE state IN ('AB','BC','MB','NB','NL','NS','NT','NU','ON','PE','QC','SK','YT');
-- Delete the rest so the table can repopulate correctly
DELETE FROM ag.zipcodes WHERE country = '';