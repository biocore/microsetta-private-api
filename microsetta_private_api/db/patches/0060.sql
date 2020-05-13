-- set sample-is-valid for existing samples that for all intensive purposes
-- appear valid
UPDATE barcodes.barcode SET sample_status = 'sample-is-valid' 
WHERE barcode IN (SELECT barcode 
                  FROM ag.ag_kit_barcodes 
                    LEfT JOIN barcodes.barcode USING (barcode) 
                  WHERE status = 'Received' 
                    AND scan_date IS NOT NULL 
                    AND site_sampled IS NOT NULL
                    AND site_sampled != ''
                 );
