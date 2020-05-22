-- BUGFIX: Due to crash on logging in legacy users, we set nullable string
-- fields of the account table that can appear in yaml object to empty string

-- Fields, Should be updated
-- id,      No
-- email,   No
-- account_type, No
-- auth_issuer, No
-- auth_sub, No
-- first_name, Yes
-- last_name, Yes
-- street, Yes
-- city, Yes
-- state, Yes
-- post_code, Yes
-- country_code, Yes
-- latitude, No
-- longitude, No
-- cannot_geocode, No
-- elevation, No
-- creation_time, No
-- update_time, No

UPDATE ag.account
    SET first_name=''
    WHERE first_name is null;
UPDATE ag.account
    SET last_name=''
    WHERE last_name is null;
UPDATE ag.account
    SET street=''
    WHERE street is null;
UPDATE ag.account
    SET city=''
    WHERE city is null;
UPDATE ag.account
    SET state=''
    WHERE state is null;
UPDATE ag.account
    SET post_code=''
    WHERE post_code is null;
UPDATE ag.account
    SET country_code=''
    WHERE country_code is null;
