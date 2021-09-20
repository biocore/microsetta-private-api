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
CREATE UNIQUE INDEX vio_eatpa_by_sessionidcode ON ag.vioscreen_eatingpatterns(sessionId,code);

CREATE TABLE ag.vioscreen_mpeds (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    sessionId varchar NOT NULL,
    code varchar NOT NULL,
    amount float NOT NULL,
    UNIQUE (sessionId, code),
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId)
);
CREATE INDEX vio_mpeds_by_sessionid ON ag.vioscreen_mpeds(sessionId);
CREATE UNIQUE INDEX vio_mpeds_by_sessionidcode ON ag.vioscreen_mpeds(sessionId,code);

CREATE TABLE ag.vioscreen_foodconsumption (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    sessionId varchar NOT NULL,
    foodCode varchar NOT NULL,
    description varchar NOT NULL,
    foodGroup varchar NOT NULL,
    amount varchar NOT NULL,
    frequency varchar NOT NULL,
    consumptionAdjustment varchar NOT NULL,
    servingSizeText varchar NOT NULL,
    servingFrequencyText varchar NOT NULL,
    created varchar NOT NULL,
    UNIQUE (sessionId, description),
    FOREIGN KEY (sessionId) REFERENCES ag.vioscreen_sessions (sessionId)
);
CREATE INDEX vio_consu_by_sessionid ON ag.vioscreen_foodconsumption(sessionId);
CREATE UNIQUE INDEX vio_consu_by_sessioniddesc ON ag.vioscreen_foodconsumption(sessionId, description);

CREATE TABLE ag.vioscreen_foodconsumptioncomponents (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    sessionId varchar NOT NULL,
    description varchar NOT NULL,
    code varchar NOT NULL,
    amount float NOT NULL,
    UNIQUE (sessionId, description, code),
    FOREIGN KEY (sessionId, description) REFERENCES ag.vioscreen_foodconsumption(sessionId, description)
);
CREATE INDEX vio_consuc_by_sessionid ON ag.vioscreen_foodconsumptioncomponents(sessionId);
CREATE UNIQUE INDEX vio_consuc_by_sessioniddesccode ON ag.vioscreen_foodconsumptioncomponents(sessionId, description, code);