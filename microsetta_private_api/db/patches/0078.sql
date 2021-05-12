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

CREATE TABLE ag.vioscreen_percentenergy (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    sessionId varchar NOT NULL,
    code varchar NOT NULL,
    amount float NOT NULL,
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId)
);
CREATE INDEX vio_peren_by_sessionid ON ag.vioscreen_percentenergy(sessionId);
CREATE UNIQUE INDEX vio_peren_sessionidcode ON ag.vioscreen_percentenergy(sessionId, code);

CREATE TABLE ag.vioscreen_dietaryscore (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    sessionId varchar NOT NULL,
    scoresType varchar NOT NULL,
    code varchar NOT NULL,
    score float NOT NULL,
    UNIQUE (sessionId, scoresType, code),
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId)
);
CREATE INDEX vio_diet_by_sessionid ON ag.vioscreen_dietaryscore(sessionId);

CREATE TABLE ag.vioscreen_supplements (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    sessionId varchar NOT NULL,
    supplement varchar NOT NULL,
    frequency varchar NOT NULL,
    amount varchar NOT NULL,
    average varchar NOT NULL,
    UNIQUE (sessionId, supplement),
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId)
);
CREATE INDEX vio_supp_by_sessionid ON ag.vioscreen_supplements(sessionId);
