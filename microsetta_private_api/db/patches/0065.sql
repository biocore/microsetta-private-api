CREATE TABLE ag.event_log(
    id uuid PRIMARY KEY NOT NULL,
    event_type varchar(100) NOT NULL,
    event_subtype varchar(100) NOT NULL,
    event_time timestamptz default current_timestamp NOT NULL,
    event_state jsonb);

-- Full event log sorted by time
CREATE INDEX idx_event_log_event_time ON ag.event_log (event_time);
-- Event log filtered by type sorted by time
CREATE INDEX idx_event_log_event_type_event_time ON ag.event_log (event_type, event_time);
-- Event log filtered by type and subtype sorted by time
CREATE INDEX idx_event_log_event_type_event_subtype_event_time ON ag.event_log (event_type, event_subtype, event_time);
-- Event log filtered by user email sorted by time
CREATE INDEX idx_events_state_email_time ON ag.event_log ((event_state->>'email'), event_time);
-- Event log filtered by user account id sorted by time
CREATE INDEX idx_events_state_account_id_time ON ag.event_log ((event_state->>'account_id'), event_time);
