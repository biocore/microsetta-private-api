/*
24 April 2015
----------------
Add columns needed for new UCSD consent parameters
*/
ALTER TABLE ag.ag_consent ADD COLUMN date_signed date, ADD COLUMN assent_obtainer varchar, ADD COLUMN age_range varchar;
