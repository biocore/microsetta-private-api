-- create a column that can be used to record what kit was used 
-- when the account was created. 
ALTER TABLE ag.account ADD COLUMN created_with_kit_id VARCHAR;

-- from existing accounts, recover a kit that is associated with
-- the account. if someone has a single kit, then that kit is used
-- and has to be what was registered with. If they have multiple
-- kits, then we'll just pick one of them as in the old system,
-- users would have had to register with each kit individually.
-- This should be suitable for newly created accounts where 
-- people have assigned samples.
UPDATE ag.account a SET created_with_kit_id = ss.kit_id
    FROM (SELECT s.account_id, (array_agg(supplied_kit_id))[1] AS kit_id 
          FROM ag.ag_kit ak 
             JOIN ag.ag_kit_barcodes akb USING (ag_kit_id) 
             INNER JOIN ag.source s ON (akb.source_id=s.id) 
          GROUP BY s.account_id) ss
    WHERE a.id = ss.account_id;

-- a large number of kits have samples that were never assigned, 
-- which resulted in them not being linked to the "source" table
-- during migration. to handle this, let's use the older links in 
-- the database.
UPDATE ag.account SET created_with_kit_id=subquery.kit_id
    FROM (SELECT ag_login_id, (array_agg(supplied_kit_id))[1] AS kit_id
          FROM ag.account a
              JOIN ag.ag_kit ak ON a.id=ak.ag_login_id
              JOIN ag.ag_kit_barcodes USING(ag_kit_id)
          WHERE created_with_kit_id IS NULL 
          GROUP BY ag_login_id) AS subquery
    WHERE id=subquery.ag_login_id;

-- finally, there are a handful where the created_with_kit_id remains null.
-- on inspection, this appears to happen in the new system when someone
-- has created an account but hasn't yet claimed samples from a kit. We'll 
-- set those to the empty string so that we can make created_with_kit_id
-- not null
UPDATE ag.account SET created_with_kit_id=''
    WHERE created_with_kit_id IS NULL;

ALTER TABLE ag.account ALTER COLUMN created_with_kit_id SET NOT NULL;