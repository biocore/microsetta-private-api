-- August 12, 2015
-- Update privs for ag_wwwuser
GRANT USAGE ON SCHEMA barcodes TO "ag_wwwuser";
GRANT INSERT, UPDATE, DELETE, SELECT ON ALL TABLES IN SCHEMA ag, public, barcodes TO "ag_wwwuser";
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA ag, public, barcodes TO "ag_wwwuser";
