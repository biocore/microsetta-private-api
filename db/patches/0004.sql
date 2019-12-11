/*
25 February 2015
----------------
Resizes the kit_password column so that a bcrypt hash will fit.
*/
ALTER TABLE ag.ag_handout_kits ALTER COLUMN password TYPE varchar(60);
