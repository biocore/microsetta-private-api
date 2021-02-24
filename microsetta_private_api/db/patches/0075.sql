-- Allow unlinking vioscreen surveys (in case of deleting source)
ALTER TABLE ag.vioscreen_registry ADD COLUMN deleted BOOLEAN NOT NULL DEFAULT false;
ALTER TABLE ag.vioscreen_registry ALTER COLUMN source_id DROP NOT NULL;
