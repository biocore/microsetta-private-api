/*
10 December 2014
---------------
Adds a column for the Open Humans access token to the ag_kit table.
*/
ALTER TABLE ag.ag_kit ADD COLUMN open_humans_token varchar(64);

COMMENT ON COLUMN ag.ag_kit.open_humans_token IS 'The Open Humans access token corresponding to the Open Humans user that has authorized data sharing with this kit.';
