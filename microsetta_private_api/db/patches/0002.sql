/*
12 December 2014
---------------
Resizes the kit_password column so that a bcrypt hash will fit.
*/
ALTER TABLE ag.ag_kit ALTER COLUMN kit_password TYPE varchar(60);
