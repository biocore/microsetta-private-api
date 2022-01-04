-- empty all the contents of the fulfillment_hold_msg in barcodes.daklapack_order,
-- then change its datatype to a date and rename it to planned_send_date
UPDATE barcodes.daklapack_order
SET fulfillment_hold_msg = null;
ALTER TABLE barcodes.daklapack_order ALTER COLUMN fulfillment_hold_msg TYPE DATE USING fulfillment_hold_msg::date;
ALTER TABLE barcodes.daklapack_order RENAME COLUMN fulfillment_hold_msg TO planned_send_date;
