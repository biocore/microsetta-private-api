CREATE SCHEMA ag;

CREATE TABLE ag.ag_handout_kits ( 
	kit_id               varchar(9)  ,
	password             varchar(11)  ,
	barcode              varchar(9)  ,
	verification_code    varchar(5)  ,
	sample_barcode_file  varchar(13)  ,
	swabs_per_kit        bigint  ,
	print_results        varchar(1) DEFAULT 'n'::character varying 
 );

CREATE TABLE ag.ag_import_stats_tmp ( 
	tmp_login_count      bigint  ,
	tmp_kit_count        bigint  ,
	tmp_barcode_count    bigint  ,
	before_login_count   bigint  ,
	before_kit_count     bigint  ,
	before_barcode_count bigint  ,
	after_login_count    bigint  ,
	after_kit_count      bigint  ,
	after_barcode_count  bigint  ,
	login_diff           bigint  ,
	kit_diff             bigint  ,
	barcode_diff         bigint  
 );

CREATE TABLE ag.ag_login ( 
	ag_login_id          uuid DEFAULT uuid_generate_v4() NOT NULL,
	email                varchar(100)  ,
	name                 varchar(200)  ,
	address              varchar(500)  ,
	city                 varchar(100)  ,
	state                varchar(100)  ,
	zip                  varchar(10)  ,
	country              varchar(100)  ,
	latitude             float8  ,
	longitude            float8  ,
	cannot_geocode       char(1)  ,
	elevation            float8  ,
	CONSTRAINT ag_login_pkey PRIMARY KEY ( ag_login_id )
 );

CREATE TABLE ag.ag_map_markers ( 
	zipcode              varchar(20)  ,
	latitude             float8  ,
	longitude            float8  ,
	marker_color         varchar(10)  ,
	order_by             bigint  
 );

CREATE TABLE ag.ag_participant_exceptions ( 
	ag_login_id          uuid  ,
	participant_name     varchar(200)  ,
	CONSTRAINT fk_ag_participant_exceptions FOREIGN KEY ( ag_login_id ) REFERENCES ag.ag_login( ag_login_id )    
 );

CREATE INDEX idx_ag_participant_exceptions ON ag.ag_participant_exceptions ( ag_login_id );

CREATE TABLE ag.ag_survey_answer ( 
	ag_login_id          uuid  NOT NULL,
	participant_name     varchar(200)  NOT NULL,
	question             varchar(100)  NOT NULL,
	ag_survery_answer_id uuid DEFAULT uuid_generate_v4() ,
	answer               varchar(4000)  ,
	CONSTRAINT ag_survey_answer_pkey PRIMARY KEY ( ag_login_id, participant_name, question ),
	CONSTRAINT fk_sur_an_to_ag_login FOREIGN KEY ( ag_login_id ) REFERENCES ag.ag_login( ag_login_id )    
 );

CREATE TABLE ag.ag_survey_multiples ( 
	ag_login_id          uuid  NOT NULL,
	participant_name     varchar(200)  NOT NULL,
	item_name            varchar(50)  NOT NULL,
	item_value           varchar(1000)  ,
	CONSTRAINT ag_survey_multiples_pkey PRIMARY KEY ( ag_login_id, participant_name, item_name ),
	CONSTRAINT fk_ag_mul_to_ag_login FOREIGN KEY ( ag_login_id ) REFERENCES ag.ag_login( ag_login_id )    
 );

CREATE TABLE ag.ag_survey_multiples_backup ( 
	ag_login_id          uuid  NOT NULL,
	participant_name     varchar(200)  ,
	item_name            varchar(50)  NOT NULL,
	item_value           varchar(1000)  
 );

CREATE INDEX idx_ag_survey_multiples_backup ON ag.ag_survey_multiples_backup ( ag_login_id );

CREATE INDEX idx_ag_survey_multiples_backup_0 ON ag.ag_survey_multiples_backup ( participant_name );

