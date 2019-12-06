-- Populates the test database
SET search_path TO ag, barcodes, public;

INSERT INTO ag_login (
  ag_login_id,
  email,
  name,
  address,
  city,
  state,
  zip,
  country,
  latitude,
  longitude
) VALUES (
  'd8592c74-7da1-2135-e040-8a80115d6401',
  'test@microbio.me',
  'Test',
  'Test',
  'Boulder',
  'CO',
  '80303',
  'United States',
  '40.0005378',
  '-105.2077798'
);

-- the password for account test is '%^&*test'
INSERT INTO ag_kit (
  ag_kit_id,
  ag_login_id,
  supplied_kit_id,
  swabs_per_kit,
  kit_password,
  kit_verified,
  kit_verification_code
) VALUES (
  'd8592c74-7da2-2135-e040-8a80115d6401',
  'd8592c74-7da1-2135-e040-8a80115d6401',
  'test',
  1,
  '$2a$12$pKAKSEwg3U6gFXtjRYbeyOgmmCPlPqoY1LTeQdsokR50sQUfS9Nhe',
  'y',
  'test'
);

-- the password for account 1111 is '1111'
INSERT INTO ag_kit (
  ag_kit_id,
  ag_login_id,
  supplied_kit_id,
  swabs_per_kit,
  kit_password,
  kit_verified
) VALUES (
  'dbd466b5-651b-bfb2-e040-8a80115d6775',
  'd8592c74-7da1-2135-e040-8a80115d6401',
  '1111',
  5,
  '$2a$12$ODekrwlLuxU2uOCzojSn/umCb5XyXpWfDgrgemBk3VFGaDOSP2JpK',
  'y'
);

insert into ag_consent (ag_login_id, participant_name, participant_email)
    values ('d8592c74-7da1-2135-e040-8a80115d6401', 'foo', 'foo@bar.com');

insert into ag_login_surveys (ag_login_id, survey_id, participant_name)
    values ('d8592c74-7da1-2135-e040-8a80115d6401', 19, 'foo');

insert into project (project_id, project) values ('1', 'American Gut Project');
insert into barcode (barcode, status) values ('000010860',''), ('000000001', 'Received'), ('000006616', 'Received'), ('000000002', 'Received'), ('000000003', 'Received'), ('000000004', 'Received');
insert into project_barcode (project_id, barcode) values (1, '000010860'), (1, '000000001'), (1, '000000002'), (1, '000000003'), (1, '000000004'), (1, '000006616');
 insert into ag_kit_barcodes(ag_kit_barcode_id,ag_kit_id,barcode,survey_id,sample_barcode_file, sample_barcode_file_md5,
    site_sampled,sample_date,participant_name,sample_time,notes,environment_sampled,moldy,overloaded,other,other_text,date_of_last_email,results_ready,withdrawn,refunded)
 values('e8d5446c-d7ab-e504-e040-8a80115d067f','d8592c74-7da2-2135-e040-8a80115d6401','000010860',19,'000010860.jpg','','','','','','','','','','','','','','',''),
        ('d8592c74-7da3-2135-e040-8a80115d6401','d8592c74-7da2-2135-e040-8a80115d6401','000000001',19,'000000001.jpg','','Stool',
            '12/02/2013','foo','06:20 AM','','','N','N','N','','None','Y','N','N'),
        ('ded369ec-7d0f-4d8c-e040-8a80115d6742','d8592c74-7da2-2135-e040-8a80115d6401','000006616',19,'000006616.jpg','','Nasal mucus','08/12/2014',
            'MAKE SURE THIS IS BEING PASSED','12:05 PM','','','','','','','','','','');
insert into ag_handout_kits (kit_id, password, verification_code, swabs_per_kit, print_results)
    values('test_ha', '$2a$12$GfYI6sxlVGTamDJ3FEQzMuQ46eSV6YJ.DxUxiZvKJaAn1NJtTDtFS', '5678', '3', 'n');
insert into ag_handout_barcodes (kit_id, barcode)
    values ('test_ha', '000000002'),('test_ha', '000000003'),('test_ha', '000000004');
insert into ag_participant_exceptions (ag_login_id, participant_name)
    values ('d8592c74-7da1-2135-e040-8a80115d6401', 'exception');
insert into ag_login_surveys (ag_login_id, survey_id, participant_name)
    values ('d8592c74-7da1-2135-e040-8a80115d6401', '1234', 'foo');

insert into survey_answers (survey_id, survey_question_id, response)
    values (19, 1, 'Unspecified');
insert into survey_answers (survey_id, survey_question_id, response)
    values (19, 2, 'Yes');
insert into external_survey_sources (external_survey, external_survey_description, external_survey_url)
    values ('vioscreen', 'dietary survey', 'http://fakevioscreenurl.com/%s');
insert into external_survey_answers (survey_id, external_survey_id, pulldown_date, answers)
    values (19, 1, '2015-07-20', '{"chicken":"lots","grains":"some","greens":5}');
