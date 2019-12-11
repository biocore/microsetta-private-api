-- This script is used to scrub the live American Gut database in order to
-- generate a test database for Travis without personal information but
-- representative of the real world.

-- Function to generate a string with all the different characters present in
-- a column (adapted from: http://dba.stackexchange.com/a/83679)
CREATE FUNCTION retrieve_chars(column_name varchar, table_name varchar) RETURNS varchar AS $$
    DECLARE
        result varchar;
    BEGIN
         EXECUTE format(
            'SELECT string_agg(c, '''') FROM (SELECT DISTINCT regexp_split_to_table(%s, '''') AS c FROM %s) t',
            column_name, table_name)
         INTO result;
         RETURN result;
    END;
$$ language plpgsql;

-- Function to generate random strings of a given length from a given set
-- of characters (adapted from: http://stackoverflow.com/a/3972983/3746629)
CREATE FUNCTION random_string(length integer, source varchar, suffix varchar) RETURNS varchar AS $$
    DECLARE
        result varchar;
        chars text[];
    BEGIN
        chars := regexp_split_to_array(source, '');
        result := suffix;
        FOR i in 1..length LOOP
            result := result || chars[1+random()*(array_length(chars, 1) - 1)];
        END LOOP;
        RETURN result;
    END;
$$ language plpgsql;

-- Function to generate a random latitude or longitude
CREATE FUNCTION random_lat_or_long() RETURNS float8 AS $$
    DECLARE
        result varchar;
        numsource varchar;
    BEGIN
        numsource := '0123456789';
        result := random_string(2, numsource, '') || '.' || random_string(5, numsource, '');
        IF random() < 0.5 THEN
            result := '-' || result;
        END IF;
        RETURN result::float8;
    END;
$$ language plpgsql;

-- Function to generate random emails
CREATE FUNCTION random_email(source varchar) RETURNS varchar AS $$
    BEGIN
        RETURN random_string(10, source, '') || '@' || random_string(5, source, '') || '.' || random_string(3, source, '');
    END;
$$ language plpgsql;

-- Function to generate random dates
CREATE FUNCTION random_date() RETURNS varchar AS $$
    DECLARE
        result varchar;
    BEGIN
        SELECT date(now() - trunc(random()  * 80) * '1 year'::interval - trunc(random() * 12) * '1 month'::interval - trunc(random() * 30) * '1 day'::interval) INTO result;
        RETURN result;
    END
$$ language plpgsql;

-- Create a temp table for storing the zipcodes
CREATE TEMP TABLE allzipcodes AS
    SELECT DISTINCT zip_code FROM ag.ag_human_survey;

-- Create a temp table to be able to generate the source string
CREATE TEMP TABLE allsources (source varchar);

-- We have all the functions that we need, start scrubbing data
DO $do$
DECLARE
    rec         RECORD;
    rec2        RECORD;
    numsource   varchar;
    source      varchar;
    source2     varchar;
    emailsource varchar;
    passwd      varchar;
    numsteps    int;
    currstep    int;
BEGIN
    numsteps := 18;
    currstep := 1;
    -- To simplify testing, all the passwords are going to be the same ('test')
    passwd := '$2a$12$rX8UTcDkIj8bwcxZ22iRpebAxblEclT83xBiUIdJGUJGoUfznu1RK';
    numsource := '0123456789';

    RAISE NOTICE 'STEP % of %: Gathering all characters', currstep, numsteps;
    currstep := currstep + 1;
    INSERT INTO allsources VALUES (retrieve_chars('participant_name', 'ag.ag_survey_multiples_backup')),
                                  (retrieve_chars('item_value', 'ag.ag_survey_multiples_backup')),
                                  (retrieve_chars('verification_code', 'ag.ag_handout_kits')),
                                  (retrieve_chars('project', 'barcodes.project')),
                                  (retrieve_chars('participant_name', 'ag.consent_revoked')),
                                  (retrieve_chars('participant_name', 'ag.ag_consent')),
                                  (retrieve_chars('parent_1_name', 'ag.ag_consent')),
                                  (retrieve_chars('parent_2_name', 'ag.ag_consent')),
                                  (retrieve_chars('assent_obtainer', 'ag.ag_consent')),
                                  (retrieve_chars('participant_name', 'ag.ag_login_surveys')),
                                  (retrieve_chars('participant_name', 'ag.ag_human_survey')),
                                  (retrieve_chars('parent_1_name', 'ag.ag_human_survey')),
                                  (retrieve_chars('parent_2_name', 'ag.ag_human_survey')),
                                  (retrieve_chars('foodallergies_other_text', 'ag.ag_human_survey')),
                                  (retrieve_chars('race_other', 'ag.ag_human_survey')),
                                  (retrieve_chars('antibiotic_condition', 'ag.ag_human_survey')),
                                  (retrieve_chars('primary_vegetable', 'ag.ag_human_survey')),
                                  (retrieve_chars('primary_carb', 'ag.ag_human_survey')),
                                  (retrieve_chars('mainfactor_other_1', 'ag.ag_human_survey')),
                                  (retrieve_chars('mainfactor_other_2', 'ag.ag_human_survey')),
                                  (retrieve_chars('mainfactor_other_3', 'ag.ag_human_survey')),
                                  (retrieve_chars('about_yourself_text', 'ag.ag_human_survey')),
                                  (retrieve_chars('participant_name_u', 'ag.ag_human_survey')),
                                  (retrieve_chars('response', 'ag.survey_answers_other')),
                                  (retrieve_chars('participant_name', 'ag.ag_participant_exceptions')),
                                  (retrieve_chars('participant_name', 'ag.ag_animal_survey')),
                                  (retrieve_chars('comments', 'ag.ag_animal_survey')),
                                  (retrieve_chars('address', 'ag.ag_login')),
                                  (retrieve_chars('city', 'ag.ag_login')),
                                  (retrieve_chars('state', 'ag.ag_login')),
                                  (retrieve_chars('participant_name', 'ag.ag_survey_answer')),
                                  (retrieve_chars('answer', 'ag.ag_survey_answer')),
                                  (retrieve_chars('participant_name', 'ag.ag_survey_multiples')),
                                  (retrieve_chars('item_value', 'ag.ag_survey_multiples')),
                                  (retrieve_chars('kit_verification_code', 'ag.ag_kit')),
                                  (retrieve_chars('notes', 'ag.ag_kit_barcodes')),
                                  (retrieve_chars('other_text', 'ag.ag_kit_barcodes'));

    source := retrieve_chars('source', 'allsources');

    RAISE NOTICE 'STEP % of %: Gathering all email characters', currstep, numsteps;
    currstep := currstep + 1;
    DELETE FROM allsources;
    INSERT INTO allsources VALUES (retrieve_chars('participant_email', 'ag.consent_revoked')),
                                  (retrieve_chars('participant_email', 'ag.ag_consent')),
                                  (retrieve_chars('participant_email', 'ag.ag_human_survey')),
                                  (retrieve_chars('email', 'ag.ag_login'));
    emailsource := retrieve_chars('source', 'allsources');
    emailsource := lower(replace(replace(replace(replace(replace(emailsource, '@', ''), '.', ''), ' ', ''), '!', ''), ',', ''));

    RAISE NOTICE 'STEP % of %: Scrubbing ag_survey_multiples_backup', currstep, numsteps;
    currstep := currstep + 1;
    -- Table: ag_survey_multiples_backup; Columns: participant_name, item_value
    UPDATE ag.ag_survey_multiples_backup SET participant_name = random_string(10, source, 'Name - '),
                                             item_value = random_string(30, source, 'Free text - ');

    -- Table: ag_handout_kits; Columns: password and verification_code
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_handout_kits', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.ag_handout_kits SET password = passwd,
                                  verification_code = random_string(5, source, '');

    -- Table project; Columns: project
    RAISE NOTICE 'STEP % of %: Scrubbing barcodes.project', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE barcodes.project SET project = random_string(10, source, 'Project - ')
        WHERE project != 'American Gut Project';

    -- Table: consent_revoked; Columns: participant_name, participant_email
    RAISE NOTICE 'STEP % of %: Scrubbing ag.consent_revoked', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.consent_revoked SET participant_name = random_string(10, source, 'Name - '),
                                  participant_email = random_email(emailsource);

    -- Table: ag_consent; Columns: participant_name, participant_email,
    -- parent_1_name, parent_2_name, assent_obtainer
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_consent and ag.ag_login_surveys', currstep, numsteps;
    currstep := currstep + 1;
    ALTER TABLE ag.ag_login_surveys
        DROP CONSTRAINT fk_ag_login_surveys0,
        ADD CONSTRAINT fk_ag_login_surveys0 FOREIGN KEY ( ag_login_id, participant_name ) REFERENCES ag.ag_consent( ag_login_id, participant_name ) ON UPDATE CASCADE ON DELETE RESTRICT;

    UPDATE ag.ag_consent SET participant_name = random_string(10, source, 'Name - '),
                             participant_email = random_email(emailsource),
                             parent_1_name = random_string(10, source, 'Name - '),
                             parent_2_name = random_string(10, source, 'Name - '),
                             assent_obtainer = random_string(10, source, 'Name - ');

     ALTER TABLE ag.ag_login_surveys
         DROP CONSTRAINT fk_ag_login_surveys0,
         ADD CONSTRAINT fk_ag_login_surveys0 FOREIGN KEY ( ag_login_id, participant_name ) REFERENCES ag.ag_consent( ag_login_id, participant_name );

    -- Table: ag_human_survey; Columns: participant_name, parent_1_name,
    -- parent_2_name, birth_date, phone_num, zip_code, foodallergies_other_text,
    -- race_other, antibiotic_condition, primary_vegetable, primary_carb,
    -- mainfactor_other_1, mainfactor_other_2, mainfactor_other_3,
    -- about_yourself_text, participant_email, participant_name_u
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_human_survey', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.ag_human_survey SET participant_name = random_string(10, source, 'Name - '),
                                  parent_1_name = random_string(10, source, 'Name - '),
                                  parent_2_name = random_string(10, source, 'Name - '),
                                  birth_date = random_date(),
                                  phone_num = random_string(10, numsource, ''),
                                  zip_code = (SELECT zip_code FROM allzipcodes ORDER BY RANDOM() LIMIT 1),
                                  foodallergies_other_text = random_string(50, source, 'Free text - '),
                                  race_other = random_string(20, source, 'Free text - '),
                                  antibiotic_condition = random_string(30, source, 'Free text - '),
                                  primary_vegetable = random_string(15, source, 'Free text - '),
                                  primary_carb = random_string(15, source, 'Free text - '),
                                  mainfactor_other_1 = random_string(20, source, 'Free text - '),
                                  mainfactor_other_2 = random_string(20, source, 'Free text - '),
                                  mainfactor_other_3 = random_string(20, source, 'Free text - '),
                                  about_yourself_text = random_string(100, source, 'Free text - '),
                                  participant_email = random_email(emailsource),
                                  participant_name_u = random_string(10, source, 'Name - ');

    -- Table: ag_survey_answer; randomize the birth month
    -- Magic number 111: birth month question
    -- Adapted from http://dba.stackexchange.com/a/55401
    RAISE NOTICE 'STEP % of %: Scrubbing ag.survey_answers', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.survey_answers
        SET response = ('[0:11]={January,February,March,April,May,June,July,August,September,October,November,December}'::text[])[trunc(random()*12)]
        WHERE survey_question_id = 111;

    -- Table: survey_answers_other; Columns: response
    -- This column is stored in a weird way. It looks like a python list, but
    -- it always have a single element, even if it is an empty string. Thus,
    -- removing those characters that can break this structure
    source2 := replace(replace(replace(source, '""', ''), '[', ''), ']', '');
    RAISE NOTICE 'STEP % of %: Scrubbing ag.survey_answers_other', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.survey_answers_other SET response = '["' || random_string(20, source2, 'Free text - ') || '"]';

    -- Table: ag_participant_exceptions; columns: participant_name
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_participant_exceptions', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.ag_participant_exceptions SET participant_name = random_string(10, source, 'Name - ');

    -- Table: ag_animal_survey; Columns: participant_name, comments
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_animal_survey', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.ag_animal_survey SET participant_name = random_string(10, source, 'Name - '),
                                   comments = random_string(50, source, 'Free text - ');

    -- Table: ag_login; columns: email, name, address, city, state, zip, latitude, longitude
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_login', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.ag_login SET email = random_email(emailsource),
                           name = random_string(10, source, 'Name -'),
                           address = random_string(4, numsource, '') || random_string(10, source, ' '),
                           city = random_string(10, source, 'City - '),
                           state = random_string(10, source, 'State - '),
                           zip = random_string(5, numsource, ''),
                           latitude = random_lat_or_long(),
                           longitude = random_lat_or_long();

    -- Table: ag_survey_answer; columns: participant_name, answer
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_survey_answer', currstep, numsteps;
    currstep := currstep + 1;
    WITH vals AS (SELECT DISTINCT ON (participant_name) participant_name original_name, random_string(10, source, 'Name - ') newname FROM ag.ag_survey_answer)
        UPDATE ag.ag_survey_answer SET participant_name = newname,
                                       answer = random_string(30, source, 'Free text - ')
        FROM vals
        WHERE participant_name = original_name;

    -- Table: ag_survey_multiples; Columns: participant_name, item_value
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_survey_multiples', currstep, numsteps;
    currstep := currstep + 1;
    WITH vals AS (SELECT DISTINCT ON (participant_name) participant_name original_name, random_string(10, source, 'Name - ') newname FROM ag.ag_survey_answer)
        UPDATE ag.ag_survey_multiples SET participant_name = newname,
                                          item_value = random_string(10, source, 'Free text - ')
            FROM vals
            WHERE participant_name = original_name;

    -- Table: ag_kit; columns: kit_password, kit_verification_code, open_humans_token
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_kit', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.ag_kit SET kit_password = passwd,
                         kit_verification_code = random_string(5, source, ''),
                         open_humans_token = NULL;

    --Table: ag_kit_barcodes; columns: notes, other_text
    RAISE NOTICE 'STEP % of %: Scrubbing ag.ag_kit_barcodes', currstep, numsteps;
    currstep := currstep + 1;
    UPDATE ag.ag_kit_barcodes
        SET notes = random_string(50, source, 'Free text - '),
            other_text = random_string(50, source, 'Free text - ');

    -- Table: labadmin_users; columns: email, password
    RAISE NOTICE 'STEP % of %: Scrubbing labadmin user tables', currstep, numsteps;
    currstep := currstep + 1;
    -- For this table it is easier to drop everybody and add a test user
    DELETE FROM ag.labadmin_users_access;
    DELETE FROM ag.labadmin_users;
    INSERT INTO ag.labadmin_users (email, password) VALUES ('test', passwd);
    -- Magic number 7 -> admin access
    INSERT INTO ag.labadmin_users_access (email, access_id) VALUES ('test', 7);

END $do$;

-- Set this database as a test database
UPDATE ag.settings SET test_environment = 'true';


-- Drop the functions that we created
DROP FUNCTION retrieve_chars(varchar, varchar);
DROP FUNCTION random_string(integer, varchar, varchar);
DROP FUNCTION random_email(varchar);
DROP FUNCTION random_date();
DROP FUNCTION random_lat_or_long();

DROP TABLE allsources;
DROP TABLE allzipcodes;
