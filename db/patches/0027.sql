-- September 27, 2015
-- Change the print_results column to be of type bool

ALTER TABLE ag.ag_kit
ALTER COLUMN print_results DROP DEFAULT;

ALTER TABLE ag.ag_kit
ALTER COLUMN print_results TYPE BOOL
USING CAST(print_results as BOOL);


ALTER TABLE ag.ag_kit ALTER COLUMN print_results SET DEFAULT 'FALSE';

ALTER TABLE ag.ag_kit ALTER COLUMN print_results SET NOT NULL;