CREATE TABLE ag.barcode ( 
	barcode              varchar  NOT NULL,
	create_date_time     timestamp DEFAULT ('now'::text)::timestamp without time zone ,
	status               varchar(100)  ,
	scan_date            varchar(20)  ,
	sample_postmark_date varchar(20)  ,
	biomass_remaining    varchar(1)  ,
	sequencing_status    varchar(20)  ,
	obsolete             varchar(1)  ,
	CONSTRAINT barcode_pkey PRIMARY KEY ( barcode )
 );

CREATE TABLE ag.barcode_exceptions ( 
	barcode              varchar(100)  
 );

CREATE TABLE ag.controlled_vocabs ( 
	controlled_vocab_id  bigint  NOT NULL,
	vocab_name           varchar(500)  ,
	CONSTRAINT controlled_vocabs_pkey PRIMARY KEY ( controlled_vocab_id )
 );

CREATE TABLE ag.plate ( 
	plate_id             bigint  NOT NULL,
	plate                varchar(50)  ,
	sequence_date        varchar(20)  ,
	CONSTRAINT plate_pkey PRIMARY KEY ( plate_id )
 );

CREATE TABLE ag.plate_barcode ( 
	plate_id             bigint  NOT NULL,
	barcode              varchar  NOT NULL,
	CONSTRAINT fk_plate_barcode FOREIGN KEY ( barcode ) REFERENCES ag.barcode( barcode )    ,
	CONSTRAINT fk_plate_barcode_0 FOREIGN KEY ( plate_id ) REFERENCES ag.plate( plate_id )    
 );

CREATE INDEX idx_plate_barcode ON ag.plate_barcode ( barcode );

CREATE INDEX idx_plate_barcode_0 ON ag.plate_barcode ( plate_id );

CREATE TABLE ag.project ( 
	project_id           bigint  NOT NULL,
	project              varchar(1000)  ,
	CONSTRAINT project_pkey PRIMARY KEY ( project_id )
 );

CREATE TABLE ag.project_barcode ( 
	project_id           bigint  NOT NULL,
	barcode              char(9)  NOT NULL,
	CONSTRAINT project_barcode_pkey PRIMARY KEY ( project_id, barcode ),
	CONSTRAINT fk_pb_to_barcode FOREIGN KEY ( barcode ) REFERENCES ag.barcode( barcode )    ,
	CONSTRAINT fk_pb_to_project FOREIGN KEY ( project_id ) REFERENCES ag.project( project_id )    
 );

CREATE TABLE ag.survey_group ( 
	group_order          integer  NOT NULL,
	american             varchar  ,
	british              varchar  ,
	CONSTRAINT idx_human_survey_question_group UNIQUE ( american ) ,
	CONSTRAINT idx_human_survey_question_group_0 UNIQUE ( british ) ,
	CONSTRAINT pk_human_survey_question_group PRIMARY KEY ( group_order )
 );

COMMENT ON COLUMN ag.survey_group.group_order IS 'The order that this group will be displayed in';

COMMENT ON COLUMN ag.survey_group.american IS 'The american english version of the question group`s name';

CREATE TABLE ag.survey_question ( 
	survey_question_id   bigint  NOT NULL,
	american             varchar  ,
	british              varchar  ,
	CONSTRAINT pk_human_survey_question PRIMARY KEY ( survey_question_id ),
	CONSTRAINT idx_survey_question UNIQUE ( american ) ,
	CONSTRAINT idx_survey_question_0 UNIQUE ( british ) 
 );

COMMENT ON TABLE ag.survey_question IS 'Stores the human survey questions';

COMMENT ON COLUMN ag.survey_question.survey_question_id IS 'The unique question ID';

COMMENT ON COLUMN ag.survey_question.american IS 'The american english version of the question';

COMMENT ON COLUMN ag.survey_question.british IS 'The british english version of the question';

CREATE TABLE ag.survey_response ( 
	american             varchar  NOT NULL,
	british              varchar  ,
	CONSTRAINT pk_human_survey_response PRIMARY KEY ( american ),
	CONSTRAINT idx_human_survey_response UNIQUE ( british ) 
 );

COMMENT ON TABLE ag.survey_response IS 'Stores every possible predictable response on the human survey';

