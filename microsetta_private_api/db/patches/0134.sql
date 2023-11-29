-- We're going to add explicit versioning to the consent documents.
-- For the time being, this will only be used for checking whether reconsent
-- is necessary, and we're going to assume that every locale and age range is
-- kept in sync at the same version. If that ever changes - e.g. en_US adults
-- are on a different version than es_MX adults - we will likely need to modify
-- a variety of both code and operating procedures.
ALTER TABLE ag.consent_documents ADD COLUMN version INTEGER;

-- We're arbitrarily going to consider the versions that were created for
-- relaunch as v1, since that's the first version for which we have a full
-- audit trail.
UPDATE ag.consent_documents SET version = 1;

-- Now that a value exists for all documents, we're going to add a NOT NULL
-- constraint and a unique constraint on the combination of consent_type +
-- locale + version
ALTER TABLE ag.consent_documents ALTER COLUMN version SET NOT NULL;
ALTER TABLE ag.consent_documents ADD CONSTRAINT idx_consent_type_locale_version UNIQUE (consent_type, locale, version);