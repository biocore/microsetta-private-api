-- When the project's IRB protocol was renewed, it flipped the version number from 53 to 54 and changed the expiration date.
-- We need to update the string containing both of those items in the consent documents.
-- As in patch 0148.sql, we'll declare a new version in our database. However, we will NOT require reconsent, as there are no substantive changes to the consents.

-- First, we'll create a new version of the documents that are a clone of the last version (v53, created in database patch 0148.sql)
INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    SELECT consent_type, locale, NOW(), consent_content, 'false', account_id, 54
    FROM ag.consent_documents
    WHERE version = 53;

-- Update the version and expiration for English documents
UPDATE ag.consent_documents
    SET consent_content = REPLACE(
                            consent_content,
                            'v53 | Expires: January 22, 2026',
                            'v54 | Expires: December 16, 2026'
                          )
    WHERE version = 54 AND locale = 'en_US';

-- Update the version and expiration for Spanish documents
UPDATE ag.consent_documents
    SET consent_content = REPLACE(
                            consent_content,
                            'v53 | Caduca: 22 de enero de 2026',
                            'v54 | Caduca: 16 de diciembre de 2026'
                          )
    WHERE version = 54 AND locale IN ('es_MX', 'es_ES');
