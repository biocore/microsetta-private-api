-- create tables to match new models for sessions and percent energy data
DROP TABLE IF EXISTS ag.vioscreen_percentenergy;
DROP TABLE IF EXISTS ag.vioscreen_dietaryscore;
DROP TABLE IF EXISTS ag.vioscreen_foodconsumption;
DROP TABLE IF EXISTS ag.vioscreen_eatingpatterns;
DROP TABLE IF EXISTS ag.vioscreen_mpeds;
DROP TABLE IF EXISTS ag.vioscreen_percentenergy;
DROP TABLE IF EXISTS ag.vioscreen_foodcomponents;

CREATE TABLE ag.vioscreen_sessions (
    sessionId varchar PRIMARY KEY,
    username varchar NOT NULL,
    protocolId int NOT NULL,
    status varchar NOT NULL,
    startDate timestamp,  -- a startDate can be null when status is 'New'
    endDate timestamp,
    cultureCode varchar NOT NULL,
    created timestamp NOT NULL,
    modified timestamp NOT NULL
    -- no FK is set to ag.vioscreen_registry.vio_id <-> username
    -- as ag.vioscreen_registry.vio_id is not assured to be UNIQUE.
    -- this is due to the historical relationship of 1 FFQ to many 
    -- samples. 
);
CREATE INDEX vio_sess_by_username ON ag.vioscreen_sessions(username);

CREATE TABLE ag.vioscreen_percentenergy_code (
    code varchar PRIMARY KEY,
    description varchar NOT NULL,
    shortDescription varchar NOT NULL,
    units varchar NOT NULL
);

CREATE TABLE ag.vioscreen_percentenergy (
    id uuid DEFAULT uuid_generate_v4() NOT NULL,
    sessionId varchar NOT NULL,
    code varchar NOT NULL,
    amount float NOT NULL,
    CONSTRAINT vioscreen_percentenergy_pkey PRIMARY KEY ( id ),
    UNIQUE (sessionId, code),
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId),
    FOREIGN KEY (code) REFERENCES ag.vioscreen_percentenergy_code (code)
);
CREATE INDEX vio_peren_by_sessionid ON ag.vioscreen_percentenergy(sessionId);

INSERT INTO ag.vioscreen_percentenergy_code
    (code, description, shortDescription, units)
    VALUES ('%mfatot', 'Percent of calories from Monounsaturated Fat', 'Monounsaturated Fat', '%');
INSERT INTO ag.vioscreen_percentenergy_code
    (code, description, shortDescription, units)
    VALUES ('%pfatot', 'Percent of calories from Polyunsaturated Fat', 'Polyunsaturated Fat', '%');
INSERT INTO ag.vioscreen_percentenergy_code
    (code, description, shortDescription, units)
    VALUES ('%carbo', 'Percent of calories from Carbohydrate', 'Carbohydrate', '%');
INSERT INTO ag.vioscreen_percentenergy_code
    (code, description, shortDescription, units)
    VALUES ('%sfatot', 'Percent of calories from Saturated Fat', 'Saturated Fat', '%');
INSERT INTO ag.vioscreen_percentenergy_code
    (code, description, shortDescription, units)
    VALUES ('%alcohol', 'Percent of calories from Alcohol', 'Alcohol', '%');
INSERT INTO ag.vioscreen_percentenergy_code
    (code, description, shortDescription, units)
    VALUES ('%protein', 'Percent of calories from Protein', 'Protein', '%');
INSERT INTO ag.vioscreen_percentenergy_code
    (code, description, shortDescription, units)
    VALUES ('%adsugtot', 'Percent of calories from Added Sugar', 'Added Sugar', '%');
INSERT INTO ag.vioscreen_percentenergy_code
    (code, description, shortDescription, units)
    VALUES ('%fat', 'Percent of calories from Fat', 'Fat', '%');
