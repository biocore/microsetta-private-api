CREATE TABLE ag.event_log(
    id uuid PRIMARY KEY NOT NULL,
    event_type varchar(100) NOT NULL,
    event_time timestamptz default current_timestamp,
    event_subtype varchar(100) NOT NULL,
    event_state jsonb);

CREATE UNIQUE INDEX idx_event_log_event_time ON ag.event_log (event_time);
CREATE UNIQUE INDEX idx_event_log_event_type_event_time ON ag.event_log (event_type, event_time);
CREATE UNIQUE INDEX idx_events_type_time ON ag.event_log (event_type, event_time);

