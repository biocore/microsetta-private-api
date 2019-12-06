-- August 27, 2015
-- Fix all the broken freetext entered countries
UPDATE ag.ag_login SET country = NULL
WHERE lower(trim(both ' ' from country)) in ('a', 'na', 'no country');

UPDATE ag.ag_login SET country = 'United States'
WHERE lower(trim(both ' ' from country)) in
('america', 'erie', 'united states', 'united states of america', 'unites states', 'us', 'usa', 'u.s.', 'u s a', 'u.s.a.', 'use', 'ussa',
 'united dtates', 'chester county', 'st. louis', 'suffolk', 'thurston', 'buncombe', 'coconino', 'fauquier', 'grant');

UPDATE ag.ag_login SET country = 'United Kingdom'
WHERE lower(trim(both ' ' from country)) in
('england', 'england, uk', 'englang', 'englans', 'great britain', 'gb', 'london', 'uk', 'u.k', 'u.k.', 'united kinddom', 'united kingdom','united kingdon',
 'united kingtom', 'cheshire', 'clwyd', 'republic of ireland', 'scotland', 'scotland, u.k.', 'tyne and wear', 'britain');

UPDATE ag.ag_login SET country = 'Australia'
WHERE lower(trim(both ' ' from country)) in
('au', 'australia');

UPDATE ag.ag_login SET country = 'Canada'
WHERE lower(trim(both ' ' from country)) in
('ca', 'canada', 'canadian');

UPDATE ag.ag_login SET country = 'Switzerland'
WHERE lower(trim(both ' ' from country)) in
('ch', 'switzerland');

UPDATE ag.ag_login SET country = 'Netherlands'
WHERE lower(trim(both ' ' from country)) in
('ugchelen', 'the netherlands', 'nl');

UPDATE ag.ag_login SET country = 'Germany'
WHERE lower(trim(both ' ' from country)) in
('de', 'germany');

UPDATE ag.ag_login SET country = 'South Korea'
WHERE lower(trim(both ' ' from country)) in
('korea, republic of');

UPDATE ag.ag_login SET country = 'New Zealand'
WHERE lower(trim(both ' ' from country)) in
('new zealand');

UPDATE ag.ag_login SET country = 'Norway'
WHERE lower(trim(both ' ' from country)) in
('norge', 'norway');

UPDATE ag.ag_login SET country = 'Spain'
WHERE lower(trim(both ' ' from country)) in
('es');

UPDATE ag.ag_login SET country = 'France'
WHERE lower(trim(both ' ' from country)) in
('fr', 'france');

UPDATE ag.ag_login SET country = 'Italy'
WHERE lower(trim(both ' ' from country)) in
('italia');

UPDATE ag.ag_login SET country = 'United Arab Emirates'
WHERE lower(trim(both ' ' from country)) in
('uae');