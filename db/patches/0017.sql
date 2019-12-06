-- August 17, 2015
-- Rearrange barcodes to be attached to the correct projects
Do $do$
DECLARE
    ag_pid bigint;
    pid bigint;
BEGIN
ag_pid := (SELECT project_id FROM barcodes.project WHERE project = 'American Gut Project');

-- Assign british gut kits to british gut and american gut
CREATE TEMP TABLE hold_table (
    barcode varchar,
    project_id bigint
);

pid := (SELECT project_id FROM barcodes.project WHERE project = 'British Gut Project');

INSERT INTO hold_table (project_id, barcode)
    SELECT pid, barcode FROM (
        SELECT barcode FROM ag.ag_kit_barcodes
        JOIN ag.ag_kit USING (ag_kit_id)
        WHERE lower(supplied_kit_id) LIKE '%bg\_%'
        UNION
        SELECT barcode from ag.ag_handout_barcodes
        JOIN ag.ag_handout_kits USING (kit_id)
        WHERE lower(kit_id) LIKE '%bg\_%') AS b;

INSERT INTO hold_table (project_id, barcode)
    SELECT ag_pid, barcode FROM hold_table;

INSERT INTO barcodes.project_barcode (project_id, barcode)
    SELECT project_id, barcode FROM hold_table
    WHERE (project_id, barcode) NOT IN
        (SELECT project_id, barcode FROM barcodes.project_barcode);

DROP TABLE hold_table;

-- rename Anxiety/Depression cohort to 'Mind and microbiome'
UPDATE barcodes.project SET project = 'Mind and microbiome'
WHERE project = 'Anxiety/Depression cohort';

CREATE TEMP TABLE hold_table (
    barcode varchar,
    project_id bigint
);

pid := (SELECT project_id FROM barcodes.project WHERE project = 'Mind and microbiome');

INSERT INTO hold_table (project_id, barcode)
    SELECT pid, barcode FROM (
        SELECT barcode FROM ag.ag_kit_barcodes
        JOIN ag.ag_kit USING (ag_kit_id)
        WHERE lower(supplied_kit_id) LIKE '%stz\_%'
        UNION
        SELECT barcode from ag.ag_handout_barcodes
        JOIN ag.ag_handout_kits USING (kit_id)
        WHERE lower(kit_id) LIKE '%stz\_%') AS b;

INSERT INTO hold_table (project_id, barcode)
    SELECT ag_pid, barcode FROM hold_table;

INSERT INTO barcodes.project_barcode (project_id, barcode)
    SELECT project_id, barcode FROM hold_table
    WHERE (project_id, barcode) NOT IN
        (SELECT project_id, barcode FROM barcodes.project_barcode);

DROP TABLE hold_table;

-- Assign PGP kits to american gut and PGP
CREATE TEMP TABLE hold_table (
    barcode varchar,
    project_id bigint
);

pid := (SELECT project_id FROM barcodes.project WHERE project = 'Personal Genome Project');

INSERT INTO hold_table (project_id, barcode)
    SELECT pid, barcode FROM (
        SELECT barcode FROM ag.ag_kit_barcodes
        JOIN ag.ag_kit USING (ag_kit_id)
        WHERE lower(supplied_kit_id) LIKE '%pgp\_%'
        UNION
        SELECT barcode from ag.ag_handout_barcodes
        JOIN ag.ag_handout_kits USING (kit_id)
        WHERE lower(kit_id) LIKE '%pgp\_%') AS b;

INSERT INTO hold_table (project_id, barcode)
    SELECT ag_pid, barcode FROM hold_table;

INSERT INTO barcodes.project_barcode (project_id, barcode)
    SELECT project_id, barcode FROM hold_table
    WHERE (project_id, barcode) NOT IN
        (SELECT project_id, barcode FROM barcodes.project_barcode);

DROP TABLE hold_table;

-- Assign barcodes to American Gut and Sleep Study
CREATE TEMP TABLE hold_table (
    barcode varchar,
    project_id bigint
);