CREATE TABLE ag.survey_response_types ( 
	survey_response_type varchar  NOT NULL,
	CONSTRAINT pk_human_survey_response_types PRIMARY KEY ( survey_response_type )
 );

COMMENT ON TABLE ag.survey_response_types IS 'Stores every possible type of response.  The response type will be processed in python to determine how the question is represented in the interface.';

CREATE TABLE ag.surveys ( 
	survey_id            integer  NOT NULL,
	survey_group         integer  NOT NULL,
	CONSTRAINT idx_surveys_0 PRIMARY KEY ( survey_id, survey_group ),
	CONSTRAINT fk_surveys FOREIGN KEY ( survey_group ) REFERENCES ag.survey_group( group_order )    
 );

CREATE INDEX idx_surveys ON ag.surveys ( survey_group );

CREATE TABLE ag.zipcodes ( 
	zipcode              varchar(5)  NOT NULL,
	state                varchar(2)  NOT NULL,
	fips_regions         varchar(2)  NOT NULL,
	city                 varchar(64)  NOT NULL,
	latitude             float8  NOT NULL,
	longitude            float8  NOT NULL,
	CONSTRAINT zipcodes_pkey PRIMARY KEY ( zipcode )
 );

CREATE INDEX ix_zipcode_lat ON ag.zipcodes ( latitude );

CREATE INDEX ix_zipcode_long ON ag.zipcodes ( longitude );

CREATE TABLE ag.ag_animal_survey ( 
	ag_login_id          uuid  NOT NULL,
	participant_name     varchar(200)  NOT NULL,
	type                 varchar(100)  ,
	origin               varchar(100)  ,
	age                  varchar(100)  ,
	gender               varchar(100)  ,
	setting              varchar(100)  ,
	weight               varchar(100)  ,
	diet                 varchar(100)  ,
	food_source_store    varchar(100)  ,
	food_source_human    varchar(100)  ,
	food_source_wild     varchar(100)  ,
	food_type            varchar(100)  ,
	organic_food         varchar(100)  ,
	grain_free_food      varchar(100)  ,
	living_status        varchar(100)  ,
	outside_time         varchar(100)  ,
	toilet               varchar(100)  ,
	coprophage           varchar(100)  ,
	comments             varchar(2000)  ,
	CONSTRAINT ag_animal_survey_pkey PRIMARY KEY ( ag_login_id, participant_name ),
	CONSTRAINT fk_ag_animal_surv_to_ag_login FOREIGN KEY ( ag_login_id ) REFERENCES ag.ag_login( ag_login_id )    
 );

CREATE TABLE ag.ag_consent ( 
	ag_login_id          uuid  NOT NULL,
	participant_name     varchar(200)  NOT NULL,
	participant_email    varchar  NOT NULL,
	is_juvenile          bool  ,
	parent_1_name        varchar(200)  ,
	parent_2_name        varchar(200)  ,
	parent_1_code        varchar(200)  ,
	parent_2_code        varchar(200)  ,
	deceased_parent      varchar(10)  ,
	CONSTRAINT pk_american_gut_consent PRIMARY KEY ( ag_login_id, participant_name ),
	CONSTRAINT fk_american_gut_consent FOREIGN KEY ( ag_login_id ) REFERENCES ag.ag_login( ag_login_id )    
 );

CREATE INDEX idx_american_gut_consent ON ag.ag_consent ( ag_login_id );

