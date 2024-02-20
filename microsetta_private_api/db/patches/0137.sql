-- Feb 5, 2024
-- Add delete_reason to ag.account_removal_log
ALTER TABLE ag.account_removal_log
    ADD COLUMN delete_reason VARCHAR;

COMMENT ON COLUMN ag.account_removal_log.delete_reason
    IS 'Reason the admin gave for deleting the account.';