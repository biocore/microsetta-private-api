-- tablefunc is an additional supplied module that comes with postgres
-- and enables data pivoting in queries
CREATE EXTENSION IF NOT EXISTS tablefunc;

-- extend the project table to hold lots more info
ALTER TABLE barcodes.project ADD COLUMN subproject_name varchar;
ALTER TABLE barcodes.project ADD COLUMN alias varchar;
ALTER TABLE barcodes.project ADD COLUMN sponsor varchar;
ALTER TABLE barcodes.project ADD COLUMN coordination varchar;
ALTER TABLE barcodes.project ADD COLUMN contact_name varchar;
ALTER TABLE barcodes.project ADD COLUMN additional_contact_name varchar;
ALTER TABLE barcodes.project ADD COLUMN contact_email varchar;
ALTER TABLE barcodes.project ADD COLUMN deadlines varchar;
-- The below two columns are varchar bc there are projects with variable or
-- unknown numbers of subjects or time points ... and we don't expect to do
-- math on this column, so it is acceptable to store e.g. num_subjects = "Variable"
ALTER TABLE barcodes.project ADD COLUMN num_subjects varchar;
ALTER TABLE barcodes.project ADD COLUMN num_timepoints varchar;
ALTER TABLE barcodes.project ADD COLUMN start_date varchar;
ALTER TABLE barcodes.project ADD COLUMN disposition_comments varchar;
ALTER TABLE barcodes.project ADD COLUMN collection varchar;
ALTER TABLE barcodes.project ADD COLUMN is_fecal varchar;
ALTER TABLE barcodes.project ADD COLUMN is_saliva varchar;
ALTER TABLE barcodes.project ADD COLUMN is_skin varchar;
ALTER TABLE barcodes.project ADD COLUMN is_blood varchar;
ALTER TABLE barcodes.project ADD COLUMN is_other varchar;
ALTER TABLE barcodes.project ADD COLUMN do_16s varchar;
ALTER TABLE barcodes.project ADD COLUMN do_shallow_shotgun varchar;
ALTER TABLE barcodes.project ADD COLUMN do_shotgun varchar;
ALTER TABLE barcodes.project ADD COLUMN do_rt_qpcr varchar;
ALTER TABLE barcodes.project ADD COLUMN do_serology varchar;
ALTER TABLE barcodes.project ADD COLUMN do_metatranscriptomics varchar;
ALTER TABLE barcodes.project ADD COLUMN do_mass_spec varchar;
ALTER TABLE barcodes.project ADD COLUMN mass_spec_comments varchar;
ALTER TABLE barcodes.project ADD COLUMN mass_spec_contact_name varchar;
ALTER TABLE barcodes.project ADD COLUMN mass_spec_contact_email varchar;
ALTER TABLE barcodes.project ADD COLUMN do_other varchar;
ALTER TABLE barcodes.project ADD COLUMN branding_associated_instructions varchar;
ALTER TABLE barcodes.project ADD COLUMN branding_status varchar;