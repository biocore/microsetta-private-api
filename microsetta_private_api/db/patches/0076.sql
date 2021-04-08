-- create table to track activation codes
-- TODO: Expecting the user to use the same email will probably blow up in our face.
-- Procedure:
-- 1. Admin user sends requested emails to url
-- 2. Codes are generated as necessary, written to db, returned to admin
-- 3. Admin sends codes to distributor service, which passes activation code on to user
-- 4. User creates account using same email and code.
CREATE TABLE ag.activation
(
    email varchar NOT NULL,
    code varchar NOT NULL,
    activated boolean NOT NULL
);

-- Table is one to one, and allows lookup by either email or code.
CREATE UNIQUE INDEX activation_code ON ag.activation(code);
CREATE UNIQUE INDEX activation_email ON ag.activation(email);
