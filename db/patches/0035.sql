-- April 25, 2016
-- Adds tables needed for labadmin access control

CREATE TABLE IF NOT EXISTS ag.labadmin_users (
	email            varchar(100)  NOT NULL,
	password          varchar(100)  NOT NULL,
	CONSTRAINT pk_labadmin_users PRIMARY KEY ( email )
 );

CREATE TABLE ag.labadmin_access ( 
	access_id            serial  NOT NULL,
	access_name          varchar(100)  NOT NULL,
	access_description   varchar  ,
	CONSTRAINT pk_labadmin_access PRIMARY KEY ( access_id )
 );

CREATE TABLE ag.labadmin_users_access ( 
	access_id            integer  NOT NULL,
	email                varchar  NOT NULL
 );
CREATE INDEX idx_labadmin_access ON ag.labadmin_users_access ( email );
CREATE INDEX idx_labadmin_users_access ON ag.labadmin_users_access ( access_id );
ALTER TABLE ag.labadmin_users_access ADD CONSTRAINT fk_labadmin_access FOREIGN KEY ( email ) REFERENCES ag.labadmin_users( email );
ALTER TABLE ag.labadmin_users_access ADD CONSTRAINT fk_labadmin_users_access FOREIGN KEY ( access_id ) REFERENCES ag.labadmin_access( access_id );

INSERT INTO ag.labadmin_access (access_name, access_description) VALUES
('Barcodes', 'Allows a person to create barcodes and attach them to projects'),
('AG kits', 'Allows a person to create AG kits in the system and add barcdoes to existing kits'),
('Scan Barcodes', 'Can Scan barcodes and get information'),
('External surveys', 'Allows a person to add external surveys and survey data to the system'),
('Metadata Pulldown', 'Allows metadata pulldown access'),
('Search', 'Allows access to searching by barcode, name, kit id, etc'),
('Admin', 'Makes a person a sys admin');
