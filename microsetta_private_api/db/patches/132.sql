-- We have three contributions that contained orders for multiple kits but only one was fulfilled.
-- To fulfills the remaining kits, we're going to create duplicate transactions in an unfulfilled state.

-- First, we'll create duplicate transactions with a suffix on the ID to reflect the manual nature of the process.
-- We're going to set the amount and net_amount columns to 0 so that we're not reflecting duplicate revenue.
INSERT INTO campaign.transaction (
    id,
    interested_user_id,
    transaction_type,
    remote_campaign_id,
    created,
    amount,
    net_amount,
    currency,
    payer_first_name,
    payer_last_name,
    payer_email,
    account_type,
    message,
    subscribed_to_updates
    )
SELECT
    CONCAT(id, '-manual-patch-132'),
    interested_user_id,
    transaction_type,
    remote_campaign_id,
    created,
    0,
    0,
    currency,
    payer_first_name,
    payer_last_name,
    payer_email,
    account_type,
    message,
    subscribed_to_updates
    FROM campaign.transaction WHERE id IN ('73A565339S129053J', '9G656551639672613', '8X951176NJ262430Y');

-- Next, we'll create the new records in campaign.fundrazr_transaction_perk.
-- We'll decrement quantity by 1 to reflect the kit that was already processed for each order.
INSERT INTO campaign.fundrazr_transaction_perk (transaction_id, perk_id, quantity, processed)
SELECT CONCAT(id, '-manual-patch-132'), perk_id, quantity-1, FALSE
    FROM campaign.fundrazr_transaction_perk WHERE transaction_id IN ('73A565339S129053J', '9G656551639672613', '8X951176NJ262430Y');

-- Lastly, we're going to set the original records in campaign.fundrazr_transaction_perk to a quantity of 1 to reflect what was fulfilled
UPDATE campaign.fundrazr_transaction_perk SET quantity = 1 WHERE transaction_id IN ('73A565339S129053J', '9G656551639672613', '8X951176NJ262430Y');

