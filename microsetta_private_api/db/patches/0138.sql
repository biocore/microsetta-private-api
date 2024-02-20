-- Feb 12, 2024
-- Add user_delete_reason to ag.delete_account_queue
ALTER TABLE ag.delete_account_queue
    ADD COLUMN user_delete_reason VARCHAR;

COMMENT ON COLUMN ag.delete_account_queue.user_delete_reason
    IS 'Reason the user gave for deleting the account.';