CREATE TABLE ag.ag_human_survey ( 
	ag_login_id          uuid  NOT NULL,
	participant_name     varchar(200)  NOT NULL,
	consent              varchar(20)  ,
	juvenile_age         varchar(20)  ,
	parent_1_name        varchar(200)  ,
	parent_2_name        varchar(200)  ,
	deceased_parent      varchar(20)  ,
	country_of_birth     varchar(100)  ,
	birth_date           varchar(100)  ,
	gender               varchar(100)  ,
	height_in            varchar(100)  ,
	height_cm            varchar(100)  ,
	weight_lbs           varchar(100)  ,
	weight_kg            varchar(100)  ,
	phone_num            varchar(100)  ,
	zip_code             varchar(100)  ,
	diet_type            varchar(100)  ,
	multivitamin         varchar(100)  ,
	supplements          varchar(100)  ,
	lactose              varchar(100)  ,
	gluten               varchar(100)  ,
	foodallergies_peanuts varchar(100)  ,
	foodallergies_treenuts varchar(100)  ,
	foodallergies_shellfish varchar(100)  ,
	foodallergies_other  varchar(100)  ,
	foodallergies_other_text varchar(400)  ,
	special_restrictions varchar(100)  ,
	drinking_water_source varchar(100)  ,
	race                 varchar(100)  ,
	race_other           varchar(100)  ,
	current_residence_duration varchar(100)  ,
	last_travel          varchar(100)  ,
	livingwith           varchar(100)  ,
	dog                  varchar(100)  ,
	cat                  varchar(100)  ,
	hand                 varchar(100)  ,
	shared_housing       varchar(100)  ,
	tanning_beds         varchar(100)  ,
	tanning_sprays       varchar(100)  ,
	exercise_frequency   varchar(100)  ,
	exercise_location    varchar(100)  ,
	nails                varchar(100)  ,
	pool_frequency       varchar(100)  ,
	smoking_frequency    varchar(100)  ,
	alcohol_frequency    varchar(100)  ,
	teethbrushing_frequency varchar(100)  ,
	flossing_frequency   varchar(100)  ,
	cosmetics_frequency  varchar(100)  ,
	deoderant_use        varchar(100)  ,
	sleep_duration       varchar(100)  ,
	softener             varchar(100)  ,
	antibiotic_select    varchar(100)  ,
	antibiotic_condition varchar(100)  ,
	flu_vaccine_date     varchar(100)  ,
	weight_change        varchar(100)  ,
	tonsils_removed      varchar(100)  ,
	appendix_removed     varchar(100)  ,
	chickenpox           varchar(100)  ,
	acne_medication      varchar(100)  ,
	acne_medication_otc  varchar(100)  ,
	conditions_medication varchar(100)  ,
	csection             varchar(100)  ,
	pku                  varchar(100)  ,
	asthma               varchar(100)  ,
	seasonal_allergies   varchar(100)  ,
	nonfoodallergies_drug varchar(100)  ,
	nonfoodallergies_dander varchar(100)  ,
	nonfoodallergies_beestings varchar(100)  ,
	nonfoodallergies_poisonivy varchar(100)  ,
	nonfoodallergies_sun varchar(100)  ,
	nonfoodallergies_no  varchar(100)  ,
	ibd                  varchar(100)  ,
	skin_condition       varchar(100)  ,
	diabetes             varchar(100)  ,
	migraine             varchar(100)  ,
	protein_per          varchar(100)  ,
	fat_per              varchar(100)  ,
	carbohydrate_per     varchar(100)  ,
	plant_per            varchar(100)  ,
	animal_per           varchar(100)  ,
	fiber_grams          varchar(100)  ,
	types_of_plants      varchar(100)  ,
	percentage_from_carbs varchar(100)  ,
	primary_vegetable    varchar(100)  ,
	primary_carb         varchar(100)  ,
	diabetes_diagnose_date varchar(100)  ,
	diabetes_medication  varchar(100)  ,
	contraceptive        varchar(100)  ,
	pregnant             varchar(100)  ,
	pregnant_due_date    varchar(100)  ,
	frat                 varchar(100)  ,
	communal_dining      varchar(100)  ,
	roommates            varchar(100)  ,
	migraine_frequency   varchar(100)  ,
	migraine_factor_1    varchar(100)  ,
	mainfactor_other_1   varchar(100)  ,
	migraine_factor_2    varchar(100)  ,
	mainfactor_other_2   varchar(100)  ,
	migraine_factor_3    varchar(100)  ,
	mainfactor_other_3   varchar(100)  ,
	migraine_pain        varchar(100)  ,
	migraine_photophobia varchar(100)  ,
	migraine_phonophobia varchar(100)  ,
	migraine_nausea      varchar(100)  ,
	migraine_aggravation varchar(100)  ,
	migraine_aura        varchar(100)  ,
	migraine_relatives   varchar(100)  ,
	migrainemeds         varchar(100)  ,
	about_yourself_text  varchar(2000)  ,
	participant_email    varchar(300)  ,
	participant_name_u   varchar(400)  ,
	CONSTRAINT ag_human_survey_pkey PRIMARY KEY ( ag_login_id, participant_name ),
	CONSTRAINT fk_ag_hum_surv_to_ag_login FOREIGN KEY ( ag_login_id ) REFERENCES ag.ag_login( ag_login_id )    
 );

