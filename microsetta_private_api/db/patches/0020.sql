-- August 25, 2015
-- Add EBI expected country names to database

--Update country names from google
ALTER TABLE ag.iso_country_lookup DROP CONSTRAINT fk_iso_country_lookup;
UPDATE ag.iso_country_lookup SET country = 'North Korea' WHERE country = 'Korea, Democratic People''s Republic of';
UPDATE ag.iso_country_lookup SET country = 'Moldova' WHERE country = 'Moldova, Republic of';
UPDATE ag.iso_country_lookup SET country = 'Federated States of Micronesia' WHERE country = 'Micronesia, Federated States of';
UPDATE ag.iso_country_lookup SET country = 'Pitcairn Islands' WHERE country = 'Pitcairn';
UPDATE ag.iso_country_lookup SET country = 'Russia' WHERE country = 'Russian Federation';
UPDATE ag.iso_country_lookup SET country = 'South Korea' WHERE country = 'Korea, Republic of';
UPDATE ag.iso_country_lookup SET country = 'Syria' WHERE country = 'Syrian Arab Republic';
UPDATE ag.iso_country_lookup SET country = 'Taiwan' WHERE country = 'Taiwan, Province of China';
UPDATE ag.iso_country_lookup SET country = 'Tanzania' WHERE country = 'Tanzania, United Republic of';
UPDATE ag.iso_country_lookup SET country = 'U.S. Virgin Islands' WHERE country = 'Virgin Islands, U.S.';
UPDATE ag.iso_country_lookup SET country = 'Brunei' WHERE country = 'Brunei Darussalam';
UPDATE ag.iso_country_lookup SET country = 'Democratic Republic of the Congo' WHERE country = 'Congo, The Democratic Republic of The';
UPDATE ag.iso_country_lookup SET country = 'Falkland Islands (Islas Malvinas)' WHERE country = 'Falkland Islands (Malvinas)';
UPDATE ag.iso_country_lookup SET country = 'French Southern and Antarctic Lands' WHERE country = 'French Southern Territories';
UPDATE ag.iso_country_lookup SET country = 'Iran' WHERE country = 'Iran, Islamic Republic of';
UPDATE ag.iso_country_lookup SET country = 'Laos' WHERE country = 'Lao People''s Democratic Republic';
UPDATE ag.iso_country_lookup SET country = 'Libya' WHERE country = 'Libyan Arab Jamahiriya';
UPDATE ag.iso_country_lookup SET country = 'Macau' WHERE country = 'Macao';
UPDATE ag.iso_country_lookup SET country = 'Macedonia (FYROM)' WHERE country = 'Macedonia, The Former Yugoslav Republic of';
UPDATE ag.iso_country_lookup SET country = 'Tanzania' WHERE country = 'The United Republic of Tanzania';
UPDATE ag.iso_country_lookup SET country = 'Côte d''Ivoire' WHERE country = 'Cote D''ivoire';
UPDATE ag.iso_country_lookup SET country = 'The Bahamas' WHERE country = 'Bahamas';
UPDATE ag.iso_country_lookup SET country = 'The Gambia' WHERE country = 'Gambia';
UPDATE ag.iso_country_lookup SET country = 'Guinea-Bissau' WHERE country = 'Guinea-bissau';
UPDATE ag.iso_country_lookup SET country = 'Heard Island and McDonald Islands' WHERE country = 'Heard Island and Mcdonald Islands';
UPDATE ag.iso_country_lookup SET country = 'Vatican City' WHERE country = 'Holy See (Vatican City State)';
UPDATE ag.iso_country_lookup SET country = 'Myanmar (Burma)' WHERE country = 'Myanmar';
UPDATE ag.iso_country_lookup SET country = 'Palestine' WHERE country = 'Palestinian Territory, Occupied';
UPDATE ag.iso_country_lookup SET country = 'Pitcairn Islands' WHERE country = 'Pitcairn';
UPDATE ag.iso_country_lookup SET country = 'Saint Vincent and the Grenadines' WHERE country = 'Saint Vincent and The Grenadines';
UPDATE ag.iso_country_lookup SET country = 'São Tomé and Príncipe' WHERE country = 'Sao Tome and Principe';
UPDATE ag.iso_country_lookup SET country = 'South Georgia and the South Sandwich Islands' WHERE country = 'South Georgia and The South Sandwich Islands';
UPDATE ag.iso_country_lookup SET country = 'Timor-Leste' WHERE country = 'Timor-leste';
UPDATE ag.iso_country_lookup SET country = 'Vietnam' WHERE country = 'Viet Nam';
UPDATE ag.iso_country_lookup SET country = 'Åland Islands' WHERE country = 'Aland Islands';

-- Add EBI country name column and populate it
ALTER TABLE ag.iso_country_lookup ADD COLUMN EBI varchar;
UPDATE ag.iso_country_lookup SET EBI = country;

-- Alter only countries as needed
UPDATE ag.iso_country_lookup SET EBI = 'Cocos Islands' WHERE country = 'Cocos (Keeling) Islands';
UPDATE ag.iso_country_lookup SET EBI = 'Macedonia' WHERE country = 'Macedonia (FYROM)';
UPDATE ag.iso_country_lookup SET EBI = 'Micronesia' WHERE country = 'Federated States of Micronesia';
UPDATE ag.iso_country_lookup SET EBI = 'Republic of the Congo' WHERE country = 'Congo';
UPDATE ag.iso_country_lookup SET EBI = 'Svalbard' WHERE country = 'Svalbard and Jan Mayen';
UPDATE ag.iso_country_lookup SET EBI = 'USA' WHERE country = 'United States';
UPDATE ag.iso_country_lookup SET EBI = 'Virgin Islands' WHERE country = 'U.S. Virgin Islands';
UPDATE ag.iso_country_lookup SET EBI = 'Cote D''ivoire' WHERE country = 'Côte d''Ivoire';
UPDATE ag.iso_country_lookup SET EBI = 'Bahamas' WHERE country = 'The Bahamas';
UPDATE ag.iso_country_lookup SET EBI = 'Gambia' WHERE country = 'The Gambia';
UPDATE ag.iso_country_lookup SET EBI = 'Myanmar' WHERE country = 'Myanmar (Burma)';
UPDATE ag.iso_country_lookup SET EBI = 'Sao Tome and Principe' WHERE country = 'São Tomé and Príncipe';
UPDATE ag.iso_country_lookup SET EBI = 'Viet Nam' WHERE country = 'Vietnam';
UPDATE ag.iso_country_lookup SET EBI = 'Aland Islands' WHERE country = 'Åland Islands';