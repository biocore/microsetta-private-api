-- Add new article codes for matrix tube kits
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3510005E', 'TMI 1matrix tube', 'TMI 1 matrix tube, American English');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3510006E', 'TMI 1matrix tube', 'TMI 1 matrix tube, American English, no inbound label');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3510006M', 'TMI 1matrix tube', 'TMI 1 matrix tube, Mexican Spanish, no inbound label');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3510006S', 'TMI 1matrix tube', 'TMI 1 matrix tube, Spanish, no inbound label');
INSERT INTO barcodes.daklapack_article (dak_article_code, short_description, detailed_description) VALUES ('3510006J', 'TMI 1matrix tube', 'TMI 1 matrix tube, Japanese, no inbound label');

-- Retire old kit configurations that we won't be using in the future
UPDATE barcodes.daklapack_article SET retired = true WHERE dak_article_code IN ('3510000E', '3510001E', '3511000E', '3541002E', '3510001M', '3510001S', '3510001J', '3521003E');
