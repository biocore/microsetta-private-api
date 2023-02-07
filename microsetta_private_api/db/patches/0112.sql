-- We need to clean up stale state on an account that requested deletion.
-- Using a non-sequential patch filename to ease merging master and master-overhaul soon.
DELETE FROM ag.polyphenol_ffq_registry WHERE account_id = 'b499417a-0840-44da-b269-d243f6eb02ae';
DELETE FROM ag.spain_ffq_registry WHERE account_id = 'b499417a-0840-44da-b269-d243f6eb02ae';
