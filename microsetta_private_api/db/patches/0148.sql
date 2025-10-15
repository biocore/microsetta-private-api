-- This update to the consent documents serves two purposes:
-- 1) We need to update the phone number in all consent documents.
-- 2) We need to add the IRB Protocol number, version, and expiration to all of the consent documents.
-- NOTE: With this patch, we're going to update our internal version number in the database to match the IRB protocol version.

-- First, we'll create a new version of the documents that are a clone of the last version (v2, created in database patch 0147.sql)
INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    SELECT consent_type, locale, NOW(), consent_content, 'true', account_id, 48
    FROM ag.consent_documents
    WHERE version = 2;

-- Next, we'll replace the phone number
UPDATE ag.consent_documents
    SET consent_content = REPLACE(consent_content, '858-246-1184', '858-822-2379')
    WHERE version = 48;

-- Then, we'll tack the IRB protocol number, version, and expiration on. We need to do this in two steps, one for each language we support.
-- English versions
UPDATE ag.consent_documents
    SET consent_content = consent_content || '<p class="consent_content">Protocol #141853 | v47 | Expires: January 22, 2026</p>'
    WHERE version = 48 AND locale = 'en_US';

-- Spanish versions
UPDATE ag.consent_documents
    SET consent_content = consent_content || '<p class="consent_content">Protocolo n.° 141853 | v47 | Caduca: 22 de enero de 2026</p>'
    WHERE version = 48 AND locale IN ('es_MX', 'es_ES');
