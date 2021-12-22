-- a few columns in foodconsumption were inadvertantly set as 
-- varchar
ALTER TABLE ag.vioscreen_foodconsumption
    ALTER COLUMN amount TYPE float USING amount::double precision,
    ALTER COLUMN frequency TYPE float USING amount::double precision,
    ALTER COLUMN consumptionadjustment TYPE float USING amount::double precision;