CREATE TABLE ag.ag_kit ( 
	ag_kit_id            uuid DEFAULT uuid_generate_v4() NOT NULL,
	ag_login_id          uuid  NOT NULL,
	supplied_kit_id      varchar(50)  NOT NULL,
	kit_password         varchar(50)  ,
	swabs_per_kit        bigint  NOT NULL,
	kit_verification_code varchar(50)  ,
	kit_verified         char(1) DEFAULT 'n'::bpchar ,
	verification_email_sent char(1) DEFAULT 'n'::bpchar ,
	pass_reset_code      varchar(20)  ,
	pass_reset_time      timestamp  ,
	print_results        varchar(1) DEFAULT 'n'::character varying ,
	CONSTRAINT ag_kit_pkey PRIMARY KEY ( ag_kit_id ),
	CONSTRAINT ag_kit_supplied_kit_id_key UNIQUE ( supplied_kit_id ) ,
	CONSTRAINT fk_ag_kit_to_login_id FOREIGN KEY ( ag_login_id ) REFERENCES ag.ag_login( ag_login_id )    
 );

CREATE INDEX ix_ag_kit_login ON ag.ag_kit ( ag_login_id );

CREATE TABLE ag.ag_login_surveys ( 
	ag_login_id          uuid  NOT NULL,
	survey_id            varchar  NOT NULL,
	participant_name     varchar  ,
	vioscreen_status     integer  ,
	CONSTRAINT pk_ag_login_surveys PRIMARY KEY ( survey_id ),
	CONSTRAINT fk_ag_login_surveys FOREIGN KEY ( ag_login_id ) REFERENCES ag.ag_login( ag_login_id )    ,
	CONSTRAINT fk_ag_login_surveys0 FOREIGN KEY ( ag_login_id, participant_name ) REFERENCES ag.ag_consent( ag_login_id, participant_name )    
 );

CREATE INDEX idx_ag_login_surveys ON ag.ag_login_surveys ( participant_name );

CREATE INDEX idx_ag_login_surveys_0 ON ag.ag_login_surveys ( ag_login_id, participant_name );

CREATE TABLE ag.controlled_vocab_values ( 
	vocab_value_id       bigint  NOT NULL,
	controlled_vocab_id  bigint  NOT NULL,
	term                 varchar(500)  NOT NULL,
	order_by             bigint  ,
	default_item         char(1)  ,
	CONSTRAINT controlled_vocab_values_pkey PRIMARY KEY ( vocab_value_id ),
	CONSTRAINT fk_cont_vcb_values_cont_vcbs FOREIGN KEY ( controlled_vocab_id ) REFERENCES ag.controlled_vocabs( controlled_vocab_id )    
 );

CREATE TABLE ag.group_questions ( 
	survey_group         integer  NOT NULL,
	survey_question_id   bigint  NOT NULL,
	display_index        integer  NOT NULL,
	CONSTRAINT pk_human_survey_group_question PRIMARY KEY ( survey_group, survey_question_id ),
	CONSTRAINT idx_group_questions UNIQUE ( survey_group, display_index ) ,
	CONSTRAINT fk_human_survey_group_question FOREIGN KEY ( survey_group ) REFERENCES ag.survey_group( group_order )    ,
	CONSTRAINT fk_human_survey_group_question_0 FOREIGN KEY ( survey_question_id ) REFERENCES ag.survey_question( survey_question_id )    
 );

