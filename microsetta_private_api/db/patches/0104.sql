ALTER TABLE campaign.fundrazr_perk ADD COLUMN perk_type VARCHAR;
ALTER TABLE campaign.transaction ADD status VARCHAR;

--new patch to remove the not a null constraint in the account table for column created_with_kit_id
ALTER TABLE ag.account ALTER COLUMN created_with_kit_id DROP NOT NULL;
