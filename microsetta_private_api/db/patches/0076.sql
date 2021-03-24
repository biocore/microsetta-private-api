-- create tables to match new models for sessions and percent energy data
DROP TABLE ag.vioscreen_sessions
DROP TABLE ag.vioscreen_percentenergy

CREATE TABLE ag.vioscreen_sessions (
    sessionId varchar PRIMARY KEY,
    username varchar,
    protocolId int,
    status varchar,
    startDate timestamp,
    endDate timestamp,
    cultureCode varchar,
    created timestamp,
    modified timestamp
);

CREATE TABLE ag.vioscreen_percentenergy (
    sessionId varchar PRIMARY KEY,
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId)
);

CREATE TABLE ag.vioscreen_energycomponent (
    sessionId varchar PRIMARY KEY,
    code varchar,
    description varchar,
    shortDescription varchar,
    units varchar,
    amount float,
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_percentenergy (sessionId)
);