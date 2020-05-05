-- automatically record the time the survey was stored
ALTER TABLE ag.ag_login_surveys ADD COLUMN creation_time timestamptz DEFAULT current_timestamp;
