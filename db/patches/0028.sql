-- October 6, 2015
-- Correct site_sampled from two previously logged samples as supported by the
-- platemaps.

UPDATE ag.ag_kit_barcodes SET site_sampled = 'Stool' WHERE barcode = '000001161';
UPDATE ag.ag_kit_barcodes SET site_sampled = 'Mouth' WHERE barcode = '000002182';
