CREATE TABLE ag.vioscreen_foodcomponents (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    sessionId varchar NOT NULL,
    code varchar NOT NULL,
    amount float NOT NULL,
    UNIQUE (sessionId, code),
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId)
);
CREATE INDEX vio_foodc_by_sessionid ON ag.vioscreen_foodcomponents(sessionId);
CREATE UNIQUE INDEX vio_foodc_by_sessionidcode ON ag.vioscreen_foodcomponents(sessionId, code);

CREATE TABLE ag.vioscreen_eatingpatterns (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    sessionId varchar NOT NULL,
    code varchar NOT NULL,
    amount float NOT NULL,
    UNIQUE (sessionId, code),
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId)
);
CREATE INDEX vio_eatpa_by_sessionid ON ag.vioscreen_eatingpatterns(sessionId);
CREATE UNIQUE INDEX vio_eatpa_by_sessionidcode ON ag.vioscreen_eatingpatterns(sessionId,code)