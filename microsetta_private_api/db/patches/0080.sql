CREATE TABLE ag.vioscreen_foodcomponents (
    id uuid DEFAULT uuid_generate_v4() NOT NULL,
    sessionId varchar NOT NULL,
    code varchar NOT NULL,
    amount float NOT NULL,
    CONSTRAINT vioscreen_foodcomponents_pkey PRIMARY KEY ( id ),
    UNIQUE (sessionId, code),
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId)
);
CREATE INDEX vio_foodc_by_sessionid ON ag.vioscreen_foodcomponents(sessionId);