CREATE INDEX idx_human_survey_group_question ON ag.group_questions ( survey_group );

CREATE INDEX idx_human_survey_group_question_0 ON ag.group_questions ( survey_question_id );

CREATE TABLE ag.iso_country_lookup ( 
	iso_code             varchar  NOT NULL,
	country              varchar  NOT NULL,
	CONSTRAINT pk_iso_country_lookup PRIMARY KEY ( iso_code ),
	CONSTRAINT fk_iso_country_lookup FOREIGN KEY ( country ) REFERENCES ag.survey_response( american )    
 );

CREATE INDEX idx_iso_country_lookup ON ag.iso_country_lookup ( country );

COMMENT ON TABLE ag.iso_country_lookup IS 'ISO standard codes for countries';

COMMENT ON COLUMN ag.iso_country_lookup.iso_code IS 'The ISO code for the country';

CREATE TABLE ag.survey_answers_other ( 
	survey_id            varchar  NOT NULL,
	survey_question_id   bigint  NOT NULL,
	response             varchar  NOT NULL,
	CONSTRAINT pk_survey_answers_other PRIMARY KEY ( survey_id, survey_question_id ),
	CONSTRAINT fk_survey_answers_other FOREIGN KEY ( survey_id ) REFERENCES ag.ag_login_surveys( survey_id )    ,
	CONSTRAINT fk_survey_answers_other_0 FOREIGN KEY ( survey_question_id ) REFERENCES ag.survey_question( survey_question_id )    
 );

CREATE INDEX idx_survey_answers_other ON ag.survey_answers_other ( survey_id );

CREATE INDEX idx_survey_answers_other_0 ON ag.survey_answers_other ( survey_question_id );

COMMENT ON TABLE ag.survey_answers_other IS 'Survey answers for which there are no corresponding foreign keys';

CREATE TABLE ag.survey_question_response ( 
	survey_question_id   bigint  NOT NULL,
	response             varchar  NOT NULL,
	display_index        serial  ,
	CONSTRAINT pk_question_response PRIMARY KEY ( survey_question_id, response ),
	CONSTRAINT idx_survey_question_response UNIQUE ( survey_question_id, display_index ) ,
	CONSTRAINT fk_question_response FOREIGN KEY ( response ) REFERENCES ag.survey_response( american )    ,
	CONSTRAINT fk_question_response_0 FOREIGN KEY ( survey_question_id ) REFERENCES ag.survey_question( survey_question_id )    
 );

COMMENT ON TABLE ag.survey_question_response IS 'Maps questions to responses';

COMMENT ON COLUMN ag.survey_question_response.display_index IS 'The display order of this response';

CREATE TABLE ag.survey_question_response_type ( 
	survey_question_id   bigint  ,
	survey_response_type varchar  NOT NULL,
	CONSTRAINT fk_human_survey_response_type FOREIGN KEY ( survey_question_id ) REFERENCES ag.survey_question( survey_question_id )    ,
	CONSTRAINT fk_human_survey_question_response_type FOREIGN KEY ( survey_response_type ) REFERENCES ag.survey_response_types( survey_response_type )    
 );

CREATE INDEX idx_human_survey_response_type ON ag.survey_question_response_type ( survey_question_id );

CREATE INDEX idx_human_survey_question_response_type ON ag.survey_question_response_type ( survey_response_type );

COMMENT ON TABLE ag.survey_question_response_type IS 'Stores the type of response for each question';

CREATE TABLE ag.survey_question_triggers ( 
	survey_question_id   bigint  ,
	triggering_response  varchar  ,
	triggered_question   bigint  ,
	CONSTRAINT fk_survey_question_triggers FOREIGN KEY ( triggered_question ) REFERENCES ag.survey_question( survey_question_id )    ,
	CONSTRAINT fk_survey_question_triggers0 FOREIGN KEY ( survey_question_id, triggering_response ) REFERENCES ag.survey_question_response( survey_question_id, response )    
 );

CREATE INDEX idx_human_survey_question_triggered_by ON ag.survey_question_triggers ( survey_question_id );