pid := (SELECT project_id FROM barcodes.project WHERE project = 'Sleep Study');

INSERT INTO hold_table (project_id, barcode)
    SELECT pid, barcode FROM (
        SELECT barcode FROM ag.ag_kit_barcodes
        JOIN ag.ag_kit USING (ag_kit_id)
        WHERE lower(supplied_kit_id) LIKE '%slp\_%'
        UNION
        SELECT barcode from ag.ag_handout_barcodes
        JOIN ag.ag_handout_kits USING (kit_id)
        WHERE lower(kit_id) LIKE '%slp\_%') AS b;

INSERT INTO hold_table (project_id, barcode)
    SELECT ag_pid, barcode FROM hold_table;

INSERT INTO barcodes.project_barcode (project_id, barcode)
    SELECT project_id, barcode FROM hold_table
    WHERE (project_id, barcode) NOT IN
        (SELECT project_id, barcode FROM barcodes.project_barcode);

DROP TABLE hold_table;

-- Create ASD project
INSERT INTO project (project_id, project)
    SELECT max(project_id)+1, 'Autism Spectrum Disorder'
    FROM project;

pid := (SELECT project_id FROM barcodes.project WHERE project = 'Autism Spectrum Disorder');

-- Assign all ASD kits to ASD project and American Gut
CREATE TEMP TABLE hold_table (
    barcode varchar,
    project_id bigint
);

INSERT INTO hold_table (project_id, barcode)
    SELECT pid, barcode FROM (
        SELECT barcode FROM ag.ag_kit_barcodes
        JOIN ag.ag_kit USING (ag_kit_id)
        WHERE lower(supplied_kit_id) LIKE '%asd\_%'
        OR lower(supplied_kit_id) LIKE '%asdp\_%'
        UNION
        SELECT barcode from ag.ag_handout_barcodes
        JOIN ag.ag_handout_kits USING (kit_id)
        WHERE lower(kit_id) LIKE '%asd\_%'
        OR lower(kit_id) LIKE '%asdp\_%') AS b;

INSERT INTO hold_table (project_id, barcode)
    SELECT ag_pid, barcode FROM hold_table;

INSERT INTO barcodes.project_barcode (project_id, barcode)
    SELECT project_id, barcode FROM hold_table
    WHERE (project_id, barcode) NOT IN
        (SELECT project_id, barcode FROM barcodes.project_barcode);

DROP TABLE hold_table;

-- Unassign from American gut and assign to 'Amnon Oral Timeseries'
CREATE TEMP TABLE hold_table (
    barcode varchar,
    project_id bigint
);

INSERT INTO project (project_id, project)
    SELECT max(project_id)+1, 'Amnon Oral Timeseries' FROM project;

pid := (SELECT project_id FROM barcodes.project WHERE project = 'Amnon Oral Timeseries');
INSERT INTO hold_table (project_id, barcode)
    SELECT pid, barcode FROM (
        SELECT barcode FROM ag.ag_kit_barcodes
        JOIN ag.ag_kit USING (ag_kit_id)
        WHERE lower(supplied_kit_id) LIKE '%mts\_%'
        OR lower(supplied_kit_id) LIKE '%osc\_%'
        OR lower(supplied_kit_id) LIKE '%pulse\_%'
        UNION
        SELECT barcode from ag.ag_handout_barcodes
        JOIN ag.ag_handout_kits USING (kit_id)
        WHERE lower(kit_id) LIKE '%mts\_%'
        OR lower(kit_id) LIKE '%osc\_%'
        OR lower(kit_id) LIKE '%pulse\_%') AS b;

INSERT INTO barcodes.project_barcode (project_id, barcode)
    SELECT project_id, barcode FROM hold_table;

DELETE FROM barcodes.project_barcode
WHERE barcode IN (SELECT barcode FROM hold_table)
AND project_id = ag_pid;

DROP TABLE hold_table;
END $do$
