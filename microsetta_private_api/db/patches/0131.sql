-- Add column to settings that controls whether Perk Fulfillment jobs run
ALTER TABLE ag.settings ADD COLUMN perk_fulfillment_active BOOLEAN DEFAULT FALSE NOT NULL;