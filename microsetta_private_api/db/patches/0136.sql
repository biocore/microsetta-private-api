-- Add constraint to the ag.account table so that
-- auth_issuer and auth_sub should either both be null or both be non-null
ALTER TABLE ag.account
ADD CONSTRAINT auth_nullable
CHECK (
    (auth_issuer IS NULL AND auth_sub IS NULL) OR 
    (auth_issuer IS NOT NULL AND auth_sub IS NOT NULL)
);