CREATE INDEX idx_human_survey_question_triggered_by_0 ON ag.survey_question_triggers ( triggered_question );

CREATE INDEX idx_human_survey_question_triggered_by_1 ON ag.survey_question_triggers ( triggering_response );

CREATE INDEX idx_survey_question_triggered_by ON ag.survey_question_triggers ( triggered_question, triggering_response );

CREATE INDEX idx_survey_question_triggers ON ag.survey_question_triggers ( survey_question_id, triggering_response );

COMMENT ON TABLE ag.survey_question_triggers IS 'Which question/answer combos trigger other questions';

COMMENT ON COLUMN ag.survey_question_triggers.survey_question_id IS 'The ID of the question that is triggered';

COMMENT ON COLUMN ag.survey_question_triggers.triggering_response IS 'The response to the question that will cause the appearance of the triggered_question';

COMMENT ON COLUMN ag.survey_question_triggers.triggered_question IS 'The question that is triggered';

CREATE TABLE ag.ag_kit_barcodes ( 
	ag_kit_barcode_id    uuid DEFAULT uuid_generate_v4() NOT NULL,
	ag_kit_id            uuid  ,
	barcode              varchar  NOT NULL,
	survey_id            varchar  ,
	sample_barcode_file  varchar(500)  ,
	sample_barcode_file_md5 varchar(50)  ,
	site_sampled         varchar(200)  ,
	sample_date          varchar(20)  ,
	participant_name     varchar(200)  ,
	sample_time          varchar(100)  ,
	notes                varchar(2000)  ,
	environment_sampled  varchar(100)  ,
	moldy                char(1)  ,
	overloaded           char(1)  ,
	other                char(1)  ,
	other_text           varchar(2000)  ,
	date_of_last_email   varchar(20)  ,
	results_ready        varchar(1)  ,
	withdrawn            varchar(1)  ,
	refunded             varchar(1)  ,
	CONSTRAINT ag_kit_barcodes_pkey PRIMARY KEY ( ag_kit_barcode_id ),
	CONSTRAINT ag_kit_barcodes_barcode_key UNIQUE ( barcode ) ,
	CONSTRAINT fk_ag_kit_barcodes FOREIGN KEY ( ag_kit_id ) REFERENCES ag.ag_kit( ag_kit_id )    ,
	CONSTRAINT fk_ag_kit_barcodes_0 FOREIGN KEY ( barcode ) REFERENCES ag.barcode( barcode )    ,
	CONSTRAINT fk_ag_kit_barcodes_1 FOREIGN KEY ( survey_id ) REFERENCES ag.ag_login_surveys( survey_id )    
 );

CREATE INDEX ix_ag_kit_bc_kit ON ag.ag_kit_barcodes ( ag_kit_id );

CREATE INDEX idx_ag_kit_barcodes ON ag.ag_kit_barcodes ( survey_id );

CREATE TABLE ag.survey_answers ( 
	survey_id            varchar  NOT NULL,
	survey_question_id   bigint  NOT NULL,
	response             varchar  NOT NULL,
	CONSTRAINT pk_survey_answers PRIMARY KEY ( survey_id, survey_question_id, response ),
	CONSTRAINT fk_survey_answers FOREIGN KEY ( survey_question_id, response ) REFERENCES ag.survey_question_response( survey_question_id, response )    ,
	CONSTRAINT fk_survey_answers_0 FOREIGN KEY ( survey_id ) REFERENCES ag.ag_login_surveys( survey_id )    
 );

CREATE INDEX idx_survey_answers ON ag.survey_answers ( survey_question_id, response );

CREATE INDEX idx_survey_answers_0 ON ag.survey_answers ( survey_id );

COMMENT ON TABLE ag.survey_answers IS 'Stores answers to questions of type SINGLE and MULTIPLE';

COMMENT ON COLUMN ag.survey_answers.survey_id IS 'The unique identifier for the survey';

COMMENT ON COLUMN ag.survey_answers.survey_question_id IS 'The question being answered';

COMMENT ON COLUMN ag.survey_answers.response IS 'The answer the question being asked';

