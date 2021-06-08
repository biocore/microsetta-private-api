-- Scans are often looked up by barcode
CREATE INDEX barcode_scans_barcode_idx ON barcodes.barcode_scans (barcode);
