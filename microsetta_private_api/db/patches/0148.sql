-- This update to the consent documents serves three purposes:
-- 1) Update the contact information in all consent documents.
-- 2) Add the IRB Protocol number, version, and expiration to all of the consent documents.
-- 3) Fix an oustanding typo in the English versions
-- NOTE: With this patch, we're going to update our internal version number in the database to match the IRB protocol version.

-- First, we'll create a new version of the documents that are a clone of the last version (v2, created in database patch 0147.sql)
INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    SELECT consent_type, locale, NOW(), consent_content, 'true', account_id, 48
    FROM ag.consent_documents
    WHERE version = 2;

-- Next, we'll replace the contact information. It appears there were multiple different sets of verbiage for each language, so we will need to run several different queries to catch all of them.
-- English version I
UPDATE ag.consent_documents
    SET consent_content = REPLACE(
                            consent_content,
                            'If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.',
                            'If you have questions or research-related problems, you may contact:<ul><li>Rob Knight at 858-246-1184 or</li><li>The research team (phone: 858-246-3234, email: microsetta@ucsd.edu)</li></ul>'
                          )
    WHERE version = 48 AND locale = 'en_US';

-- English version II
UPDATE ag.consent_documents
    SET consent_content = REPLACE(
                            consent_content,
                            'If you have questions or research-related problems, you may reach us by emailing our help account microsetta@ucsd.edu or Rob Knight at 858-246-1184.',
                            'If you have questions or research-related problems, you may contact:<ul><li>Rob Knight at 858-246-1184 or</li><li>The research team (phone: 858-246-3234, email: microsetta@ucsd.edu)</li></ul>'
                          )
    WHERE version = 48 AND locale = 'en_US';

-- Spanish version I
UPDATE ag.consent_documents
    SET consent_content = REPLACE(
                            consent_content,
                            'Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.',
                            'Si tiene alguna duda o problemas relacionados con la investigación, puede comunicarse con<ul><li>Rob Knight al 858-246-1184 o con</li><li>El equipo de investigación (teléfono: 858-246-3234, correo electrónico: microsetta@ucsd.edu)</li></ul>'
                          )
    WHERE version = 48 AND locale IN ('es_MX', 'es_ES');

-- Spanish version II
UPDATE ag.consent_documents
    SET consent_content = REPLACE(
                            consent_content,
                            'Si tiene alguna duda o problemas relacionados con la investigación, puede llamar a Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.',
                            'Si tiene alguna duda o problemas relacionados con la investigación, puede comunicarse con<ul><li>Rob Knight al 858-246-1184 o con</li><li>El equipo de investigación (teléfono: 858-246-3234, correo electrónico: microsetta@ucsd.edu)</li></ul>'
                          )
    WHERE version = 48 AND locale IN ('es_MX', 'es_ES');

-- Spanish version III
UPDATE ag.consent_documents
    SET consent_content = REPLACE(
                            consent_content,
                            'Si tiene alguna duda o problemas relacionados con la investigación, usted puede comunicarse con nosotros enviando un correo electrónico a nuestra cuenta de ayuda microsetta@ucsd.edu o llamando a Rob Knight al 858-246-1184.',
                            'Si tiene alguna duda o problemas relacionados con la investigación, puede comunicarse con<ul><li>Rob Knight al 858-246-1184 o con</li><li>El equipo de investigación (teléfono: 858-246-3234, correo electrónico: microsetta@ucsd.edu)</li></ul>'
                          )
    WHERE version = 48 AND locale IN ('es_MX', 'es_ES');


-- Then, we'll tack the IRB protocol number, version, and expiration on. We need to do this in two steps, one for each language we support.
-- English versions
UPDATE ag.consent_documents
    SET consent_content = consent_content || '<p class="consent_content">Protocol #141853 | v48 | Expires: January 22, 2026</p>'
    WHERE version = 48 AND locale = 'en_US';

-- Spanish versions
UPDATE ag.consent_documents
    SET consent_content = consent_content || '<p class="consent_content">Protocolo n.° 141853 | v48 | Caduca: 22 de enero de 2026</p>'
    WHERE version = 48 AND locale IN ('es_MX', 'es_ES');


-- Lastly, we'll fix the outstanding typo in the English documents
UPDATE ag.consent_documents
    SET consent_content = REPLACE(
                            consent_content,
                            'You may contact UC San Diego Office of IRB Administration',
                            'You may contact the UC San Diego Office of IRB Administration'
                          )
    WHERE version = 48 AND locale = 'en_US';
