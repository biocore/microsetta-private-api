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
    startDate timestamp NOT NULL,
    endDate timestamp,
    cultureCode varchar NOT NULL,
    created timestamp NOT NULL,
    modified timestamp NOT NULL
);

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

