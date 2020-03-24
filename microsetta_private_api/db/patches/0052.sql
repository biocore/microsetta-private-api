ALTER TABLE ag.survey_question
    ADD COLUMN spanish varchar;
ALTER TABLE ag.survey_question_response
    ADD COLUMN spanish varchar;
UPDATE ag.survey_question SET spanish = '¿Cómo describiría su dieta?'
  WHERE survey_question_id = 1;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 1 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Omnívora'
  WHERE survey_question_id = 1 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Omnívora, pero no consumo carne roja'
  WHERE survey_question_id = 1 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Vegetariana'
  WHERE survey_question_id = 1 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Vegetariana, pero consumo pescado y mariscos'
  WHERE survey_question_id = 1 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Vegana'
  WHERE survey_question_id = 1 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Lleva una dieta paleolítica, paleolítica modificada, primitiva, FODMAP, de Weston-Price o alguna otra dieta con bajo contenido de cereales y de alimentos procesados?'
  WHERE survey_question_id = 10;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 10 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 10 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 10 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Vive el perro dentro/fuera de la casa o está encerrado (en una jaula)?'
  WHERE survey_question_id = 101;

UPDATE ag.survey_question SET spanish = 'Raza/etnia:'
  WHERE survey_question_id = 103;

UPDATE ag.survey_question SET spanish = 'Suplementos alimenticios:'
  WHERE survey_question_id = 104;

UPDATE ag.survey_question SET spanish = 'Nivel de contacto con el perro:'
  WHERE survey_question_id = 105;

UPDATE ag.survey_question SET spanish = 'Otras afecciones que tenga y que no aparezcan en las preguntas sobre afecciones diagnosticadas'
  WHERE survey_question_id = 106;

UPDATE ag.survey_question SET spanish = 'Sexo:'
  WHERE survey_question_id = 107;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 107 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Hombre'
  WHERE survey_question_id = 107 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Mujer'
  WHERE survey_question_id = 107 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Otro'
  WHERE survey_question_id = 107 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = 'Estatura:'
  WHERE survey_question_id = 108;

UPDATE ag.survey_question SET spanish = 'Unidades de medida de estatura:'
  WHERE survey_question_id = 109;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 109 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'pulgadas'
  WHERE survey_question_id = 109 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'centímetros'
  WHERE survey_question_id = 109 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Consume carne o productos lácteos  de animales tratados con antibióticos?'
  WHERE survey_question_id = 11;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 11 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 11 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 11 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro'
  WHERE survey_question_id = 11 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = 'País de nacimiento:'
  WHERE survey_question_id = 110;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 110 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Afganistán'
  WHERE survey_question_id = 110 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Aland'
  WHERE survey_question_id = 110 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Albania'
  WHERE survey_question_id = 110 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Argelia'
  WHERE survey_question_id = 110 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Samoa Americana'
  WHERE survey_question_id = 110 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Andorra'
  WHERE survey_question_id = 110 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Angola'
  WHERE survey_question_id = 110 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = 'Anguila'
  WHERE survey_question_id = 110 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = 'Antártida'
  WHERE survey_question_id = 110 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET spanish = 'Antigua y Barbuda'
  WHERE survey_question_id = 110 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET spanish = 'Argentina'
  WHERE survey_question_id = 110 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET spanish = 'Armenia'
  WHERE survey_question_id = 110 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET spanish = 'Aruba'
  WHERE survey_question_id = 110 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET spanish = 'Australia'
  WHERE survey_question_id = 110 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET spanish = 'Austria'
  WHERE survey_question_id = 110 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET spanish = 'Azerbaiyán'
  WHERE survey_question_id = 110 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET spanish = 'Bahamas'
  WHERE survey_question_id = 110 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET spanish = 'Bahrein'
  WHERE survey_question_id = 110 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET spanish = 'Bangladesh'
  WHERE survey_question_id = 110 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET spanish = 'Barbados'
  WHERE survey_question_id = 110 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET spanish = 'Bielorrusia'
  WHERE survey_question_id = 110 AND
        display_index = 21;
UPDATE ag.survey_question_response 
  SET spanish = 'Bélgica'
  WHERE survey_question_id = 110 AND
        display_index = 22;
UPDATE ag.survey_question_response 
  SET spanish = 'Belice'
  WHERE survey_question_id = 110 AND
        display_index = 23;
UPDATE ag.survey_question_response 
  SET spanish = 'Benin'
  WHERE survey_question_id = 110 AND
        display_index = 24;
UPDATE ag.survey_question_response 
  SET spanish = 'islas Bermudas'
  WHERE survey_question_id = 110 AND
        display_index = 25;
UPDATE ag.survey_question_response 
  SET spanish = 'Bután'
  WHERE survey_question_id = 110 AND
        display_index = 26;
UPDATE ag.survey_question_response 
  SET spanish = 'Bolivia'
  WHERE survey_question_id = 110 AND
        display_index = 27;
UPDATE ag.survey_question_response 
  SET spanish = 'Bosnia y Herzegovina'
  WHERE survey_question_id = 110 AND
        display_index = 28;
UPDATE ag.survey_question_response 
  SET spanish = 'Botsuana'
  WHERE survey_question_id = 110 AND
        display_index = 29;
UPDATE ag.survey_question_response 
  SET spanish = 'Isla Bouvet'
  WHERE survey_question_id = 110 AND
        display_index = 30;
UPDATE ag.survey_question_response 
  SET spanish = 'Brasil'
  WHERE survey_question_id = 110 AND
        display_index = 31;
UPDATE ag.survey_question_response 
  SET spanish = 'Territorio Británico del Océano Índico'
  WHERE survey_question_id = 110 AND
        display_index = 32;
UPDATE ag.survey_question_response 
  SET spanish = 'Brunei Darussalam'
  WHERE survey_question_id = 110 AND
        display_index = 33;
UPDATE ag.survey_question_response 
  SET spanish = 'Bulgaria'
  WHERE survey_question_id = 110 AND
        display_index = 34;
UPDATE ag.survey_question_response 
  SET spanish = 'Burkina Faso'
  WHERE survey_question_id = 110 AND
        display_index = 35;
UPDATE ag.survey_question_response 
  SET spanish = 'Burundi'
  WHERE survey_question_id = 110 AND
        display_index = 36;
UPDATE ag.survey_question_response 
  SET spanish = 'Camboya'
  WHERE survey_question_id = 110 AND
        display_index = 37;
UPDATE ag.survey_question_response 
  SET spanish = 'Camerún'
  WHERE survey_question_id = 110 AND
        display_index = 38;
UPDATE ag.survey_question_response 
  SET spanish = 'Canadá'
  WHERE survey_question_id = 110 AND
        display_index = 39;
UPDATE ag.survey_question_response 
  SET spanish = 'Cabo Verde'
  WHERE survey_question_id = 110 AND
        display_index = 40;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Caimán'
  WHERE survey_question_id = 110 AND
        display_index = 41;
UPDATE ag.survey_question_response 
  SET spanish = 'República Centroafricana'
  WHERE survey_question_id = 110 AND
        display_index = 42;
UPDATE ag.survey_question_response 
  SET spanish = 'Chad'
  WHERE survey_question_id = 110 AND
        display_index = 43;
UPDATE ag.survey_question_response 
  SET spanish = 'Chile'
  WHERE survey_question_id = 110 AND
        display_index = 44;
UPDATE ag.survey_question_response 
  SET spanish = 'China'
  WHERE survey_question_id = 110 AND
        display_index = 45;
UPDATE ag.survey_question_response 
  SET spanish = 'Isla de Navidad'
  WHERE survey_question_id = 110 AND
        display_index = 46;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Cocos (Keeling)'
  WHERE survey_question_id = 110 AND
        display_index = 47;
UPDATE ag.survey_question_response 
  SET spanish = 'Colombia'
  WHERE survey_question_id = 110 AND
        display_index = 48;
UPDATE ag.survey_question_response 
  SET spanish = 'Comoras'
  WHERE survey_question_id = 110 AND
        display_index = 49;
UPDATE ag.survey_question_response 
  SET spanish = 'Congo'
  WHERE survey_question_id = 110 AND
        display_index = 50;
UPDATE ag.survey_question_response 
  SET spanish = 'Congo, República Democrática del'
  WHERE survey_question_id = 110 AND
        display_index = 51;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Cook'
  WHERE survey_question_id = 110 AND
        display_index = 52;
UPDATE ag.survey_question_response 
  SET spanish = 'Costa Rica'
  WHERE survey_question_id = 110 AND
        display_index = 53;
UPDATE ag.survey_question_response 
  SET spanish = 'Costa de Marfil'
  WHERE survey_question_id = 110 AND
        display_index = 54;
UPDATE ag.survey_question_response 
  SET spanish = 'Croacia'
  WHERE survey_question_id = 110 AND
        display_index = 55;
UPDATE ag.survey_question_response 
  SET spanish = 'Cuba'
  WHERE survey_question_id = 110 AND
        display_index = 56;
UPDATE ag.survey_question_response 
  SET spanish = 'Chipre'
  WHERE survey_question_id = 110 AND
        display_index = 57;
UPDATE ag.survey_question_response 
  SET spanish = 'Republica checa'
  WHERE survey_question_id = 110 AND
        display_index = 58;
UPDATE ag.survey_question_response 
  SET spanish = 'Dinamarca'
  WHERE survey_question_id = 110 AND
        display_index = 59;
UPDATE ag.survey_question_response 
  SET spanish = 'Djibouti'
  WHERE survey_question_id = 110 AND
        display_index = 60;
UPDATE ag.survey_question_response 
  SET spanish = 'Dominica'
  WHERE survey_question_id = 110 AND
        display_index = 61;
UPDATE ag.survey_question_response 
  SET spanish = 'República Dominicana'
  WHERE survey_question_id = 110 AND
        display_index = 62;
UPDATE ag.survey_question_response 
  SET spanish = 'Ecuador'
  WHERE survey_question_id = 110 AND
        display_index = 63;
UPDATE ag.survey_question_response 
  SET spanish = 'Egipto'
  WHERE survey_question_id = 110 AND
        display_index = 64;
UPDATE ag.survey_question_response 
  SET spanish = 'El Salvador'
  WHERE survey_question_id = 110 AND
        display_index = 65;
UPDATE ag.survey_question_response 
  SET spanish = 'Guinea Ecuatorial'
  WHERE survey_question_id = 110 AND
        display_index = 66;
UPDATE ag.survey_question_response 
  SET spanish = 'Eritrea'
  WHERE survey_question_id = 110 AND
        display_index = 67;
UPDATE ag.survey_question_response 
  SET spanish = 'Estonia'
  WHERE survey_question_id = 110 AND
        display_index = 68;
UPDATE ag.survey_question_response 
  SET spanish = 'Etiopía'
  WHERE survey_question_id = 110 AND
        display_index = 69;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Malvinas (Falkland Islands)'
  WHERE survey_question_id = 110 AND
        display_index = 70;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Faroe'
  WHERE survey_question_id = 110 AND
        display_index = 71;
UPDATE ag.survey_question_response 
  SET spanish = 'Fiyi'
  WHERE survey_question_id = 110 AND
        display_index = 72;
UPDATE ag.survey_question_response 
  SET spanish = 'Finlandia'
  WHERE survey_question_id = 110 AND
        display_index = 73;
UPDATE ag.survey_question_response 
  SET spanish = 'Francia'
  WHERE survey_question_id = 110 AND
        display_index = 74;
UPDATE ag.survey_question_response 
  SET spanish = 'Guayana Francesa'
  WHERE survey_question_id = 110 AND
        display_index = 75;
UPDATE ag.survey_question_response 
  SET spanish = 'Polinesia francés'
  WHERE survey_question_id = 110 AND
        display_index = 76;
UPDATE ag.survey_question_response 
  SET spanish = 'Territorios Franceses del Sur'
  WHERE survey_question_id = 110 AND
        display_index = 77;
UPDATE ag.survey_question_response 
  SET spanish = 'Gabón'
  WHERE survey_question_id = 110 AND
        display_index = 78;
UPDATE ag.survey_question_response 
  SET spanish = 'Gambia'
  WHERE survey_question_id = 110 AND
        display_index = 79;
UPDATE ag.survey_question_response 
  SET spanish = 'Georgia'
  WHERE survey_question_id = 110 AND
        display_index = 80;
UPDATE ag.survey_question_response 
  SET spanish = 'Alemania'
  WHERE survey_question_id = 110 AND
        display_index = 81;
UPDATE ag.survey_question_response 
  SET spanish = 'Ghana'
  WHERE survey_question_id = 110 AND
        display_index = 82;
UPDATE ag.survey_question_response 
  SET spanish = 'Gibraltar'
  WHERE survey_question_id = 110 AND
        display_index = 83;
UPDATE ag.survey_question_response 
  SET spanish = 'Grecia'
  WHERE survey_question_id = 110 AND
        display_index = 84;
UPDATE ag.survey_question_response 
  SET spanish = 'Groenlandia'
  WHERE survey_question_id = 110 AND
        display_index = 85;
UPDATE ag.survey_question_response 
  SET spanish = 'Granada'
  WHERE survey_question_id = 110 AND
        display_index = 86;
UPDATE ag.survey_question_response 
  SET spanish = 'Guadalupe'
  WHERE survey_question_id = 110 AND
        display_index = 87;
UPDATE ag.survey_question_response 
  SET spanish = 'Guam'
  WHERE survey_question_id = 110 AND
        display_index = 88;
UPDATE ag.survey_question_response 
  SET spanish = 'Guatemala'
  WHERE survey_question_id = 110 AND
        display_index = 89;
UPDATE ag.survey_question_response 
  SET spanish = 'Guernsey'
  WHERE survey_question_id = 110 AND
        display_index = 90;
UPDATE ag.survey_question_response 
  SET spanish = 'Guinea'
  WHERE survey_question_id = 110 AND
        display_index = 91;
UPDATE ag.survey_question_response 
  SET spanish = 'Guinea-Bissau'
  WHERE survey_question_id = 110 AND
        display_index = 92;
UPDATE ag.survey_question_response 
  SET spanish = 'Guayana'
  WHERE survey_question_id = 110 AND
        display_index = 93;
UPDATE ag.survey_question_response 
  SET spanish = 'Haití'
  WHERE survey_question_id = 110 AND
        display_index = 94;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Heard y Mcdonald'
  WHERE survey_question_id = 110 AND
        display_index = 95;
UPDATE ag.survey_question_response 
  SET spanish = 'Santa Sede (Estado de la Ciudad del Vaticano)'
  WHERE survey_question_id = 110 AND
        display_index = 96;
UPDATE ag.survey_question_response 
  SET spanish = 'Honduras'
  WHERE survey_question_id = 110 AND
        display_index = 97;
UPDATE ag.survey_question_response 
  SET spanish = 'Hong Kong'
  WHERE survey_question_id = 110 AND
        display_index = 98;
UPDATE ag.survey_question_response 
  SET spanish = 'Hungría'
  WHERE survey_question_id = 110 AND
        display_index = 99;
UPDATE ag.survey_question_response 
  SET spanish = 'Islandia'
  WHERE survey_question_id = 110 AND
        display_index = 100;
UPDATE ag.survey_question_response 
  SET spanish = 'India'
  WHERE survey_question_id = 110 AND
        display_index = 101;
UPDATE ag.survey_question_response 
  SET spanish = 'Indonesia'
  WHERE survey_question_id = 110 AND
        display_index = 102;
UPDATE ag.survey_question_response 
  SET spanish = 'Irán (República Islámica de'
  WHERE survey_question_id = 110 AND
        display_index = 103;
UPDATE ag.survey_question_response 
  SET spanish = 'Irak'
  WHERE survey_question_id = 110 AND
        display_index = 104;
UPDATE ag.survey_question_response 
  SET spanish = 'Irlanda'
  WHERE survey_question_id = 110 AND
        display_index = 105;
UPDATE ag.survey_question_response 
  SET spanish = 'Isla del hombre'
  WHERE survey_question_id = 110 AND
        display_index = 106;
UPDATE ag.survey_question_response 
  SET spanish = 'Israel'
  WHERE survey_question_id = 110 AND
        display_index = 107;
UPDATE ag.survey_question_response 
  SET spanish = 'Italia'
  WHERE survey_question_id = 110 AND
        display_index = 108;
UPDATE ag.survey_question_response 
  SET spanish = 'Jamaica'
  WHERE survey_question_id = 110 AND
        display_index = 109;
UPDATE ag.survey_question_response 
  SET spanish = 'Japón'
  WHERE survey_question_id = 110 AND
        display_index = 110;
UPDATE ag.survey_question_response 
  SET spanish = 'Jersey'
  WHERE survey_question_id = 110 AND
        display_index = 111;
UPDATE ag.survey_question_response 
  SET spanish = 'Jordán'
  WHERE survey_question_id = 110 AND
        display_index = 112;
UPDATE ag.survey_question_response 
  SET spanish = 'Kazajstán'
  WHERE survey_question_id = 110 AND
        display_index = 113;
UPDATE ag.survey_question_response 
  SET spanish = 'Kenia'
  WHERE survey_question_id = 110 AND
        display_index = 114;
UPDATE ag.survey_question_response 
  SET spanish = 'Kiribati'
  WHERE survey_question_id = 110 AND
        display_index = 115;
UPDATE ag.survey_question_response 
  SET spanish = 'República de Corea, Popular Democrática de'
  WHERE survey_question_id = 110 AND
        display_index = 116;
UPDATE ag.survey_question_response 
  SET spanish = 'Corea, república de'
  WHERE survey_question_id = 110 AND
        display_index = 117;
UPDATE ag.survey_question_response 
  SET spanish = 'Kuwait'
  WHERE survey_question_id = 110 AND
        display_index = 118;
UPDATE ag.survey_question_response 
  SET spanish = 'Kirguistán'
  WHERE survey_question_id = 110 AND
        display_index = 119;
UPDATE ag.survey_question_response 
  SET spanish = 'República Democrática Popular Lao'
  WHERE survey_question_id = 110 AND
        display_index = 120;
UPDATE ag.survey_question_response 
  SET spanish = 'Letonia'
  WHERE survey_question_id = 110 AND
        display_index = 121;
UPDATE ag.survey_question_response 
  SET spanish = 'Líbano'
  WHERE survey_question_id = 110 AND
        display_index = 122;
UPDATE ag.survey_question_response 
  SET spanish = 'Lesoto'
  WHERE survey_question_id = 110 AND
        display_index = 123;
UPDATE ag.survey_question_response 
  SET spanish = 'Liberia'
  WHERE survey_question_id = 110 AND
        display_index = 124;
UPDATE ag.survey_question_response 
  SET spanish = 'Jamahiriya Árabe Libia'
  WHERE survey_question_id = 110 AND
        display_index = 125;
UPDATE ag.survey_question_response 
  SET spanish = 'Liechtenstein'
  WHERE survey_question_id = 110 AND
        display_index = 126;
UPDATE ag.survey_question_response 
  SET spanish = 'Lituania'
  WHERE survey_question_id = 110 AND
        display_index = 127;
UPDATE ag.survey_question_response 
  SET spanish = 'Luxemburgo'
  WHERE survey_question_id = 110 AND
        display_index = 128;
UPDATE ag.survey_question_response 
  SET spanish = 'Macao'
  WHERE survey_question_id = 110 AND
        display_index = 129;
UPDATE ag.survey_question_response 
  SET spanish = 'Macedonia, la ex República Yugoslava de'
  WHERE survey_question_id = 110 AND
        display_index = 130;
UPDATE ag.survey_question_response 
  SET spanish = 'Madagascar'
  WHERE survey_question_id = 110 AND
        display_index = 131;
UPDATE ag.survey_question_response 
  SET spanish = 'Malawi'
  WHERE survey_question_id = 110 AND
        display_index = 132;
UPDATE ag.survey_question_response 
  SET spanish = 'Malasia'
  WHERE survey_question_id = 110 AND
        display_index = 133;
UPDATE ag.survey_question_response 
  SET spanish = 'Maldivas'
  WHERE survey_question_id = 110 AND
        display_index = 134;
UPDATE ag.survey_question_response 
  SET spanish = 'Mali'
  WHERE survey_question_id = 110 AND
        display_index = 135;
UPDATE ag.survey_question_response 
  SET spanish = 'Malta'
  WHERE survey_question_id = 110 AND
        display_index = 136;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Marshall'
  WHERE survey_question_id = 110 AND
        display_index = 137;
UPDATE ag.survey_question_response 
  SET spanish = 'Martinica'
  WHERE survey_question_id = 110 AND
        display_index = 138;
UPDATE ag.survey_question_response 
  SET spanish = 'Mauritania'
  WHERE survey_question_id = 110 AND
        display_index = 139;
UPDATE ag.survey_question_response 
  SET spanish = 'Mauricio'
  WHERE survey_question_id = 110 AND
        display_index = 140;
UPDATE ag.survey_question_response 
  SET spanish = 'Mayotte'
  WHERE survey_question_id = 110 AND
        display_index = 141;
UPDATE ag.survey_question_response 
  SET spanish = 'Mexico'
  WHERE survey_question_id = 110 AND
        display_index = 142;
UPDATE ag.survey_question_response 
  SET spanish = 'Micronesia, Estados Federados de'
  WHERE survey_question_id = 110 AND
        display_index = 143;
UPDATE ag.survey_question_response 
  SET spanish = 'Moldavia, República de'
  WHERE survey_question_id = 110 AND
        display_index = 144;
UPDATE ag.survey_question_response 
  SET spanish = 'Mónaco'
  WHERE survey_question_id = 110 AND
        display_index = 145;
UPDATE ag.survey_question_response 
  SET spanish = 'Mongolia'
  WHERE survey_question_id = 110 AND
        display_index = 146;
UPDATE ag.survey_question_response 
  SET spanish = 'Montenegro'
  WHERE survey_question_id = 110 AND
        display_index = 147;
UPDATE ag.survey_question_response 
  SET spanish = 'Montserrat'
  WHERE survey_question_id = 110 AND
        display_index = 148;
UPDATE ag.survey_question_response 
  SET spanish = 'Marruecos'
  WHERE survey_question_id = 110 AND
        display_index = 149;
UPDATE ag.survey_question_response 
  SET spanish = 'Mozambique'
  WHERE survey_question_id = 110 AND
        display_index = 150;
UPDATE ag.survey_question_response 
  SET spanish = 'Myanmar'
  WHERE survey_question_id = 110 AND
        display_index = 151;
UPDATE ag.survey_question_response 
  SET spanish = 'Namibia'
  WHERE survey_question_id = 110 AND
        display_index = 152;
UPDATE ag.survey_question_response 
  SET spanish = 'Nauru'
  WHERE survey_question_id = 110 AND
        display_index = 153;
UPDATE ag.survey_question_response 
  SET spanish = 'Nepal'
  WHERE survey_question_id = 110 AND
        display_index = 154;
UPDATE ag.survey_question_response 
  SET spanish = 'Países Bajos'
  WHERE survey_question_id = 110 AND
        display_index = 155;
UPDATE ag.survey_question_response 
  SET spanish = 'Antillas Holandesas'
  WHERE survey_question_id = 110 AND
        display_index = 156;
UPDATE ag.survey_question_response 
  SET spanish = 'Nueva Caledonia'
  WHERE survey_question_id = 110 AND
        display_index = 157;
UPDATE ag.survey_question_response 
  SET spanish = 'Nueva Zelanda'
  WHERE survey_question_id = 110 AND
        display_index = 158;
UPDATE ag.survey_question_response 
  SET spanish = 'Nicaragua'
  WHERE survey_question_id = 110 AND
        display_index = 159;
UPDATE ag.survey_question_response 
  SET spanish = 'Níger'
  WHERE survey_question_id = 110 AND
        display_index = 160;
UPDATE ag.survey_question_response 
  SET spanish = 'Nigeria'
  WHERE survey_question_id = 110 AND
        display_index = 161;
UPDATE ag.survey_question_response 
  SET spanish = 'Niue'
  WHERE survey_question_id = 110 AND
        display_index = 162;
UPDATE ag.survey_question_response 
  SET spanish = 'Isla Norfolk'
  WHERE survey_question_id = 110 AND
        display_index = 163;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Marianas del Norte'
  WHERE survey_question_id = 110 AND
        display_index = 164;
UPDATE ag.survey_question_response 
  SET spanish = 'Noruega'
  WHERE survey_question_id = 110 AND
        display_index = 165;
UPDATE ag.survey_question_response 
  SET spanish = 'Omán'
  WHERE survey_question_id = 110 AND
        display_index = 166;
UPDATE ag.survey_question_response 
  SET spanish = 'Pakistán'
  WHERE survey_question_id = 110 AND
        display_index = 167;
UPDATE ag.survey_question_response 
  SET spanish = 'Palau'
  WHERE survey_question_id = 110 AND
        display_index = 168;
UPDATE ag.survey_question_response 
  SET spanish = 'Territorio Palestino, Ocupado'
  WHERE survey_question_id = 110 AND
        display_index = 169;
UPDATE ag.survey_question_response 
  SET spanish = 'Panamá'
  WHERE survey_question_id = 110 AND
        display_index = 170;
UPDATE ag.survey_question_response 
  SET spanish = 'Papúa Nueva Guinea'
  WHERE survey_question_id = 110 AND
        display_index = 171;
UPDATE ag.survey_question_response 
  SET spanish = 'Paraguay'
  WHERE survey_question_id = 110 AND
        display_index = 172;
UPDATE ag.survey_question_response 
  SET spanish = 'Perú'
  WHERE survey_question_id = 110 AND
        display_index = 173;
UPDATE ag.survey_question_response 
  SET spanish = 'Filipinas'
  WHERE survey_question_id = 110 AND
        display_index = 174;
UPDATE ag.survey_question_response 
  SET spanish = 'Pitcairn'
  WHERE survey_question_id = 110 AND
        display_index = 175;
UPDATE ag.survey_question_response 
  SET spanish = 'Polonia'
  WHERE survey_question_id = 110 AND
        display_index = 176;
UPDATE ag.survey_question_response 
  SET spanish = 'Portugal'
  WHERE survey_question_id = 110 AND
        display_index = 177;
UPDATE ag.survey_question_response 
  SET spanish = 'Puerto Rico'
  WHERE survey_question_id = 110 AND
        display_index = 178;
UPDATE ag.survey_question_response 
  SET spanish = 'Katar'
  WHERE survey_question_id = 110 AND
        display_index = 179;
UPDATE ag.survey_question_response 
  SET spanish = 'Reunión'
  WHERE survey_question_id = 110 AND
        display_index = 180;
UPDATE ag.survey_question_response 
  SET spanish = 'Rumania'
  WHERE survey_question_id = 110 AND
        display_index = 181;
UPDATE ag.survey_question_response 
  SET spanish = 'Federación Rusa'
  WHERE survey_question_id = 110 AND
        display_index = 182;
UPDATE ag.survey_question_response 
  SET spanish = 'Ruanda'
  WHERE survey_question_id = 110 AND
        display_index = 183;
UPDATE ag.survey_question_response 
  SET spanish = 'Santa helena'
  WHERE survey_question_id = 110 AND
        display_index = 184;
UPDATE ag.survey_question_response 
  SET spanish = 'San Cristóbal y Nieves'
  WHERE survey_question_id = 110 AND
        display_index = 185;
UPDATE ag.survey_question_response 
  SET spanish = 'Santa Lucía'
  WHERE survey_question_id = 110 AND
        display_index = 186;
UPDATE ag.survey_question_response 
  SET spanish = 'San Pedro y Miquelón'
  WHERE survey_question_id = 110 AND
        display_index = 187;
UPDATE ag.survey_question_response 
  SET spanish = 'San Vicente y las Granadinas'
  WHERE survey_question_id = 110 AND
        display_index = 188;
UPDATE ag.survey_question_response 
  SET spanish = 'Samoa'
  WHERE survey_question_id = 110 AND
        display_index = 189;
UPDATE ag.survey_question_response 
  SET spanish = 'San Marino'
  WHERE survey_question_id = 110 AND
        display_index = 190;
UPDATE ag.survey_question_response 
  SET spanish = 'Santo Tomé y Príncipe'
  WHERE survey_question_id = 110 AND
        display_index = 191;
UPDATE ag.survey_question_response 
  SET spanish = 'Arabia Saudita'
  WHERE survey_question_id = 110 AND
        display_index = 192;
UPDATE ag.survey_question_response 
  SET spanish = 'Senegal'
  WHERE survey_question_id = 110 AND
        display_index = 193;
UPDATE ag.survey_question_response 
  SET spanish = 'Serbia'
  WHERE survey_question_id = 110 AND
        display_index = 194;
UPDATE ag.survey_question_response 
  SET spanish = 'Seychelles'
  WHERE survey_question_id = 110 AND
        display_index = 195;
UPDATE ag.survey_question_response 
  SET spanish = 'Sierra Leona'
  WHERE survey_question_id = 110 AND
        display_index = 196;
UPDATE ag.survey_question_response 
  SET spanish = 'Singapur'
  WHERE survey_question_id = 110 AND
        display_index = 197;
UPDATE ag.survey_question_response 
  SET spanish = 'Eslovaquia'
  WHERE survey_question_id = 110 AND
        display_index = 198;
UPDATE ag.survey_question_response 
  SET spanish = 'Eslovenia'
  WHERE survey_question_id = 110 AND
        display_index = 199;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Salomón'
  WHERE survey_question_id = 110 AND
        display_index = 200;
UPDATE ag.survey_question_response 
  SET spanish = 'Somalia'
  WHERE survey_question_id = 110 AND
        display_index = 201;
UPDATE ag.survey_question_response 
  SET spanish = 'Sudáfrica'
  WHERE survey_question_id = 110 AND
        display_index = 202;
UPDATE ag.survey_question_response 
  SET spanish = 'Georgia del sur y las islas Sandwich del sur'
  WHERE survey_question_id = 110 AND
        display_index = 203;
UPDATE ag.survey_question_response 
  SET spanish = 'España'
  WHERE survey_question_id = 110 AND
        display_index = 204;
UPDATE ag.survey_question_response 
  SET spanish = 'Sri Lanka'
  WHERE survey_question_id = 110 AND
        display_index = 205;
UPDATE ag.survey_question_response 
  SET spanish = 'Sudán'
  WHERE survey_question_id = 110 AND
        display_index = 206;
UPDATE ag.survey_question_response 
  SET spanish = 'Surinam'
  WHERE survey_question_id = 110 AND
        display_index = 207;
UPDATE ag.survey_question_response 
  SET spanish = 'Svalbard y Jan Mayen'
  WHERE survey_question_id = 110 AND
        display_index = 208;
UPDATE ag.survey_question_response 
  SET spanish = 'Swazilandia'
  WHERE survey_question_id = 110 AND
        display_index = 209;
UPDATE ag.survey_question_response 
  SET spanish = 'Suecia'
  WHERE survey_question_id = 110 AND
        display_index = 210;
UPDATE ag.survey_question_response 
  SET spanish = 'Suiza'
  WHERE survey_question_id = 110 AND
        display_index = 211;
UPDATE ag.survey_question_response 
  SET spanish = 'República Árabe Siria'
  WHERE survey_question_id = 110 AND
        display_index = 212;
UPDATE ag.survey_question_response 
  SET spanish = 'Taiwan, provincia de China'
  WHERE survey_question_id = 110 AND
        display_index = 213;
UPDATE ag.survey_question_response 
  SET spanish = 'Tayikistán'
  WHERE survey_question_id = 110 AND
        display_index = 214;
UPDATE ag.survey_question_response 
  SET spanish = 'Tanzania, República Unida de'
  WHERE survey_question_id = 110 AND
        display_index = 215;
UPDATE ag.survey_question_response 
  SET spanish = 'Tailandia'
  WHERE survey_question_id = 110 AND
        display_index = 216;
UPDATE ag.survey_question_response 
  SET spanish = 'Timor-leste'
  WHERE survey_question_id = 110 AND
        display_index = 217;
UPDATE ag.survey_question_response 
  SET spanish = 'Ir'
  WHERE survey_question_id = 110 AND
        display_index = 218;
UPDATE ag.survey_question_response 
  SET spanish = 'Tokelau'
  WHERE survey_question_id = 110 AND
        display_index = 219;
UPDATE ag.survey_question_response 
  SET spanish = 'Tonga'
  WHERE survey_question_id = 110 AND
        display_index = 220;
UPDATE ag.survey_question_response 
  SET spanish = 'Trinidad y Tobago'
  WHERE survey_question_id = 110 AND
        display_index = 221;
UPDATE ag.survey_question_response 
  SET spanish = 'Túnez'
  WHERE survey_question_id = 110 AND
        display_index = 222;
UPDATE ag.survey_question_response 
  SET spanish = 'pavo'
  WHERE survey_question_id = 110 AND
        display_index = 223;
UPDATE ag.survey_question_response 
  SET spanish = 'Turkmenistán'
  WHERE survey_question_id = 110 AND
        display_index = 224;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Turcas y Caicos'
  WHERE survey_question_id = 110 AND
        display_index = 225;
UPDATE ag.survey_question_response 
  SET spanish = 'Tuvalu'
  WHERE survey_question_id = 110 AND
        display_index = 226;
UPDATE ag.survey_question_response 
  SET spanish = 'Uganda'
  WHERE survey_question_id = 110 AND
        display_index = 227;
UPDATE ag.survey_question_response 
  SET spanish = 'Ucrania'
  WHERE survey_question_id = 110 AND
        display_index = 228;
UPDATE ag.survey_question_response 
  SET spanish = 'Emiratos Árabes Unidos'
  WHERE survey_question_id = 110 AND
        display_index = 229;
UPDATE ag.survey_question_response 
  SET spanish = 'Reino Unido'
  WHERE survey_question_id = 110 AND
        display_index = 230;
UPDATE ag.survey_question_response 
  SET spanish = 'Estados Unidos'
  WHERE survey_question_id = 110 AND
        display_index = 231;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas ultramarinas menores de Estados Unidos'
  WHERE survey_question_id = 110 AND
        display_index = 232;
UPDATE ag.survey_question_response 
  SET spanish = 'Uruguay'
  WHERE survey_question_id = 110 AND
        display_index = 233;
UPDATE ag.survey_question_response 
  SET spanish = 'Uzbekistán'
  WHERE survey_question_id = 110 AND
        display_index = 234;
UPDATE ag.survey_question_response 
  SET spanish = 'Vanuatu'
  WHERE survey_question_id = 110 AND
        display_index = 235;
UPDATE ag.survey_question_response 
  SET spanish = 'Venezuela'
  WHERE survey_question_id = 110 AND
        display_index = 236;
UPDATE ag.survey_question_response 
  SET spanish = 'Vietnam'
  WHERE survey_question_id = 110 AND
        display_index = 237;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Vírgenes Británicas'
  WHERE survey_question_id = 110 AND
        display_index = 238;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Vírgenes, EE. UU.'
  WHERE survey_question_id = 110 AND
        display_index = 239;
UPDATE ag.survey_question_response 
  SET spanish = 'Wallis y Futuna'
  WHERE survey_question_id = 110 AND
        display_index = 240;
UPDATE ag.survey_question_response 
  SET spanish = 'Sahara Occidental'
  WHERE survey_question_id = 110 AND
        display_index = 241;
UPDATE ag.survey_question_response 
  SET spanish = 'Yemen'
  WHERE survey_question_id = 110 AND
        display_index = 242;
UPDATE ag.survey_question_response 
  SET spanish = 'Zambia'
  WHERE survey_question_id = 110 AND
        display_index = 243;
UPDATE ag.survey_question_response 
  SET spanish = 'Zimbabue'
  WHERE survey_question_id = 110 AND
        display_index = 244;

UPDATE ag.survey_question SET spanish = 'Mes de nacimiento:'
  WHERE survey_question_id = 111;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 111 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'enero'
  WHERE survey_question_id = 111 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'febrero'
  WHERE survey_question_id = 111 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'marzo'
  WHERE survey_question_id = 111 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'abril'
  WHERE survey_question_id = 111 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Mayo'
  WHERE survey_question_id = 111 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'junio'
  WHERE survey_question_id = 111 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'julio'
  WHERE survey_question_id = 111 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = 'agosto'
  WHERE survey_question_id = 111 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = 'septiembre'
  WHERE survey_question_id = 111 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET spanish = 'octubre'
  WHERE survey_question_id = 111 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET spanish = 'noviembre'
  WHERE survey_question_id = 111 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET spanish = 'diciembre'
  WHERE survey_question_id = 111 AND
        display_index = 12;

UPDATE ag.survey_question SET spanish = 'Año de nacimiento:'
  WHERE survey_question_id = 112;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 112 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = '2018'
  WHERE survey_question_id = 112 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = '2017'
  WHERE survey_question_id = 112 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '2016'
  WHERE survey_question_id = 112 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = '2015'
  WHERE survey_question_id = 112 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = '2014'
  WHERE survey_question_id = 112 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = '2013'
  WHERE survey_question_id = 112 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = '2012'
  WHERE survey_question_id = 112 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = '2011'
  WHERE survey_question_id = 112 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = '2010'
  WHERE survey_question_id = 112 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET spanish = '2009'
  WHERE survey_question_id = 112 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET spanish = '2008'
  WHERE survey_question_id = 112 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET spanish = '2007'
  WHERE survey_question_id = 112 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET spanish = '2006'
  WHERE survey_question_id = 112 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET spanish = '2005'
  WHERE survey_question_id = 112 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET spanish = '2004'
  WHERE survey_question_id = 112 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET spanish = '2003'
  WHERE survey_question_id = 112 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET spanish = '2002'
  WHERE survey_question_id = 112 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET spanish = '2001'
  WHERE survey_question_id = 112 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET spanish = '2000'
  WHERE survey_question_id = 112 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET spanish = '1999'
  WHERE survey_question_id = 112 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET spanish = '1998'
  WHERE survey_question_id = 112 AND
        display_index = 21;
UPDATE ag.survey_question_response 
  SET spanish = '1997'
  WHERE survey_question_id = 112 AND
        display_index = 22;
UPDATE ag.survey_question_response 
  SET spanish = '1996'
  WHERE survey_question_id = 112 AND
        display_index = 23;
UPDATE ag.survey_question_response 
  SET spanish = '1995'
  WHERE survey_question_id = 112 AND
        display_index = 24;
UPDATE ag.survey_question_response 
  SET spanish = '1994'
  WHERE survey_question_id = 112 AND
        display_index = 25;
UPDATE ag.survey_question_response 
  SET spanish = '1993'
  WHERE survey_question_id = 112 AND
        display_index = 26;
UPDATE ag.survey_question_response 
  SET spanish = '1992'
  WHERE survey_question_id = 112 AND
        display_index = 27;
UPDATE ag.survey_question_response 
  SET spanish = '1991'
  WHERE survey_question_id = 112 AND
        display_index = 28;
UPDATE ag.survey_question_response 
  SET spanish = '1990'
  WHERE survey_question_id = 112 AND
        display_index = 29;
UPDATE ag.survey_question_response 
  SET spanish = '1989'
  WHERE survey_question_id = 112 AND
        display_index = 30;
UPDATE ag.survey_question_response 
  SET spanish = '1988'
  WHERE survey_question_id = 112 AND
        display_index = 31;
UPDATE ag.survey_question_response 
  SET spanish = '1987'
  WHERE survey_question_id = 112 AND
        display_index = 32;
UPDATE ag.survey_question_response 
  SET spanish = '1986'
  WHERE survey_question_id = 112 AND
        display_index = 33;
UPDATE ag.survey_question_response 
  SET spanish = '1985'
  WHERE survey_question_id = 112 AND
        display_index = 34;
UPDATE ag.survey_question_response 
  SET spanish = '1984'
  WHERE survey_question_id = 112 AND
        display_index = 35;
UPDATE ag.survey_question_response 
  SET spanish = '1983'
  WHERE survey_question_id = 112 AND
        display_index = 36;
UPDATE ag.survey_question_response 
  SET spanish = '1982'
  WHERE survey_question_id = 112 AND
        display_index = 37;
UPDATE ag.survey_question_response 
  SET spanish = '1981'
  WHERE survey_question_id = 112 AND
        display_index = 38;
UPDATE ag.survey_question_response 
  SET spanish = '1980'
  WHERE survey_question_id = 112 AND
        display_index = 39;
UPDATE ag.survey_question_response 
  SET spanish = '1979'
  WHERE survey_question_id = 112 AND
        display_index = 40;
UPDATE ag.survey_question_response 
  SET spanish = '1978'
  WHERE survey_question_id = 112 AND
        display_index = 41;
UPDATE ag.survey_question_response 
  SET spanish = '1977'
  WHERE survey_question_id = 112 AND
        display_index = 42;
UPDATE ag.survey_question_response 
  SET spanish = '1976'
  WHERE survey_question_id = 112 AND
        display_index = 43;
UPDATE ag.survey_question_response 
  SET spanish = '1975'
  WHERE survey_question_id = 112 AND
        display_index = 44;
UPDATE ag.survey_question_response 
  SET spanish = '1974'
  WHERE survey_question_id = 112 AND
        display_index = 45;
UPDATE ag.survey_question_response 
  SET spanish = '1973'
  WHERE survey_question_id = 112 AND
        display_index = 46;
UPDATE ag.survey_question_response 
  SET spanish = '1972'
  WHERE survey_question_id = 112 AND
        display_index = 47;
UPDATE ag.survey_question_response 
  SET spanish = '1971'
  WHERE survey_question_id = 112 AND
        display_index = 48;
UPDATE ag.survey_question_response 
  SET spanish = '1970'
  WHERE survey_question_id = 112 AND
        display_index = 49;
UPDATE ag.survey_question_response 
  SET spanish = '1969'
  WHERE survey_question_id = 112 AND
        display_index = 50;
UPDATE ag.survey_question_response 
  SET spanish = '1968'
  WHERE survey_question_id = 112 AND
        display_index = 51;
UPDATE ag.survey_question_response 
  SET spanish = '1967'
  WHERE survey_question_id = 112 AND
        display_index = 52;
UPDATE ag.survey_question_response 
  SET spanish = '1966'
  WHERE survey_question_id = 112 AND
        display_index = 53;
UPDATE ag.survey_question_response 
  SET spanish = '1965'
  WHERE survey_question_id = 112 AND
        display_index = 54;
UPDATE ag.survey_question_response 
  SET spanish = '1964'
  WHERE survey_question_id = 112 AND
        display_index = 55;
UPDATE ag.survey_question_response 
  SET spanish = '1963'
  WHERE survey_question_id = 112 AND
        display_index = 56;
UPDATE ag.survey_question_response 
  SET spanish = '1962'
  WHERE survey_question_id = 112 AND
        display_index = 57;
UPDATE ag.survey_question_response 
  SET spanish = '1961'
  WHERE survey_question_id = 112 AND
        display_index = 58;
UPDATE ag.survey_question_response 
  SET spanish = '1960'
  WHERE survey_question_id = 112 AND
        display_index = 59;
UPDATE ag.survey_question_response 
  SET spanish = '1959'
  WHERE survey_question_id = 112 AND
        display_index = 60;
UPDATE ag.survey_question_response 
  SET spanish = '1958'
  WHERE survey_question_id = 112 AND
        display_index = 61;
UPDATE ag.survey_question_response 
  SET spanish = '1957'
  WHERE survey_question_id = 112 AND
        display_index = 62;
UPDATE ag.survey_question_response 
  SET spanish = '1956'
  WHERE survey_question_id = 112 AND
        display_index = 63;
UPDATE ag.survey_question_response 
  SET spanish = '1955'
  WHERE survey_question_id = 112 AND
        display_index = 64;
UPDATE ag.survey_question_response 
  SET spanish = '1954'
  WHERE survey_question_id = 112 AND
        display_index = 65;
UPDATE ag.survey_question_response 
  SET spanish = '1953'
  WHERE survey_question_id = 112 AND
        display_index = 66;
UPDATE ag.survey_question_response 
  SET spanish = '1952'
  WHERE survey_question_id = 112 AND
        display_index = 67;
UPDATE ag.survey_question_response 
  SET spanish = '1951'
  WHERE survey_question_id = 112 AND
        display_index = 68;
UPDATE ag.survey_question_response 
  SET spanish = '1950'
  WHERE survey_question_id = 112 AND
        display_index = 69;
UPDATE ag.survey_question_response 
  SET spanish = '1949'
  WHERE survey_question_id = 112 AND
        display_index = 70;
UPDATE ag.survey_question_response 
  SET spanish = '1948'
  WHERE survey_question_id = 112 AND
        display_index = 71;
UPDATE ag.survey_question_response 
  SET spanish = '1947'
  WHERE survey_question_id = 112 AND
        display_index = 72;
UPDATE ag.survey_question_response 
  SET spanish = '1946'
  WHERE survey_question_id = 112 AND
        display_index = 73;
UPDATE ag.survey_question_response 
  SET spanish = '1945'
  WHERE survey_question_id = 112 AND
        display_index = 74;
UPDATE ag.survey_question_response 
  SET spanish = '1944'
  WHERE survey_question_id = 112 AND
        display_index = 75;
UPDATE ag.survey_question_response 
  SET spanish = '1943'
  WHERE survey_question_id = 112 AND
        display_index = 76;
UPDATE ag.survey_question_response 
  SET spanish = '1942'
  WHERE survey_question_id = 112 AND
        display_index = 77;
UPDATE ag.survey_question_response 
  SET spanish = '1941'
  WHERE survey_question_id = 112 AND
        display_index = 78;
UPDATE ag.survey_question_response 
  SET spanish = '1940'
  WHERE survey_question_id = 112 AND
        display_index = 79;
UPDATE ag.survey_question_response 
  SET spanish = '1939'
  WHERE survey_question_id = 112 AND
        display_index = 80;
UPDATE ag.survey_question_response 
  SET spanish = '1938'
  WHERE survey_question_id = 112 AND
        display_index = 81;
UPDATE ag.survey_question_response 
  SET spanish = '1937'
  WHERE survey_question_id = 112 AND
        display_index = 82;
UPDATE ag.survey_question_response 
  SET spanish = '1936'
  WHERE survey_question_id = 112 AND
        display_index = 83;
UPDATE ag.survey_question_response 
  SET spanish = '1935'
  WHERE survey_question_id = 112 AND
        display_index = 84;
UPDATE ag.survey_question_response 
  SET spanish = '1934'
  WHERE survey_question_id = 112 AND
        display_index = 85;
UPDATE ag.survey_question_response 
  SET spanish = '1933'
  WHERE survey_question_id = 112 AND
        display_index = 86;
UPDATE ag.survey_question_response 
  SET spanish = '1932'
  WHERE survey_question_id = 112 AND
        display_index = 87;
UPDATE ag.survey_question_response 
  SET spanish = '1931'
  WHERE survey_question_id = 112 AND
        display_index = 88;
UPDATE ag.survey_question_response 
  SET spanish = '1930'
  WHERE survey_question_id = 112 AND
        display_index = 89;
UPDATE ag.survey_question_response 
  SET spanish = '1929'
  WHERE survey_question_id = 112 AND
        display_index = 90;
UPDATE ag.survey_question_response 
  SET spanish = '1928'
  WHERE survey_question_id = 112 AND
        display_index = 91;
UPDATE ag.survey_question_response 
  SET spanish = '1927'
  WHERE survey_question_id = 112 AND
        display_index = 92;
UPDATE ag.survey_question_response 
  SET spanish = '1926'
  WHERE survey_question_id = 112 AND
        display_index = 93;
UPDATE ag.survey_question_response 
  SET spanish = '1925'
  WHERE survey_question_id = 112 AND
        display_index = 94;
UPDATE ag.survey_question_response 
  SET spanish = '1924'
  WHERE survey_question_id = 112 AND
        display_index = 95;
UPDATE ag.survey_question_response 
  SET spanish = '1923'
  WHERE survey_question_id = 112 AND
        display_index = 96;
UPDATE ag.survey_question_response 
  SET spanish = '1922'
  WHERE survey_question_id = 112 AND
        display_index = 97;
UPDATE ag.survey_question_response 
  SET spanish = '1921'
  WHERE survey_question_id = 112 AND
        display_index = 98;
UPDATE ag.survey_question_response 
  SET spanish = '1920'
  WHERE survey_question_id = 112 AND
        display_index = 99;
UPDATE ag.survey_question_response 
  SET spanish = '1919'
  WHERE survey_question_id = 112 AND
        display_index = 100;
UPDATE ag.survey_question_response 
  SET spanish = '1918'
  WHERE survey_question_id = 112 AND
        display_index = 101;
UPDATE ag.survey_question_response 
  SET spanish = '1917'
  WHERE survey_question_id = 112 AND
        display_index = 102;
UPDATE ag.survey_question_response 
  SET spanish = '1916'
  WHERE survey_question_id = 112 AND
        display_index = 103;
UPDATE ag.survey_question_response 
  SET spanish = '1915'
  WHERE survey_question_id = 112 AND
        display_index = 104;
UPDATE ag.survey_question_response 
  SET spanish = '1914'
  WHERE survey_question_id = 112 AND
        display_index = 105;
UPDATE ag.survey_question_response 
  SET spanish = '1913'
  WHERE survey_question_id = 112 AND
        display_index = 106;
UPDATE ag.survey_question_response 
  SET spanish = '1912'
  WHERE survey_question_id = 112 AND
        display_index = 107;
UPDATE ag.survey_question_response 
  SET spanish = '1911'
  WHERE survey_question_id = 112 AND
        display_index = 108;
UPDATE ag.survey_question_response 
  SET spanish = '1910'
  WHERE survey_question_id = 112 AND
        display_index = 109;
UPDATE ag.survey_question_response 
  SET spanish = '1909'
  WHERE survey_question_id = 112 AND
        display_index = 110;
UPDATE ag.survey_question_response 
  SET spanish = '1908'
  WHERE survey_question_id = 112 AND
        display_index = 111;
UPDATE ag.survey_question_response 
  SET spanish = '1907'
  WHERE survey_question_id = 112 AND
        display_index = 112;
UPDATE ag.survey_question_response 
  SET spanish = '1906'
  WHERE survey_question_id = 112 AND
        display_index = 113;
UPDATE ag.survey_question_response 
  SET spanish = '1905'
  WHERE survey_question_id = 112 AND
        display_index = 114;
UPDATE ag.survey_question_response 
  SET spanish = '1904'
  WHERE survey_question_id = 112 AND
        display_index = 115;
UPDATE ag.survey_question_response 
  SET spanish = '1903'
  WHERE survey_question_id = 112 AND
        display_index = 116;
UPDATE ag.survey_question_response 
  SET spanish = '1902'
  WHERE survey_question_id = 112 AND
        display_index = 117;
UPDATE ag.survey_question_response 
  SET spanish = '1901'
  WHERE survey_question_id = 112 AND
        display_index = 118;
UPDATE ag.survey_question_response 
  SET spanish = '1900'
  WHERE survey_question_id = 112 AND
        display_index = 119;
UPDATE ag.survey_question_response 
  SET spanish = '1899'
  WHERE survey_question_id = 112 AND
        display_index = 120;
UPDATE ag.survey_question_response 
  SET spanish = '1898'
  WHERE survey_question_id = 112 AND
        display_index = 121;
UPDATE ag.survey_question_response 
  SET spanish = '1897'
  WHERE survey_question_id = 112 AND
        display_index = 122;
UPDATE ag.survey_question_response 
  SET spanish = '1896'
  WHERE survey_question_id = 112 AND
        display_index = 123;
UPDATE ag.survey_question_response 
  SET spanish = '1895'
  WHERE survey_question_id = 112 AND
        display_index = 124;
UPDATE ag.survey_question_response 
  SET spanish = '1894'
  WHERE survey_question_id = 112 AND
        display_index = 125;
UPDATE ag.survey_question_response 
  SET spanish = '1893'
  WHERE survey_question_id = 112 AND
        display_index = 126;
UPDATE ag.survey_question_response 
  SET spanish = '1892'
  WHERE survey_question_id = 112 AND
        display_index = 127;
UPDATE ag.survey_question_response 
  SET spanish = '1891'
  WHERE survey_question_id = 112 AND
        display_index = 128;
UPDATE ag.survey_question_response 
  SET spanish = '1890'
  WHERE survey_question_id = 112 AND
        display_index = 129;

UPDATE ag.survey_question SET spanish = 'Peso:'
  WHERE survey_question_id = 113;

UPDATE ag.survey_question SET spanish = 'Unidades de medida de peso:'
  WHERE survey_question_id = 114;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 114 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'libras'
  WHERE survey_question_id = 114 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'kilogramos'
  WHERE survey_question_id = 114 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = 'Código postal actual:'
  WHERE survey_question_id = 115;

UPDATE ag.survey_question SET spanish = 'Indique cualquier otro dato sobre usted que cree que podría afectar a sus propios microorganismos.'
  WHERE survey_question_id = 116;

UPDATE ag.survey_question SET spanish = '¿Vive el gato dentro/fuera de la casa o está encerrado (en una jaula)?'
  WHERE survey_question_id = 117;

UPDATE ag.survey_question SET spanish = 'Restricciones alimentarias:'
  WHERE survey_question_id = 118;

UPDATE ag.survey_question SET spanish = 'Viajes:'
  WHERE survey_question_id = 119;

UPDATE ag.survey_question SET spanish = '¿Sigue alguna restricción especial en su dieta distinta de las mencionadas anteriormente?'
  WHERE survey_question_id = 12;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 12 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 12 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 12 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Tiene algún vínculo con otros participantes que le hayan contado de forma voluntaria que participan en el estudio (p. ej., pareja, hijos o compañeros de vivienda)? En el caso de los hijos, indique si se trata de vínculo de consanguinidad. Solo utilizaremos los datos que aporten ambas personas.'
  WHERE survey_question_id = 120;

UPDATE ag.survey_question SET spanish = 'Nivel de contacto con el gato:'
  WHERE survey_question_id = 122;

UPDATE ag.survey_question SET spanish = 'Antibiótico utilizado:'
  WHERE survey_question_id = 124;

UPDATE ag.survey_question SET spanish = 'Tratamiento para:'
  WHERE survey_question_id = 126;

UPDATE ag.survey_question SET spanish = '¿De dónde procede el agua que se bebe en su hogar?'
  WHERE survey_question_id = 13;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 13 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Agua del acueducto local'
  WHERE survey_question_id = 13 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Agua de pozo'
  WHERE survey_question_id = 13 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Agua embotellada'
  WHERE survey_question_id = 13 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Agua filtrada'
  WHERE survey_question_id = 13 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro'
  WHERE survey_question_id = 13 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Cuál es su raza/etnia?'
  WHERE survey_question_id = 14;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 14 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Blanco'
  WHERE survey_question_id = 14 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Asiático o isleño del Pacífico'
  WHERE survey_question_id = 14 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Afroamericano'
  WHERE survey_question_id = 14 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Hispano'
  WHERE survey_question_id = 14 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Otro'
  WHERE survey_question_id = 14 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas especies vegetales consume a la semana? Por ejemplo, si consume una lata de sopa que contiene zanahoria, papa y cebolla, puede indicar que son tres especies vegetales diferentes. Si consume pan multicereales, cada cereal cuenta como una especie vegetal.'
  WHERE survey_question_id = 146;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 146 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Menos de 5'
  WHERE survey_question_id = 146 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'De 6 a 10'
  WHERE survey_question_id = 146 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'De 11 a 20'
  WHERE survey_question_id = 146 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'De 21 a 30'
  WHERE survey_question_id = 146 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Más de 30'
  WHERE survey_question_id = 146 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'País de residencia:'
  WHERE survey_question_id = 148;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 148 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Afganistán'
  WHERE survey_question_id = 148 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Aland'
  WHERE survey_question_id = 148 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Albania'
  WHERE survey_question_id = 148 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Argelia'
  WHERE survey_question_id = 148 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Samoa Americana'
  WHERE survey_question_id = 148 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Andorra'
  WHERE survey_question_id = 148 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Angola'
  WHERE survey_question_id = 148 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = 'Anguila'
  WHERE survey_question_id = 148 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = 'Antártida'
  WHERE survey_question_id = 148 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET spanish = 'Antigua y Barbuda'
  WHERE survey_question_id = 148 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET spanish = 'Argentina'
  WHERE survey_question_id = 148 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET spanish = 'Armenia'
  WHERE survey_question_id = 148 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET spanish = 'Aruba'
  WHERE survey_question_id = 148 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET spanish = 'Australia'
  WHERE survey_question_id = 148 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET spanish = 'Austria'
  WHERE survey_question_id = 148 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET spanish = 'Azerbaiyán'
  WHERE survey_question_id = 148 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET spanish = 'Bahamas'
  WHERE survey_question_id = 148 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET spanish = 'Bahrein'
  WHERE survey_question_id = 148 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET spanish = 'Bangladesh'
  WHERE survey_question_id = 148 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET spanish = 'Barbados'
  WHERE survey_question_id = 148 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET spanish = 'Bielorrusia'
  WHERE survey_question_id = 148 AND
        display_index = 21;
UPDATE ag.survey_question_response 
  SET spanish = 'Bélgica'
  WHERE survey_question_id = 148 AND
        display_index = 22;
UPDATE ag.survey_question_response 
  SET spanish = 'Belice'
  WHERE survey_question_id = 148 AND
        display_index = 23;
UPDATE ag.survey_question_response 
  SET spanish = 'Benin'
  WHERE survey_question_id = 148 AND
        display_index = 24;
UPDATE ag.survey_question_response 
  SET spanish = 'islas Bermudas'
  WHERE survey_question_id = 148 AND
        display_index = 25;
UPDATE ag.survey_question_response 
  SET spanish = 'Bután'
  WHERE survey_question_id = 148 AND
        display_index = 26;
UPDATE ag.survey_question_response 
  SET spanish = 'Bolivia'
  WHERE survey_question_id = 148 AND
        display_index = 27;
UPDATE ag.survey_question_response 
  SET spanish = 'Bosnia y Herzegovina'
  WHERE survey_question_id = 148 AND
        display_index = 28;
UPDATE ag.survey_question_response 
  SET spanish = 'Botsuana'
  WHERE survey_question_id = 148 AND
        display_index = 29;
UPDATE ag.survey_question_response 
  SET spanish = 'Isla Bouvet'
  WHERE survey_question_id = 148 AND
        display_index = 30;
UPDATE ag.survey_question_response 
  SET spanish = 'Brasil'
  WHERE survey_question_id = 148 AND
        display_index = 31;
UPDATE ag.survey_question_response 
  SET spanish = 'Territorio Británico del Océano Índico'
  WHERE survey_question_id = 148 AND
        display_index = 32;
UPDATE ag.survey_question_response 
  SET spanish = 'Brunei Darussalam'
  WHERE survey_question_id = 148 AND
        display_index = 33;
UPDATE ag.survey_question_response 
  SET spanish = 'Bulgaria'
  WHERE survey_question_id = 148 AND
        display_index = 34;
UPDATE ag.survey_question_response 
  SET spanish = 'Burkina Faso'
  WHERE survey_question_id = 148 AND
        display_index = 35;
UPDATE ag.survey_question_response 
  SET spanish = 'Burundi'
  WHERE survey_question_id = 148 AND
        display_index = 36;
UPDATE ag.survey_question_response 
  SET spanish = 'Camboya'
  WHERE survey_question_id = 148 AND
        display_index = 37;
UPDATE ag.survey_question_response 
  SET spanish = 'Camerún'
  WHERE survey_question_id = 148 AND
        display_index = 38;
UPDATE ag.survey_question_response 
  SET spanish = 'Canadá'
  WHERE survey_question_id = 148 AND
        display_index = 39;
UPDATE ag.survey_question_response 
  SET spanish = 'Cabo Verde'
  WHERE survey_question_id = 148 AND
        display_index = 40;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Caimán'
  WHERE survey_question_id = 148 AND
        display_index = 41;
UPDATE ag.survey_question_response 
  SET spanish = 'República Centroafricana'
  WHERE survey_question_id = 148 AND
        display_index = 42;
UPDATE ag.survey_question_response 
  SET spanish = 'Chad'
  WHERE survey_question_id = 148 AND
        display_index = 43;
UPDATE ag.survey_question_response 
  SET spanish = 'Chile'
  WHERE survey_question_id = 148 AND
        display_index = 44;
UPDATE ag.survey_question_response 
  SET spanish = 'China'
  WHERE survey_question_id = 148 AND
        display_index = 45;
UPDATE ag.survey_question_response 
  SET spanish = 'Isla de Navidad'
  WHERE survey_question_id = 148 AND
        display_index = 46;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Cocos (Keeling)'
  WHERE survey_question_id = 148 AND
        display_index = 47;
UPDATE ag.survey_question_response 
  SET spanish = 'Colombia'
  WHERE survey_question_id = 148 AND
        display_index = 48;
UPDATE ag.survey_question_response 
  SET spanish = 'Comoras'
  WHERE survey_question_id = 148 AND
        display_index = 49;
UPDATE ag.survey_question_response 
  SET spanish = 'Congo'
  WHERE survey_question_id = 148 AND
        display_index = 50;
UPDATE ag.survey_question_response 
  SET spanish = 'Congo, República Democrática del'
  WHERE survey_question_id = 148 AND
        display_index = 51;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Cook'
  WHERE survey_question_id = 148 AND
        display_index = 52;
UPDATE ag.survey_question_response 
  SET spanish = 'Costa Rica'
  WHERE survey_question_id = 148 AND
        display_index = 53;
UPDATE ag.survey_question_response 
  SET spanish = 'Costa de Marfil'
  WHERE survey_question_id = 148 AND
        display_index = 54;
UPDATE ag.survey_question_response 
  SET spanish = 'Croacia'
  WHERE survey_question_id = 148 AND
        display_index = 55;
UPDATE ag.survey_question_response 
  SET spanish = 'Cuba'
  WHERE survey_question_id = 148 AND
        display_index = 56;
UPDATE ag.survey_question_response 
  SET spanish = 'Chipre'
  WHERE survey_question_id = 148 AND
        display_index = 57;
UPDATE ag.survey_question_response 
  SET spanish = 'Republica checa'
  WHERE survey_question_id = 148 AND
        display_index = 58;
UPDATE ag.survey_question_response 
  SET spanish = 'Dinamarca'
  WHERE survey_question_id = 148 AND
        display_index = 59;
UPDATE ag.survey_question_response 
  SET spanish = 'Djibouti'
  WHERE survey_question_id = 148 AND
        display_index = 60;
UPDATE ag.survey_question_response 
  SET spanish = 'Dominica'
  WHERE survey_question_id = 148 AND
        display_index = 61;
UPDATE ag.survey_question_response 
  SET spanish = 'República Dominicana'
  WHERE survey_question_id = 148 AND
        display_index = 62;
UPDATE ag.survey_question_response 
  SET spanish = 'Ecuador'
  WHERE survey_question_id = 148 AND
        display_index = 63;
UPDATE ag.survey_question_response 
  SET spanish = 'Egipto'
  WHERE survey_question_id = 148 AND
        display_index = 64;
UPDATE ag.survey_question_response 
  SET spanish = 'El Salvador'
  WHERE survey_question_id = 148 AND
        display_index = 65;
UPDATE ag.survey_question_response 
  SET spanish = 'Guinea Ecuatorial'
  WHERE survey_question_id = 148 AND
        display_index = 66;
UPDATE ag.survey_question_response 
  SET spanish = 'Eritrea'
  WHERE survey_question_id = 148 AND
        display_index = 67;
UPDATE ag.survey_question_response 
  SET spanish = 'Estonia'
  WHERE survey_question_id = 148 AND
        display_index = 68;
UPDATE ag.survey_question_response 
  SET spanish = 'Etiopía'
  WHERE survey_question_id = 148 AND
        display_index = 69;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Malvinas (Falkland Islands)'
  WHERE survey_question_id = 148 AND
        display_index = 70;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Faroe'
  WHERE survey_question_id = 148 AND
        display_index = 71;
UPDATE ag.survey_question_response 
  SET spanish = 'Fiyi'
  WHERE survey_question_id = 148 AND
        display_index = 72;
UPDATE ag.survey_question_response 
  SET spanish = 'Finlandia'
  WHERE survey_question_id = 148 AND
        display_index = 73;
UPDATE ag.survey_question_response 
  SET spanish = 'Francia'
  WHERE survey_question_id = 148 AND
        display_index = 74;
UPDATE ag.survey_question_response 
  SET spanish = 'Guayana Francesa'
  WHERE survey_question_id = 148 AND
        display_index = 75;
UPDATE ag.survey_question_response 
  SET spanish = 'Polinesia francés'
  WHERE survey_question_id = 148 AND
        display_index = 76;
UPDATE ag.survey_question_response 
  SET spanish = 'Territorios Franceses del Sur'
  WHERE survey_question_id = 148 AND
        display_index = 77;
UPDATE ag.survey_question_response 
  SET spanish = 'Gabón'
  WHERE survey_question_id = 148 AND
        display_index = 78;
UPDATE ag.survey_question_response 
  SET spanish = 'Gambia'
  WHERE survey_question_id = 148 AND
        display_index = 79;
UPDATE ag.survey_question_response 
  SET spanish = 'Georgia'
  WHERE survey_question_id = 148 AND
        display_index = 80;
UPDATE ag.survey_question_response 
  SET spanish = 'Alemania'
  WHERE survey_question_id = 148 AND
        display_index = 81;
UPDATE ag.survey_question_response 
  SET spanish = 'Ghana'
  WHERE survey_question_id = 148 AND
        display_index = 82;
UPDATE ag.survey_question_response 
  SET spanish = 'Gibraltar'
  WHERE survey_question_id = 148 AND
        display_index = 83;
UPDATE ag.survey_question_response 
  SET spanish = 'Grecia'
  WHERE survey_question_id = 148 AND
        display_index = 84;
UPDATE ag.survey_question_response 
  SET spanish = 'Groenlandia'
  WHERE survey_question_id = 148 AND
        display_index = 85;
UPDATE ag.survey_question_response 
  SET spanish = 'Granada'
  WHERE survey_question_id = 148 AND
        display_index = 86;
UPDATE ag.survey_question_response 
  SET spanish = 'Guadalupe'
  WHERE survey_question_id = 148 AND
        display_index = 87;
UPDATE ag.survey_question_response 
  SET spanish = 'Guam'
  WHERE survey_question_id = 148 AND
        display_index = 88;
UPDATE ag.survey_question_response 
  SET spanish = 'Guatemala'
  WHERE survey_question_id = 148 AND
        display_index = 89;
UPDATE ag.survey_question_response 
  SET spanish = 'Guernsey'
  WHERE survey_question_id = 148 AND
        display_index = 90;
UPDATE ag.survey_question_response 
  SET spanish = 'Guinea'
  WHERE survey_question_id = 148 AND
        display_index = 91;
UPDATE ag.survey_question_response 
  SET spanish = 'Guinea-Bissau'
  WHERE survey_question_id = 148 AND
        display_index = 92;
UPDATE ag.survey_question_response 
  SET spanish = 'Guayana'
  WHERE survey_question_id = 148 AND
        display_index = 93;
UPDATE ag.survey_question_response 
  SET spanish = 'Haití'
  WHERE survey_question_id = 148 AND
        display_index = 94;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Heard y Mcdonald'
  WHERE survey_question_id = 148 AND
        display_index = 95;
UPDATE ag.survey_question_response 
  SET spanish = 'Santa Sede (Estado de la Ciudad del Vaticano)'
  WHERE survey_question_id = 148 AND
        display_index = 96;
UPDATE ag.survey_question_response 
  SET spanish = 'Honduras'
  WHERE survey_question_id = 148 AND
        display_index = 97;
UPDATE ag.survey_question_response 
  SET spanish = 'Hong Kong'
  WHERE survey_question_id = 148 AND
        display_index = 98;
UPDATE ag.survey_question_response 
  SET spanish = 'Hungría'
  WHERE survey_question_id = 148 AND
        display_index = 99;
UPDATE ag.survey_question_response 
  SET spanish = 'Islandia'
  WHERE survey_question_id = 148 AND
        display_index = 100;
UPDATE ag.survey_question_response 
  SET spanish = 'India'
  WHERE survey_question_id = 148 AND
        display_index = 101;
UPDATE ag.survey_question_response 
  SET spanish = 'Indonesia'
  WHERE survey_question_id = 148 AND
        display_index = 102;
UPDATE ag.survey_question_response 
  SET spanish = 'Irán (República Islámica de'
  WHERE survey_question_id = 148 AND
        display_index = 103;
UPDATE ag.survey_question_response 
  SET spanish = 'Irak'
  WHERE survey_question_id = 148 AND
        display_index = 104;
UPDATE ag.survey_question_response 
  SET spanish = 'Irlanda'
  WHERE survey_question_id = 148 AND
        display_index = 105;
UPDATE ag.survey_question_response 
  SET spanish = 'Isla del hombre'
  WHERE survey_question_id = 148 AND
        display_index = 106;
UPDATE ag.survey_question_response 
  SET spanish = 'Israel'
  WHERE survey_question_id = 148 AND
        display_index = 107;
UPDATE ag.survey_question_response 
  SET spanish = 'Italia'
  WHERE survey_question_id = 148 AND
        display_index = 108;
UPDATE ag.survey_question_response 
  SET spanish = 'Jamaica'
  WHERE survey_question_id = 148 AND
        display_index = 109;
UPDATE ag.survey_question_response 
  SET spanish = 'Japón'
  WHERE survey_question_id = 148 AND
        display_index = 110;
UPDATE ag.survey_question_response 
  SET spanish = 'Jersey'
  WHERE survey_question_id = 148 AND
        display_index = 111;
UPDATE ag.survey_question_response 
  SET spanish = 'Jordán'
  WHERE survey_question_id = 148 AND
        display_index = 112;
UPDATE ag.survey_question_response 
  SET spanish = 'Kazajstán'
  WHERE survey_question_id = 148 AND
        display_index = 113;
UPDATE ag.survey_question_response 
  SET spanish = 'Kenia'
  WHERE survey_question_id = 148 AND
        display_index = 114;
UPDATE ag.survey_question_response 
  SET spanish = 'Kiribati'
  WHERE survey_question_id = 148 AND
        display_index = 115;
UPDATE ag.survey_question_response 
  SET spanish = 'República de Corea, Popular Democrática de'
  WHERE survey_question_id = 148 AND
        display_index = 116;
UPDATE ag.survey_question_response 
  SET spanish = 'Corea, república de'
  WHERE survey_question_id = 148 AND
        display_index = 117;
UPDATE ag.survey_question_response 
  SET spanish = 'Kuwait'
  WHERE survey_question_id = 148 AND
        display_index = 118;
UPDATE ag.survey_question_response 
  SET spanish = 'Kirguistán'
  WHERE survey_question_id = 148 AND
        display_index = 119;
UPDATE ag.survey_question_response 
  SET spanish = 'República Democrática Popular Lao'
  WHERE survey_question_id = 148 AND
        display_index = 120;
UPDATE ag.survey_question_response 
  SET spanish = 'Letonia'
  WHERE survey_question_id = 148 AND
        display_index = 121;
UPDATE ag.survey_question_response 
  SET spanish = 'Líbano'
  WHERE survey_question_id = 148 AND
        display_index = 122;
UPDATE ag.survey_question_response 
  SET spanish = 'Lesoto'
  WHERE survey_question_id = 148 AND
        display_index = 123;
UPDATE ag.survey_question_response 
  SET spanish = 'Liberia'
  WHERE survey_question_id = 148 AND
        display_index = 124;
UPDATE ag.survey_question_response 
  SET spanish = 'Jamahiriya Árabe Libia'
  WHERE survey_question_id = 148 AND
        display_index = 125;
UPDATE ag.survey_question_response 
  SET spanish = 'Liechtenstein'
  WHERE survey_question_id = 148 AND
        display_index = 126;
UPDATE ag.survey_question_response 
  SET spanish = 'Lituania'
  WHERE survey_question_id = 148 AND
        display_index = 127;
UPDATE ag.survey_question_response 
  SET spanish = 'Luxemburgo'
  WHERE survey_question_id = 148 AND
        display_index = 128;
UPDATE ag.survey_question_response 
  SET spanish = 'Macao'
  WHERE survey_question_id = 148 AND
        display_index = 129;
UPDATE ag.survey_question_response 
  SET spanish = 'Macedonia, la ex República Yugoslava de'
  WHERE survey_question_id = 148 AND
        display_index = 130;
UPDATE ag.survey_question_response 
  SET spanish = 'Madagascar'
  WHERE survey_question_id = 148 AND
        display_index = 131;
UPDATE ag.survey_question_response 
  SET spanish = 'Malawi'
  WHERE survey_question_id = 148 AND
        display_index = 132;
UPDATE ag.survey_question_response 
  SET spanish = 'Malasia'
  WHERE survey_question_id = 148 AND
        display_index = 133;
UPDATE ag.survey_question_response 
  SET spanish = 'Maldivas'
  WHERE survey_question_id = 148 AND
        display_index = 134;
UPDATE ag.survey_question_response 
  SET spanish = 'Mali'
  WHERE survey_question_id = 148 AND
        display_index = 135;
UPDATE ag.survey_question_response 
  SET spanish = 'Malta'
  WHERE survey_question_id = 148 AND
        display_index = 136;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Marshall'
  WHERE survey_question_id = 148 AND
        display_index = 137;
UPDATE ag.survey_question_response 
  SET spanish = 'Martinica'
  WHERE survey_question_id = 148 AND
        display_index = 138;
UPDATE ag.survey_question_response 
  SET spanish = 'Mauritania'
  WHERE survey_question_id = 148 AND
        display_index = 139;
UPDATE ag.survey_question_response 
  SET spanish = 'Mauricio'
  WHERE survey_question_id = 148 AND
        display_index = 140;
UPDATE ag.survey_question_response 
  SET spanish = 'Mayotte'
  WHERE survey_question_id = 148 AND
        display_index = 141;
UPDATE ag.survey_question_response 
  SET spanish = 'Mexico'
  WHERE survey_question_id = 148 AND
        display_index = 142;
UPDATE ag.survey_question_response 
  SET spanish = 'Micronesia, Estados Federados de'
  WHERE survey_question_id = 148 AND
        display_index = 143;
UPDATE ag.survey_question_response 
  SET spanish = 'Moldavia, República de'
  WHERE survey_question_id = 148 AND
        display_index = 144;
UPDATE ag.survey_question_response 
  SET spanish = 'Mónaco'
  WHERE survey_question_id = 148 AND
        display_index = 145;
UPDATE ag.survey_question_response 
  SET spanish = 'Mongolia'
  WHERE survey_question_id = 148 AND
        display_index = 146;
UPDATE ag.survey_question_response 
  SET spanish = 'Montenegro'
  WHERE survey_question_id = 148 AND
        display_index = 147;
UPDATE ag.survey_question_response 
  SET spanish = 'Montserrat'
  WHERE survey_question_id = 148 AND
        display_index = 148;
UPDATE ag.survey_question_response 
  SET spanish = 'Marruecos'
  WHERE survey_question_id = 148 AND
        display_index = 149;
UPDATE ag.survey_question_response 
  SET spanish = 'Mozambique'
  WHERE survey_question_id = 148 AND
        display_index = 150;
UPDATE ag.survey_question_response 
  SET spanish = 'Myanmar'
  WHERE survey_question_id = 148 AND
        display_index = 151;
UPDATE ag.survey_question_response 
  SET spanish = 'Namibia'
  WHERE survey_question_id = 148 AND
        display_index = 152;
UPDATE ag.survey_question_response 
  SET spanish = 'Nauru'
  WHERE survey_question_id = 148 AND
        display_index = 153;
UPDATE ag.survey_question_response 
  SET spanish = 'Nepal'
  WHERE survey_question_id = 148 AND
        display_index = 154;
UPDATE ag.survey_question_response 
  SET spanish = 'Países Bajos'
  WHERE survey_question_id = 148 AND
        display_index = 155;
UPDATE ag.survey_question_response 
  SET spanish = 'Antillas Holandesas'
  WHERE survey_question_id = 148 AND
        display_index = 156;
UPDATE ag.survey_question_response 
  SET spanish = 'Nueva Caledonia'
  WHERE survey_question_id = 148 AND
        display_index = 157;
UPDATE ag.survey_question_response 
  SET spanish = 'Nueva Zelanda'
  WHERE survey_question_id = 148 AND
        display_index = 158;
UPDATE ag.survey_question_response 
  SET spanish = 'Nicaragua'
  WHERE survey_question_id = 148 AND
        display_index = 159;
UPDATE ag.survey_question_response 
  SET spanish = 'Níger'
  WHERE survey_question_id = 148 AND
        display_index = 160;
UPDATE ag.survey_question_response 
  SET spanish = 'Nigeria'
  WHERE survey_question_id = 148 AND
        display_index = 161;
UPDATE ag.survey_question_response 
  SET spanish = 'Niue'
  WHERE survey_question_id = 148 AND
        display_index = 162;
UPDATE ag.survey_question_response 
  SET spanish = 'Isla Norfolk'
  WHERE survey_question_id = 148 AND
        display_index = 163;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Marianas del Norte'
  WHERE survey_question_id = 148 AND
        display_index = 164;
UPDATE ag.survey_question_response 
  SET spanish = 'Noruega'
  WHERE survey_question_id = 148 AND
        display_index = 165;
UPDATE ag.survey_question_response 
  SET spanish = 'Omán'
  WHERE survey_question_id = 148 AND
        display_index = 166;
UPDATE ag.survey_question_response 
  SET spanish = 'Pakistán'
  WHERE survey_question_id = 148 AND
        display_index = 167;
UPDATE ag.survey_question_response 
  SET spanish = 'Palau'
  WHERE survey_question_id = 148 AND
        display_index = 168;
UPDATE ag.survey_question_response 
  SET spanish = 'Territorio Palestino, Ocupado'
  WHERE survey_question_id = 148 AND
        display_index = 169;
UPDATE ag.survey_question_response 
  SET spanish = 'Panamá'
  WHERE survey_question_id = 148 AND
        display_index = 170;
UPDATE ag.survey_question_response 
  SET spanish = 'Papúa Nueva Guinea'
  WHERE survey_question_id = 148 AND
        display_index = 171;
UPDATE ag.survey_question_response 
  SET spanish = 'Paraguay'
  WHERE survey_question_id = 148 AND
        display_index = 172;
UPDATE ag.survey_question_response 
  SET spanish = 'Perú'
  WHERE survey_question_id = 148 AND
        display_index = 173;
UPDATE ag.survey_question_response 
  SET spanish = 'Filipinas'
  WHERE survey_question_id = 148 AND
        display_index = 174;
UPDATE ag.survey_question_response 
  SET spanish = 'Pitcairn'
  WHERE survey_question_id = 148 AND
        display_index = 175;
UPDATE ag.survey_question_response 
  SET spanish = 'Polonia'
  WHERE survey_question_id = 148 AND
        display_index = 176;
UPDATE ag.survey_question_response 
  SET spanish = 'Portugal'
  WHERE survey_question_id = 148 AND
        display_index = 177;
UPDATE ag.survey_question_response 
  SET spanish = 'Puerto Rico'
  WHERE survey_question_id = 148 AND
        display_index = 178;
UPDATE ag.survey_question_response 
  SET spanish = 'Katar'
  WHERE survey_question_id = 148 AND
        display_index = 179;
UPDATE ag.survey_question_response 
  SET spanish = 'Reunión'
  WHERE survey_question_id = 148 AND
        display_index = 180;
UPDATE ag.survey_question_response 
  SET spanish = 'Rumania'
  WHERE survey_question_id = 148 AND
        display_index = 181;
UPDATE ag.survey_question_response 
  SET spanish = 'Federación Rusa'
  WHERE survey_question_id = 148 AND
        display_index = 182;
UPDATE ag.survey_question_response 
  SET spanish = 'Ruanda'
  WHERE survey_question_id = 148 AND
        display_index = 183;
UPDATE ag.survey_question_response 
  SET spanish = 'Santa helena'
  WHERE survey_question_id = 148 AND
        display_index = 184;
UPDATE ag.survey_question_response 
  SET spanish = 'San Cristóbal y Nieves'
  WHERE survey_question_id = 148 AND
        display_index = 185;
UPDATE ag.survey_question_response 
  SET spanish = 'Santa Lucía'
  WHERE survey_question_id = 148 AND
        display_index = 186;
UPDATE ag.survey_question_response 
  SET spanish = 'San Pedro y Miquelón'
  WHERE survey_question_id = 148 AND
        display_index = 187;
UPDATE ag.survey_question_response 
  SET spanish = 'San Vicente y las Granadinas'
  WHERE survey_question_id = 148 AND
        display_index = 188;
UPDATE ag.survey_question_response 
  SET spanish = 'Samoa'
  WHERE survey_question_id = 148 AND
        display_index = 189;
UPDATE ag.survey_question_response 
  SET spanish = 'San Marino'
  WHERE survey_question_id = 148 AND
        display_index = 190;
UPDATE ag.survey_question_response 
  SET spanish = 'Santo Tomé y Príncipe'
  WHERE survey_question_id = 148 AND
        display_index = 191;
UPDATE ag.survey_question_response 
  SET spanish = 'Arabia Saudita'
  WHERE survey_question_id = 148 AND
        display_index = 192;
UPDATE ag.survey_question_response 
  SET spanish = 'Senegal'
  WHERE survey_question_id = 148 AND
        display_index = 193;
UPDATE ag.survey_question_response 
  SET spanish = 'Serbia'
  WHERE survey_question_id = 148 AND
        display_index = 194;
UPDATE ag.survey_question_response 
  SET spanish = 'Seychelles'
  WHERE survey_question_id = 148 AND
        display_index = 195;
UPDATE ag.survey_question_response 
  SET spanish = 'Sierra Leona'
  WHERE survey_question_id = 148 AND
        display_index = 196;
UPDATE ag.survey_question_response 
  SET spanish = 'Singapur'
  WHERE survey_question_id = 148 AND
        display_index = 197;
UPDATE ag.survey_question_response 
  SET spanish = 'Eslovaquia'
  WHERE survey_question_id = 148 AND
        display_index = 198;
UPDATE ag.survey_question_response 
  SET spanish = 'Eslovenia'
  WHERE survey_question_id = 148 AND
        display_index = 199;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Salomón'
  WHERE survey_question_id = 148 AND
        display_index = 200;
UPDATE ag.survey_question_response 
  SET spanish = 'Somalia'
  WHERE survey_question_id = 148 AND
        display_index = 201;
UPDATE ag.survey_question_response 
  SET spanish = 'Sudáfrica'
  WHERE survey_question_id = 148 AND
        display_index = 202;
UPDATE ag.survey_question_response 
  SET spanish = 'Georgia del sur y las islas Sandwich del sur'
  WHERE survey_question_id = 148 AND
        display_index = 203;
UPDATE ag.survey_question_response 
  SET spanish = 'España'
  WHERE survey_question_id = 148 AND
        display_index = 204;
UPDATE ag.survey_question_response 
  SET spanish = 'Sri Lanka'
  WHERE survey_question_id = 148 AND
        display_index = 205;
UPDATE ag.survey_question_response 
  SET spanish = 'Sudán'
  WHERE survey_question_id = 148 AND
        display_index = 206;
UPDATE ag.survey_question_response 
  SET spanish = 'Surinam'
  WHERE survey_question_id = 148 AND
        display_index = 207;
UPDATE ag.survey_question_response 
  SET spanish = 'Svalbard y Jan Mayen'
  WHERE survey_question_id = 148 AND
        display_index = 208;
UPDATE ag.survey_question_response 
  SET spanish = 'Swazilandia'
  WHERE survey_question_id = 148 AND
        display_index = 209;
UPDATE ag.survey_question_response 
  SET spanish = 'Suecia'
  WHERE survey_question_id = 148 AND
        display_index = 210;
UPDATE ag.survey_question_response 
  SET spanish = 'Suiza'
  WHERE survey_question_id = 148 AND
        display_index = 211;
UPDATE ag.survey_question_response 
  SET spanish = 'República Árabe Siria'
  WHERE survey_question_id = 148 AND
        display_index = 212;
UPDATE ag.survey_question_response 
  SET spanish = 'Taiwan, provincia de China'
  WHERE survey_question_id = 148 AND
        display_index = 213;
UPDATE ag.survey_question_response 
  SET spanish = 'Tayikistán'
  WHERE survey_question_id = 148 AND
        display_index = 214;
UPDATE ag.survey_question_response 
  SET spanish = 'Tanzania, República Unida de'
  WHERE survey_question_id = 148 AND
        display_index = 215;
UPDATE ag.survey_question_response 
  SET spanish = 'Tailandia'
  WHERE survey_question_id = 148 AND
        display_index = 216;
UPDATE ag.survey_question_response 
  SET spanish = 'Timor-leste'
  WHERE survey_question_id = 148 AND
        display_index = 217;
UPDATE ag.survey_question_response 
  SET spanish = 'Ir'
  WHERE survey_question_id = 148 AND
        display_index = 218;
UPDATE ag.survey_question_response 
  SET spanish = 'Tokelau'
  WHERE survey_question_id = 148 AND
        display_index = 219;
UPDATE ag.survey_question_response 
  SET spanish = 'Tonga'
  WHERE survey_question_id = 148 AND
        display_index = 220;
UPDATE ag.survey_question_response 
  SET spanish = 'Trinidad y Tobago'
  WHERE survey_question_id = 148 AND
        display_index = 221;
UPDATE ag.survey_question_response 
  SET spanish = 'Túnez'
  WHERE survey_question_id = 148 AND
        display_index = 222;
UPDATE ag.survey_question_response 
  SET spanish = 'pavo'
  WHERE survey_question_id = 148 AND
        display_index = 223;
UPDATE ag.survey_question_response 
  SET spanish = 'Turkmenistán'
  WHERE survey_question_id = 148 AND
        display_index = 224;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Turcas y Caicos'
  WHERE survey_question_id = 148 AND
        display_index = 225;
UPDATE ag.survey_question_response 
  SET spanish = 'Tuvalu'
  WHERE survey_question_id = 148 AND
        display_index = 226;
UPDATE ag.survey_question_response 
  SET spanish = 'Uganda'
  WHERE survey_question_id = 148 AND
        display_index = 227;
UPDATE ag.survey_question_response 
  SET spanish = 'Ucrania'
  WHERE survey_question_id = 148 AND
        display_index = 228;
UPDATE ag.survey_question_response 
  SET spanish = 'Emiratos Árabes Unidos'
  WHERE survey_question_id = 148 AND
        display_index = 229;
UPDATE ag.survey_question_response 
  SET spanish = 'Reino Unido'
  WHERE survey_question_id = 148 AND
        display_index = 230;
UPDATE ag.survey_question_response 
  SET spanish = 'Estados Unidos'
  WHERE survey_question_id = 148 AND
        display_index = 231;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas ultramarinas menores de Estados Unidos'
  WHERE survey_question_id = 148 AND
        display_index = 232;
UPDATE ag.survey_question_response 
  SET spanish = 'Uruguay'
  WHERE survey_question_id = 148 AND
        display_index = 233;
UPDATE ag.survey_question_response 
  SET spanish = 'Uzbekistán'
  WHERE survey_question_id = 148 AND
        display_index = 234;
UPDATE ag.survey_question_response 
  SET spanish = 'Vanuatu'
  WHERE survey_question_id = 148 AND
        display_index = 235;
UPDATE ag.survey_question_response 
  SET spanish = 'Venezuela'
  WHERE survey_question_id = 148 AND
        display_index = 236;
UPDATE ag.survey_question_response 
  SET spanish = 'Vietnam'
  WHERE survey_question_id = 148 AND
        display_index = 237;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Vírgenes Británicas'
  WHERE survey_question_id = 148 AND
        display_index = 238;
UPDATE ag.survey_question_response 
  SET spanish = 'Islas Vírgenes, EE. UU.'
  WHERE survey_question_id = 148 AND
        display_index = 239;
UPDATE ag.survey_question_response 
  SET spanish = 'Wallis y Futuna'
  WHERE survey_question_id = 148 AND
        display_index = 240;
UPDATE ag.survey_question_response 
  SET spanish = 'Sahara Occidental'
  WHERE survey_question_id = 148 AND
        display_index = 241;
UPDATE ag.survey_question_response 
  SET spanish = 'Yemen'
  WHERE survey_question_id = 148 AND
        display_index = 242;
UPDATE ag.survey_question_response 
  SET spanish = 'Zambia'
  WHERE survey_question_id = 148 AND
        display_index = 243;
UPDATE ag.survey_question_response 
  SET spanish = 'Zimbabue'
  WHERE survey_question_id = 148 AND
        display_index = 244;

UPDATE ag.survey_question SET spanish = '¿Tiene alguna otra mascota?'
  WHERE survey_question_id = 149;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 149 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 149 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 149 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Cuándo se mudó al estado en el que reside actualmente?'
  WHERE survey_question_id = 15;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 15 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'En el último mes'
  WHERE survey_question_id = 15 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'En los últimos 3 meses'
  WHERE survey_question_id = 15 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'En los últimos 6 meses'
  WHERE survey_question_id = 15 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'En el último año'
  WHERE survey_question_id = 15 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Llevo más de un año viviendo en el estado en el que resido actualmente.'
  WHERE survey_question_id = 15 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Enumere sus mascotas'
  WHERE survey_question_id = 150;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado una enfermedad mental?'
  WHERE survey_question_id = 153;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 153 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 153 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 153 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = 'Seleccione los trastornos de la siguiente lista:'
  WHERE survey_question_id = 154;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 154 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Depresión'
  WHERE survey_question_id = 154 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Trastorno bipolar'
  WHERE survey_question_id = 154 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Trastorno por estrés postraumático'
  WHERE survey_question_id = 154 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Esquizofrenia'
  WHERE survey_question_id = 154 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Anorexia nerviosa'
  WHERE survey_question_id = 154 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Bulimia nerviosa'
  WHERE survey_question_id = 154 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Drogadicción'
  WHERE survey_question_id = 154 AND
        display_index = 7;

UPDATE ag.survey_question SET spanish = '¿Qué tipo de diabetes?'
  WHERE survey_question_id = 155;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 155 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Diabetes de tipo 1'
  WHERE survey_question_id = 155 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Diabetes de tipo 2'
  WHERE survey_question_id = 155 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Diabetes gestacional'
  WHERE survey_question_id = 155 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Tiene sueños intensos o aterradores?'
  WHERE survey_question_id = 156;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 156 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 156 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (unas cuantas veces al mes)'
  WHERE survey_question_id = 156 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 156 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 156 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 156 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Consume bebidas dietéticas con endulzantes artificiales?'
  WHERE survey_question_id = 157;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 157 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 157 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (alguna vez al mes)'
  WHERE survey_question_id = 157 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 157 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 157 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 157 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado cáncer?'
  WHERE survey_question_id = 158;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 158 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 158 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 158 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 158 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 158 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'Si le han diagnosticado cáncer, ¿cómo se trató?'
  WHERE survey_question_id = 159;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 159 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sin tratamiento'
  WHERE survey_question_id = 159 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Solo cirugía'
  WHERE survey_question_id = 159 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Quimioterapia'
  WHERE survey_question_id = 159 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Radioterapia'
  WHERE survey_question_id = 159 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'He salido del país en el que resido en el último/los últimos _________.'
  WHERE survey_question_id = 16;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 16 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'mes'
  WHERE survey_question_id = 16 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = '3 meses'
  WHERE survey_question_id = 16 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '6 meses'
  WHERE survey_question_id = 16 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'año'
  WHERE survey_question_id = 16 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'No he salido del país en el que resido en el último año.'
  WHERE survey_question_id = 16 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado reflujo o ERGE (enfermedad por reflujo gastroesofágico)?'
  WHERE survey_question_id = 160;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 160 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 160 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 160 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 160 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 160 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Qué tipo de síndrome de intestino irritable (SII) tiene?'
  WHERE survey_question_id = 161;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 161 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Colitis ulcerosa'
  WHERE survey_question_id = 161 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Enfermedad de Crohn'
  WHERE survey_question_id = 161 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Lleva una dieta especial? (seleccione todas las opciones que correspondan)'
  WHERE survey_question_id = 162;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 162 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Dieta paleolítica o primitiva'
  WHERE survey_question_id = 162 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Dieta paleolítica modificada'
  WHERE survey_question_id = 162 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Dieta de alimentos crudos'
  WHERE survey_question_id = 162 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'FODMAP'
  WHERE survey_question_id = 162 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Dieta Weston-Price o alguna otra dieta con bajo contenido de cereales y alimentos procesados'
  WHERE survey_question_id = 162 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Kosher'
  WHERE survey_question_id = 162 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Halal'
  WHERE survey_question_id = 162 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = 'No consumo verduras solanáceas'
  WHERE survey_question_id = 162 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = 'No consumo productos lácteos'
  WHERE survey_question_id = 162 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET spanish = 'No consumo azúcares refinados'
  WHERE survey_question_id = 162 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET spanish = 'Otras restricciones no indicadas aquí'
  WHERE survey_question_id = 162 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET spanish = 'No llevo una dieta especial'
  WHERE survey_question_id = 162 AND
        display_index = 12;

UPDATE ag.survey_question SET spanish = '¿Cuántas bebidas alcohólicas consume cuando bebe?'
  WHERE survey_question_id = 163;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 163 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = '1'
  WHERE survey_question_id = 163 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = '1-2'
  WHERE survey_question_id = 163 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '2-3'
  WHERE survey_question_id = 163 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = '3-4'
  WHERE survey_question_id = 163 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Más de 4'
  WHERE survey_question_id = 163 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'No bebo'
  WHERE survey_question_id = 163 AND
        display_index = 6;

UPDATE ag.survey_question SET spanish = '¿Qué tipo de SII tiene?'
  WHERE survey_question_id = 164;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 164 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Enfermedad de Crohn, localización ileal'
  WHERE survey_question_id = 164 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Enfermedad de Crohn, localización colónica'
  WHERE survey_question_id = 164 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Enfermedad de Crohn, localización ilecolónica'
  WHERE survey_question_id = 164 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Colitis ulcerosa'
  WHERE survey_question_id = 164 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Colitis microscópica'
  WHERE survey_question_id = 164 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con cuántas personas distintas de sus familiares vive?'
  WHERE survey_question_id = 17;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 17 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Ninguna'
  WHERE survey_question_id = 17 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Una'
  WHERE survey_question_id = 17 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Dos'
  WHERE survey_question_id = 17 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Tres'
  WHERE survey_question_id = 17 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Más de tres'
  WHERE survey_question_id = 17 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Alguna de las personas con las que vive participa en este estudio?'
  WHERE survey_question_id = 18;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 18 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 18 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 18 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro'
  WHERE survey_question_id = 18 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Es familiar de alguno de los participantes del estudio o vive con alguno de ellos?'
  WHERE survey_question_id = 19;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 19 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 19 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 19 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro'
  WHERE survey_question_id = 19 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Toma algún complejo multivitamínico a diario?'
  WHERE survey_question_id = 2;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 2 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 2 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 2 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Tiene perro/s?'
  WHERE survey_question_id = 20;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 20 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 20 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 20 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Tiene gato/s?'
  WHERE survey_question_id = 21;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 21 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 21 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 21 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Cuál es su mano dominante?'
  WHERE survey_question_id = 22;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 22 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Soy diestro'
  WHERE survey_question_id = 22 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Soy zurdo'
  WHERE survey_question_id = 22 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Soy ambidiestro'
  WHERE survey_question_id = 22 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Cuál es su nivel de estudios académicos?'
  WHERE survey_question_id = 23;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 23 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No terminé la escuela secundaria'
  WHERE survey_question_id = 23 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Título de estudios secundarios o equivalente al GED'
  WHERE survey_question_id = 23 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Estudios universitarios o técnicos incompletos'
  WHERE survey_question_id = 23 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Título de pregrado (grado tras 2 años de universidad)'
  WHERE survey_question_id = 23 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Licenciatura (grado tras 4 o más años de universidad)'
  WHERE survey_question_id = 23 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Estudios de posgrado o profesionales incompletos'
  WHERE survey_question_id = 23 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Título de estudios de posgrado o profesionales'
  WHERE survey_question_id = 23 AND
        display_index = 7;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia hace ejercicio?'
  WHERE survey_question_id = 24;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 24 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 24 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (unas cuantas veces al mes)'
  WHERE survey_question_id = 24 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 24 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 24 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 24 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Por lo general, hace ejercicio en interiores o al aire libre?'
  WHERE survey_question_id = 25;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 25 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'En interiores'
  WHERE survey_question_id = 25 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Al aire libre'
  WHERE survey_question_id = 25 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ambos'
  WHERE survey_question_id = 25 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Depende de la estación'
  WHERE survey_question_id = 25 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Ninguna de las opciones anteriores'
  WHERE survey_question_id = 25 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Se come las uñas?'
  WHERE survey_question_id = 26;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 26 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 26 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 26 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia usa piscinas/bañeras de hidromasaje?'
  WHERE survey_question_id = 27;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 27 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 27 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (unas cuantas veces al mes)'
  WHERE survey_question_id = 27 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 27 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 27 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 27 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia fuma cigarrillos?'
  WHERE survey_question_id = 28;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 28 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 28 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (unas cuantas veces al mes)'
  WHERE survey_question_id = 28 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 28 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 28 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 28 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia bebe alcohol?'
  WHERE survey_question_id = 29;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 29 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 29 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (unas cuantas veces al mes)'
  WHERE survey_question_id = 29 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 29 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 29 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 29 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia toma probióticos?'
  WHERE survey_question_id = 3;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 3 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 3 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (unas cuantas veces al mes)'
  WHERE survey_question_id = 3 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 3 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 3 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 3 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Qué tipo de alcohol suele consumir? (seleccione todas las opciones que correspondan)'
  WHERE survey_question_id = 30;

UPDATE ag.survey_question_response 
  SET spanish = 'Cerveza/sidra'
  WHERE survey_question_id = 30 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Cervezas ácidas'
  WHERE survey_question_id = 30 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Vino blanco'
  WHERE survey_question_id = 30 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Vino tinto'
  WHERE survey_question_id = 30 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Bebidas destiladas/con alto grado alcohólico'
  WHERE survey_question_id = 30 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 30 AND
        display_index = 999;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia se cepilla los dientes?'
  WHERE survey_question_id = 31;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 31 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 31 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (menos de una vez al día)'
  WHERE survey_question_id = 31 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (1-2 veces al día)'
  WHERE survey_question_id = 31 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Frecuentemente (más de 2 veces al día)'
  WHERE survey_question_id = 31 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 31 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia usa hilo dental?'
  WHERE survey_question_id = 32;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 32 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 32 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (una cuantas veces al mes)'
  WHERE survey_question_id = 32 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 32 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 32 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 32 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia se maquilla la cara?'
  WHERE survey_question_id = 33;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 33 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 33 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (unas cuantas veces al mes)'
  WHERE survey_question_id = 33 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 33 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 33 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 33 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Usa desodorante o antisudorífico? (los antisudoríficos suelen contener aluminio)'
  WHERE survey_question_id = 34;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 34 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Uso desodorante'
  WHERE survey_question_id = 34 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Uso antisudorífico'
  WHERE survey_question_id = 34 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro, pero uso algún tipo de desodorante/antisudorífico'
  WHERE survey_question_id = 34 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'No uso desodorante ni antisudorífico'
  WHERE survey_question_id = 34 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Cuántas horas duerme aproximadamente durante una noche habitual?'
  WHERE survey_question_id = 35;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 35 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Menos de 5 horas'
  WHERE survey_question_id = 35 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = '5-6 horas'
  WHERE survey_question_id = 35 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '6-7 horas'
  WHERE survey_question_id = 35 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = '7-8 horas'
  WHERE survey_question_id = 35 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = '8 horas o más'
  WHERE survey_question_id = 35 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Usa suavizante para la ropa a la hora de secarla?'
  WHERE survey_question_id = 36;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 36 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 36 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 36 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Cuántas veces suele evacuar materia fecal en un día habitual?'
  WHERE survey_question_id = 37;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 37 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Menos de una'
  WHERE survey_question_id = 37 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Una'
  WHERE survey_question_id = 37 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Dos'
  WHERE survey_question_id = 37 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Tres'
  WHERE survey_question_id = 37 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Cuatro'
  WHERE survey_question_id = 37 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Cinco o más'
  WHERE survey_question_id = 37 AND
        display_index = 6;

UPDATE ag.survey_question SET spanish = 'Describa la calidad de la evacuación. Utilice el siguiente cuadro a modo de referencia:'
  WHERE survey_question_id = 38;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 38 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Suelo estreñirme (dificultad para evacuar): tipos 1 y 2'
  WHERE survey_question_id = 38 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Suelo tener diarrea (heces líquidas): tipos 5, 6 y 7'
  WHERE survey_question_id = 38 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Suelo evacuar heces normales: tipos 3 y 4'
  WHERE survey_question_id = 38 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro, no tengo ningún punto de referencia'
  WHERE survey_question_id = 38 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'He tomado antibióticos en los últimos ____________.'
  WHERE survey_question_id = 39;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 39 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Semana'
  WHERE survey_question_id = 39 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Mes'
  WHERE survey_question_id = 39 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '6 meses'
  WHERE survey_question_id = 39 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Año'
  WHERE survey_question_id = 39 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'No he tomado antibióticos a lo largo del último año.'
  WHERE survey_question_id = 39 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia toma complejos de vitamina B, folato o ácido fólico?'
  WHERE survey_question_id = 4;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 4 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 4 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (unas cuantas veces al mes)'
  WHERE survey_question_id = 4 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 4 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 4 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 4 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Me han puesto la vacuna antigripal en los últimos ____________.'
  WHERE survey_question_id = 40;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 40 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Semana'
  WHERE survey_question_id = 40 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Mes'
  WHERE survey_question_id = 40 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '6 meses'
  WHERE survey_question_id = 40 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Año'
  WHERE survey_question_id = 40 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'No me han puesto la vacuna antigripal a lo largo del último año.'
  WHERE survey_question_id = 40 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Utiliza actualmente algún tipo de método anticonceptivo hormonal?'
  WHERE survey_question_id = 41;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 41 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí, tomo la píldora'
  WHERE survey_question_id = 41 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí, uso un anticonceptivo inyectable (DMPA)'
  WHERE survey_question_id = 41 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí, uso un parche anticonceptivo (Ortho-Evra)'
  WHERE survey_question_id = 41 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí, uso NuvaRing'
  WHERE survey_question_id = 41 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí, uso un DIU hormonal (Mirena)'
  WHERE survey_question_id = 41 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 41 AND
        display_index = 6;

UPDATE ag.survey_question SET spanish = '¿Está embarazada?'
  WHERE survey_question_id = 42;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 42 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 42 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 42 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy segura'
  WHERE survey_question_id = 42 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = 'A lo largo de los últimos 6 meses, mi peso _________.'
  WHERE survey_question_id = 43;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 43 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'aumentó más de 10 libras'
  WHERE survey_question_id = 43 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'se redujo más de 10 libras'
  WHERE survey_question_id = 43 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'se mantuvo estable'
  WHERE survey_question_id = 43 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Le han extirpado las amígdalas?'
  WHERE survey_question_id = 44;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 44 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 44 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 44 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro'
  WHERE survey_question_id = 44 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Le han extirpado el apéndice?'
  WHERE survey_question_id = 45;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 45 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 45 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 45 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro'
  WHERE survey_question_id = 45 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Ha tenido varicela?'
  WHERE survey_question_id = 46;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 46 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 46 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 46 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro'
  WHERE survey_question_id = 46 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Toma algún medicamento de venta con receta para el acné facial?'
  WHERE survey_question_id = 47;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 47 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 47 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 47 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Toma algún medicamento de venta sin receta para el acné facial?'
  WHERE survey_question_id = 48;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 48 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 48 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 48 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Toma algún medicamento de venta con o sin receta para otras afecciones?'
  WHERE survey_question_id = 49;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 49 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 49 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 49 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia toma un suplemento de vitamina D?'
  WHERE survey_question_id = 5;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 5 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 5 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (unas cuantas veces al mes)'
  WHERE survey_question_id = 5 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 5 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 5 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 5 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Nació por cesárea?'
  WHERE survey_question_id = 50;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 50 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 50 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 50 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro'
  WHERE survey_question_id = 50 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Cómo lo alimentaron cuando era recién nacido?'
  WHERE survey_question_id = 51;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 51 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Principalmente con leche materna'
  WHERE survey_question_id = 51 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Principalmente con fórmula para recién nacidos'
  WHERE survey_question_id = 51 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Con una mezcla de leche materna y fórmula para recién nacidos'
  WHERE survey_question_id = 51 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'No estoy seguro'
  WHERE survey_question_id = 51 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Está dispuesto a que nos pongamos en contacto con usted para que responda más preguntas sobre las afecciones mencionadas?'
  WHERE survey_question_id = 52;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 52 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 52 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 52 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Tiene alergia estacional?'
  WHERE survey_question_id = 53;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 53 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 53 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 53 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Tiene alguna de las siguientes alergias no alimentarias? (marque todas las opciones que correspondan)'
  WHERE survey_question_id = 54;

UPDATE ag.survey_question_response 
  SET spanish = 'Fármacos (p. ej., penicilina)'
  WHERE survey_question_id = 54 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Caspa de los animales'
  WHERE survey_question_id = 54 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Picadura de las abejas'
  WHERE survey_question_id = 54 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Roble/hiedra venenoso'
  WHERE survey_question_id = 54 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Sol'
  WHERE survey_question_id = 54 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 54 AND
        display_index = 999;

UPDATE ag.survey_question SET spanish = '¿Es usted recién nacido y se alimenta principalmente de leche materna o fórmula o es adulto y se alimenta principalmente (recibe más del 75 % de las calorías diarias) de batidos alimenticios para adultos (p. ej., Ensure)?'
  WHERE survey_question_id = 55;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 55 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 55 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 55 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Consumo alimentos sólidos y leche materna/fórmula'
  WHERE survey_question_id = 55 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume carne/huevos?'
  WHERE survey_question_id = 56;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 56 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 56 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 56 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 56 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 56 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 56 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana cocina y come comidas caseras? (Excluya las comidas listas para consumir, como los macarrones con queso en caja, las sopas de fideos orientales o los alimentos de Lean Cuisine)'
  WHERE survey_question_id = 57;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 57 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 57 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 57 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 57 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 57 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 57 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana come alimentos listos para consumir (p. ej., macarrones con queso, sopas de fideos orientales o alimentos de Lean Cuisine)?'
  WHERE survey_question_id = 58;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 58 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 58 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 58 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 58 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 58 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 58 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume alimentos preparados en un restaurante (incluidas las comidas para llevar?'
  WHERE survey_question_id = 59;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 59 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 59 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 59 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 59 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 59 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 59 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Toma algún otro suplemento alimenticio o herbal?'
  WHERE survey_question_id = 6;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 6 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 6 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 6 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado enfermedad de los riñones?'
  WHERE survey_question_id = 60;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 60 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 60 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 60 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 60 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 60 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume al menos 2-3 porciones de fruta al día? (1 porción = 1/2 taza de fruta; 1 fruta mediana; 4 oz. de jugo de frutas 100 % natural).'
  WHERE survey_question_id = 61;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 61 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 61 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 61 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 61 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 61 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 61 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume al menos 2-3 porciones de verdura al día (incluidas las papas)? (1 porción = 1/2 taza de verduras/papas; 1 taza de verduras de hoja crudas).'
  WHERE survey_question_id = 62;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 62 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 62 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 62 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 62 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 62 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 62 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume una o más porciones de verduras o productos vegetales fermentados al día? (1 porción = 1/2 taza de chucrut, kimchi o verduras fermentadas o 1 taza de kombucha).'
  WHERE survey_question_id = 63;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 63 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 63 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 63 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 63 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 63 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 63 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume al menos 2 porciones de leche o queso al día? (1 porción = 1 taza de leche o yogur; 1 y 1/2 o 2 onzas de queso).'
  WHERE survey_question_id = 64;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 64 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 64 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 64 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 64 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 64 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 64 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume productos de reemplazo de la leche (leche de soja, leche sin lactosa, leche de almendras, etc.)?'
  WHERE survey_question_id = 65;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 65 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 65 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 65 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 65 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 65 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 65 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia consume postres congelados (helado, helado de tipo italiano, batidos de helado, sorbetes, yogur helado, etc.)?'
  WHERE survey_question_id = 66;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 66 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 66 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 66 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 66 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 66 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 66 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume carnes rojas?'
  WHERE survey_question_id = 67;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 67 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 67 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 67 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 67 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 67 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 67 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume carnes rojas con mayor contenido de grasa, como costillar, chuleta, carne picada, costilla, panceta, etc.?'
  WHERE survey_question_id = 68;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 68 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 68 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 68 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 68 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 68 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 68 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántos días a la semana consume carne de ave (pollo, pavo, etc.) al menos una vez al día?'
  WHERE survey_question_id = 69;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 69 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 69 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 69 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 69 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 69 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 69 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Es intolerante a la lactosa?'
  WHERE survey_question_id = 7;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 7 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sí'
  WHERE survey_question_id = 7 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 7 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántos días a la semana consume pescado y marisco (pescado, camarones, langostas, cangrejos, etc.)?'
  WHERE survey_question_id = 70;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 70 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 70 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 70 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 70 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 70 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 70 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántos días a la semana consume aperitivos salados (papas fritas de paquete, nachos, totopos, palomitas de maíz con mantequilla, papas fritas, etc.)?'
  WHERE survey_question_id = 71;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 71 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 71 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 71 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 71 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 71 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 71 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántos días a la semana consume cosas dulces (tartas, galletas, bollos, rosquillas, pastelillos, chocolate, etc.) al menos una vez al día?'
  WHERE survey_question_id = 72;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 72 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 72 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 72 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 72 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 72 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 72 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántos días a la semana cocina con aceite de oliva (o usa aceite de oliva para condimentar ensaladas)?'
  WHERE survey_question_id = 73;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 73 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 73 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 73 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 73 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 73 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 73 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Consume huevos enteros (no productos del tipo Egg Beaters ni solo claras de huevo)?'
  WHERE survey_question_id = 74;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 74 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 74 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 74 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 74 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 74 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 74 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Bebe 16 onzas o más de bebidas endulzadas con azúcar como refrescos no dietéticos o bebidas frutales/ponche (que no incluyan jugo 100 % natural) al día? (1 lata de refresco = 12 onzas).'
  WHERE survey_question_id = 75;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 75 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 75 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 75 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 75 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 75 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 75 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Consume al menos 1 litro (aproximadamente 32 onzas) de agua al día?'
  WHERE survey_question_id = 76;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 76 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 76 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 76 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 76 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 76 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 76 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado autismo o trastorno del espectro autista?'
  WHERE survey_question_id = 77;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 77 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 77 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 77 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 77 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 77 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado proliferación bacteriana en el intestino delgado?'
  WHERE survey_question_id = 78;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 78 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo Esa afección'
  WHERE survey_question_id = 78 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 78 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 78 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 78 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado síndrome de intestino irritable (SII)?'
  WHERE survey_question_id = 79;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 79 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 79 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 79 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 79 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 79 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Es intolerante al gluten?'
  WHERE survey_question_id = 8;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 8 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Me diagnosticaron celiaquía'
  WHERE survey_question_id = 8 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Me diagnosticaron alergia al gluten (IgG antigluten), pero no celiaquía'
  WHERE survey_question_id = 8 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'No consumo gluten porque me produce malestar'
  WHERE survey_question_id = 8 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'No'
  WHERE survey_question_id = 8 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado una infección por Clostridium difficile (C. diff)?'
  WHERE survey_question_id = 80;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 80 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 80 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 80 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 80 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 80 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado otra afección importante?'
  WHERE survey_question_id = 81;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 81 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 81 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 81 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 81 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 81 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado diabetes?'
  WHERE survey_question_id = 82;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 82 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 82 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 82 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 82 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 82 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado enfermedad inflamatoria intestinal (EII)?'
  WHERE survey_question_id = 83;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 83 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 83 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 83 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 83 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 83 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado la enfermedad de Alzheimer/demencia?'
  WHERE survey_question_id = 84;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 84 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 84 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 84 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 84 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 84 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado TDA/TDAH?'
  WHERE survey_question_id = 85;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 85 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 85 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 85 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 85 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 85 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado enfermedad del hígado?'
  WHERE survey_question_id = 86;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 86 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 86 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 86 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 86 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 86 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado alguna enfermedad autoinmunitaria, como lupus (lupus eritematoso diseminado), AR (artritis reumatoide), EM (esclerosis múltiple) o tiroiditis de Hashimoto (u otra enfermedad autoinmunitaria)?'
  WHERE survey_question_id = 87;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 87 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 87 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 87 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional la medicina alternativa'
  WHERE survey_question_id = 87 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 87 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado alguna enfermedad de la piel?'
  WHERE survey_question_id = 88;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 88 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 88 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 88 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 88 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 88 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado enfermedad de arterias coronarias o del corazón, o ha tenido un infarto de miocardio o un accidente cerebrovascular?'
  WHERE survey_question_id = 89;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 89 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 89 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 89 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 89 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 89 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'Soy alérgico al/a los __________ (marque todas las opciones que correspondan).'
  WHERE survey_question_id = 9;

UPDATE ag.survey_question_response 
  SET spanish = 'Maní'
  WHERE survey_question_id = 9 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Frutos secos'
  WHERE survey_question_id = 9 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Marisco'
  WHERE survey_question_id = 9 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Otro'
  WHERE survey_question_id = 9 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Que yo sepa, no tengo ninguna alergia alimentaria.'
  WHERE survey_question_id = 9 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 9 AND
        display_index = 999;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado epilepsia u otros trastornos convulsivos?'
  WHERE survey_question_id = 90;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 90 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 90 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 90 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 90 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 90 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume al menos 2 porciones de cereales enteros al día?'
  WHERE survey_question_id = 91;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 91 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 91 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (menos de 1 vez a la semana)'
  WHERE survey_question_id = 91 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 91 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 91 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 91 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado migraña?'
  WHERE survey_question_id = 92;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 92 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 92 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 92 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 92 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 92 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado asma, fibrosis quística o EPOC (enfermedad pulmonar obstructiva crónica)?'
  WHERE survey_question_id = 93;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 93 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 93 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 93 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 93 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 93 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado fenilcetonuria?'
  WHERE survey_question_id = 94;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 94 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 94 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 94 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 94 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 94 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado candidiasis o proliferación fúngica en el intestino?'
  WHERE survey_question_id = 95;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 95 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 95 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 95 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 95 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 95 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado una enfermedad de la tiroides?'
  WHERE survey_question_id = 96;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 96 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 96 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 96 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 96 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 96 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Alguna vez le han diagnosticado depresión, trastorno bipolar o esquizofrenia?'
  WHERE survey_question_id = 97;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 97 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'No tengo esa afección'
  WHERE survey_question_id = 97 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional médico (médico o auxiliar médico)'
  WHERE survey_question_id = 97 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'La diagnosticó un profesional de medicina alternativa'
  WHERE survey_question_id = 97 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Yo mismo me diagnostiqué'
  WHERE survey_question_id = 97 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'Fecha del parto:'
  WHERE survey_question_id = 98;

UPDATE ag.survey_question SET spanish = 'Medicamentos de venta con y sin receta:'
  WHERE survey_question_id = 99;

UPDATE ag.survey_question SET spanish = 'Por lo general, ¿cuántas veces a la semana consume una o más porciones de verduras o productos vegetales fermentados al día? (1 porción = 1/2 taza de chucrut, kimchi o verduras fermentadas o 1 taza de kombucha).'
  WHERE survey_question_id = 165;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 165 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 165 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca (alguna vez al mes)'
  WHERE survey_question_id = 165 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ocasionalmente (1-2 veces a la semana)'
  WHERE survey_question_id = 165 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente (3-5 veces a la semana)'
  WHERE survey_question_id = 165 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'A diario'
  WHERE survey_question_id = 165 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'En los últimos ____, he aumentado considerablemente (es decir, a más del doble) el consumo de alimentos fermentados (sin contar la cerveza, el vino y el alcohol), ya sea en frecuencia o en cantidad.'
  WHERE survey_question_id = 166;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 166 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Semana'
  WHERE survey_question_id = 166 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Mes'
  WHERE survey_question_id = 166 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '6 meses'
  WHERE survey_question_id = 166 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Año'
  WHERE survey_question_id = 166 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'No he aumentado el consumo'
  WHERE survey_question_id = 166 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Cuáles de los siguientes alimentos o bebidas fermentados consume más de una vez a la semana? Seleccione todas las opciones que corresponda.'
  WHERE survey_question_id = 167;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 167 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Kimchi'
  WHERE survey_question_id = 167 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Chucrut'
  WHERE survey_question_id = 167 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Frijoles fermentados/miso/natto'
  WHERE survey_question_id = 167 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Verduras encurtidas'
  WHERE survey_question_id = 167 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Tempeh'
  WHERE survey_question_id = 167 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Tofu fermentado'
  WHERE survey_question_id = 167 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Kéfir (agua)'
  WHERE survey_question_id = 167 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = 'Kéfir (leche)'
  WHERE survey_question_id = 167 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = 'Requesón'
  WHERE survey_question_id = 167 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET spanish = 'Yogur/lassi'
  WHERE survey_question_id = 167 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET spanish = 'Crema agria/nata'
  WHERE survey_question_id = 167 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET spanish = 'Pescado fermentado'
  WHERE survey_question_id = 167 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET spanish = 'Salsa de pescado'
  WHERE survey_question_id = 167 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET spanish = 'Pan fermentado/de masa madre/injera'
  WHERE survey_question_id = 167 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET spanish = 'Kombucha'
  WHERE survey_question_id = 167 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET spanish = 'Chicha'
  WHERE survey_question_id = 167 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET spanish = 'Cerveza'
  WHERE survey_question_id = 167 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET spanish = 'Sidra'
  WHERE survey_question_id = 167 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET spanish = 'Vino'
  WHERE survey_question_id = 167 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET spanish = 'Hidromiel'
  WHERE survey_question_id = 167 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET spanish = 'Otros'
  WHERE survey_question_id = 167 AND
        display_index = 21;

UPDATE ag.survey_question SET spanish = 'En “Otros”, indique cualquier otro alimento que consuma y que no esté en la lista.'
  WHERE survey_question_id = 168;

UPDATE ag.survey_question SET spanish = '¿Prepara alguno de los siguientes alimentos o bebidas fermentados en su casa para consumo propio? Seleccione todas las opciones que correspondan.'
  WHERE survey_question_id = 169;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 169 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Kimchi'
  WHERE survey_question_id = 169 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Chucrut'
  WHERE survey_question_id = 169 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Frijoles fermentados/miso/natto'
  WHERE survey_question_id = 169 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Verduras encurtidas'
  WHERE survey_question_id = 169 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Tempeh'
  WHERE survey_question_id = 169 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Tofu fermentado'
  WHERE survey_question_id = 169 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Kéfir (agua)'
  WHERE survey_question_id = 169 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = 'Kéfir (leche)'
  WHERE survey_question_id = 169 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = 'Requesón'
  WHERE survey_question_id = 169 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET spanish = 'Yogur/lassi'
  WHERE survey_question_id = 169 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET spanish = 'Crema agria/nata'
  WHERE survey_question_id = 169 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET spanish = 'Pescado fermentado'
  WHERE survey_question_id = 169 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET spanish = 'Salsa de pescado'
  WHERE survey_question_id = 169 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET spanish = 'Pan fermentado/de masa madre/injera'
  WHERE survey_question_id = 169 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET spanish = 'Kombucha'
  WHERE survey_question_id = 169 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET spanish = 'Chicha'
  WHERE survey_question_id = 169 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET spanish = 'Cerveza'
  WHERE survey_question_id = 169 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET spanish = 'Sidra'
  WHERE survey_question_id = 169 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET spanish = 'Vino'
  WHERE survey_question_id = 169 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET spanish = 'Hidromiel'
  WHERE survey_question_id = 169 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET spanish = 'Otros'
  WHERE survey_question_id = 169 AND
        display_index = 21;

UPDATE ag.survey_question SET spanish = 'En “Otros”, indique cualquier otro alimento que prepare para su consumo propio y que no esté en la lista.'
  WHERE survey_question_id = 170;

UPDATE ag.survey_question SET spanish = '¿Prepara alguno de los siguientes alimentos o bebidas fermentados con fines comerciales? Seleccione todas las opciones que correspondan.'
  WHERE survey_question_id = 171;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 171 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Kimchi'
  WHERE survey_question_id = 171 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Chucrut'
  WHERE survey_question_id = 171 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Frijoles fermentados/miso/natto'
  WHERE survey_question_id = 171 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Verduras encurtidas'
  WHERE survey_question_id = 171 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Tempeh'
  WHERE survey_question_id = 171 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Tofu fermentado'
  WHERE survey_question_id = 171 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Kéfir (agua)'
  WHERE survey_question_id = 171 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = 'Kéfir (leche)'
  WHERE survey_question_id = 171 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = 'Requesón'
  WHERE survey_question_id = 171 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET spanish = 'Yogur/lassi'
  WHERE survey_question_id = 171 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET spanish = 'Crema agria/nata'
  WHERE survey_question_id = 171 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET spanish = 'Pescado fermentado'
  WHERE survey_question_id = 171 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET spanish = 'Salsa de pescado'
  WHERE survey_question_id = 171 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET spanish = 'Pan fermentado/de masa madre/injera'
  WHERE survey_question_id = 171 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET spanish = 'Kombucha'
  WHERE survey_question_id = 171 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET spanish = 'Chicha'
  WHERE survey_question_id = 171 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET spanish = 'Cerveza'
  WHERE survey_question_id = 171 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET spanish = 'Sidra'
  WHERE survey_question_id = 171 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET spanish = 'Vino'
  WHERE survey_question_id = 171 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET spanish = 'Hidromiel'
  WHERE survey_question_id = 171 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET spanish = 'Otros'
  WHERE survey_question_id = 171 AND
        display_index = 21;

UPDATE ag.survey_question SET spanish = 'En “Otros”, indique cualquier otro alimento que prepare con fines comerciales y que no esté en la lista.'
  WHERE survey_question_id = 172;

UPDATE ag.survey_question SET spanish = 'Aporte más datos sobre esta actividad.'
  WHERE survey_question_id = 173;

UPDATE ag.survey_question SET spanish = 'Nombre'
  WHERE survey_question_id = 127;

UPDATE ag.survey_question SET spanish = 'Tipo de animal'
  WHERE survey_question_id = 128;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 128 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Perro'
  WHERE survey_question_id = 128 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Gato'
  WHERE survey_question_id = 128 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Mamífero pequeño'
  WHERE survey_question_id = 128 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Mamífero grande'
  WHERE survey_question_id = 128 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Pez'
  WHERE survey_question_id = 128 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Ave'
  WHERE survey_question_id = 128 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Reptil'
  WHERE survey_question_id = 128 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = 'Anfibio'
  WHERE survey_question_id = 128 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = 'Otros'
  WHERE survey_question_id = 128 AND
        display_index = 9;

UPDATE ag.survey_question SET spanish = 'Origen'
  WHERE survey_question_id = 129;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 129 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Criadero'
  WHERE survey_question_id = 129 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Refugio'
  WHERE survey_question_id = 129 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Hogar'
  WHERE survey_question_id = 129 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Silvestre'
  WHERE survey_question_id = 129 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'Edad'
  WHERE survey_question_id = 130;

UPDATE ag.survey_question SET spanish = 'Sexo'
  WHERE survey_question_id = 131;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 131 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Masculino'
  WHERE survey_question_id = 131 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Femenino'
  WHERE survey_question_id = 131 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = 'Contexto'
  WHERE survey_question_id = 132;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 132 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Urbano'
  WHERE survey_question_id = 132 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Suburbano'
  WHERE survey_question_id = 132 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Rural'
  WHERE survey_question_id = 132 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = 'Categoría de peso'
  WHERE survey_question_id = 133;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 133 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Con peso insuficiente'
  WHERE survey_question_id = 133 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Delgado'
  WHERE survey_question_id = 133 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Con peso normal'
  WHERE survey_question_id = 133 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Regordete'
  WHERE survey_question_id = 133 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Con sobrepeso'
  WHERE survey_question_id = 133 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Clasificación de la dieta'
  WHERE survey_question_id = 134;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 134 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Carnívora'
  WHERE survey_question_id = 134 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Omnívora'
  WHERE survey_question_id = 134 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Herbívora'
  WHERE survey_question_id = 134 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = 'Fuente de alimento'
  WHERE survey_question_id = 135;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 135 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Alimento de la tienda de mascotas'
  WHERE survey_question_id = 135 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Alimento humano'
  WHERE survey_question_id = 135 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Alimento silvestre'
  WHERE survey_question_id = 135 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = 'Tipo de alimento'
  WHERE survey_question_id = 136;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 136 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Seco'
  WHERE survey_question_id = 136 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Húmedo'
  WHERE survey_question_id = 136 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Ambos'
  WHERE survey_question_id = 136 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = 'Características alimenticias especiales'
  WHERE survey_question_id = 137;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 137 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Biológico (orgánico)'
  WHERE survey_question_id = 137 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Sin cereales'
  WHERE survey_question_id = 137 AND
        display_index = 2;

UPDATE ag.survey_question SET spanish = 'Cómo vive'
  WHERE survey_question_id = 138;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 138 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Vive solo, con humanos'
  WHERE survey_question_id = 138 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Vive solo, sin humanos/con pocos humanos (refugio)'
  WHERE survey_question_id = 138 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Vive con otros animales y humanos'
  WHERE survey_question_id = 138 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Vive con otros animales/pocos humanos'
  WHERE survey_question_id = 138 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'Horas que pasa al aire libre'
  WHERE survey_question_id = 139;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 139 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Ninguna'
  WHERE survey_question_id = 139 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Menos de 2'
  WHERE survey_question_id = 139 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '2-4'
  WHERE survey_question_id = 139 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = '4-8'
  WHERE survey_question_id = 139 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Más de 8'
  WHERE survey_question_id = 139 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = 'Acceso a agua del inodoro'
  WHERE survey_question_id = 140;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 140 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Periódicamente'
  WHERE survey_question_id = 140 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'A veces'
  WHERE survey_question_id = 140 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 140 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = 'Nivel de coprofagia (que come materia fecal)'
  WHERE survey_question_id = 141;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 141 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Alto'
  WHERE survey_question_id = 141 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Moderado'
  WHERE survey_question_id = 141 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Bajo'
  WHERE survey_question_id = 141 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 141 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = 'Indique cualquier otro dato sobre este animal que usted cree que podría afectar los microorganismos del animal.'
  WHERE survey_question_id = 142;

UPDATE ag.survey_question SET spanish = 'Indique el tipo de animal.'
  WHERE survey_question_id = 143;

UPDATE ag.survey_question SET spanish = 'Indique el tipo de los demás animales.'
  WHERE survey_question_id = 144;

UPDATE ag.survey_question SET spanish = 'Indique la edad (en años) y el sexo de los humanos con los que el animal vive actualmente.'
  WHERE survey_question_id = 145;

UPDATE ag.survey_question SET spanish = '¿Dónde hace surf en su zona?'
  WHERE survey_question_id = 174;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 174 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Point Loma/Ocean Beach, San Diego, California (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'La Jolla, San Diego, California (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Encinitas, California (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Sur de California (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Centro de California (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Norte de California (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET spanish = 'Noroeste del Pacífico (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET spanish = 'Hawái (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET spanish = 'Noreste (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET spanish = 'Sureste (EE. UU.)'
  WHERE survey_question_id = 174 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET spanish = 'Sudamérica'
  WHERE survey_question_id = 174 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET spanish = 'Europa'
  WHERE survey_question_id = 174 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET spanish = 'África'
  WHERE survey_question_id = 174 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET spanish = 'Australia'
  WHERE survey_question_id = 174 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET spanish = 'Nueva Zelanda'
  WHERE survey_question_id = 174 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET spanish = 'Sudeste asiático'
  WHERE survey_question_id = 174 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET spanish = 'Asia'
  WHERE survey_question_id = 174 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET spanish = 'Otro'
  WHERE survey_question_id = 174 AND
        display_index = 18;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia hace surf en su zona?'
  WHERE survey_question_id = 175;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 175 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Varias veces al día'
  WHERE survey_question_id = 175 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Una vez al día'
  WHERE survey_question_id = 175 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Varias veces a la semana'
  WHERE survey_question_id = 175 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Una vez a la semana'
  WHERE survey_question_id = 175 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Varias veces al mes'
  WHERE survey_question_id = 175 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia hace surf?'
  WHERE survey_question_id = 176;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 176 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Varias veces al día'
  WHERE survey_question_id = 176 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Una vez al día'
  WHERE survey_question_id = 176 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Varias veces a la semana'
  WHERE survey_question_id = 176 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Una vez a la semana'
  WHERE survey_question_id = 176 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Varias veces al mes'
  WHERE survey_question_id = 176 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia viaja para hacer surf en otros lugares?'
  WHERE survey_question_id = 177;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 177 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Varias veces al día'
  WHERE survey_question_id = 177 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Una vez al día'
  WHERE survey_question_id = 177 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Varias veces a la semana'
  WHERE survey_question_id = 177 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Una vez a la semana'
  WHERE survey_question_id = 177 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Varias veces al mes'
  WHERE survey_question_id = 177 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Qué distancia recorre desde la playa entre las sesiones (casa/trabajo/viaje)?'
  WHERE survey_question_id = 178;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 178 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = '< 1 km'
  WHERE survey_question_id = 178 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = '5-10 km'
  WHERE survey_question_id = 178 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '> 10 km'
  WHERE survey_question_id = 178 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Qué tipo de traje de neopreno usa?'
  WHERE survey_question_id = 179;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 179 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Ninguno'
  WHERE survey_question_id = 179 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = '< 1 mm'
  WHERE survey_question_id = 179 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = '2-3 mm'
  WHERE survey_question_id = 179 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = '3-4 mm'
  WHERE survey_question_id = 179 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = '4-5 mm'
  WHERE survey_question_id = 179 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Qué tipo de protector solar usa?'
  WHERE survey_question_id = 180;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 180 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'FPS < 25'
  WHERE survey_question_id = 180 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'FPS de 25 a 50'
  WHERE survey_question_id = 180 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'FPS de más de 50'
  WHERE survey_question_id = 180 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Otro'
  WHERE survey_question_id = 180 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia se pone el protector solar?'
  WHERE survey_question_id = 181;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 181 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Cada vez que hago surf'
  WHERE survey_question_id = 181 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'A menudo'
  WHERE survey_question_id = 181 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca'
  WHERE survey_question_id = 181 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 181 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Con qué frecuencia se ducha después de hacer surf?'
  WHERE survey_question_id = 182;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 182 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Cada vez que hago surf'
  WHERE survey_question_id = 182 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'A menudo'
  WHERE survey_question_id = 182 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Casi nunca'
  WHERE survey_question_id = 182 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Nunca'
  WHERE survey_question_id = 182 AND
        display_index = 4;

UPDATE ag.survey_question SET spanish = '¿Cuál es su posición en la tabla?'
  WHERE survey_question_id = 183;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 183 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Natural'
  WHERE survey_question_id = 183 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Pie derecho delante'
  WHERE survey_question_id = 183 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Tumbado boca abajo'
  WHERE survey_question_id = 183 AND
        display_index = 3;

UPDATE ag.survey_question SET spanish = '¿Qué tipo de tabla de surf prefiere?'
  WHERE survey_question_id = 184;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 184 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Longboard'
  WHERE survey_question_id = 184 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Shortboard'
  WHERE survey_question_id = 184 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Bodyboard'
  WHERE survey_question_id = 184 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Sin tabla'
  WHERE survey_question_id = 184 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Sin preferencia'
  WHERE survey_question_id = 184 AND
        display_index = 5;

UPDATE ag.survey_question SET spanish = '¿Qué tipo de cera usa?'
  WHERE survey_question_id = 185;

UPDATE ag.survey_question_response 
  SET spanish = 'Sin determinar'
  WHERE survey_question_id = 185 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET spanish = 'Sex Wax'
  WHERE survey_question_id = 185 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET spanish = 'Sticky Bumps'
  WHERE survey_question_id = 185 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET spanish = 'Mrs. Palmers'
  WHERE survey_question_id = 185 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET spanish = 'Bubble Gum'
  WHERE survey_question_id = 185 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET spanish = 'Famous'
  WHERE survey_question_id = 185 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET spanish = 'Otras'
  WHERE survey_question_id = 185 AND
        display_index = 6;

ALTER TABLE ag.survey_question
    ADD COLUMN french varchar;
ALTER TABLE ag.survey_question_response
    ADD COLUMN french varchar;
UPDATE ag.survey_question SET french = 'Comment définiriez-vous votre régime alimentaire ?'
  WHERE survey_question_id = 1;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 1 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Omnivore'
  WHERE survey_question_id = 1 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Omnivore, mais je ne mange pas de viande rouge'
  WHERE survey_question_id = 1 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Végétarien'
  WHERE survey_question_id = 1 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Végétarien, mais je mange des produits de la mer'
  WHERE survey_question_id = 1 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Végane'
  WHERE survey_question_id = 1 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Suivez-vous un régime paléolithique, paléolithique modifié, primitif, FODMAP, Weston-Price ou tout autre régime comprenant peu de céréales et d’aliments transformés ?'
  WHERE survey_question_id = 10;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 10 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 10 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 10 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Votre chien vit-il à l’intérieur/extérieur ou son espace est-il limité (cage/abri) ?'
  WHERE survey_question_id = 101;

UPDATE ag.survey_question SET french = 'Race/origines :'
  WHERE survey_question_id = 103;

UPDATE ag.survey_question SET french = 'Compléments alimentaires :'
  WHERE survey_question_id = 104;

UPDATE ag.survey_question SET french = 'Nature des contacts avec votre chien :'
  WHERE survey_question_id = 105;

UPDATE ag.survey_question SET french = 'Autres maladies dont vous êtes atteint(e) qui ne figurent pas sur la liste de la question concernant les maladies diagnostiquées'
  WHERE survey_question_id = 106;

UPDATE ag.survey_question SET french = 'Sexe :'
  WHERE survey_question_id = 107;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 107 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Homme'
  WHERE survey_question_id = 107 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Femme'
  WHERE survey_question_id = 107 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 107 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Taille :'
  WHERE survey_question_id = 108;

UPDATE ag.survey_question SET french = 'Unités de taille :'
  WHERE survey_question_id = 109;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 109 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'pouces'
  WHERE survey_question_id = 109 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'centimètres'
  WHERE survey_question_id = 109 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Mangez-vous de la viande/des produits laitiers issus d’animaux traités avec des antibiotiques ?'
  WHERE survey_question_id = 11;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 11 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 11 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 11 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 11 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Pays de naissance :'
  WHERE survey_question_id = 110;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 110 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Afghanistan'
  WHERE survey_question_id = 110 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Iles Aland'
  WHERE survey_question_id = 110 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Albanie'
  WHERE survey_question_id = 110 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Algérie'
  WHERE survey_question_id = 110 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Samoa américaines'
  WHERE survey_question_id = 110 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Andorre'
  WHERE survey_question_id = 110 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Angola'
  WHERE survey_question_id = 110 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = 'Anguilla'
  WHERE survey_question_id = 110 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = 'Antarctique'
  WHERE survey_question_id = 110 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET french = 'Antigua-et-Barbuda'
  WHERE survey_question_id = 110 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET french = 'Argentine'
  WHERE survey_question_id = 110 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET french = 'Arménie'
  WHERE survey_question_id = 110 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET french = 'Aruba'
  WHERE survey_question_id = 110 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET french = 'Australie'
  WHERE survey_question_id = 110 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET french = 'L''Autriche'
  WHERE survey_question_id = 110 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET french = 'Azerbaïdjan'
  WHERE survey_question_id = 110 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET french = 'Bahamas'
  WHERE survey_question_id = 110 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET french = 'Bahrein'
  WHERE survey_question_id = 110 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET french = 'Bangladesh'
  WHERE survey_question_id = 110 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET french = 'Barbade'
  WHERE survey_question_id = 110 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET french = 'Biélorussie'
  WHERE survey_question_id = 110 AND
        display_index = 21;
UPDATE ag.survey_question_response 
  SET french = 'Belgique'
  WHERE survey_question_id = 110 AND
        display_index = 22;
UPDATE ag.survey_question_response 
  SET french = 'Belize'
  WHERE survey_question_id = 110 AND
        display_index = 23;
UPDATE ag.survey_question_response 
  SET french = 'Bénin'
  WHERE survey_question_id = 110 AND
        display_index = 24;
UPDATE ag.survey_question_response 
  SET french = 'Bermudes'
  WHERE survey_question_id = 110 AND
        display_index = 25;
UPDATE ag.survey_question_response 
  SET french = 'Bhoutan'
  WHERE survey_question_id = 110 AND
        display_index = 26;
UPDATE ag.survey_question_response 
  SET french = 'Bolivie'
  WHERE survey_question_id = 110 AND
        display_index = 27;
UPDATE ag.survey_question_response 
  SET french = 'Bosnie Herzégovine'
  WHERE survey_question_id = 110 AND
        display_index = 28;
UPDATE ag.survey_question_response 
  SET french = 'Botswana'
  WHERE survey_question_id = 110 AND
        display_index = 29;
UPDATE ag.survey_question_response 
  SET french = 'Île Bouvet'
  WHERE survey_question_id = 110 AND
        display_index = 30;
UPDATE ag.survey_question_response 
  SET french = 'Brésil'
  WHERE survey_question_id = 110 AND
        display_index = 31;
UPDATE ag.survey_question_response 
  SET french = 'Territoire britannique de l''océan Indien'
  WHERE survey_question_id = 110 AND
        display_index = 32;
UPDATE ag.survey_question_response 
  SET french = 'Brunei Darussalam'
  WHERE survey_question_id = 110 AND
        display_index = 33;
UPDATE ag.survey_question_response 
  SET french = 'Bulgarie'
  WHERE survey_question_id = 110 AND
        display_index = 34;
UPDATE ag.survey_question_response 
  SET french = 'Burkina Faso'
  WHERE survey_question_id = 110 AND
        display_index = 35;
UPDATE ag.survey_question_response 
  SET french = 'Burundi'
  WHERE survey_question_id = 110 AND
        display_index = 36;
UPDATE ag.survey_question_response 
  SET french = 'Cambodge'
  WHERE survey_question_id = 110 AND
        display_index = 37;
UPDATE ag.survey_question_response 
  SET french = 'Cameroun'
  WHERE survey_question_id = 110 AND
        display_index = 38;
UPDATE ag.survey_question_response 
  SET french = 'Canada'
  WHERE survey_question_id = 110 AND
        display_index = 39;
UPDATE ag.survey_question_response 
  SET french = 'Cap-Vert'
  WHERE survey_question_id = 110 AND
        display_index = 40;
UPDATE ag.survey_question_response 
  SET french = 'Îles Caïmans'
  WHERE survey_question_id = 110 AND
        display_index = 41;
UPDATE ag.survey_question_response 
  SET french = 'République centrafricaine'
  WHERE survey_question_id = 110 AND
        display_index = 42;
UPDATE ag.survey_question_response 
  SET french = 'Tchad'
  WHERE survey_question_id = 110 AND
        display_index = 43;
UPDATE ag.survey_question_response 
  SET french = 'Chili'
  WHERE survey_question_id = 110 AND
        display_index = 44;
UPDATE ag.survey_question_response 
  SET french = 'Chine'
  WHERE survey_question_id = 110 AND
        display_index = 45;
UPDATE ag.survey_question_response 
  SET french = 'L''île de noël'
  WHERE survey_question_id = 110 AND
        display_index = 46;
UPDATE ag.survey_question_response 
  SET french = 'Îles Cocos (Keeling)'
  WHERE survey_question_id = 110 AND
        display_index = 47;
UPDATE ag.survey_question_response 
  SET french = 'Colombie'
  WHERE survey_question_id = 110 AND
        display_index = 48;
UPDATE ag.survey_question_response 
  SET french = 'Comores'
  WHERE survey_question_id = 110 AND
        display_index = 49;
UPDATE ag.survey_question_response 
  SET french = 'Congo'
  WHERE survey_question_id = 110 AND
        display_index = 50;
UPDATE ag.survey_question_response 
  SET french = 'Congo, République démocratique du'
  WHERE survey_question_id = 110 AND
        display_index = 51;
UPDATE ag.survey_question_response 
  SET french = 'les Îles Cook'
  WHERE survey_question_id = 110 AND
        display_index = 52;
UPDATE ag.survey_question_response 
  SET french = 'Costa Rica'
  WHERE survey_question_id = 110 AND
        display_index = 53;
UPDATE ag.survey_question_response 
  SET french = 'Côte d''Ivoire'
  WHERE survey_question_id = 110 AND
        display_index = 54;
UPDATE ag.survey_question_response 
  SET french = 'Croatie'
  WHERE survey_question_id = 110 AND
        display_index = 55;
UPDATE ag.survey_question_response 
  SET french = 'Cuba'
  WHERE survey_question_id = 110 AND
        display_index = 56;
UPDATE ag.survey_question_response 
  SET french = 'Chypre'
  WHERE survey_question_id = 110 AND
        display_index = 57;
UPDATE ag.survey_question_response 
  SET french = 'République Tchèque'
  WHERE survey_question_id = 110 AND
        display_index = 58;
UPDATE ag.survey_question_response 
  SET french = 'Danemark'
  WHERE survey_question_id = 110 AND
        display_index = 59;
UPDATE ag.survey_question_response 
  SET french = 'Djibouti'
  WHERE survey_question_id = 110 AND
        display_index = 60;
UPDATE ag.survey_question_response 
  SET french = 'Dominique'
  WHERE survey_question_id = 110 AND
        display_index = 61;
UPDATE ag.survey_question_response 
  SET french = 'République Dominicaine'
  WHERE survey_question_id = 110 AND
        display_index = 62;
UPDATE ag.survey_question_response 
  SET french = 'Équateur'
  WHERE survey_question_id = 110 AND
        display_index = 63;
UPDATE ag.survey_question_response 
  SET french = 'Egypte'
  WHERE survey_question_id = 110 AND
        display_index = 64;
UPDATE ag.survey_question_response 
  SET french = 'Le Salvador'
  WHERE survey_question_id = 110 AND
        display_index = 65;
UPDATE ag.survey_question_response 
  SET french = 'Guinée Équatoriale'
  WHERE survey_question_id = 110 AND
        display_index = 66;
UPDATE ag.survey_question_response 
  SET french = 'Érythrée'
  WHERE survey_question_id = 110 AND
        display_index = 67;
UPDATE ag.survey_question_response 
  SET french = 'Estonie'
  WHERE survey_question_id = 110 AND
        display_index = 68;
UPDATE ag.survey_question_response 
  SET french = 'Ethiopie'
  WHERE survey_question_id = 110 AND
        display_index = 69;
UPDATE ag.survey_question_response 
  SET french = 'Îles Falkland (Malvinas)'
  WHERE survey_question_id = 110 AND
        display_index = 70;
UPDATE ag.survey_question_response 
  SET french = 'Îles Féroé'
  WHERE survey_question_id = 110 AND
        display_index = 71;
UPDATE ag.survey_question_response 
  SET french = 'Fidji'
  WHERE survey_question_id = 110 AND
        display_index = 72;
UPDATE ag.survey_question_response 
  SET french = 'Finlande'
  WHERE survey_question_id = 110 AND
        display_index = 73;
UPDATE ag.survey_question_response 
  SET french = 'France'
  WHERE survey_question_id = 110 AND
        display_index = 74;
UPDATE ag.survey_question_response 
  SET french = 'Guyane Française'
  WHERE survey_question_id = 110 AND
        display_index = 75;
UPDATE ag.survey_question_response 
  SET french = 'Polynésie française'
  WHERE survey_question_id = 110 AND
        display_index = 76;
UPDATE ag.survey_question_response 
  SET french = 'Territoires français du Sud'
  WHERE survey_question_id = 110 AND
        display_index = 77;
UPDATE ag.survey_question_response 
  SET french = 'Gabon'
  WHERE survey_question_id = 110 AND
        display_index = 78;
UPDATE ag.survey_question_response 
  SET french = 'Gambie'
  WHERE survey_question_id = 110 AND
        display_index = 79;
UPDATE ag.survey_question_response 
  SET french = 'Géorgie'
  WHERE survey_question_id = 110 AND
        display_index = 80;
UPDATE ag.survey_question_response 
  SET french = 'Allemagne'
  WHERE survey_question_id = 110 AND
        display_index = 81;
UPDATE ag.survey_question_response 
  SET french = 'Ghana'
  WHERE survey_question_id = 110 AND
        display_index = 82;
UPDATE ag.survey_question_response 
  SET french = 'Gibraltar'
  WHERE survey_question_id = 110 AND
        display_index = 83;
UPDATE ag.survey_question_response 
  SET french = 'Grèce'
  WHERE survey_question_id = 110 AND
        display_index = 84;
UPDATE ag.survey_question_response 
  SET french = 'Groenland'
  WHERE survey_question_id = 110 AND
        display_index = 85;
UPDATE ag.survey_question_response 
  SET french = 'Grenade'
  WHERE survey_question_id = 110 AND
        display_index = 86;
UPDATE ag.survey_question_response 
  SET french = 'Guadeloupe'
  WHERE survey_question_id = 110 AND
        display_index = 87;
UPDATE ag.survey_question_response 
  SET french = 'Guam'
  WHERE survey_question_id = 110 AND
        display_index = 88;
UPDATE ag.survey_question_response 
  SET french = 'Guatemala'
  WHERE survey_question_id = 110 AND
        display_index = 89;
UPDATE ag.survey_question_response 
  SET french = 'Guernesey'
  WHERE survey_question_id = 110 AND
        display_index = 90;
UPDATE ag.survey_question_response 
  SET french = 'Guinée'
  WHERE survey_question_id = 110 AND
        display_index = 91;
UPDATE ag.survey_question_response 
  SET french = 'Guinée-bissau'
  WHERE survey_question_id = 110 AND
        display_index = 92;
UPDATE ag.survey_question_response 
  SET french = 'Guyane'
  WHERE survey_question_id = 110 AND
        display_index = 93;
UPDATE ag.survey_question_response 
  SET french = 'Haïti'
  WHERE survey_question_id = 110 AND
        display_index = 94;
UPDATE ag.survey_question_response 
  SET french = 'Îles Heard et Mcdonald'
  WHERE survey_question_id = 110 AND
        display_index = 95;
UPDATE ag.survey_question_response 
  SET french = 'Saint-Siège (État de la Cité du Vatican)'
  WHERE survey_question_id = 110 AND
        display_index = 96;
UPDATE ag.survey_question_response 
  SET french = 'Honduras'
  WHERE survey_question_id = 110 AND
        display_index = 97;
UPDATE ag.survey_question_response 
  SET french = 'Hong Kong'
  WHERE survey_question_id = 110 AND
        display_index = 98;
UPDATE ag.survey_question_response 
  SET french = 'Hongrie'
  WHERE survey_question_id = 110 AND
        display_index = 99;
UPDATE ag.survey_question_response 
  SET french = 'Islande'
  WHERE survey_question_id = 110 AND
        display_index = 100;
UPDATE ag.survey_question_response 
  SET french = 'Inde'
  WHERE survey_question_id = 110 AND
        display_index = 101;
UPDATE ag.survey_question_response 
  SET french = 'Indonésie'
  WHERE survey_question_id = 110 AND
        display_index = 102;
UPDATE ag.survey_question_response 
  SET french = 'Iran (République islamique d'
  WHERE survey_question_id = 110 AND
        display_index = 103;
UPDATE ag.survey_question_response 
  SET french = 'Irak'
  WHERE survey_question_id = 110 AND
        display_index = 104;
UPDATE ag.survey_question_response 
  SET french = 'Irlande'
  WHERE survey_question_id = 110 AND
        display_index = 105;
UPDATE ag.survey_question_response 
  SET french = 'île de Man'
  WHERE survey_question_id = 110 AND
        display_index = 106;
UPDATE ag.survey_question_response 
  SET french = 'Israël'
  WHERE survey_question_id = 110 AND
        display_index = 107;
UPDATE ag.survey_question_response 
  SET french = 'Italie'
  WHERE survey_question_id = 110 AND
        display_index = 108;
UPDATE ag.survey_question_response 
  SET french = 'Jamaïque'
  WHERE survey_question_id = 110 AND
        display_index = 109;
UPDATE ag.survey_question_response 
  SET french = 'Japon'
  WHERE survey_question_id = 110 AND
        display_index = 110;
UPDATE ag.survey_question_response 
  SET french = 'Jersey'
  WHERE survey_question_id = 110 AND
        display_index = 111;
UPDATE ag.survey_question_response 
  SET french = 'Jordan'
  WHERE survey_question_id = 110 AND
        display_index = 112;
UPDATE ag.survey_question_response 
  SET french = 'Kazakhstan'
  WHERE survey_question_id = 110 AND
        display_index = 113;
UPDATE ag.survey_question_response 
  SET french = 'Kenya'
  WHERE survey_question_id = 110 AND
        display_index = 114;
UPDATE ag.survey_question_response 
  SET french = 'Kiribati'
  WHERE survey_question_id = 110 AND
        display_index = 115;
UPDATE ag.survey_question_response 
  SET french = 'République populaire démocratique de Corée'
  WHERE survey_question_id = 110 AND
        display_index = 116;
UPDATE ag.survey_question_response 
  SET french = 'Corée, République de'
  WHERE survey_question_id = 110 AND
        display_index = 117;
UPDATE ag.survey_question_response 
  SET french = 'Koweit'
  WHERE survey_question_id = 110 AND
        display_index = 118;
UPDATE ag.survey_question_response 
  SET french = 'Kirghizistan'
  WHERE survey_question_id = 110 AND
        display_index = 119;
UPDATE ag.survey_question_response 
  SET french = 'République démocratique populaire lao'
  WHERE survey_question_id = 110 AND
        display_index = 120;
UPDATE ag.survey_question_response 
  SET french = 'Lettonie'
  WHERE survey_question_id = 110 AND
        display_index = 121;
UPDATE ag.survey_question_response 
  SET french = 'Liban'
  WHERE survey_question_id = 110 AND
        display_index = 122;
UPDATE ag.survey_question_response 
  SET french = 'Lesotho'
  WHERE survey_question_id = 110 AND
        display_index = 123;
UPDATE ag.survey_question_response 
  SET french = 'Libéria'
  WHERE survey_question_id = 110 AND
        display_index = 124;
UPDATE ag.survey_question_response 
  SET french = 'Jamahiriya arabe libyenne'
  WHERE survey_question_id = 110 AND
        display_index = 125;
UPDATE ag.survey_question_response 
  SET french = 'Liechtenstein'
  WHERE survey_question_id = 110 AND
        display_index = 126;
UPDATE ag.survey_question_response 
  SET french = 'Lituanie'
  WHERE survey_question_id = 110 AND
        display_index = 127;
UPDATE ag.survey_question_response 
  SET french = 'Luxembourg'
  WHERE survey_question_id = 110 AND
        display_index = 128;
UPDATE ag.survey_question_response 
  SET french = 'Macao'
  WHERE survey_question_id = 110 AND
        display_index = 129;
UPDATE ag.survey_question_response 
  SET french = 'Macédoine, ancienne République yougoslave de'
  WHERE survey_question_id = 110 AND
        display_index = 130;
UPDATE ag.survey_question_response 
  SET french = 'Madagascar'
  WHERE survey_question_id = 110 AND
        display_index = 131;
UPDATE ag.survey_question_response 
  SET french = 'Malawi'
  WHERE survey_question_id = 110 AND
        display_index = 132;
UPDATE ag.survey_question_response 
  SET french = 'Malaisie'
  WHERE survey_question_id = 110 AND
        display_index = 133;
UPDATE ag.survey_question_response 
  SET french = 'Maldives'
  WHERE survey_question_id = 110 AND
        display_index = 134;
UPDATE ag.survey_question_response 
  SET french = 'Mali'
  WHERE survey_question_id = 110 AND
        display_index = 135;
UPDATE ag.survey_question_response 
  SET french = 'Malte'
  WHERE survey_question_id = 110 AND
        display_index = 136;
UPDATE ag.survey_question_response 
  SET french = 'Iles Marshall'
  WHERE survey_question_id = 110 AND
        display_index = 137;
UPDATE ag.survey_question_response 
  SET french = 'Martinique'
  WHERE survey_question_id = 110 AND
        display_index = 138;
UPDATE ag.survey_question_response 
  SET french = 'Mauritanie'
  WHERE survey_question_id = 110 AND
        display_index = 139;
UPDATE ag.survey_question_response 
  SET french = 'Maurice'
  WHERE survey_question_id = 110 AND
        display_index = 140;
UPDATE ag.survey_question_response 
  SET french = 'Mayotte'
  WHERE survey_question_id = 110 AND
        display_index = 141;
UPDATE ag.survey_question_response 
  SET french = 'Mexique'
  WHERE survey_question_id = 110 AND
        display_index = 142;
UPDATE ag.survey_question_response 
  SET french = 'Micronésie, États fédérés de'
  WHERE survey_question_id = 110 AND
        display_index = 143;
UPDATE ag.survey_question_response 
  SET french = 'Moldova, République de'
  WHERE survey_question_id = 110 AND
        display_index = 144;
UPDATE ag.survey_question_response 
  SET french = 'Monaco'
  WHERE survey_question_id = 110 AND
        display_index = 145;
UPDATE ag.survey_question_response 
  SET french = 'Mongolie'
  WHERE survey_question_id = 110 AND
        display_index = 146;
UPDATE ag.survey_question_response 
  SET french = 'Monténégro'
  WHERE survey_question_id = 110 AND
        display_index = 147;
UPDATE ag.survey_question_response 
  SET french = 'Montserrat'
  WHERE survey_question_id = 110 AND
        display_index = 148;
UPDATE ag.survey_question_response 
  SET french = 'Maroc'
  WHERE survey_question_id = 110 AND
        display_index = 149;
UPDATE ag.survey_question_response 
  SET french = 'Mozambique'
  WHERE survey_question_id = 110 AND
        display_index = 150;
UPDATE ag.survey_question_response 
  SET french = 'Myanmar'
  WHERE survey_question_id = 110 AND
        display_index = 151;
UPDATE ag.survey_question_response 
  SET french = 'Namibie'
  WHERE survey_question_id = 110 AND
        display_index = 152;
UPDATE ag.survey_question_response 
  SET french = 'Nauru'
  WHERE survey_question_id = 110 AND
        display_index = 153;
UPDATE ag.survey_question_response 
  SET french = 'Népal'
  WHERE survey_question_id = 110 AND
        display_index = 154;
UPDATE ag.survey_question_response 
  SET french = 'Pays-Bas'
  WHERE survey_question_id = 110 AND
        display_index = 155;
UPDATE ag.survey_question_response 
  SET french = 'Antilles néerlandaises'
  WHERE survey_question_id = 110 AND
        display_index = 156;
UPDATE ag.survey_question_response 
  SET french = 'Nouvelle Calédonie'
  WHERE survey_question_id = 110 AND
        display_index = 157;
UPDATE ag.survey_question_response 
  SET french = 'Nouvelle-Zélande'
  WHERE survey_question_id = 110 AND
        display_index = 158;
UPDATE ag.survey_question_response 
  SET french = 'Nicaragua'
  WHERE survey_question_id = 110 AND
        display_index = 159;
UPDATE ag.survey_question_response 
  SET french = 'Niger'
  WHERE survey_question_id = 110 AND
        display_index = 160;
UPDATE ag.survey_question_response 
  SET french = 'Nigeria'
  WHERE survey_question_id = 110 AND
        display_index = 161;
UPDATE ag.survey_question_response 
  SET french = 'Niue'
  WHERE survey_question_id = 110 AND
        display_index = 162;
UPDATE ag.survey_question_response 
  SET french = 'l''ile de Norfolk'
  WHERE survey_question_id = 110 AND
        display_index = 163;
UPDATE ag.survey_question_response 
  SET french = 'Îles Mariannes du Nord'
  WHERE survey_question_id = 110 AND
        display_index = 164;
UPDATE ag.survey_question_response 
  SET french = 'Norvège'
  WHERE survey_question_id = 110 AND
        display_index = 165;
UPDATE ag.survey_question_response 
  SET french = 'Oman'
  WHERE survey_question_id = 110 AND
        display_index = 166;
UPDATE ag.survey_question_response 
  SET french = 'Pakistan'
  WHERE survey_question_id = 110 AND
        display_index = 167;
UPDATE ag.survey_question_response 
  SET french = 'Palau'
  WHERE survey_question_id = 110 AND
        display_index = 168;
UPDATE ag.survey_question_response 
  SET french = 'Territoire palestinien, occupé'
  WHERE survey_question_id = 110 AND
        display_index = 169;
UPDATE ag.survey_question_response 
  SET french = 'Panama'
  WHERE survey_question_id = 110 AND
        display_index = 170;
UPDATE ag.survey_question_response 
  SET french = 'Papouasie Nouvelle Guinée'
  WHERE survey_question_id = 110 AND
        display_index = 171;
UPDATE ag.survey_question_response 
  SET french = 'Paraguay'
  WHERE survey_question_id = 110 AND
        display_index = 172;
UPDATE ag.survey_question_response 
  SET french = 'Pérou'
  WHERE survey_question_id = 110 AND
        display_index = 173;
UPDATE ag.survey_question_response 
  SET french = 'Philippines'
  WHERE survey_question_id = 110 AND
        display_index = 174;
UPDATE ag.survey_question_response 
  SET french = 'Pitcairn'
  WHERE survey_question_id = 110 AND
        display_index = 175;
UPDATE ag.survey_question_response 
  SET french = 'Pologne'
  WHERE survey_question_id = 110 AND
        display_index = 176;
UPDATE ag.survey_question_response 
  SET french = 'le Portugal'
  WHERE survey_question_id = 110 AND
        display_index = 177;
UPDATE ag.survey_question_response 
  SET french = 'Porto Rico'
  WHERE survey_question_id = 110 AND
        display_index = 178;
UPDATE ag.survey_question_response 
  SET french = 'Qatar'
  WHERE survey_question_id = 110 AND
        display_index = 179;
UPDATE ag.survey_question_response 
  SET french = 'Réunion'
  WHERE survey_question_id = 110 AND
        display_index = 180;
UPDATE ag.survey_question_response 
  SET french = 'Roumanie'
  WHERE survey_question_id = 110 AND
        display_index = 181;
UPDATE ag.survey_question_response 
  SET french = 'Fédération Russe'
  WHERE survey_question_id = 110 AND
        display_index = 182;
UPDATE ag.survey_question_response 
  SET french = 'Rwanda'
  WHERE survey_question_id = 110 AND
        display_index = 183;
UPDATE ag.survey_question_response 
  SET french = 'Sainte-Hélène'
  WHERE survey_question_id = 110 AND
        display_index = 184;
UPDATE ag.survey_question_response 
  SET french = 'Saint-Christophe-et-Niévès'
  WHERE survey_question_id = 110 AND
        display_index = 185;
UPDATE ag.survey_question_response 
  SET french = 'Sainte-Lucie'
  WHERE survey_question_id = 110 AND
        display_index = 186;
UPDATE ag.survey_question_response 
  SET french = 'Saint-Pierre-et-Miquelon'
  WHERE survey_question_id = 110 AND
        display_index = 187;
UPDATE ag.survey_question_response 
  SET french = 'Saint-Vincent-et-les-Grenadines'
  WHERE survey_question_id = 110 AND
        display_index = 188;
UPDATE ag.survey_question_response 
  SET french = 'Samoa'
  WHERE survey_question_id = 110 AND
        display_index = 189;
UPDATE ag.survey_question_response 
  SET french = 'Saint Marin'
  WHERE survey_question_id = 110 AND
        display_index = 190;
UPDATE ag.survey_question_response 
  SET french = 'Sao Tomé et Principe'
  WHERE survey_question_id = 110 AND
        display_index = 191;
UPDATE ag.survey_question_response 
  SET french = 'Arabie Saoudite'
  WHERE survey_question_id = 110 AND
        display_index = 192;
UPDATE ag.survey_question_response 
  SET french = 'Sénégal'
  WHERE survey_question_id = 110 AND
        display_index = 193;
UPDATE ag.survey_question_response 
  SET french = 'Serbie'
  WHERE survey_question_id = 110 AND
        display_index = 194;
UPDATE ag.survey_question_response 
  SET french = 'les Seychelles'
  WHERE survey_question_id = 110 AND
        display_index = 195;
UPDATE ag.survey_question_response 
  SET french = 'Sierra Leone'
  WHERE survey_question_id = 110 AND
        display_index = 196;
UPDATE ag.survey_question_response 
  SET french = 'Singapour'
  WHERE survey_question_id = 110 AND
        display_index = 197;
UPDATE ag.survey_question_response 
  SET french = 'Slovaquie'
  WHERE survey_question_id = 110 AND
        display_index = 198;
UPDATE ag.survey_question_response 
  SET french = 'Slovénie'
  WHERE survey_question_id = 110 AND
        display_index = 199;
UPDATE ag.survey_question_response 
  SET french = 'Les îles Salomon'
  WHERE survey_question_id = 110 AND
        display_index = 200;
UPDATE ag.survey_question_response 
  SET french = 'Somalie'
  WHERE survey_question_id = 110 AND
        display_index = 201;
UPDATE ag.survey_question_response 
  SET french = 'Afrique du Sud'
  WHERE survey_question_id = 110 AND
        display_index = 202;
UPDATE ag.survey_question_response 
  SET french = 'Géorgie du Sud et les îles Sandwich du Sud'
  WHERE survey_question_id = 110 AND
        display_index = 203;
UPDATE ag.survey_question_response 
  SET french = 'Espagne'
  WHERE survey_question_id = 110 AND
        display_index = 204;
UPDATE ag.survey_question_response 
  SET french = 'Sri Lanka'
  WHERE survey_question_id = 110 AND
        display_index = 205;
UPDATE ag.survey_question_response 
  SET french = 'Soudan'
  WHERE survey_question_id = 110 AND
        display_index = 206;
UPDATE ag.survey_question_response 
  SET french = 'Suriname'
  WHERE survey_question_id = 110 AND
        display_index = 207;
UPDATE ag.survey_question_response 
  SET french = 'Svalbard et Jan Mayen'
  WHERE survey_question_id = 110 AND
        display_index = 208;
UPDATE ag.survey_question_response 
  SET french = 'Swaziland'
  WHERE survey_question_id = 110 AND
        display_index = 209;
UPDATE ag.survey_question_response 
  SET french = 'Suède'
  WHERE survey_question_id = 110 AND
        display_index = 210;
UPDATE ag.survey_question_response 
  SET french = 'Suisse'
  WHERE survey_question_id = 110 AND
        display_index = 211;
UPDATE ag.survey_question_response 
  SET french = 'République arabe syrienne'
  WHERE survey_question_id = 110 AND
        display_index = 212;
UPDATE ag.survey_question_response 
  SET french = 'Taiwan, Province de Chine'
  WHERE survey_question_id = 110 AND
        display_index = 213;
UPDATE ag.survey_question_response 
  SET french = 'Tadjikistan'
  WHERE survey_question_id = 110 AND
        display_index = 214;
UPDATE ag.survey_question_response 
  SET french = 'Tanzanie, République-Unie de'
  WHERE survey_question_id = 110 AND
        display_index = 215;
UPDATE ag.survey_question_response 
  SET french = 'Thaïlande'
  WHERE survey_question_id = 110 AND
        display_index = 216;
UPDATE ag.survey_question_response 
  SET french = 'Timor-leste'
  WHERE survey_question_id = 110 AND
        display_index = 217;
UPDATE ag.survey_question_response 
  SET french = 'Aller'
  WHERE survey_question_id = 110 AND
        display_index = 218;
UPDATE ag.survey_question_response 
  SET french = 'Tokelau'
  WHERE survey_question_id = 110 AND
        display_index = 219;
UPDATE ag.survey_question_response 
  SET french = 'Tonga'
  WHERE survey_question_id = 110 AND
        display_index = 220;
UPDATE ag.survey_question_response 
  SET french = 'Trinité-et-Tobago'
  WHERE survey_question_id = 110 AND
        display_index = 221;
UPDATE ag.survey_question_response 
  SET french = 'Tunisie'
  WHERE survey_question_id = 110 AND
        display_index = 222;
UPDATE ag.survey_question_response 
  SET french = 'Turquie'
  WHERE survey_question_id = 110 AND
        display_index = 223;
UPDATE ag.survey_question_response 
  SET french = 'Turkménistan'
  WHERE survey_question_id = 110 AND
        display_index = 224;
UPDATE ag.survey_question_response 
  SET french = 'îles Turques-et-Caïques'
  WHERE survey_question_id = 110 AND
        display_index = 225;
UPDATE ag.survey_question_response 
  SET french = 'Tuvalu'
  WHERE survey_question_id = 110 AND
        display_index = 226;
UPDATE ag.survey_question_response 
  SET french = 'Ouganda'
  WHERE survey_question_id = 110 AND
        display_index = 227;
UPDATE ag.survey_question_response 
  SET french = 'Ukraine'
  WHERE survey_question_id = 110 AND
        display_index = 228;
UPDATE ag.survey_question_response 
  SET french = 'Emirats Arabes Unis'
  WHERE survey_question_id = 110 AND
        display_index = 229;
UPDATE ag.survey_question_response 
  SET french = 'Royaume-Uni'
  WHERE survey_question_id = 110 AND
        display_index = 230;
UPDATE ag.survey_question_response 
  SET french = 'États Unis'
  WHERE survey_question_id = 110 AND
        display_index = 231;
UPDATE ag.survey_question_response 
  SET french = 'Îles mineures éloignées des États-Unis'
  WHERE survey_question_id = 110 AND
        display_index = 232;
UPDATE ag.survey_question_response 
  SET french = 'Uruguay'
  WHERE survey_question_id = 110 AND
        display_index = 233;
UPDATE ag.survey_question_response 
  SET french = 'Ouzbékistan'
  WHERE survey_question_id = 110 AND
        display_index = 234;
UPDATE ag.survey_question_response 
  SET french = 'Vanuatu'
  WHERE survey_question_id = 110 AND
        display_index = 235;
UPDATE ag.survey_question_response 
  SET french = 'Venezuela'
  WHERE survey_question_id = 110 AND
        display_index = 236;
UPDATE ag.survey_question_response 
  SET french = 'Viet Nam'
  WHERE survey_question_id = 110 AND
        display_index = 237;
UPDATE ag.survey_question_response 
  SET french = 'Îles Vierges britanniques'
  WHERE survey_question_id = 110 AND
        display_index = 238;
UPDATE ag.survey_question_response 
  SET french = 'Îles Vierges américaines'
  WHERE survey_question_id = 110 AND
        display_index = 239;
UPDATE ag.survey_question_response 
  SET french = 'Wallis et Futuna'
  WHERE survey_question_id = 110 AND
        display_index = 240;
UPDATE ag.survey_question_response 
  SET french = 'Sahara occidental'
  WHERE survey_question_id = 110 AND
        display_index = 241;
UPDATE ag.survey_question_response 
  SET french = 'Yémen'
  WHERE survey_question_id = 110 AND
        display_index = 242;
UPDATE ag.survey_question_response 
  SET french = 'Zambie'
  WHERE survey_question_id = 110 AND
        display_index = 243;
UPDATE ag.survey_question_response 
  SET french = 'Zimbabwe'
  WHERE survey_question_id = 110 AND
        display_index = 244;

UPDATE ag.survey_question SET french = 'Mois de naissance :'
  WHERE survey_question_id = 111;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 111 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'janvier'
  WHERE survey_question_id = 111 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'février'
  WHERE survey_question_id = 111 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Mars'
  WHERE survey_question_id = 111 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'avril'
  WHERE survey_question_id = 111 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Mai'
  WHERE survey_question_id = 111 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'juin'
  WHERE survey_question_id = 111 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'juillet'
  WHERE survey_question_id = 111 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = 'août'
  WHERE survey_question_id = 111 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = 'septembre'
  WHERE survey_question_id = 111 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET french = 'octobre'
  WHERE survey_question_id = 111 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET french = 'novembre'
  WHERE survey_question_id = 111 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET french = 'décembre'
  WHERE survey_question_id = 111 AND
        display_index = 12;

UPDATE ag.survey_question SET french = 'Année de naissance :'
  WHERE survey_question_id = 112;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 112 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = '2018'
  WHERE survey_question_id = 112 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = '2017'
  WHERE survey_question_id = 112 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = '2016'
  WHERE survey_question_id = 112 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = '2015'
  WHERE survey_question_id = 112 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = '2014'
  WHERE survey_question_id = 112 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = '2013'
  WHERE survey_question_id = 112 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = '2012'
  WHERE survey_question_id = 112 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = '2011'
  WHERE survey_question_id = 112 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = '2010'
  WHERE survey_question_id = 112 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET french = '2009'
  WHERE survey_question_id = 112 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET french = '2008'
  WHERE survey_question_id = 112 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET french = '2007'
  WHERE survey_question_id = 112 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET french = '2006'
  WHERE survey_question_id = 112 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET french = '2005'
  WHERE survey_question_id = 112 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET french = '2004'
  WHERE survey_question_id = 112 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET french = '2003'
  WHERE survey_question_id = 112 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET french = '2002'
  WHERE survey_question_id = 112 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET french = '2001'
  WHERE survey_question_id = 112 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET french = '2000'
  WHERE survey_question_id = 112 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET french = '1999'
  WHERE survey_question_id = 112 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET french = '1998'
  WHERE survey_question_id = 112 AND
        display_index = 21;
UPDATE ag.survey_question_response 
  SET french = '1997'
  WHERE survey_question_id = 112 AND
        display_index = 22;
UPDATE ag.survey_question_response 
  SET french = '1996'
  WHERE survey_question_id = 112 AND
        display_index = 23;
UPDATE ag.survey_question_response 
  SET french = '1995'
  WHERE survey_question_id = 112 AND
        display_index = 24;
UPDATE ag.survey_question_response 
  SET french = '1994'
  WHERE survey_question_id = 112 AND
        display_index = 25;
UPDATE ag.survey_question_response 
  SET french = '1993'
  WHERE survey_question_id = 112 AND
        display_index = 26;
UPDATE ag.survey_question_response 
  SET french = '1992'
  WHERE survey_question_id = 112 AND
        display_index = 27;
UPDATE ag.survey_question_response 
  SET french = '1991'
  WHERE survey_question_id = 112 AND
        display_index = 28;
UPDATE ag.survey_question_response 
  SET french = '1990'
  WHERE survey_question_id = 112 AND
        display_index = 29;
UPDATE ag.survey_question_response 
  SET french = '1989'
  WHERE survey_question_id = 112 AND
        display_index = 30;
UPDATE ag.survey_question_response 
  SET french = '1988'
  WHERE survey_question_id = 112 AND
        display_index = 31;
UPDATE ag.survey_question_response 
  SET french = '1987'
  WHERE survey_question_id = 112 AND
        display_index = 32;
UPDATE ag.survey_question_response 
  SET french = '1986'
  WHERE survey_question_id = 112 AND
        display_index = 33;
UPDATE ag.survey_question_response 
  SET french = '1985'
  WHERE survey_question_id = 112 AND
        display_index = 34;
UPDATE ag.survey_question_response 
  SET french = '1984'
  WHERE survey_question_id = 112 AND
        display_index = 35;
UPDATE ag.survey_question_response 
  SET french = '1983'
  WHERE survey_question_id = 112 AND
        display_index = 36;
UPDATE ag.survey_question_response 
  SET french = '1982'
  WHERE survey_question_id = 112 AND
        display_index = 37;
UPDATE ag.survey_question_response 
  SET french = '1981'
  WHERE survey_question_id = 112 AND
        display_index = 38;
UPDATE ag.survey_question_response 
  SET french = '1980'
  WHERE survey_question_id = 112 AND
        display_index = 39;
UPDATE ag.survey_question_response 
  SET french = '1979'
  WHERE survey_question_id = 112 AND
        display_index = 40;
UPDATE ag.survey_question_response 
  SET french = '1978'
  WHERE survey_question_id = 112 AND
        display_index = 41;
UPDATE ag.survey_question_response 
  SET french = '1977'
  WHERE survey_question_id = 112 AND
        display_index = 42;
UPDATE ag.survey_question_response 
  SET french = '1976'
  WHERE survey_question_id = 112 AND
        display_index = 43;
UPDATE ag.survey_question_response 
  SET french = '1975'
  WHERE survey_question_id = 112 AND
        display_index = 44;
UPDATE ag.survey_question_response 
  SET french = '1974'
  WHERE survey_question_id = 112 AND
        display_index = 45;
UPDATE ag.survey_question_response 
  SET french = '1973'
  WHERE survey_question_id = 112 AND
        display_index = 46;
UPDATE ag.survey_question_response 
  SET french = '1972'
  WHERE survey_question_id = 112 AND
        display_index = 47;
UPDATE ag.survey_question_response 
  SET french = '1971'
  WHERE survey_question_id = 112 AND
        display_index = 48;
UPDATE ag.survey_question_response 
  SET french = '1970'
  WHERE survey_question_id = 112 AND
        display_index = 49;
UPDATE ag.survey_question_response 
  SET french = '1969'
  WHERE survey_question_id = 112 AND
        display_index = 50;
UPDATE ag.survey_question_response 
  SET french = '1968'
  WHERE survey_question_id = 112 AND
        display_index = 51;
UPDATE ag.survey_question_response 
  SET french = '1967'
  WHERE survey_question_id = 112 AND
        display_index = 52;
UPDATE ag.survey_question_response 
  SET french = '1966'
  WHERE survey_question_id = 112 AND
        display_index = 53;
UPDATE ag.survey_question_response 
  SET french = '1965'
  WHERE survey_question_id = 112 AND
        display_index = 54;
UPDATE ag.survey_question_response 
  SET french = '1964'
  WHERE survey_question_id = 112 AND
        display_index = 55;
UPDATE ag.survey_question_response 
  SET french = '1963'
  WHERE survey_question_id = 112 AND
        display_index = 56;
UPDATE ag.survey_question_response 
  SET french = '1962'
  WHERE survey_question_id = 112 AND
        display_index = 57;
UPDATE ag.survey_question_response 
  SET french = '1961'
  WHERE survey_question_id = 112 AND
        display_index = 58;
UPDATE ag.survey_question_response 
  SET french = '1960'
  WHERE survey_question_id = 112 AND
        display_index = 59;
UPDATE ag.survey_question_response 
  SET french = '1959'
  WHERE survey_question_id = 112 AND
        display_index = 60;
UPDATE ag.survey_question_response 
  SET french = '1958'
  WHERE survey_question_id = 112 AND
        display_index = 61;
UPDATE ag.survey_question_response 
  SET french = '1957'
  WHERE survey_question_id = 112 AND
        display_index = 62;
UPDATE ag.survey_question_response 
  SET french = '1956'
  WHERE survey_question_id = 112 AND
        display_index = 63;
UPDATE ag.survey_question_response 
  SET french = '1955'
  WHERE survey_question_id = 112 AND
        display_index = 64;
UPDATE ag.survey_question_response 
  SET french = '1954'
  WHERE survey_question_id = 112 AND
        display_index = 65;
UPDATE ag.survey_question_response 
  SET french = '1953'
  WHERE survey_question_id = 112 AND
        display_index = 66;
UPDATE ag.survey_question_response 
  SET french = '1952'
  WHERE survey_question_id = 112 AND
        display_index = 67;
UPDATE ag.survey_question_response 
  SET french = '1951'
  WHERE survey_question_id = 112 AND
        display_index = 68;
UPDATE ag.survey_question_response 
  SET french = '1950'
  WHERE survey_question_id = 112 AND
        display_index = 69;
UPDATE ag.survey_question_response 
  SET french = '1949'
  WHERE survey_question_id = 112 AND
        display_index = 70;
UPDATE ag.survey_question_response 
  SET french = '1948'
  WHERE survey_question_id = 112 AND
        display_index = 71;
UPDATE ag.survey_question_response 
  SET french = '1947'
  WHERE survey_question_id = 112 AND
        display_index = 72;
UPDATE ag.survey_question_response 
  SET french = '1946'
  WHERE survey_question_id = 112 AND
        display_index = 73;
UPDATE ag.survey_question_response 
  SET french = '1945'
  WHERE survey_question_id = 112 AND
        display_index = 74;
UPDATE ag.survey_question_response 
  SET french = '1944'
  WHERE survey_question_id = 112 AND
        display_index = 75;
UPDATE ag.survey_question_response 
  SET french = '1943'
  WHERE survey_question_id = 112 AND
        display_index = 76;
UPDATE ag.survey_question_response 
  SET french = '1942'
  WHERE survey_question_id = 112 AND
        display_index = 77;
UPDATE ag.survey_question_response 
  SET french = '1941'
  WHERE survey_question_id = 112 AND
        display_index = 78;
UPDATE ag.survey_question_response 
  SET french = '1940'
  WHERE survey_question_id = 112 AND
        display_index = 79;
UPDATE ag.survey_question_response 
  SET french = '1939'
  WHERE survey_question_id = 112 AND
        display_index = 80;
UPDATE ag.survey_question_response 
  SET french = '1938'
  WHERE survey_question_id = 112 AND
        display_index = 81;
UPDATE ag.survey_question_response 
  SET french = '1937'
  WHERE survey_question_id = 112 AND
        display_index = 82;
UPDATE ag.survey_question_response 
  SET french = '1936'
  WHERE survey_question_id = 112 AND
        display_index = 83;
UPDATE ag.survey_question_response 
  SET french = '1935'
  WHERE survey_question_id = 112 AND
        display_index = 84;
UPDATE ag.survey_question_response 
  SET french = '1934'
  WHERE survey_question_id = 112 AND
        display_index = 85;
UPDATE ag.survey_question_response 
  SET french = '1933'
  WHERE survey_question_id = 112 AND
        display_index = 86;
UPDATE ag.survey_question_response 
  SET french = '1932'
  WHERE survey_question_id = 112 AND
        display_index = 87;
UPDATE ag.survey_question_response 
  SET french = '1931'
  WHERE survey_question_id = 112 AND
        display_index = 88;
UPDATE ag.survey_question_response 
  SET french = '1930'
  WHERE survey_question_id = 112 AND
        display_index = 89;
UPDATE ag.survey_question_response 
  SET french = '1929'
  WHERE survey_question_id = 112 AND
        display_index = 90;
UPDATE ag.survey_question_response 
  SET french = '1928'
  WHERE survey_question_id = 112 AND
        display_index = 91;
UPDATE ag.survey_question_response 
  SET french = '1927'
  WHERE survey_question_id = 112 AND
        display_index = 92;
UPDATE ag.survey_question_response 
  SET french = '1926'
  WHERE survey_question_id = 112 AND
        display_index = 93;
UPDATE ag.survey_question_response 
  SET french = '1925'
  WHERE survey_question_id = 112 AND
        display_index = 94;
UPDATE ag.survey_question_response 
  SET french = '1924'
  WHERE survey_question_id = 112 AND
        display_index = 95;
UPDATE ag.survey_question_response 
  SET french = '1923'
  WHERE survey_question_id = 112 AND
        display_index = 96;
UPDATE ag.survey_question_response 
  SET french = '1922'
  WHERE survey_question_id = 112 AND
        display_index = 97;
UPDATE ag.survey_question_response 
  SET french = '1921'
  WHERE survey_question_id = 112 AND
        display_index = 98;
UPDATE ag.survey_question_response 
  SET french = '1920'
  WHERE survey_question_id = 112 AND
        display_index = 99;
UPDATE ag.survey_question_response 
  SET french = '1919'
  WHERE survey_question_id = 112 AND
        display_index = 100;
UPDATE ag.survey_question_response 
  SET french = '1918'
  WHERE survey_question_id = 112 AND
        display_index = 101;
UPDATE ag.survey_question_response 
  SET french = '1917'
  WHERE survey_question_id = 112 AND
        display_index = 102;
UPDATE ag.survey_question_response 
  SET french = '1916'
  WHERE survey_question_id = 112 AND
        display_index = 103;
UPDATE ag.survey_question_response 
  SET french = '1915'
  WHERE survey_question_id = 112 AND
        display_index = 104;
UPDATE ag.survey_question_response 
  SET french = '1914'
  WHERE survey_question_id = 112 AND
        display_index = 105;
UPDATE ag.survey_question_response 
  SET french = '1913'
  WHERE survey_question_id = 112 AND
        display_index = 106;
UPDATE ag.survey_question_response 
  SET french = '1912'
  WHERE survey_question_id = 112 AND
        display_index = 107;
UPDATE ag.survey_question_response 
  SET french = '1911'
  WHERE survey_question_id = 112 AND
        display_index = 108;
UPDATE ag.survey_question_response 
  SET french = '1910'
  WHERE survey_question_id = 112 AND
        display_index = 109;
UPDATE ag.survey_question_response 
  SET french = '1909'
  WHERE survey_question_id = 112 AND
        display_index = 110;
UPDATE ag.survey_question_response 
  SET french = '1908'
  WHERE survey_question_id = 112 AND
        display_index = 111;
UPDATE ag.survey_question_response 
  SET french = '1907'
  WHERE survey_question_id = 112 AND
        display_index = 112;
UPDATE ag.survey_question_response 
  SET french = '1906'
  WHERE survey_question_id = 112 AND
        display_index = 113;
UPDATE ag.survey_question_response 
  SET french = '1905'
  WHERE survey_question_id = 112 AND
        display_index = 114;
UPDATE ag.survey_question_response 
  SET french = '1904'
  WHERE survey_question_id = 112 AND
        display_index = 115;
UPDATE ag.survey_question_response 
  SET french = '1903'
  WHERE survey_question_id = 112 AND
        display_index = 116;
UPDATE ag.survey_question_response 
  SET french = '1902'
  WHERE survey_question_id = 112 AND
        display_index = 117;
UPDATE ag.survey_question_response 
  SET french = '1901'
  WHERE survey_question_id = 112 AND
        display_index = 118;
UPDATE ag.survey_question_response 
  SET french = '1900'
  WHERE survey_question_id = 112 AND
        display_index = 119;
UPDATE ag.survey_question_response 
  SET french = '1899'
  WHERE survey_question_id = 112 AND
        display_index = 120;
UPDATE ag.survey_question_response 
  SET french = '1898'
  WHERE survey_question_id = 112 AND
        display_index = 121;
UPDATE ag.survey_question_response 
  SET french = '1897'
  WHERE survey_question_id = 112 AND
        display_index = 122;
UPDATE ag.survey_question_response 
  SET french = '1896'
  WHERE survey_question_id = 112 AND
        display_index = 123;
UPDATE ag.survey_question_response 
  SET french = '1895'
  WHERE survey_question_id = 112 AND
        display_index = 124;
UPDATE ag.survey_question_response 
  SET french = '1894'
  WHERE survey_question_id = 112 AND
        display_index = 125;
UPDATE ag.survey_question_response 
  SET french = '1893'
  WHERE survey_question_id = 112 AND
        display_index = 126;
UPDATE ag.survey_question_response 
  SET french = '1892'
  WHERE survey_question_id = 112 AND
        display_index = 127;
UPDATE ag.survey_question_response 
  SET french = '1891'
  WHERE survey_question_id = 112 AND
        display_index = 128;
UPDATE ag.survey_question_response 
  SET french = '1890'
  WHERE survey_question_id = 112 AND
        display_index = 129;

UPDATE ag.survey_question SET french = 'Poids :'
  WHERE survey_question_id = 113;

UPDATE ag.survey_question SET french = 'Unités de poids :'
  WHERE survey_question_id = 114;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 114 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'livres'
  WHERE survey_question_id = 114 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'kilogrammes'
  WHERE survey_question_id = 114 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Code postal actuel :'
  WHERE survey_question_id = 115;

UPDATE ag.survey_question SET french = 'Veuillez indiquer toute autre information vous concernant que vous estimez susceptible d’avoir un impact sur vos micro-organismes.'
  WHERE survey_question_id = 116;

UPDATE ag.survey_question SET french = 'Votre chat vit-il à l’intérieur/extérieur ou son espace est-il limité (cage/abri) ?'
  WHERE survey_question_id = 117;

UPDATE ag.survey_question SET french = 'Restrictions alimentaires :'
  WHERE survey_question_id = 118;

UPDATE ag.survey_question SET french = 'Voyage :'
  WHERE survey_question_id = 119;

UPDATE ag.survey_question SET french = 'Suivez-vous une restriction alimentaire autre que celles figurant ci-dessus ?'
  WHERE survey_question_id = 12;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 12 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 12 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 12 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Quelle est votre relation avec les autres personnes participant à cette étude, qui vous ont volontairement informé(e) de leur participation (par exemple, partenaire, enfants, colocataires) ? Pour les enfants, veuillez indiquer si vous avez un lien de parenté génétique ou non. Veuillez noter que nous n’utiliserons que les informations fournies par les deux parties.'
  WHERE survey_question_id = 120;

UPDATE ag.survey_question SET french = 'Nature des contacts avec votre chat :'
  WHERE survey_question_id = 122;

UPDATE ag.survey_question SET french = 'Antibiotique utilisé :'
  WHERE survey_question_id = 124;

UPDATE ag.survey_question SET french = 'Traitement pour :'
  WHERE survey_question_id = 126;

UPDATE ag.survey_question SET french = 'D’où provient l’eau que vous buvez chez vous ?'
  WHERE survey_question_id = 13;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 13 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Eau du robinet'
  WHERE survey_question_id = 13 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Puits'
  WHERE survey_question_id = 13 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Bouteille'
  WHERE survey_question_id = 13 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Filtrée'
  WHERE survey_question_id = 13 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 13 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Quelle est votre origine ethnique ?'
  WHERE survey_question_id = 14;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 14 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Caucasienne'
  WHERE survey_question_id = 14 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Asiatique ou insulaire du Pacifique'
  WHERE survey_question_id = 14 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Afro-américaine'
  WHERE survey_question_id = 14 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Hispanique'
  WHERE survey_question_id = 14 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 14 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne chaque semaine, combien d’espèces de plantes différentes mangez-vous ? Par exemple, si vous consommez une boîte de soupe contenant des carottes, des pommes de terre et des oignons, vous pouvez compter 3 plantes différentes. Si vous consommez du pain multicéréales, chaque céréale compte comme une plante.'
  WHERE survey_question_id = 146;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 146 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Moins de 5'
  WHERE survey_question_id = 146 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = '6 à 10'
  WHERE survey_question_id = 146 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = '11 à 20'
  WHERE survey_question_id = 146 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = '21 à 30'
  WHERE survey_question_id = 146 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Plus de 30'
  WHERE survey_question_id = 146 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Pays de résidence :'
  WHERE survey_question_id = 148;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 148 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Afghanistan'
  WHERE survey_question_id = 148 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Iles Aland'
  WHERE survey_question_id = 148 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Albanie'
  WHERE survey_question_id = 148 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Algérie'
  WHERE survey_question_id = 148 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Samoa américaines'
  WHERE survey_question_id = 148 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Andorre'
  WHERE survey_question_id = 148 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Angola'
  WHERE survey_question_id = 148 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = 'Anguilla'
  WHERE survey_question_id = 148 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = 'Antarctique'
  WHERE survey_question_id = 148 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET french = 'Antigua-et-Barbuda'
  WHERE survey_question_id = 148 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET french = 'Argentine'
  WHERE survey_question_id = 148 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET french = 'Arménie'
  WHERE survey_question_id = 148 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET french = 'Aruba'
  WHERE survey_question_id = 148 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET french = 'Australie'
  WHERE survey_question_id = 148 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET french = 'L''Autriche'
  WHERE survey_question_id = 148 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET french = 'Azerbaïdjan'
  WHERE survey_question_id = 148 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET french = 'Bahamas'
  WHERE survey_question_id = 148 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET french = 'Bahrein'
  WHERE survey_question_id = 148 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET french = 'Bangladesh'
  WHERE survey_question_id = 148 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET french = 'Barbade'
  WHERE survey_question_id = 148 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET french = 'Biélorussie'
  WHERE survey_question_id = 148 AND
        display_index = 21;
UPDATE ag.survey_question_response 
  SET french = 'Belgique'
  WHERE survey_question_id = 148 AND
        display_index = 22;
UPDATE ag.survey_question_response 
  SET french = 'Belize'
  WHERE survey_question_id = 148 AND
        display_index = 23;
UPDATE ag.survey_question_response 
  SET french = 'Bénin'
  WHERE survey_question_id = 148 AND
        display_index = 24;
UPDATE ag.survey_question_response 
  SET french = 'Bermudes'
  WHERE survey_question_id = 148 AND
        display_index = 25;
UPDATE ag.survey_question_response 
  SET french = 'Bhoutan'
  WHERE survey_question_id = 148 AND
        display_index = 26;
UPDATE ag.survey_question_response 
  SET french = 'Bolivie'
  WHERE survey_question_id = 148 AND
        display_index = 27;
UPDATE ag.survey_question_response 
  SET french = 'Bosnie Herzégovine'
  WHERE survey_question_id = 148 AND
        display_index = 28;
UPDATE ag.survey_question_response 
  SET french = 'Botswana'
  WHERE survey_question_id = 148 AND
        display_index = 29;
UPDATE ag.survey_question_response 
  SET french = 'Île Bouvet'
  WHERE survey_question_id = 148 AND
        display_index = 30;
UPDATE ag.survey_question_response 
  SET french = 'Brésil'
  WHERE survey_question_id = 148 AND
        display_index = 31;
UPDATE ag.survey_question_response 
  SET french = 'Territoire britannique de l''océan Indien'
  WHERE survey_question_id = 148 AND
        display_index = 32;
UPDATE ag.survey_question_response 
  SET french = 'Brunei Darussalam'
  WHERE survey_question_id = 148 AND
        display_index = 33;
UPDATE ag.survey_question_response 
  SET french = 'Bulgarie'
  WHERE survey_question_id = 148 AND
        display_index = 34;
UPDATE ag.survey_question_response 
  SET french = 'Burkina Faso'
  WHERE survey_question_id = 148 AND
        display_index = 35;
UPDATE ag.survey_question_response 
  SET french = 'Burundi'
  WHERE survey_question_id = 148 AND
        display_index = 36;
UPDATE ag.survey_question_response 
  SET french = 'Cambodge'
  WHERE survey_question_id = 148 AND
        display_index = 37;
UPDATE ag.survey_question_response 
  SET french = 'Cameroun'
  WHERE survey_question_id = 148 AND
        display_index = 38;
UPDATE ag.survey_question_response 
  SET french = 'Canada'
  WHERE survey_question_id = 148 AND
        display_index = 39;
UPDATE ag.survey_question_response 
  SET french = 'Cap-Vert'
  WHERE survey_question_id = 148 AND
        display_index = 40;
UPDATE ag.survey_question_response 
  SET french = 'Îles Caïmans'
  WHERE survey_question_id = 148 AND
        display_index = 41;
UPDATE ag.survey_question_response 
  SET french = 'République centrafricaine'
  WHERE survey_question_id = 148 AND
        display_index = 42;
UPDATE ag.survey_question_response 
  SET french = 'Tchad'
  WHERE survey_question_id = 148 AND
        display_index = 43;
UPDATE ag.survey_question_response 
  SET french = 'Chili'
  WHERE survey_question_id = 148 AND
        display_index = 44;
UPDATE ag.survey_question_response 
  SET french = 'Chine'
  WHERE survey_question_id = 148 AND
        display_index = 45;
UPDATE ag.survey_question_response 
  SET french = 'L''île de noël'
  WHERE survey_question_id = 148 AND
        display_index = 46;
UPDATE ag.survey_question_response 
  SET french = 'Îles Cocos (Keeling)'
  WHERE survey_question_id = 148 AND
        display_index = 47;
UPDATE ag.survey_question_response 
  SET french = 'Colombie'
  WHERE survey_question_id = 148 AND
        display_index = 48;
UPDATE ag.survey_question_response 
  SET french = 'Comores'
  WHERE survey_question_id = 148 AND
        display_index = 49;
UPDATE ag.survey_question_response 
  SET french = 'Congo'
  WHERE survey_question_id = 148 AND
        display_index = 50;
UPDATE ag.survey_question_response 
  SET french = 'Congo, République démocratique du'
  WHERE survey_question_id = 148 AND
        display_index = 51;
UPDATE ag.survey_question_response 
  SET french = 'les Îles Cook'
  WHERE survey_question_id = 148 AND
        display_index = 52;
UPDATE ag.survey_question_response 
  SET french = 'Costa Rica'
  WHERE survey_question_id = 148 AND
        display_index = 53;
UPDATE ag.survey_question_response 
  SET french = 'Côte d''Ivoire'
  WHERE survey_question_id = 148 AND
        display_index = 54;
UPDATE ag.survey_question_response 
  SET french = 'Croatie'
  WHERE survey_question_id = 148 AND
        display_index = 55;
UPDATE ag.survey_question_response 
  SET french = 'Cuba'
  WHERE survey_question_id = 148 AND
        display_index = 56;
UPDATE ag.survey_question_response 
  SET french = 'Chypre'
  WHERE survey_question_id = 148 AND
        display_index = 57;
UPDATE ag.survey_question_response 
  SET french = 'République Tchèque'
  WHERE survey_question_id = 148 AND
        display_index = 58;
UPDATE ag.survey_question_response 
  SET french = 'Danemark'
  WHERE survey_question_id = 148 AND
        display_index = 59;
UPDATE ag.survey_question_response 
  SET french = 'Djibouti'
  WHERE survey_question_id = 148 AND
        display_index = 60;
UPDATE ag.survey_question_response 
  SET french = 'Dominique'
  WHERE survey_question_id = 148 AND
        display_index = 61;
UPDATE ag.survey_question_response 
  SET french = 'République Dominicaine'
  WHERE survey_question_id = 148 AND
        display_index = 62;
UPDATE ag.survey_question_response 
  SET french = 'Équateur'
  WHERE survey_question_id = 148 AND
        display_index = 63;
UPDATE ag.survey_question_response 
  SET french = 'Egypte'
  WHERE survey_question_id = 148 AND
        display_index = 64;
UPDATE ag.survey_question_response 
  SET french = 'Le Salvador'
  WHERE survey_question_id = 148 AND
        display_index = 65;
UPDATE ag.survey_question_response 
  SET french = 'Guinée Équatoriale'
  WHERE survey_question_id = 148 AND
        display_index = 66;
UPDATE ag.survey_question_response 
  SET french = 'Érythrée'
  WHERE survey_question_id = 148 AND
        display_index = 67;
UPDATE ag.survey_question_response 
  SET french = 'Estonie'
  WHERE survey_question_id = 148 AND
        display_index = 68;
UPDATE ag.survey_question_response 
  SET french = 'Ethiopie'
  WHERE survey_question_id = 148 AND
        display_index = 69;
UPDATE ag.survey_question_response 
  SET french = 'Îles Falkland (Malvinas)'
  WHERE survey_question_id = 148 AND
        display_index = 70;
UPDATE ag.survey_question_response 
  SET french = 'Îles Féroé'
  WHERE survey_question_id = 148 AND
        display_index = 71;
UPDATE ag.survey_question_response 
  SET french = 'Fidji'
  WHERE survey_question_id = 148 AND
        display_index = 72;
UPDATE ag.survey_question_response 
  SET french = 'Finlande'
  WHERE survey_question_id = 148 AND
        display_index = 73;
UPDATE ag.survey_question_response 
  SET french = 'France'
  WHERE survey_question_id = 148 AND
        display_index = 74;
UPDATE ag.survey_question_response 
  SET french = 'Guyane Française'
  WHERE survey_question_id = 148 AND
        display_index = 75;
UPDATE ag.survey_question_response 
  SET french = 'Polynésie française'
  WHERE survey_question_id = 148 AND
        display_index = 76;
UPDATE ag.survey_question_response 
  SET french = 'Territoires français du Sud'
  WHERE survey_question_id = 148 AND
        display_index = 77;
UPDATE ag.survey_question_response 
  SET french = 'Gabon'
  WHERE survey_question_id = 148 AND
        display_index = 78;
UPDATE ag.survey_question_response 
  SET french = 'Gambie'
  WHERE survey_question_id = 148 AND
        display_index = 79;
UPDATE ag.survey_question_response 
  SET french = 'Géorgie'
  WHERE survey_question_id = 148 AND
        display_index = 80;
UPDATE ag.survey_question_response 
  SET french = 'Allemagne'
  WHERE survey_question_id = 148 AND
        display_index = 81;
UPDATE ag.survey_question_response 
  SET french = 'Ghana'
  WHERE survey_question_id = 148 AND
        display_index = 82;
UPDATE ag.survey_question_response 
  SET french = 'Gibraltar'
  WHERE survey_question_id = 148 AND
        display_index = 83;
UPDATE ag.survey_question_response 
  SET french = 'Grèce'
  WHERE survey_question_id = 148 AND
        display_index = 84;
UPDATE ag.survey_question_response 
  SET french = 'Groenland'
  WHERE survey_question_id = 148 AND
        display_index = 85;
UPDATE ag.survey_question_response 
  SET french = 'Grenade'
  WHERE survey_question_id = 148 AND
        display_index = 86;
UPDATE ag.survey_question_response 
  SET french = 'Guadeloupe'
  WHERE survey_question_id = 148 AND
        display_index = 87;
UPDATE ag.survey_question_response 
  SET french = 'Guam'
  WHERE survey_question_id = 148 AND
        display_index = 88;
UPDATE ag.survey_question_response 
  SET french = 'Guatemala'
  WHERE survey_question_id = 148 AND
        display_index = 89;
UPDATE ag.survey_question_response 
  SET french = 'Guernesey'
  WHERE survey_question_id = 148 AND
        display_index = 90;
UPDATE ag.survey_question_response 
  SET french = 'Guinée'
  WHERE survey_question_id = 148 AND
        display_index = 91;
UPDATE ag.survey_question_response 
  SET french = 'Guinée-bissau'
  WHERE survey_question_id = 148 AND
        display_index = 92;
UPDATE ag.survey_question_response 
  SET french = 'Guyane'
  WHERE survey_question_id = 148 AND
        display_index = 93;
UPDATE ag.survey_question_response 
  SET french = 'Haïti'
  WHERE survey_question_id = 148 AND
        display_index = 94;
UPDATE ag.survey_question_response 
  SET french = 'Îles Heard et Mcdonald'
  WHERE survey_question_id = 148 AND
        display_index = 95;
UPDATE ag.survey_question_response 
  SET french = 'Saint-Siège (État de la Cité du Vatican)'
  WHERE survey_question_id = 148 AND
        display_index = 96;
UPDATE ag.survey_question_response 
  SET french = 'Honduras'
  WHERE survey_question_id = 148 AND
        display_index = 97;
UPDATE ag.survey_question_response 
  SET french = 'Hong Kong'
  WHERE survey_question_id = 148 AND
        display_index = 98;
UPDATE ag.survey_question_response 
  SET french = 'Hongrie'
  WHERE survey_question_id = 148 AND
        display_index = 99;
UPDATE ag.survey_question_response 
  SET french = 'Islande'
  WHERE survey_question_id = 148 AND
        display_index = 100;
UPDATE ag.survey_question_response 
  SET french = 'Inde'
  WHERE survey_question_id = 148 AND
        display_index = 101;
UPDATE ag.survey_question_response 
  SET french = 'Indonésie'
  WHERE survey_question_id = 148 AND
        display_index = 102;
UPDATE ag.survey_question_response 
  SET french = 'Iran (République islamique d'
  WHERE survey_question_id = 148 AND
        display_index = 103;
UPDATE ag.survey_question_response 
  SET french = 'Irak'
  WHERE survey_question_id = 148 AND
        display_index = 104;
UPDATE ag.survey_question_response 
  SET french = 'Irlande'
  WHERE survey_question_id = 148 AND
        display_index = 105;
UPDATE ag.survey_question_response 
  SET french = 'île de Man'
  WHERE survey_question_id = 148 AND
        display_index = 106;
UPDATE ag.survey_question_response 
  SET french = 'Israël'
  WHERE survey_question_id = 148 AND
        display_index = 107;
UPDATE ag.survey_question_response 
  SET french = 'Italie'
  WHERE survey_question_id = 148 AND
        display_index = 108;
UPDATE ag.survey_question_response 
  SET french = 'Jamaïque'
  WHERE survey_question_id = 148 AND
        display_index = 109;
UPDATE ag.survey_question_response 
  SET french = 'Japon'
  WHERE survey_question_id = 148 AND
        display_index = 110;
UPDATE ag.survey_question_response 
  SET french = 'Jersey'
  WHERE survey_question_id = 148 AND
        display_index = 111;
UPDATE ag.survey_question_response 
  SET french = 'Jordan'
  WHERE survey_question_id = 148 AND
        display_index = 112;
UPDATE ag.survey_question_response 
  SET french = 'Kazakhstan'
  WHERE survey_question_id = 148 AND
        display_index = 113;
UPDATE ag.survey_question_response 
  SET french = 'Kenya'
  WHERE survey_question_id = 148 AND
        display_index = 114;
UPDATE ag.survey_question_response 
  SET french = 'Kiribati'
  WHERE survey_question_id = 148 AND
        display_index = 115;
UPDATE ag.survey_question_response 
  SET french = 'République populaire démocratique de Corée'
  WHERE survey_question_id = 148 AND
        display_index = 116;
UPDATE ag.survey_question_response 
  SET french = 'Corée, République de'
  WHERE survey_question_id = 148 AND
        display_index = 117;
UPDATE ag.survey_question_response 
  SET french = 'Koweit'
  WHERE survey_question_id = 148 AND
        display_index = 118;
UPDATE ag.survey_question_response 
  SET french = 'Kirghizistan'
  WHERE survey_question_id = 148 AND
        display_index = 119;
UPDATE ag.survey_question_response 
  SET french = 'République démocratique populaire lao'
  WHERE survey_question_id = 148 AND
        display_index = 120;
UPDATE ag.survey_question_response 
  SET french = 'Lettonie'
  WHERE survey_question_id = 148 AND
        display_index = 121;
UPDATE ag.survey_question_response 
  SET french = 'Liban'
  WHERE survey_question_id = 148 AND
        display_index = 122;
UPDATE ag.survey_question_response 
  SET french = 'Lesotho'
  WHERE survey_question_id = 148 AND
        display_index = 123;
UPDATE ag.survey_question_response 
  SET french = 'Libéria'
  WHERE survey_question_id = 148 AND
        display_index = 124;
UPDATE ag.survey_question_response 
  SET french = 'Jamahiriya arabe libyenne'
  WHERE survey_question_id = 148 AND
        display_index = 125;
UPDATE ag.survey_question_response 
  SET french = 'Liechtenstein'
  WHERE survey_question_id = 148 AND
        display_index = 126;
UPDATE ag.survey_question_response 
  SET french = 'Lituanie'
  WHERE survey_question_id = 148 AND
        display_index = 127;
UPDATE ag.survey_question_response 
  SET french = 'Luxembourg'
  WHERE survey_question_id = 148 AND
        display_index = 128;
UPDATE ag.survey_question_response 
  SET french = 'Macao'
  WHERE survey_question_id = 148 AND
        display_index = 129;
UPDATE ag.survey_question_response 
  SET french = 'Macédoine, ancienne République yougoslave de'
  WHERE survey_question_id = 148 AND
        display_index = 130;
UPDATE ag.survey_question_response 
  SET french = 'Madagascar'
  WHERE survey_question_id = 148 AND
        display_index = 131;
UPDATE ag.survey_question_response 
  SET french = 'Malawi'
  WHERE survey_question_id = 148 AND
        display_index = 132;
UPDATE ag.survey_question_response 
  SET french = 'Malaisie'
  WHERE survey_question_id = 148 AND
        display_index = 133;
UPDATE ag.survey_question_response 
  SET french = 'Maldives'
  WHERE survey_question_id = 148 AND
        display_index = 134;
UPDATE ag.survey_question_response 
  SET french = 'Mali'
  WHERE survey_question_id = 148 AND
        display_index = 135;
UPDATE ag.survey_question_response 
  SET french = 'Malte'
  WHERE survey_question_id = 148 AND
        display_index = 136;
UPDATE ag.survey_question_response 
  SET french = 'Iles Marshall'
  WHERE survey_question_id = 148 AND
        display_index = 137;
UPDATE ag.survey_question_response 
  SET french = 'Martinique'
  WHERE survey_question_id = 148 AND
        display_index = 138;
UPDATE ag.survey_question_response 
  SET french = 'Mauritanie'
  WHERE survey_question_id = 148 AND
        display_index = 139;
UPDATE ag.survey_question_response 
  SET french = 'Maurice'
  WHERE survey_question_id = 148 AND
        display_index = 140;
UPDATE ag.survey_question_response 
  SET french = 'Mayotte'
  WHERE survey_question_id = 148 AND
        display_index = 141;
UPDATE ag.survey_question_response 
  SET french = 'Mexique'
  WHERE survey_question_id = 148 AND
        display_index = 142;
UPDATE ag.survey_question_response 
  SET french = 'Micronésie, États fédérés de'
  WHERE survey_question_id = 148 AND
        display_index = 143;
UPDATE ag.survey_question_response 
  SET french = 'Moldova, République de'
  WHERE survey_question_id = 148 AND
        display_index = 144;
UPDATE ag.survey_question_response 
  SET french = 'Monaco'
  WHERE survey_question_id = 148 AND
        display_index = 145;
UPDATE ag.survey_question_response 
  SET french = 'Mongolie'
  WHERE survey_question_id = 148 AND
        display_index = 146;
UPDATE ag.survey_question_response 
  SET french = 'Monténégro'
  WHERE survey_question_id = 148 AND
        display_index = 147;
UPDATE ag.survey_question_response 
  SET french = 'Montserrat'
  WHERE survey_question_id = 148 AND
        display_index = 148;
UPDATE ag.survey_question_response 
  SET french = 'Maroc'
  WHERE survey_question_id = 148 AND
        display_index = 149;
UPDATE ag.survey_question_response 
  SET french = 'Mozambique'
  WHERE survey_question_id = 148 AND
        display_index = 150;
UPDATE ag.survey_question_response 
  SET french = 'Myanmar'
  WHERE survey_question_id = 148 AND
        display_index = 151;
UPDATE ag.survey_question_response 
  SET french = 'Namibie'
  WHERE survey_question_id = 148 AND
        display_index = 152;
UPDATE ag.survey_question_response 
  SET french = 'Nauru'
  WHERE survey_question_id = 148 AND
        display_index = 153;
UPDATE ag.survey_question_response 
  SET french = 'Népal'
  WHERE survey_question_id = 148 AND
        display_index = 154;
UPDATE ag.survey_question_response 
  SET french = 'Pays-Bas'
  WHERE survey_question_id = 148 AND
        display_index = 155;
UPDATE ag.survey_question_response 
  SET french = 'Antilles néerlandaises'
  WHERE survey_question_id = 148 AND
        display_index = 156;
UPDATE ag.survey_question_response 
  SET french = 'Nouvelle Calédonie'
  WHERE survey_question_id = 148 AND
        display_index = 157;
UPDATE ag.survey_question_response 
  SET french = 'Nouvelle-Zélande'
  WHERE survey_question_id = 148 AND
        display_index = 158;
UPDATE ag.survey_question_response 
  SET french = 'Nicaragua'
  WHERE survey_question_id = 148 AND
        display_index = 159;
UPDATE ag.survey_question_response 
  SET french = 'Niger'
  WHERE survey_question_id = 148 AND
        display_index = 160;
UPDATE ag.survey_question_response 
  SET french = 'Nigeria'
  WHERE survey_question_id = 148 AND
        display_index = 161;
UPDATE ag.survey_question_response 
  SET french = 'Niue'
  WHERE survey_question_id = 148 AND
        display_index = 162;
UPDATE ag.survey_question_response 
  SET french = 'l''ile de Norfolk'
  WHERE survey_question_id = 148 AND
        display_index = 163;
UPDATE ag.survey_question_response 
  SET french = 'Îles Mariannes du Nord'
  WHERE survey_question_id = 148 AND
        display_index = 164;
UPDATE ag.survey_question_response 
  SET french = 'Norvège'
  WHERE survey_question_id = 148 AND
        display_index = 165;
UPDATE ag.survey_question_response 
  SET french = 'Oman'
  WHERE survey_question_id = 148 AND
        display_index = 166;
UPDATE ag.survey_question_response 
  SET french = 'Pakistan'
  WHERE survey_question_id = 148 AND
        display_index = 167;
UPDATE ag.survey_question_response 
  SET french = 'Palau'
  WHERE survey_question_id = 148 AND
        display_index = 168;
UPDATE ag.survey_question_response 
  SET french = 'Territoire palestinien, occupé'
  WHERE survey_question_id = 148 AND
        display_index = 169;
UPDATE ag.survey_question_response 
  SET french = 'Panama'
  WHERE survey_question_id = 148 AND
        display_index = 170;
UPDATE ag.survey_question_response 
  SET french = 'Papouasie Nouvelle Guinée'
  WHERE survey_question_id = 148 AND
        display_index = 171;
UPDATE ag.survey_question_response 
  SET french = 'Paraguay'
  WHERE survey_question_id = 148 AND
        display_index = 172;
UPDATE ag.survey_question_response 
  SET french = 'Pérou'
  WHERE survey_question_id = 148 AND
        display_index = 173;
UPDATE ag.survey_question_response 
  SET french = 'Philippines'
  WHERE survey_question_id = 148 AND
        display_index = 174;
UPDATE ag.survey_question_response 
  SET french = 'Pitcairn'
  WHERE survey_question_id = 148 AND
        display_index = 175;
UPDATE ag.survey_question_response 
  SET french = 'Pologne'
  WHERE survey_question_id = 148 AND
        display_index = 176;
UPDATE ag.survey_question_response 
  SET french = 'le Portugal'
  WHERE survey_question_id = 148 AND
        display_index = 177;
UPDATE ag.survey_question_response 
  SET french = 'Porto Rico'
  WHERE survey_question_id = 148 AND
        display_index = 178;
UPDATE ag.survey_question_response 
  SET french = 'Qatar'
  WHERE survey_question_id = 148 AND
        display_index = 179;
UPDATE ag.survey_question_response 
  SET french = 'Réunion'
  WHERE survey_question_id = 148 AND
        display_index = 180;
UPDATE ag.survey_question_response 
  SET french = 'Roumanie'
  WHERE survey_question_id = 148 AND
        display_index = 181;
UPDATE ag.survey_question_response 
  SET french = 'Fédération Russe'
  WHERE survey_question_id = 148 AND
        display_index = 182;
UPDATE ag.survey_question_response 
  SET french = 'Rwanda'
  WHERE survey_question_id = 148 AND
        display_index = 183;
UPDATE ag.survey_question_response 
  SET french = 'Sainte-Hélène'
  WHERE survey_question_id = 148 AND
        display_index = 184;
UPDATE ag.survey_question_response 
  SET french = 'Saint-Christophe-et-Niévès'
  WHERE survey_question_id = 148 AND
        display_index = 185;
UPDATE ag.survey_question_response 
  SET french = 'Sainte-Lucie'
  WHERE survey_question_id = 148 AND
        display_index = 186;
UPDATE ag.survey_question_response 
  SET french = 'Saint-Pierre-et-Miquelon'
  WHERE survey_question_id = 148 AND
        display_index = 187;
UPDATE ag.survey_question_response 
  SET french = 'Saint-Vincent-et-les-Grenadines'
  WHERE survey_question_id = 148 AND
        display_index = 188;
UPDATE ag.survey_question_response 
  SET french = 'Samoa'
  WHERE survey_question_id = 148 AND
        display_index = 189;
UPDATE ag.survey_question_response 
  SET french = 'Saint Marin'
  WHERE survey_question_id = 148 AND
        display_index = 190;
UPDATE ag.survey_question_response 
  SET french = 'Sao Tomé et Principe'
  WHERE survey_question_id = 148 AND
        display_index = 191;
UPDATE ag.survey_question_response 
  SET french = 'Arabie Saoudite'
  WHERE survey_question_id = 148 AND
        display_index = 192;
UPDATE ag.survey_question_response 
  SET french = 'Sénégal'
  WHERE survey_question_id = 148 AND
        display_index = 193;
UPDATE ag.survey_question_response 
  SET french = 'Serbie'
  WHERE survey_question_id = 148 AND
        display_index = 194;
UPDATE ag.survey_question_response 
  SET french = 'les Seychelles'
  WHERE survey_question_id = 148 AND
        display_index = 195;
UPDATE ag.survey_question_response 
  SET french = 'Sierra Leone'
  WHERE survey_question_id = 148 AND
        display_index = 196;
UPDATE ag.survey_question_response 
  SET french = 'Singapour'
  WHERE survey_question_id = 148 AND
        display_index = 197;
UPDATE ag.survey_question_response 
  SET french = 'Slovaquie'
  WHERE survey_question_id = 148 AND
        display_index = 198;
UPDATE ag.survey_question_response 
  SET french = 'Slovénie'
  WHERE survey_question_id = 148 AND
        display_index = 199;
UPDATE ag.survey_question_response 
  SET french = 'Les îles Salomon'
  WHERE survey_question_id = 148 AND
        display_index = 200;
UPDATE ag.survey_question_response 
  SET french = 'Somalie'
  WHERE survey_question_id = 148 AND
        display_index = 201;
UPDATE ag.survey_question_response 
  SET french = 'Afrique du Sud'
  WHERE survey_question_id = 148 AND
        display_index = 202;
UPDATE ag.survey_question_response 
  SET french = 'Géorgie du Sud et les îles Sandwich du Sud'
  WHERE survey_question_id = 148 AND
        display_index = 203;
UPDATE ag.survey_question_response 
  SET french = 'Espagne'
  WHERE survey_question_id = 148 AND
        display_index = 204;
UPDATE ag.survey_question_response 
  SET french = 'Sri Lanka'
  WHERE survey_question_id = 148 AND
        display_index = 205;
UPDATE ag.survey_question_response 
  SET french = 'Soudan'
  WHERE survey_question_id = 148 AND
        display_index = 206;
UPDATE ag.survey_question_response 
  SET french = 'Suriname'
  WHERE survey_question_id = 148 AND
        display_index = 207;
UPDATE ag.survey_question_response 
  SET french = 'Svalbard et Jan Mayen'
  WHERE survey_question_id = 148 AND
        display_index = 208;
UPDATE ag.survey_question_response 
  SET french = 'Swaziland'
  WHERE survey_question_id = 148 AND
        display_index = 209;
UPDATE ag.survey_question_response 
  SET french = 'Suède'
  WHERE survey_question_id = 148 AND
        display_index = 210;
UPDATE ag.survey_question_response 
  SET french = 'Suisse'
  WHERE survey_question_id = 148 AND
        display_index = 211;
UPDATE ag.survey_question_response 
  SET french = 'République arabe syrienne'
  WHERE survey_question_id = 148 AND
        display_index = 212;
UPDATE ag.survey_question_response 
  SET french = 'Taiwan, Province de Chine'
  WHERE survey_question_id = 148 AND
        display_index = 213;
UPDATE ag.survey_question_response 
  SET french = 'Tadjikistan'
  WHERE survey_question_id = 148 AND
        display_index = 214;
UPDATE ag.survey_question_response 
  SET french = 'Tanzanie, République-Unie de'
  WHERE survey_question_id = 148 AND
        display_index = 215;
UPDATE ag.survey_question_response 
  SET french = 'Thaïlande'
  WHERE survey_question_id = 148 AND
        display_index = 216;
UPDATE ag.survey_question_response 
  SET french = 'Timor-leste'
  WHERE survey_question_id = 148 AND
        display_index = 217;
UPDATE ag.survey_question_response 
  SET french = 'Aller'
  WHERE survey_question_id = 148 AND
        display_index = 218;
UPDATE ag.survey_question_response 
  SET french = 'Tokelau'
  WHERE survey_question_id = 148 AND
        display_index = 219;
UPDATE ag.survey_question_response 
  SET french = 'Tonga'
  WHERE survey_question_id = 148 AND
        display_index = 220;
UPDATE ag.survey_question_response 
  SET french = 'Trinité-et-Tobago'
  WHERE survey_question_id = 148 AND
        display_index = 221;
UPDATE ag.survey_question_response 
  SET french = 'Tunisie'
  WHERE survey_question_id = 148 AND
        display_index = 222;
UPDATE ag.survey_question_response 
  SET french = 'Turquie'
  WHERE survey_question_id = 148 AND
        display_index = 223;
UPDATE ag.survey_question_response 
  SET french = 'Turkménistan'
  WHERE survey_question_id = 148 AND
        display_index = 224;
UPDATE ag.survey_question_response 
  SET french = 'îles Turques-et-Caïques'
  WHERE survey_question_id = 148 AND
        display_index = 225;
UPDATE ag.survey_question_response 
  SET french = 'Tuvalu'
  WHERE survey_question_id = 148 AND
        display_index = 226;
UPDATE ag.survey_question_response 
  SET french = 'Ouganda'
  WHERE survey_question_id = 148 AND
        display_index = 227;
UPDATE ag.survey_question_response 
  SET french = 'Ukraine'
  WHERE survey_question_id = 148 AND
        display_index = 228;
UPDATE ag.survey_question_response 
  SET french = 'Emirats Arabes Unis'
  WHERE survey_question_id = 148 AND
        display_index = 229;
UPDATE ag.survey_question_response 
  SET french = 'Royaume-Uni'
  WHERE survey_question_id = 148 AND
        display_index = 230;
UPDATE ag.survey_question_response 
  SET french = 'États Unis'
  WHERE survey_question_id = 148 AND
        display_index = 231;
UPDATE ag.survey_question_response 
  SET french = 'Îles mineures éloignées des États-Unis'
  WHERE survey_question_id = 148 AND
        display_index = 232;
UPDATE ag.survey_question_response 
  SET french = 'Uruguay'
  WHERE survey_question_id = 148 AND
        display_index = 233;
UPDATE ag.survey_question_response 
  SET french = 'Ouzbékistan'
  WHERE survey_question_id = 148 AND
        display_index = 234;
UPDATE ag.survey_question_response 
  SET french = 'Vanuatu'
  WHERE survey_question_id = 148 AND
        display_index = 235;
UPDATE ag.survey_question_response 
  SET french = 'Venezuela'
  WHERE survey_question_id = 148 AND
        display_index = 236;
UPDATE ag.survey_question_response 
  SET french = 'Viet Nam'
  WHERE survey_question_id = 148 AND
        display_index = 237;
UPDATE ag.survey_question_response 
  SET french = 'Îles Vierges britanniques'
  WHERE survey_question_id = 148 AND
        display_index = 238;
UPDATE ag.survey_question_response 
  SET french = 'Îles Vierges américaines'
  WHERE survey_question_id = 148 AND
        display_index = 239;
UPDATE ag.survey_question_response 
  SET french = 'Wallis et Futuna'
  WHERE survey_question_id = 148 AND
        display_index = 240;
UPDATE ag.survey_question_response 
  SET french = 'Sahara occidental'
  WHERE survey_question_id = 148 AND
        display_index = 241;
UPDATE ag.survey_question_response 
  SET french = 'Yémen'
  WHERE survey_question_id = 148 AND
        display_index = 242;
UPDATE ag.survey_question_response 
  SET french = 'Zambie'
  WHERE survey_question_id = 148 AND
        display_index = 243;
UPDATE ag.survey_question_response 
  SET french = 'Zimbabwe'
  WHERE survey_question_id = 148 AND
        display_index = 244;

UPDATE ag.survey_question SET french = 'Avez-vous d’autres animaux de compagnie ?'
  WHERE survey_question_id = 149;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 149 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 149 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 149 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Quand avez-vous emménagé dans votre lieu de résidence actuel ?'
  WHERE survey_question_id = 15;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 15 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Au cours du mois dernier'
  WHERE survey_question_id = 15 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Au cours des 3 derniers mois'
  WHERE survey_question_id = 15 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Au cours des 6 derniers mois'
  WHERE survey_question_id = 15 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Au cours de l’année dernière'
  WHERE survey_question_id = 15 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Je vis dans mon lieu de résidence actuel depuis plus d’un an.'
  WHERE survey_question_id = 15 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Veuillez dresser la liste de vos animaux de compagnie'
  WHERE survey_question_id = 150;

UPDATE ag.survey_question SET french = 'Une maladie mentale vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 153;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 153 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 153 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 153 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Veuillez sélectionner le ou les troubles sur la liste ci-dessous :'
  WHERE survey_question_id = 154;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 154 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Dépression'
  WHERE survey_question_id = 154 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Trouble bipolaire'
  WHERE survey_question_id = 154 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'ESPT (état de stress post-traumatique)'
  WHERE survey_question_id = 154 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Schizophrénie'
  WHERE survey_question_id = 154 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Anorexie mentale'
  WHERE survey_question_id = 154 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Boulimie'
  WHERE survey_question_id = 154 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Toxicomanie'
  WHERE survey_question_id = 154 AND
        display_index = 7;

UPDATE ag.survey_question SET french = 'Quel type de diabète ?'
  WHERE survey_question_id = 155;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 155 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Diabète de type I'
  WHERE survey_question_id = 155 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diabète de type II'
  WHERE survey_question_id = 155 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diabète gestationnel'
  WHERE survey_question_id = 155 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Avez-vous des rêves intenses et/ou effrayants ?'
  WHERE survey_question_id = 156;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 156 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 156 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 156 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 156 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 156 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 156 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Consommez-vous des boissons diététiques contenant des édulcorants ?'
  WHERE survey_question_id = 157;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 157 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 157 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 157 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 157 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 157 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 157 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Un cancer vous a-t-il été diagnostiqué ?'
  WHERE survey_question_id = 158;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 158 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 158 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 158 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un thérapeute de médecine alternative'
  WHERE survey_question_id = 158 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiqué'
  WHERE survey_question_id = 158 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Si un cancer vous a été diagnostiqué, comment a-t-il été traité ?'
  WHERE survey_question_id = 159;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 159 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Aucun traitement'
  WHERE survey_question_id = 159 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Par chirurgie uniquement'
  WHERE survey_question_id = 159 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Par chimiothérapie'
  WHERE survey_question_id = 159 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Par radiothérapie'
  WHERE survey_question_id = 159 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'J’ai voyagé hors de mon pays de résidence au cours _________.'
  WHERE survey_question_id = 16;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 16 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Du mois dernier'
  WHERE survey_question_id = 16 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Des 3 derniers mois'
  WHERE survey_question_id = 16 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Des 6 derniers mois'
  WHERE survey_question_id = 16 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'De l’année dernière'
  WHERE survey_question_id = 16 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas voyagé hors de mon pays de résidence au cours de l’année dernière.'
  WHERE survey_question_id = 16 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Un reflux acide ou un reflux gastro-œsophagien (RGO) vous a-t-il été diagnostiqué ?'
  WHERE survey_question_id = 160;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 160 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 160 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 160 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un thérapeute de médecine alternative'
  WHERE survey_question_id = 160 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiqué'
  WHERE survey_question_id = 160 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Quel type de MICI ?'
  WHERE survey_question_id = 161;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 161 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Rectocolite hémorragique'
  WHERE survey_question_id = 161 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Maladie de Crohn'
  WHERE survey_question_id = 161 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Votre régime alimentaire est-il spécialisé ? (veuillez sélectionner toutes les réponses qui s’appliquent)'
  WHERE survey_question_id = 162;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 162 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Régime paléolithique ou primitif'
  WHERE survey_question_id = 162 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Régime paléolithique modifié'
  WHERE survey_question_id = 162 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Crudivore'
  WHERE survey_question_id = 162 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'FODMAP'
  WHERE survey_question_id = 162 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Weston-Price ou tout autre régime comprenant peu de céréales et d’aliments transformés'
  WHERE survey_question_id = 162 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Casher'
  WHERE survey_question_id = 162 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Halal'
  WHERE survey_question_id = 162 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = 'Pas de solanacées'
  WHERE survey_question_id = 162 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = 'Pas de produits laitiers'
  WHERE survey_question_id = 162 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET french = 'Pas de sucres raffinés'
  WHERE survey_question_id = 162 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET french = 'Autres restrictions non décrites ici'
  WHERE survey_question_id = 162 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET french = 'Mon régime alimentaire n’est pas spécialisé'
  WHERE survey_question_id = 162 AND
        display_index = 12;

UPDATE ag.survey_question SET french = 'Combien de boissons alcoolisées consommez-vous généralement lorsque vous buvez ?'
  WHERE survey_question_id = 163;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 163 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = '1'
  WHERE survey_question_id = 163 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = '1 à 2'
  WHERE survey_question_id = 163 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = '2 à 3'
  WHERE survey_question_id = 163 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = '3 à 4'
  WHERE survey_question_id = 163 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Plus de 4'
  WHERE survey_question_id = 163 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Je ne bois pas'
  WHERE survey_question_id = 163 AND
        display_index = 6;

UPDATE ag.survey_question SET french = 'Quel type de MICI avez-vous ?'
  WHERE survey_question_id = 164;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 164 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Maladie de Crohn iléale'
  WHERE survey_question_id = 164 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Maladie de Crohn colique'
  WHERE survey_question_id = 164 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Maladie de Crohn iléale et colique'
  WHERE survey_question_id = 164 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Rectocolite hémorragique'
  WHERE survey_question_id = 164 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Colite microscopique'
  WHERE survey_question_id = 164 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Avec combien de personnes ne faisant pas partie de votre famille partagez-vous votre logement ?'
  WHERE survey_question_id = 17;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 17 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Aucune'
  WHERE survey_question_id = 17 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Une'
  WHERE survey_question_id = 17 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Deux'
  WHERE survey_question_id = 17 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Trois'
  WHERE survey_question_id = 17 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Plus de trois'
  WHERE survey_question_id = 17 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'L’une des personnes avec qui vous partagez votre logement participe-t-elle à cette étude ?'
  WHERE survey_question_id = 18;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 18 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 18 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 18 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 18 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Avez-vous un lien de parenté ou vivez-vous avec l’un des autres participants de cette étude ?'
  WHERE survey_question_id = 19;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 19 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 19 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 19 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 19 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Prenez-vous des multivitamines chaque jour ?'
  WHERE survey_question_id = 2;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 2 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 2 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 2 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Avez-vous un ou plusieurs chiens ?'
  WHERE survey_question_id = 20;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 20 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 20 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 20 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Avez-vous un ou plusieurs chats ?'
  WHERE survey_question_id = 21;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 21 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 21 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 21 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Quelle est votre main dominante ?'
  WHERE survey_question_id = 22;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 22 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je suis droitier/droitière'
  WHERE survey_question_id = 22 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Je suis gaucher/gauchère'
  WHERE survey_question_id = 22 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je suis ambidextre'
  WHERE survey_question_id = 22 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Quel est votre niveau de scolarisation ?'
  WHERE survey_question_id = 23;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 23 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas terminé le lycée'
  WHERE survey_question_id = 23 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Lycée ou équivalent du baccalauréat'
  WHERE survey_question_id = 23 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Une partie d’un cursus universitaire ou technique post-bac'
  WHERE survey_question_id = 23 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'DEUG/BTS/DUT'
  WHERE survey_question_id = 23 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Licence ou équivalent'
  WHERE survey_question_id = 23 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Une partie d’un cursus de l’enseignement supérieur ou professionnel'
  WHERE survey_question_id = 23 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Diplôme de l’enseignement supérieur ou professionnel'
  WHERE survey_question_id = 23 AND
        display_index = 7;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence pratiquez-vous une activité physique ?'
  WHERE survey_question_id = 24;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 24 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 24 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 24 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 24 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 24 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 24 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Pratiquez-vous généralement une activité physique à l’intérieur ou à l’extérieur ?'
  WHERE survey_question_id = 25;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 25 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'À l’intérieur'
  WHERE survey_question_id = 25 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'À l’extérieur'
  WHERE survey_question_id = 25 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Les deux'
  WHERE survey_question_id = 25 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Cela dépend de la saison'
  WHERE survey_question_id = 25 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Aucune des réponses ci-dessus'
  WHERE survey_question_id = 25 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Vous rongez-vous les ongles ?'
  WHERE survey_question_id = 26;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 26 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 26 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 26 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence allez-vous à la piscine/au jacuzzi ?'
  WHERE survey_question_id = 27;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 27 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 27 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 27 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 27 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 27 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 27 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence fumez-vous des cigarettes ?'
  WHERE survey_question_id = 28;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 28 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 28 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 28 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 28 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 28 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 28 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence buvez-vous de l’alcool ?'
  WHERE survey_question_id = 29;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 29 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 29 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 29 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 29 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 29 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 29 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence prenez-vous un probiotique ?'
  WHERE survey_question_id = 3;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 3 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 3 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 3 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 3 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 3 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 3 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Quel(s) type(s) d’alcool consommez-vous généralement ? (veuillez sélectionner toutes les réponses qui s’appliquent)'
  WHERE survey_question_id = 30;

UPDATE ag.survey_question_response 
  SET french = 'Bière/cidre'
  WHERE survey_question_id = 30 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Bières amères'
  WHERE survey_question_id = 30 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Vin blanc'
  WHERE survey_question_id = 30 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Vin rouge'
  WHERE survey_question_id = 30 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Spiritueux/alcool fort'
  WHERE survey_question_id = 30 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 30 AND
        display_index = 999;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence vous brossez-vous les dents ?'
  WHERE survey_question_id = 31;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 31 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 31 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (moins d’une fois par jour)'
  WHERE survey_question_id = 31 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (1 à 2 fois par jour)'
  WHERE survey_question_id = 31 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Fréquemment (plus de 2 fois par jour)'
  WHERE survey_question_id = 31 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 31 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence utilisez-vous du fil dentaire ?'
  WHERE survey_question_id = 32;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 32 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 32 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 32 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 32 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 32 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 32 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence utilisez-vous des cosmétiques sur le visage ?'
  WHERE survey_question_id = 33;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 33 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 33 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 33 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 33 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 33 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 33 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Utilisez-vous du déodorant ou de l’antitranspirant (les antitranspirants contiennent généralement de l’aluminium) ?'
  WHERE survey_question_id = 34;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 34 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'J’utilise un déodorant'
  WHERE survey_question_id = 34 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'J’utilise un antitranspirant'
  WHERE survey_question_id = 34 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas, mais j’utilise une forme de déodorant/antitranspirant'
  WHERE survey_question_id = 34 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Je n’utilise pas de déodorant ou d’antitranspirant'
  WHERE survey_question_id = 34 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Environ combien d’heures dormez-vous la nuit en moyenne ?'
  WHERE survey_question_id = 35;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 35 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Moins de 5 heures'
  WHERE survey_question_id = 35 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = '5 à 6 heures'
  WHERE survey_question_id = 35 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = '6 à 7 heures'
  WHERE survey_question_id = 35 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = '7 à 8 heures'
  WHERE survey_question_id = 35 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = '8 heures ou plus'
  WHERE survey_question_id = 35 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Utilisez-vous un adoucissant lorsque vous faites la lessive ?'
  WHERE survey_question_id = 36;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 36 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 36 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 36 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Environ combien de fois allez-vous à la selle chaque jour ?'
  WHERE survey_question_id = 37;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 37 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Mois d’une fois'
  WHERE survey_question_id = 37 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Une fois'
  WHERE survey_question_id = 37 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Deux fois'
  WHERE survey_question_id = 37 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Trois fois'
  WHERE survey_question_id = 37 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Quatre fois'
  WHERE survey_question_id = 37 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Cinq fois ou plus'
  WHERE survey_question_id = 37 AND
        display_index = 6;

UPDATE ag.survey_question SET french = 'Veuillez décrire la qualité de vos selles. Vous pouvez utiliser le tableau ci-dessous comme référence:'
  WHERE survey_question_id = 38;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 38 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'J’ai tendance à être constipé(e) (j’ai du mal à aller à la selle) - Type 1 et 2'
  WHERE survey_question_id = 38 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'J’ai tendance à avoir la diarrhée (selles liquides) - Type 5, 6 et 7'
  WHERE survey_question_id = 38 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'J’ai tendance à avoir des selles de forme normale - Type 3 et 4'
  WHERE survey_question_id = 38 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas, je n’ai pas de point de référence.'
  WHERE survey_question_id = 38 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'J’ai pris des antibiotiques au cours ____________.'
  WHERE survey_question_id = 39;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 39 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'De la semaine dernière'
  WHERE survey_question_id = 39 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Du mois dernier'
  WHERE survey_question_id = 39 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Des 6 derniers mois'
  WHERE survey_question_id = 39 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'De l’année dernière'
  WHERE survey_question_id = 39 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas pris d’antibiotiques au cours de l’année dernière.'
  WHERE survey_question_id = 39 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence prenez-vous des vitamines du groupe B, des folates ou de l’acide folique ?'
  WHERE survey_question_id = 4;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 4 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 4 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 4 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 4 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 4 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 4 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'J’ai reçu un vaccin contre la grippe au cours ____________.'
  WHERE survey_question_id = 40;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 40 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'De la semaine dernière'
  WHERE survey_question_id = 40 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Du mois dernier'
  WHERE survey_question_id = 40 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Des 6 derniers mois'
  WHERE survey_question_id = 40 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'De l’année dernière'
  WHERE survey_question_id = 40 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas reçu de vaccin contre la grippe au cours de l’année dernière.'
  WHERE survey_question_id = 40 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Utilisez-vous une forme de contraception hormonale actuellement ?'
  WHERE survey_question_id = 41;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 41 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui, je prends la pilule'
  WHERE survey_question_id = 41 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Oui, j’utilise un contraceptif injectable (acétate de médroxyprogestérone)'
  WHERE survey_question_id = 41 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Oui, j’utilise un patch contraceptif (Evra)'
  WHERE survey_question_id = 41 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Oui, j’utilise NuvaRing'
  WHERE survey_question_id = 41 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Oui, j’utilise un dispositif intra-utérin (DIU) hormonal (Mirena)'
  WHERE survey_question_id = 41 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 41 AND
        display_index = 6;

UPDATE ag.survey_question SET french = 'Êtes-vous actuellement enceinte ?'
  WHERE survey_question_id = 42;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 42 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 42 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 42 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 42 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Au cours des 6 derniers mois, mon poids _________.'
  WHERE survey_question_id = 43;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 43 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'A augmenté de plus de 10 livres (5 kg)'
  WHERE survey_question_id = 43 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'A diminué de plus de 10 livres (5 kg)'
  WHERE survey_question_id = 43 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Est resté stable'
  WHERE survey_question_id = 43 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Les amygdales vous ont-elles été retirées ?'
  WHERE survey_question_id = 44;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 44 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 44 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 44 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 44 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'L’appendice vous a-t-elle été retirée ?'
  WHERE survey_question_id = 45;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 45 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 45 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 45 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 45 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Avez-vous eu la varicelle ?'
  WHERE survey_question_id = 46;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 46 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 46 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 46 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 46 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Prenez-vous actuellement des médicaments sur ordonnance contre l’acné du visage ?'
  WHERE survey_question_id = 47;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 47 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 47 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 47 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Utilisez-vous actuellement des produits en vente libre contre l’acné du visage ?'
  WHERE survey_question_id = 48;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 48 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 48 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 48 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Prenez-vous actuellement des médicaments sur ordonnance ou en vente libre pour d’autres maladies ?'
  WHERE survey_question_id = 49;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 49 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 49 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 49 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence prenez-vous un supplément de vitamine D ?'
  WHERE survey_question_id = 5;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 5 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 5 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 5 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 5 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 5 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 5 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Êtes-vous né(e) par césarienne ?'
  WHERE survey_question_id = 50;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 50 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 50 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 50 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 50 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Lorsque vous étiez bébé, quelle était votre alimentation ?'
  WHERE survey_question_id = 51;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 51 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Principalement du lait maternel'
  WHERE survey_question_id = 51 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Principalement des préparations pour nourrissons'
  WHERE survey_question_id = 51 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Un mélange de lait maternel et de préparations pour nourrissons'
  WHERE survey_question_id = 51 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Je ne sais pas'
  WHERE survey_question_id = 51 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Acceptez-vous d’être contacté(e) pour répondre à des questions supplémentaires concernant les maladies figurant ci-dessus ?'
  WHERE survey_question_id = 52;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 52 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 52 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 52 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Avez-vous des allergies saisonnières ?'
  WHERE survey_question_id = 53;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 53 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 53 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 53 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Êtes-vous allergique à l’un des autres éléments suivants (allergies non alimentaires) ? (veuillez sélectionner toutes les réponses qui s’appliquent)'
  WHERE survey_question_id = 54;

UPDATE ag.survey_question_response 
  SET french = 'Médicament (par exemple, pénicilline)'
  WHERE survey_question_id = 54 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Phanères animaux'
  WHERE survey_question_id = 54 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Piqûres d’abeilles'
  WHERE survey_question_id = 54 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Sumac vénéneux / sumac occidental'
  WHERE survey_question_id = 54 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Soleil'
  WHERE survey_question_id = 54 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 54 AND
        display_index = 999;

UPDATE ag.survey_question SET french = 'Êtes-vous un nourrisson recevant la majorité de son alimentation sous forme de lait maternel ou de préparation pour nourrissons ou un adulte recevant la majorité (plus de 75 % des calories quotidiennes) de son alimentation sous forme de substituts de repas pour adulte (par exemple, Ensure) ?'
  WHERE survey_question_id = 55;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 55 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 55 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 55 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je mange à la fois de la nourriture solide et du lait maternel / des préparations pour nourrissons'
  WHERE survey_question_id = 55 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous de la viande/des œufs ?'
  WHERE survey_question_id = 56;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 56 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 56 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 56 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 56 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 56 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 56 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence cuisinez-vous et consommez-vous des repas que vous avez préparés ? (Ne pas inclure les plats préparés tels que les pâtes préparées en boîte, les nouilles ramen, les plats surgelés.)'
  WHERE survey_question_id = 57;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 57 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 57 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 57 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 57 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 57 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 57 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous des plats préparés (c’est-à-dire des pâtes préparées en boîte, des nouilles ramen, des plats surgelés) ?'
  WHERE survey_question_id = 58;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 58 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 58 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 58 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 58 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 58 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 58 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous des plats préparés dans un restaurant, y compris des plats à emporter ?'
  WHERE survey_question_id = 59;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 59 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 59 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 59 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 59 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 59 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 59 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Prenez-vous un autre complément nutritionnel/à base de plantes ?'
  WHERE survey_question_id = 6;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 6 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 6 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 6 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Une maladie rénale vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 60;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 60 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 60 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 60 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 60 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 60 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous au moins 2 à 3 portions de fruits par jour ? (1 portion = 60 g de fruits ; 1 fruit de taille moyenne ; 120 ml de jus de fruits)'
  WHERE survey_question_id = 61;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 61 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 61 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 61 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 61 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 61 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 61 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous au moins 2 à 3 portions de légumes, y compris des pommes de terre, par jour ? (1 portion = 60 g de légumes/pommes de terre ; 120 g de légumes verts crus)'
  WHERE survey_question_id = 62;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 62 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 62 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 62 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 62 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 62 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 62 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous au moins une portion de légumes fermentés ou de produits à base de plante par jour ? (1 portion = 60 g de choucroute, kimchi ou légumes fermentés ou 120 g de kombucha)'
  WHERE survey_question_id = 63;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 63 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 63 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 63 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 63 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 63 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 63 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous au moins 2 portions de lait ou de formage par jour ? (1 portion = 240 ml de lait ou 60 g de yaourt ; 40 à 60 g de fromage)'
  WHERE survey_question_id = 64;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 64 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 64 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 64 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 64 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 64 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 64 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous des substituts de lait (lait de soja, lait sans lactose, lait d’amande, etc.) ?'
  WHERE survey_question_id = 65;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 65 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 65 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 65 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 65 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 65 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 65 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence mangez-vous des desserts surgelés (crème glacée/glace/milkshake, sorbets, yaourt glacé, etc.) ?'
  WHERE survey_question_id = 66;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 66 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 66 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 66 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 66 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 66 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 66 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous de la viande rouge ?'
  WHERE survey_question_id = 67;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 67 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 67 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 67 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 67 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 67 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 67 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous de la viande riche en graisses, telle que de la côte de bœuf, du steak, un hamburger, des côtes de porc, du lard, etc. ?'
  WHERE survey_question_id = 68;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 68 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 68 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 68 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 68 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 68 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 68 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous de la volaille (poulet, dinde, etc.) au moins une fois par jour ?'
  WHERE survey_question_id = 69;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 69 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 69 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 69 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 69 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 69 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 69 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Avez-vous une intolérance au lactose ?'
  WHERE survey_question_id = 7;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 7 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Oui'
  WHERE survey_question_id = 7 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 7 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous des produits de la mer (poisson, crevettes, homard, crabe, etc.) ?'
  WHERE survey_question_id = 70;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 70 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 70 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 70 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 70 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 70 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 70 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous des en-cas salés (chips, nachos, chips de maïs, popcorn au beurre, frites, etc.) ?'
  WHERE survey_question_id = 71;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 71 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 71 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 71 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 71 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 71 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 71 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous des sucreries (gâteaux, cookies, pâtisseries, beignets, muffins, chocolat, etc.) au moins une fois par jour ?'
  WHERE survey_question_id = 72;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 72 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 72 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 72 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 72 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 72 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 72 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, combien de jours cuisinez-vous avez de l’huile d’olive (y compris pour la sauce salade) ?'
  WHERE survey_question_id = 73;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 73 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 73 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 73 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 73 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 73 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 73 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous des œufs entiers (ne pas inclure les jaunes ou les blancs séparés) ?'
  WHERE survey_question_id = 74;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 74 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 74 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 74 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 74 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 74 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 74 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence buvez-vous au moins 500 ml de boisson sucrée, telle qu’un soda non édulcoré ou une boisson à base de fruit/du punch (ne pas inclure le jus 100 % fruit) par jour ? (1 cannette de soda = 350 ml)'
  WHERE survey_question_id = 75;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 75 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 75 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 75 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 75 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 75 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 75 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous au moins 1 litre d’eau par jour ?'
  WHERE survey_question_id = 76;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 76 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 76 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 76 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 76 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 76 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 76 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Un autisme ou un trouble du spectre autistique vous a-t-il été diagnostiqué ?'
  WHERE survey_question_id = 77;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 77 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 77 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 77 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un thérapeute de médecine alternative'
  WHERE survey_question_id = 77 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiqué(e)'
  WHERE survey_question_id = 77 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une prolifération bactérienne de l’intestin grêle (SIBO) vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 78;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 78 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 78 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 78 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 78 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 78 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Un syndrome de l’intestin irritable (SII) vous a-t-il été diagnostiqué ?'
  WHERE survey_question_id = 79;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 79 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 79 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 79 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un thérapeute de médecine alternative'
  WHERE survey_question_id = 79 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiqué'
  WHERE survey_question_id = 79 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Avez-vous une intolérance au gluten ?'
  WHERE survey_question_id = 8;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 8 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Une maladie cœliaque m’a été diagnostiquée'
  WHERE survey_question_id = 8 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Une allergie au gluten (IgG anti-gluten) m’a été diagnostiquée, mais pas de maladie cœliaque'
  WHERE survey_question_id = 8 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Je ne mange pas de gluten, sinon je ne me sens pas bien'
  WHERE survey_question_id = 8 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Non'
  WHERE survey_question_id = 8 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une infection à Clostridium difficile (C. diff) vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 80;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 80 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 80 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 80 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 80 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 80 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une autre maladie cliniquement significative vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 81;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 81 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 81 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 81 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 81 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 81 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Un diabète vous a-t-il été diagnostiqué ?'
  WHERE survey_question_id = 82;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 82 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 82 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 82 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un thérapeute de médecine alternative'
  WHERE survey_question_id = 82 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 82 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une maladie inflammatoire chronique de l’intestin (MICI) vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 83;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 83 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 83 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 83 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 83 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 83 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'La maladie d’Alzheimer/une démence vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 84;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 84 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 84 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 84 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 84 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 84 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Un trouble du déficit de l’attention avec hyperactivité vous a-t-il été diagnostiqué ?'
  WHERE survey_question_id = 85;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 85 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie.'
  WHERE survey_question_id = 85 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 85 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué par un thérapeute de médecine alternative'
  WHERE survey_question_id = 85 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiqué'
  WHERE survey_question_id = 85 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une maladie hépatique vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 86;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 86 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 86 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 86 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 86 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 86 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une maladie auto-immune, notamment un lupus (lupus érythémateux disséminé), une polyarthrite rhumatoïde (PR), une sclérose en plaques (SEP), une thyroïdite de Hashimoto ou autre vous a-t-elle été diagnostiquée ?'
  WHERE survey_question_id = 87;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 87 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 87 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 87 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 87 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 87 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une maladie cutanée vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 88;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 88 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 88 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 88 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 88 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 88 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une maladie coronarienne ou une maladie cardiaque vous a-t-elle déjà été diagnostiquée, ou avez-vous déjà eu une crise cardiaque et/ou un accident vasculaire cérébral ?'
  WHERE survey_question_id = 89;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 89 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 89 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 89 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un thérapeute de médecine alternative'
  WHERE survey_question_id = 89 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiqué(e)'
  WHERE survey_question_id = 89 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Je suis allergique à/aux __________ (veuillez sélectionner toutes les réponses qui s’appliquent)'
  WHERE survey_question_id = 9;

UPDATE ag.survey_question_response 
  SET french = 'Cacahuètes'
  WHERE survey_question_id = 9 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Noix'
  WHERE survey_question_id = 9 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Fruits de mer'
  WHERE survey_question_id = 9 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 9 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas d’allergies alimentaires à ma connaissance.'
  WHERE survey_question_id = 9 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 9 AND
        display_index = 999;

UPDATE ag.survey_question SET french = 'Une épilepsie ou un trouble épileptique vous a-t-il déjà été diagnostiqué ?'
  WHERE survey_question_id = 90;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 90 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 90 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 90 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un thérapeute de médecine alternative'
  WHERE survey_question_id = 90 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiqué(e)'
  WHERE survey_question_id = 90 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence mangez-vous au moins 2 portions de céréales complètes par jour ?'
  WHERE survey_question_id = 91;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 91 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 91 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (moins d’une fois/semaine)'
  WHERE survey_question_id = 91 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 91 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 91 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 91 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Des migraines vous ont-elles déjà été diagnostiquées ?'
  WHERE survey_question_id = 92;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 92 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 92 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquées par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 92 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquées par un thérapeute de médecine alternative'
  WHERE survey_question_id = 92 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquées'
  WHERE survey_question_id = 92 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Un asthme, une mucoviscidose ou une bronchopneumopathie chronique obstructive (BPCO) vous a-t-il déjà été diagnostiqué ?'
  WHERE survey_question_id = 93;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 93 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 93 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 93 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un thérapeute de médecine alternative'
  WHERE survey_question_id = 93 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiqué(e)'
  WHERE survey_question_id = 93 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une phénylcétonurie vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 94;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 94 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 94 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 94 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 94 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 94 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une candidose ou une prolifération fongique dans l’intestin vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 95;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 95 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 95 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 95 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 95 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 95 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Une maladie thyroïdienne vous a-t-elle déjà été diagnostiquée ?'
  WHERE survey_question_id = 96;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 96 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 96 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 96 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiquée par un thérapeute de médecine alternative'
  WHERE survey_question_id = 96 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiquée'
  WHERE survey_question_id = 96 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Vous a-t-on déjà diagnostiqué une dépression, un trouble bipolaire ou une schizophrénie ?'
  WHERE survey_question_id = 97;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 97 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas cette maladie'
  WHERE survey_question_id = 97 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un professionnel de santé (médecin, médecin assistant)'
  WHERE survey_question_id = 97 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Diagnostiqué(e) par un thérapeute de médecine alternative'
  WHERE survey_question_id = 97 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Auto-diagnostiqué(e)'
  WHERE survey_question_id = 97 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Date d’accouchement prévue :'
  WHERE survey_question_id = 98;

UPDATE ag.survey_question SET french = 'Médicament en vente libre et sur ordonnance :'
  WHERE survey_question_id = 99;

UPDATE ag.survey_question SET french = 'En moyenne par semaine, selon quelle fréquence consommez-vous au moins une portion de légumes fermentés ou de produits à base de plantes par jour ? (1 portion = 60 g de choucroute, kimchi ou légumes fermentés ou 120 g de kombucha)'
  WHERE survey_question_id = 165;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 165 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 165 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Rarement (quelques fois/mois)'
  WHERE survey_question_id = 165 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Occasionnellement (1 à 2 fois/semaine)'
  WHERE survey_question_id = 165 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement (3 à 5 fois/semaine)'
  WHERE survey_question_id = 165 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tous les jours'
  WHERE survey_question_id = 165 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Sans compter la bière, le vin et l’alcool, j’ai considérablement augmenté (c’est-à-dire plus que doublé) ma consommation de produits fermentés en termes de fréquence ou de quantité au cours ____.'
  WHERE survey_question_id = 166;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 166 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'De la semaine dernière'
  WHERE survey_question_id = 166 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Du mois dernier'
  WHERE survey_question_id = 166 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Des 6 derniers mois'
  WHERE survey_question_id = 166 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'De l’année dernière'
  WHERE survey_question_id = 166 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Je n’ai pas augmenté ma consommation'
  WHERE survey_question_id = 166 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Parmi les aliments/boissons fermenté(e)s suivant(e)s, lesquels consommez-vous plus d’une fois par semaine ? Veuillez sélectionner toutes les réponses qui s’appliquent.'
  WHERE survey_question_id = 167;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 167 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Kimchi'
  WHERE survey_question_id = 167 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Choucroute'
  WHERE survey_question_id = 167 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Haricots fermentés/miso/natto'
  WHERE survey_question_id = 167 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Légumes marinés'
  WHERE survey_question_id = 167 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tempeh'
  WHERE survey_question_id = 167 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Tofu fermenté'
  WHERE survey_question_id = 167 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Kéfir (eau)'
  WHERE survey_question_id = 167 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = 'Kéfir (lait)'
  WHERE survey_question_id = 167 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = 'Fromage frais'
  WHERE survey_question_id = 167 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET french = 'Yaourt/lassi'
  WHERE survey_question_id = 167 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET french = 'Crème fraîche'
  WHERE survey_question_id = 167 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET french = 'Poisson fermenté'
  WHERE survey_question_id = 167 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET french = 'Sauce au poisson'
  WHERE survey_question_id = 167 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET french = 'Pain fermenté/pain au levain/injera'
  WHERE survey_question_id = 167 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET french = 'Kombucha'
  WHERE survey_question_id = 167 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET french = 'Chicha'
  WHERE survey_question_id = 167 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET french = 'Bière'
  WHERE survey_question_id = 167 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET french = 'Cidre'
  WHERE survey_question_id = 167 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET french = 'Vin'
  WHERE survey_question_id = 167 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET french = 'Hydromel'
  WHERE survey_question_id = 167 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 167 AND
        display_index = 21;

UPDATE ag.survey_question SET french = 'Indiquez sous « Autre » tout aliment consommé ne figurant pas sur la liste'
  WHERE survey_question_id = 168;

UPDATE ag.survey_question SET french = 'Produisez-vous l’un des aliments/l’une des boissons fermenté(e)s chez vous pour votre consommation personnelle ? Veuillez sélectionner toutes les réponses qui s’appliquent.'
  WHERE survey_question_id = 169;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 169 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Kimchi'
  WHERE survey_question_id = 169 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Choucroute'
  WHERE survey_question_id = 169 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Haricots fermentés/miso/natto'
  WHERE survey_question_id = 169 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Légumes marinés'
  WHERE survey_question_id = 169 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tempeh'
  WHERE survey_question_id = 169 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Tofu fermenté'
  WHERE survey_question_id = 169 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Kéfir (eau)'
  WHERE survey_question_id = 169 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = 'Kéfir (lait)'
  WHERE survey_question_id = 169 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = 'Fromage frais'
  WHERE survey_question_id = 169 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET french = 'Yaourt/lassi'
  WHERE survey_question_id = 169 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET french = 'Crème fraîche'
  WHERE survey_question_id = 169 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET french = 'Poisson fermenté'
  WHERE survey_question_id = 169 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET french = 'Sauce au poisson'
  WHERE survey_question_id = 169 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET french = 'Pain fermenté/pain au levain/injera'
  WHERE survey_question_id = 169 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET french = 'Kombucha'
  WHERE survey_question_id = 169 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET french = 'Chicha'
  WHERE survey_question_id = 169 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET french = 'Bière'
  WHERE survey_question_id = 169 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET french = 'Cidre'
  WHERE survey_question_id = 169 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET french = 'Vin'
  WHERE survey_question_id = 169 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET french = 'Hydromel'
  WHERE survey_question_id = 169 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 169 AND
        display_index = 21;

UPDATE ag.survey_question SET french = 'Indiquez sous « Autre » tout aliment que vous fabriquez vous-même ne figurant pas dans la liste.'
  WHERE survey_question_id = 170;

UPDATE ag.survey_question SET french = 'Produisez-vous l’un des aliments/l’une des boissons fermenté(e)s à des fins commerciales ? Veuillez sélectionner toutes les réponses qui s’appliquent.'
  WHERE survey_question_id = 171;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 171 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Kimchi'
  WHERE survey_question_id = 171 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Choucroute'
  WHERE survey_question_id = 171 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Haricots fermentés/miso/natto'
  WHERE survey_question_id = 171 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Légumes marinés'
  WHERE survey_question_id = 171 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Tempeh'
  WHERE survey_question_id = 171 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Tofu fermenté'
  WHERE survey_question_id = 171 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Kéfir (eau)'
  WHERE survey_question_id = 171 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = 'Kéfir (lait)'
  WHERE survey_question_id = 171 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = 'Fromage frais'
  WHERE survey_question_id = 171 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET french = 'Yaourt/lassi'
  WHERE survey_question_id = 171 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET french = 'Crème fraîche'
  WHERE survey_question_id = 171 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET french = 'Poisson fermenté'
  WHERE survey_question_id = 171 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET french = 'Sauce au poisson'
  WHERE survey_question_id = 171 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET french = 'Pain fermenté/pain au levain/injera'
  WHERE survey_question_id = 171 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET french = 'Kombucha'
  WHERE survey_question_id = 171 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET french = 'Chicha'
  WHERE survey_question_id = 171 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET french = 'Bière'
  WHERE survey_question_id = 171 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET french = 'Cidre'
  WHERE survey_question_id = 171 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET french = 'Vin'
  WHERE survey_question_id = 171 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET french = 'Hydromel'
  WHERE survey_question_id = 171 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 171 AND
        display_index = 21;

UPDATE ag.survey_question SET french = 'Indiquez sous « Autre » tout aliment que vous fabriquez à des fins commerciales ne figurant pas dans la liste.'
  WHERE survey_question_id = 172;

UPDATE ag.survey_question SET french = 'Vous pouvez compléter les informations concernant cette activité.'
  WHERE survey_question_id = 173;

UPDATE ag.survey_question SET french = 'Nom'
  WHERE survey_question_id = 127;

UPDATE ag.survey_question SET french = 'Type d’animal'
  WHERE survey_question_id = 128;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 128 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Chien'
  WHERE survey_question_id = 128 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Chat'
  WHERE survey_question_id = 128 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Petit mammifère'
  WHERE survey_question_id = 128 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Grand mammifère'
  WHERE survey_question_id = 128 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Poisson'
  WHERE survey_question_id = 128 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Oiseau'
  WHERE survey_question_id = 128 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Reptile'
  WHERE survey_question_id = 128 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = 'Amphibien'
  WHERE survey_question_id = 128 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 128 AND
        display_index = 9;

UPDATE ag.survey_question SET french = 'Origine'
  WHERE survey_question_id = 129;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 129 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Élevage'
  WHERE survey_question_id = 129 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Refuge'
  WHERE survey_question_id = 129 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Foyer'
  WHERE survey_question_id = 129 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Sauvage'
  WHERE survey_question_id = 129 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Âge'
  WHERE survey_question_id = 130;

UPDATE ag.survey_question SET french = 'Sexe'
  WHERE survey_question_id = 131;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 131 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Mâle'
  WHERE survey_question_id = 131 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Femelle'
  WHERE survey_question_id = 131 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Contexte'
  WHERE survey_question_id = 132;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 132 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Urbain'
  WHERE survey_question_id = 132 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Périurbain'
  WHERE survey_question_id = 132 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Rural'
  WHERE survey_question_id = 132 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Catégorie pondérale'
  WHERE survey_question_id = 133;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 133 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'En insuffisance pondérale'
  WHERE survey_question_id = 133 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Maigre'
  WHERE survey_question_id = 133 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Normal'
  WHERE survey_question_id = 133 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Bien portant'
  WHERE survey_question_id = 133 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'En surpoids'
  WHERE survey_question_id = 133 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Classification du régime'
  WHERE survey_question_id = 134;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 134 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Carnivore'
  WHERE survey_question_id = 134 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Omnivore'
  WHERE survey_question_id = 134 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Herbivore'
  WHERE survey_question_id = 134 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Source d’alimentation'
  WHERE survey_question_id = 135;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 135 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Alimentation provenant d’une animalerie'
  WHERE survey_question_id = 135 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Alimentation préparée par l’homme'
  WHERE survey_question_id = 135 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Alimentation sauvage'
  WHERE survey_question_id = 135 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Type d’alimentation'
  WHERE survey_question_id = 136;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 136 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Sèche'
  WHERE survey_question_id = 136 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Humide'
  WHERE survey_question_id = 136 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Les deux'
  WHERE survey_question_id = 136 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Caractéristiques spécifiques de l’alimentation'
  WHERE survey_question_id = 137;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 137 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Bio'
  WHERE survey_question_id = 137 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Sans céréales'
  WHERE survey_question_id = 137 AND
        display_index = 2;

UPDATE ag.survey_question SET french = 'Conditions de vie'
  WHERE survey_question_id = 138;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 138 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Vit seul avec des humains'
  WHERE survey_question_id = 138 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Vit seul sans contact/avec un contact limité avec les humains (refuge)'
  WHERE survey_question_id = 138 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Vit avec d’autres animaux et des humains'
  WHERE survey_question_id = 138 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Vit avec d’autres animaux/contact limité avec les humains'
  WHERE survey_question_id = 138 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Temps passé à l’extérieur'
  WHERE survey_question_id = 139;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 139 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Aucun'
  WHERE survey_question_id = 139 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Mois de 2 heures'
  WHERE survey_question_id = 139 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = '2 à 4 heures'
  WHERE survey_question_id = 139 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = '4 à 8 heures'
  WHERE survey_question_id = 139 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Plus de 8 heures'
  WHERE survey_question_id = 139 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Accès à de l’eau des toilettes'
  WHERE survey_question_id = 140;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 140 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Régulièrement'
  WHERE survey_question_id = 140 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Parfois'
  WHERE survey_question_id = 140 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 140 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Coprophagie'
  WHERE survey_question_id = 141;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 141 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Importante'
  WHERE survey_question_id = 141 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Modérée'
  WHERE survey_question_id = 141 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Faible'
  WHERE survey_question_id = 141 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 141 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Veuillez indiquer toute autre information concernant cet animal que vous estimez susceptible d’avoir un impact sur ses micro-organismes.'
  WHERE survey_question_id = 142;

UPDATE ag.survey_question SET french = 'Veuillez indiquer le type d’animal.'
  WHERE survey_question_id = 143;

UPDATE ag.survey_question SET french = 'Veuillez indiquer les autres types d’animaux.'
  WHERE survey_question_id = 144;

UPDATE ag.survey_question SET french = 'Veuillez indiquer l’âge (en années) et le sexe de tout être humain avec lequel l’animal vit actuellement.'
  WHERE survey_question_id = 145;

UPDATE ag.survey_question SET french = 'Quel est votre spot de surf local ?'
  WHERE survey_question_id = 174;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 174 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Point Loma/Ocean Beach, San Diego, Californie, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'La Jolla, San Diego, Californie, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Encinitas, Californie, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Californie du Sud, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Californie Centrale, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Californie du Nord, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET french = 'Nord-Ouest du Pacifique, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET french = 'Hawaï, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET french = 'Nord-Est, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET french = 'Sud-Est, États-Unis'
  WHERE survey_question_id = 174 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET french = 'Amérique du Sud'
  WHERE survey_question_id = 174 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET french = 'Europe'
  WHERE survey_question_id = 174 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET french = 'Afrique'
  WHERE survey_question_id = 174 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET french = 'Australie'
  WHERE survey_question_id = 174 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET french = 'Nouvelle Zélande'
  WHERE survey_question_id = 174 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET french = 'Asie du Sud-Est'
  WHERE survey_question_id = 174 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET french = 'Asie'
  WHERE survey_question_id = 174 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 174 AND
        display_index = 18;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence surfez-vous votre vague locale ?'
  WHERE survey_question_id = 175;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 175 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Plusieurs fois par jour'
  WHERE survey_question_id = 175 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Une fois par jour'
  WHERE survey_question_id = 175 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Plusieurs fois par semaine'
  WHERE survey_question_id = 175 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Une fois par semaine'
  WHERE survey_question_id = 175 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Plusieurs fois par mois'
  WHERE survey_question_id = 175 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence surfez-vous ?'
  WHERE survey_question_id = 176;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 176 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Plusieurs fois par jour'
  WHERE survey_question_id = 176 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Une fois par jour'
  WHERE survey_question_id = 176 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Plusieurs fois par semaine'
  WHERE survey_question_id = 176 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Une fois par semaine'
  WHERE survey_question_id = 176 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Plusieurs fois par mois'
  WHERE survey_question_id = 176 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Selon quelle fréquence vous rendez-vous sur d’autres spots de surf ?'
  WHERE survey_question_id = 177;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 177 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Plusieurs fois par jour'
  WHERE survey_question_id = 177 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Une fois par jour'
  WHERE survey_question_id = 177 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Plusieurs fois par semaine'
  WHERE survey_question_id = 177 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Une fois par semaine'
  WHERE survey_question_id = 177 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Plusieurs fois par mois'
  WHERE survey_question_id = 177 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Quelle distance parcourez-vous depuis cette plage entre les séances (domicile/travail/voyage) ?'
  WHERE survey_question_id = 178;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 178 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = '< 1 km'
  WHERE survey_question_id = 178 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = '5 à 10 km'
  WHERE survey_question_id = 178 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = '> 10 km'
  WHERE survey_question_id = 178 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Quel type de combinaison utilisez-vous ?'
  WHERE survey_question_id = 179;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 179 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Aucune'
  WHERE survey_question_id = 179 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = '< 1 mm'
  WHERE survey_question_id = 179 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = '2 à 3 mm'
  WHERE survey_question_id = 179 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = '3 à 4 mm'
  WHERE survey_question_id = 179 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = '4 à 5 mm'
  WHERE survey_question_id = 179 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Quel type de protection solaire utilisez-vous ?'
  WHERE survey_question_id = 180;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 180 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = '< SPF25'
  WHERE survey_question_id = 180 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'SPF 25 à 50'
  WHERE survey_question_id = 180 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'SPF 50+'
  WHERE survey_question_id = 180 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 180 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'À quelle fréquence utilisez-vous une protection solaire ?'
  WHERE survey_question_id = 181;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 181 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'À chaque fois que je surfe'
  WHERE survey_question_id = 181 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Souvent'
  WHERE survey_question_id = 181 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Rarement'
  WHERE survey_question_id = 181 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 181 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'À quelle fréquence vous douchez-vous après avoir surfé ?'
  WHERE survey_question_id = 182;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 182 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'À chaque fois que je surfe'
  WHERE survey_question_id = 182 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Souvent'
  WHERE survey_question_id = 182 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Rarement'
  WHERE survey_question_id = 182 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Jamais'
  WHERE survey_question_id = 182 AND
        display_index = 4;

UPDATE ag.survey_question SET french = 'Quelle est votre position de surf ?'
  WHERE survey_question_id = 183;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 183 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Regular'
  WHERE survey_question_id = 183 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Goofy'
  WHERE survey_question_id = 183 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Sur le ventre'
  WHERE survey_question_id = 183 AND
        display_index = 3;

UPDATE ag.survey_question SET french = 'Quel type de planche préférez-vous ?'
  WHERE survey_question_id = 184;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 184 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Longboard'
  WHERE survey_question_id = 184 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Shortboard'
  WHERE survey_question_id = 184 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Bodyboard'
  WHERE survey_question_id = 184 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Aucune planche (bodysurf)'
  WHERE survey_question_id = 184 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Pas de préférence'
  WHERE survey_question_id = 184 AND
        display_index = 5;

UPDATE ag.survey_question SET french = 'Quel type de wax utilisez-vous ?'
  WHERE survey_question_id = 185;

UPDATE ag.survey_question_response 
  SET french = 'Non précisé'
  WHERE survey_question_id = 185 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET french = 'Sex Wax'
  WHERE survey_question_id = 185 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET french = 'Sticky Bumps'
  WHERE survey_question_id = 185 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET french = 'Mrs. Palmers'
  WHERE survey_question_id = 185 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET french = 'Bubble Gum'
  WHERE survey_question_id = 185 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET french = 'Famous'
  WHERE survey_question_id = 185 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET french = 'Autre'
  WHERE survey_question_id = 185 AND
        display_index = 6;

ALTER TABLE ag.survey_question
    ADD COLUMN chinese varchar;
ALTER TABLE ag.survey_question_response
    ADD COLUMN chinese varchar;
UPDATE ag.survey_question SET chinese = '您如何对您的饮食进行分类？'
  WHERE survey_question_id = 1;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 1 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '杂食'
  WHERE survey_question_id = 1 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '杂食但不吃红肉'
  WHERE survey_question_id = 1 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '素食'
  WHERE survey_question_id = 1 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '素食但吃海鲜'
  WHERE survey_question_id = 1 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '纯素食'
  WHERE survey_question_id = 1 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您是否食用旧石器时代饮食、改良的旧石器时代饮食、远古饮食、FODMAP、Weston-Price 或其他低谷物、低加工食品？'
  WHERE survey_question_id = 10;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 10 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 10 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 10 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您的狗住在室内/室外还是受限制（笼子/箱子）：'
  WHERE survey_question_id = 101;

UPDATE ag.survey_question SET chinese = '种族/族裔：'
  WHERE survey_question_id = 103;

UPDATE ag.survey_question SET chinese = '膳食补充剂：'
  WHERE survey_question_id = 104;

UPDATE ag.survey_question SET chinese = '与狗的接触程度：'
  WHERE survey_question_id = 105;

UPDATE ag.survey_question SET chinese = '您患有的其他病症（未在已确诊的病症问题中列出的病症）'
  WHERE survey_question_id = 106;

UPDATE ag.survey_question SET chinese = '性别：'
  WHERE survey_question_id = 107;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 107 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '男性'
  WHERE survey_question_id = 107 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '女性'
  WHERE survey_question_id = 107 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 107 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '身高：'
  WHERE survey_question_id = 108;

UPDATE ag.survey_question SET chinese = '身高单位：'
  WHERE survey_question_id = 109;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 109 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '英寸'
  WHERE survey_question_id = 109 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '厘米'
  WHERE survey_question_id = 109 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您是否食用经抗生素治疗的动物肉类/乳制品？'
  WHERE survey_question_id = 11;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 11 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 11 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 11 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 11 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '出生国家：'
  WHERE survey_question_id = 110;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 110 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '阿富汗'
  WHERE survey_question_id = 110 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '奥兰群岛'
  WHERE survey_question_id = 110 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '阿尔巴尼亚'
  WHERE survey_question_id = 110 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '阿尔及利亚'
  WHERE survey_question_id = 110 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '美属萨摩亚'
  WHERE survey_question_id = 110 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '安道尔'
  WHERE survey_question_id = 110 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '安哥拉'
  WHERE survey_question_id = 110 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '安圭拉岛'
  WHERE survey_question_id = 110 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '南极洲'
  WHERE survey_question_id = 110 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET chinese = '安提瓜和巴布达'
  WHERE survey_question_id = 110 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET chinese = '阿根廷'
  WHERE survey_question_id = 110 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET chinese = '亚美尼亚'
  WHERE survey_question_id = 110 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET chinese = '阿鲁巴岛'
  WHERE survey_question_id = 110 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET chinese = '澳大利亚'
  WHERE survey_question_id = 110 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET chinese = '奥地利'
  WHERE survey_question_id = 110 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET chinese = '阿塞拜疆'
  WHERE survey_question_id = 110 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET chinese = '巴哈马'
  WHERE survey_question_id = 110 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET chinese = '巴林'
  WHERE survey_question_id = 110 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET chinese = '孟加拉国'
  WHERE survey_question_id = 110 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET chinese = '巴巴多斯'
  WHERE survey_question_id = 110 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET chinese = '白俄罗斯'
  WHERE survey_question_id = 110 AND
        display_index = 21;
UPDATE ag.survey_question_response 
  SET chinese = '比利时'
  WHERE survey_question_id = 110 AND
        display_index = 22;
UPDATE ag.survey_question_response 
  SET chinese = '伯利兹'
  WHERE survey_question_id = 110 AND
        display_index = 23;
UPDATE ag.survey_question_response 
  SET chinese = '贝宁'
  WHERE survey_question_id = 110 AND
        display_index = 24;
UPDATE ag.survey_question_response 
  SET chinese = '百慕大'
  WHERE survey_question_id = 110 AND
        display_index = 25;
UPDATE ag.survey_question_response 
  SET chinese = '不丹'
  WHERE survey_question_id = 110 AND
        display_index = 26;
UPDATE ag.survey_question_response 
  SET chinese = '玻利维亚'
  WHERE survey_question_id = 110 AND
        display_index = 27;
UPDATE ag.survey_question_response 
  SET chinese = '波斯尼亚和黑塞哥维那'
  WHERE survey_question_id = 110 AND
        display_index = 28;
UPDATE ag.survey_question_response 
  SET chinese = '博茨瓦纳'
  WHERE survey_question_id = 110 AND
        display_index = 29;
UPDATE ag.survey_question_response 
  SET chinese = '布维岛'
  WHERE survey_question_id = 110 AND
        display_index = 30;
UPDATE ag.survey_question_response 
  SET chinese = '巴西'
  WHERE survey_question_id = 110 AND
        display_index = 31;
UPDATE ag.survey_question_response 
  SET chinese = '英属印度洋领地'
  WHERE survey_question_id = 110 AND
        display_index = 32;
UPDATE ag.survey_question_response 
  SET chinese = '文莱达鲁萨兰国'
  WHERE survey_question_id = 110 AND
        display_index = 33;
UPDATE ag.survey_question_response 
  SET chinese = '保加利亚'
  WHERE survey_question_id = 110 AND
        display_index = 34;
UPDATE ag.survey_question_response 
  SET chinese = '布基纳法索'
  WHERE survey_question_id = 110 AND
        display_index = 35;
UPDATE ag.survey_question_response 
  SET chinese = '布隆迪'
  WHERE survey_question_id = 110 AND
        display_index = 36;
UPDATE ag.survey_question_response 
  SET chinese = '柬埔寨'
  WHERE survey_question_id = 110 AND
        display_index = 37;
UPDATE ag.survey_question_response 
  SET chinese = '喀麦隆'
  WHERE survey_question_id = 110 AND
        display_index = 38;
UPDATE ag.survey_question_response 
  SET chinese = '加拿大'
  WHERE survey_question_id = 110 AND
        display_index = 39;
UPDATE ag.survey_question_response 
  SET chinese = '佛得角'
  WHERE survey_question_id = 110 AND
        display_index = 40;
UPDATE ag.survey_question_response 
  SET chinese = '开曼群岛'
  WHERE survey_question_id = 110 AND
        display_index = 41;
UPDATE ag.survey_question_response 
  SET chinese = '中非共和国'
  WHERE survey_question_id = 110 AND
        display_index = 42;
UPDATE ag.survey_question_response 
  SET chinese = '乍得'
  WHERE survey_question_id = 110 AND
        display_index = 43;
UPDATE ag.survey_question_response 
  SET chinese = '智利'
  WHERE survey_question_id = 110 AND
        display_index = 44;
UPDATE ag.survey_question_response 
  SET chinese = '中国'
  WHERE survey_question_id = 110 AND
        display_index = 45;
UPDATE ag.survey_question_response 
  SET chinese = '圣诞岛'
  WHERE survey_question_id = 110 AND
        display_index = 46;
UPDATE ag.survey_question_response 
  SET chinese = '科科斯（基林）群岛'
  WHERE survey_question_id = 110 AND
        display_index = 47;
UPDATE ag.survey_question_response 
  SET chinese = '哥伦比亚'
  WHERE survey_question_id = 110 AND
        display_index = 48;
UPDATE ag.survey_question_response 
  SET chinese = '科摩罗'
  WHERE survey_question_id = 110 AND
        display_index = 49;
UPDATE ag.survey_question_response 
  SET chinese = '刚果'
  WHERE survey_question_id = 110 AND
        display_index = 50;
UPDATE ag.survey_question_response 
  SET chinese = '刚果民主共和国'
  WHERE survey_question_id = 110 AND
        display_index = 51;
UPDATE ag.survey_question_response 
  SET chinese = '库克群岛'
  WHERE survey_question_id = 110 AND
        display_index = 52;
UPDATE ag.survey_question_response 
  SET chinese = '哥斯达黎加'
  WHERE survey_question_id = 110 AND
        display_index = 53;
UPDATE ag.survey_question_response 
  SET chinese = '科特迪瓦'
  WHERE survey_question_id = 110 AND
        display_index = 54;
UPDATE ag.survey_question_response 
  SET chinese = '克罗地亚'
  WHERE survey_question_id = 110 AND
        display_index = 55;
UPDATE ag.survey_question_response 
  SET chinese = '古巴'
  WHERE survey_question_id = 110 AND
        display_index = 56;
UPDATE ag.survey_question_response 
  SET chinese = '塞浦路斯'
  WHERE survey_question_id = 110 AND
        display_index = 57;
UPDATE ag.survey_question_response 
  SET chinese = '捷克共和国'
  WHERE survey_question_id = 110 AND
        display_index = 58;
UPDATE ag.survey_question_response 
  SET chinese = '丹麦'
  WHERE survey_question_id = 110 AND
        display_index = 59;
UPDATE ag.survey_question_response 
  SET chinese = '吉布地'
  WHERE survey_question_id = 110 AND
        display_index = 60;
UPDATE ag.survey_question_response 
  SET chinese = '多米尼加'
  WHERE survey_question_id = 110 AND
        display_index = 61;
UPDATE ag.survey_question_response 
  SET chinese = '多明尼加共和国'
  WHERE survey_question_id = 110 AND
        display_index = 62;
UPDATE ag.survey_question_response 
  SET chinese = '厄瓜多尔'
  WHERE survey_question_id = 110 AND
        display_index = 63;
UPDATE ag.survey_question_response 
  SET chinese = '埃及'
  WHERE survey_question_id = 110 AND
        display_index = 64;
UPDATE ag.survey_question_response 
  SET chinese = '萨尔瓦多'
  WHERE survey_question_id = 110 AND
        display_index = 65;
UPDATE ag.survey_question_response 
  SET chinese = '赤道几内亚'
  WHERE survey_question_id = 110 AND
        display_index = 66;
UPDATE ag.survey_question_response 
  SET chinese = '厄立特里亚'
  WHERE survey_question_id = 110 AND
        display_index = 67;
UPDATE ag.survey_question_response 
  SET chinese = '爱沙尼亚'
  WHERE survey_question_id = 110 AND
        display_index = 68;
UPDATE ag.survey_question_response 
  SET chinese = '埃塞俄比亚'
  WHERE survey_question_id = 110 AND
        display_index = 69;
UPDATE ag.survey_question_response 
  SET chinese = '福克兰群岛（马尔维纳斯）'
  WHERE survey_question_id = 110 AND
        display_index = 70;
UPDATE ag.survey_question_response 
  SET chinese = '法罗群岛'
  WHERE survey_question_id = 110 AND
        display_index = 71;
UPDATE ag.survey_question_response 
  SET chinese = '斐济'
  WHERE survey_question_id = 110 AND
        display_index = 72;
UPDATE ag.survey_question_response 
  SET chinese = '芬兰'
  WHERE survey_question_id = 110 AND
        display_index = 73;
UPDATE ag.survey_question_response 
  SET chinese = '法国'
  WHERE survey_question_id = 110 AND
        display_index = 74;
UPDATE ag.survey_question_response 
  SET chinese = '法属圭亚那'
  WHERE survey_question_id = 110 AND
        display_index = 75;
UPDATE ag.survey_question_response 
  SET chinese = '法属波利尼西亚'
  WHERE survey_question_id = 110 AND
        display_index = 76;
UPDATE ag.survey_question_response 
  SET chinese = '法属南部领地'
  WHERE survey_question_id = 110 AND
        display_index = 77;
UPDATE ag.survey_question_response 
  SET chinese = '加蓬'
  WHERE survey_question_id = 110 AND
        display_index = 78;
UPDATE ag.survey_question_response 
  SET chinese = '冈比亚'
  WHERE survey_question_id = 110 AND
        display_index = 79;
UPDATE ag.survey_question_response 
  SET chinese = '佐治亚州'
  WHERE survey_question_id = 110 AND
        display_index = 80;
UPDATE ag.survey_question_response 
  SET chinese = '德国'
  WHERE survey_question_id = 110 AND
        display_index = 81;
UPDATE ag.survey_question_response 
  SET chinese = '加纳'
  WHERE survey_question_id = 110 AND
        display_index = 82;
UPDATE ag.survey_question_response 
  SET chinese = '直布罗陀'
  WHERE survey_question_id = 110 AND
        display_index = 83;
UPDATE ag.survey_question_response 
  SET chinese = '希腊'
  WHERE survey_question_id = 110 AND
        display_index = 84;
UPDATE ag.survey_question_response 
  SET chinese = '格陵兰'
  WHERE survey_question_id = 110 AND
        display_index = 85;
UPDATE ag.survey_question_response 
  SET chinese = '格林纳达'
  WHERE survey_question_id = 110 AND
        display_index = 86;
UPDATE ag.survey_question_response 
  SET chinese = '瓜德罗普岛'
  WHERE survey_question_id = 110 AND
        display_index = 87;
UPDATE ag.survey_question_response 
  SET chinese = '关岛'
  WHERE survey_question_id = 110 AND
        display_index = 88;
UPDATE ag.survey_question_response 
  SET chinese = '危地马拉'
  WHERE survey_question_id = 110 AND
        display_index = 89;
UPDATE ag.survey_question_response 
  SET chinese = '根西岛'
  WHERE survey_question_id = 110 AND
        display_index = 90;
UPDATE ag.survey_question_response 
  SET chinese = '几内亚'
  WHERE survey_question_id = 110 AND
        display_index = 91;
UPDATE ag.survey_question_response 
  SET chinese = '几内亚比绍'
  WHERE survey_question_id = 110 AND
        display_index = 92;
UPDATE ag.survey_question_response 
  SET chinese = '圭亚那'
  WHERE survey_question_id = 110 AND
        display_index = 93;
UPDATE ag.survey_question_response 
  SET chinese = '海地'
  WHERE survey_question_id = 110 AND
        display_index = 94;
UPDATE ag.survey_question_response 
  SET chinese = '希尔德岛和麦当劳群岛'
  WHERE survey_question_id = 110 AND
        display_index = 95;
UPDATE ag.survey_question_response 
  SET chinese = '罗马教廷（梵蒂冈城国）'
  WHERE survey_question_id = 110 AND
        display_index = 96;
UPDATE ag.survey_question_response 
  SET chinese = '洪都拉斯'
  WHERE survey_question_id = 110 AND
        display_index = 97;
UPDATE ag.survey_question_response 
  SET chinese = '香港'
  WHERE survey_question_id = 110 AND
        display_index = 98;
UPDATE ag.survey_question_response 
  SET chinese = '匈牙利'
  WHERE survey_question_id = 110 AND
        display_index = 99;
UPDATE ag.survey_question_response 
  SET chinese = '冰岛'
  WHERE survey_question_id = 110 AND
        display_index = 100;
UPDATE ag.survey_question_response 
  SET chinese = '印度'
  WHERE survey_question_id = 110 AND
        display_index = 101;
UPDATE ag.survey_question_response 
  SET chinese = '印度尼西亚'
  WHERE survey_question_id = 110 AND
        display_index = 102;
UPDATE ag.survey_question_response 
  SET chinese = '伊朗伊斯兰共和国'
  WHERE survey_question_id = 110 AND
        display_index = 103;
UPDATE ag.survey_question_response 
  SET chinese = '伊拉克'
  WHERE survey_question_id = 110 AND
        display_index = 104;
UPDATE ag.survey_question_response 
  SET chinese = '爱尔兰'
  WHERE survey_question_id = 110 AND
        display_index = 105;
UPDATE ag.survey_question_response 
  SET chinese = '马恩岛'
  WHERE survey_question_id = 110 AND
        display_index = 106;
UPDATE ag.survey_question_response 
  SET chinese = '以色列'
  WHERE survey_question_id = 110 AND
        display_index = 107;
UPDATE ag.survey_question_response 
  SET chinese = '意大利'
  WHERE survey_question_id = 110 AND
        display_index = 108;
UPDATE ag.survey_question_response 
  SET chinese = '牙买加'
  WHERE survey_question_id = 110 AND
        display_index = 109;
UPDATE ag.survey_question_response 
  SET chinese = '日本'
  WHERE survey_question_id = 110 AND
        display_index = 110;
UPDATE ag.survey_question_response 
  SET chinese = '泽西岛'
  WHERE survey_question_id = 110 AND
        display_index = 111;
UPDATE ag.survey_question_response 
  SET chinese = '约旦'
  WHERE survey_question_id = 110 AND
        display_index = 112;
UPDATE ag.survey_question_response 
  SET chinese = '哈萨克斯坦'
  WHERE survey_question_id = 110 AND
        display_index = 113;
UPDATE ag.survey_question_response 
  SET chinese = '肯尼亚'
  WHERE survey_question_id = 110 AND
        display_index = 114;
UPDATE ag.survey_question_response 
  SET chinese = '基里巴斯'
  WHERE survey_question_id = 110 AND
        display_index = 115;
UPDATE ag.survey_question_response 
  SET chinese = '韩国，朝鲜民主主义人民共和国'
  WHERE survey_question_id = 110 AND
        display_index = 116;
UPDATE ag.survey_question_response 
  SET chinese = '韩国'
  WHERE survey_question_id = 110 AND
        display_index = 117;
UPDATE ag.survey_question_response 
  SET chinese = '科威特'
  WHERE survey_question_id = 110 AND
        display_index = 118;
UPDATE ag.survey_question_response 
  SET chinese = '吉尔吉斯斯坦'
  WHERE survey_question_id = 110 AND
        display_index = 119;
UPDATE ag.survey_question_response 
  SET chinese = '老挝人民民主共和国'
  WHERE survey_question_id = 110 AND
        display_index = 120;
UPDATE ag.survey_question_response 
  SET chinese = '拉脱维亚'
  WHERE survey_question_id = 110 AND
        display_index = 121;
UPDATE ag.survey_question_response 
  SET chinese = '黎巴嫩'
  WHERE survey_question_id = 110 AND
        display_index = 122;
UPDATE ag.survey_question_response 
  SET chinese = '莱索托'
  WHERE survey_question_id = 110 AND
        display_index = 123;
UPDATE ag.survey_question_response 
  SET chinese = '利比里亚'
  WHERE survey_question_id = 110 AND
        display_index = 124;
UPDATE ag.survey_question_response 
  SET chinese = '阿拉伯利比亚民众国'
  WHERE survey_question_id = 110 AND
        display_index = 125;
UPDATE ag.survey_question_response 
  SET chinese = '列支敦士登'
  WHERE survey_question_id = 110 AND
        display_index = 126;
UPDATE ag.survey_question_response 
  SET chinese = '立陶宛'
  WHERE survey_question_id = 110 AND
        display_index = 127;
UPDATE ag.survey_question_response 
  SET chinese = '卢森堡'
  WHERE survey_question_id = 110 AND
        display_index = 128;
UPDATE ag.survey_question_response 
  SET chinese = '澳门'
  WHERE survey_question_id = 110 AND
        display_index = 129;
UPDATE ag.survey_question_response 
  SET chinese = '马其顿，前南斯拉夫共和国'
  WHERE survey_question_id = 110 AND
        display_index = 130;
UPDATE ag.survey_question_response 
  SET chinese = '马达加斯加'
  WHERE survey_question_id = 110 AND
        display_index = 131;
UPDATE ag.survey_question_response 
  SET chinese = '马拉维'
  WHERE survey_question_id = 110 AND
        display_index = 132;
UPDATE ag.survey_question_response 
  SET chinese = '马来西亚'
  WHERE survey_question_id = 110 AND
        display_index = 133;
UPDATE ag.survey_question_response 
  SET chinese = '马尔代夫'
  WHERE survey_question_id = 110 AND
        display_index = 134;
UPDATE ag.survey_question_response 
  SET chinese = '马里'
  WHERE survey_question_id = 110 AND
        display_index = 135;
UPDATE ag.survey_question_response 
  SET chinese = '马耳他'
  WHERE survey_question_id = 110 AND
        display_index = 136;
UPDATE ag.survey_question_response 
  SET chinese = '马绍尔群岛'
  WHERE survey_question_id = 110 AND
        display_index = 137;
UPDATE ag.survey_question_response 
  SET chinese = '马提尼克岛'
  WHERE survey_question_id = 110 AND
        display_index = 138;
UPDATE ag.survey_question_response 
  SET chinese = '毛里塔尼亚'
  WHERE survey_question_id = 110 AND
        display_index = 139;
UPDATE ag.survey_question_response 
  SET chinese = '毛里求斯'
  WHERE survey_question_id = 110 AND
        display_index = 140;
UPDATE ag.survey_question_response 
  SET chinese = '马约特岛'
  WHERE survey_question_id = 110 AND
        display_index = 141;
UPDATE ag.survey_question_response 
  SET chinese = '墨西哥'
  WHERE survey_question_id = 110 AND
        display_index = 142;
UPDATE ag.survey_question_response 
  SET chinese = '密克罗尼西亚联邦'
  WHERE survey_question_id = 110 AND
        display_index = 143;
UPDATE ag.survey_question_response 
  SET chinese = '摩尔多瓦共和国'
  WHERE survey_question_id = 110 AND
        display_index = 144;
UPDATE ag.survey_question_response 
  SET chinese = '摩纳哥'
  WHERE survey_question_id = 110 AND
        display_index = 145;
UPDATE ag.survey_question_response 
  SET chinese = '蒙古'
  WHERE survey_question_id = 110 AND
        display_index = 146;
UPDATE ag.survey_question_response 
  SET chinese = '黑山共和国'
  WHERE survey_question_id = 110 AND
        display_index = 147;
UPDATE ag.survey_question_response 
  SET chinese = '蒙特塞拉特'
  WHERE survey_question_id = 110 AND
        display_index = 148;
UPDATE ag.survey_question_response 
  SET chinese = '摩洛哥'
  WHERE survey_question_id = 110 AND
        display_index = 149;
UPDATE ag.survey_question_response 
  SET chinese = '莫桑比克'
  WHERE survey_question_id = 110 AND
        display_index = 150;
UPDATE ag.survey_question_response 
  SET chinese = '缅甸'
  WHERE survey_question_id = 110 AND
        display_index = 151;
UPDATE ag.survey_question_response 
  SET chinese = '纳米比亚'
  WHERE survey_question_id = 110 AND
        display_index = 152;
UPDATE ag.survey_question_response 
  SET chinese = '瑙鲁'
  WHERE survey_question_id = 110 AND
        display_index = 153;
UPDATE ag.survey_question_response 
  SET chinese = '尼泊尔'
  WHERE survey_question_id = 110 AND
        display_index = 154;
UPDATE ag.survey_question_response 
  SET chinese = '荷兰'
  WHERE survey_question_id = 110 AND
        display_index = 155;
UPDATE ag.survey_question_response 
  SET chinese = '荷属安的列斯'
  WHERE survey_question_id = 110 AND
        display_index = 156;
UPDATE ag.survey_question_response 
  SET chinese = '新喀里多尼亚'
  WHERE survey_question_id = 110 AND
        display_index = 157;
UPDATE ag.survey_question_response 
  SET chinese = '新西兰'
  WHERE survey_question_id = 110 AND
        display_index = 158;
UPDATE ag.survey_question_response 
  SET chinese = '尼加拉瓜'
  WHERE survey_question_id = 110 AND
        display_index = 159;
UPDATE ag.survey_question_response 
  SET chinese = '尼日尔'
  WHERE survey_question_id = 110 AND
        display_index = 160;
UPDATE ag.survey_question_response 
  SET chinese = '奈及利亚'
  WHERE survey_question_id = 110 AND
        display_index = 161;
UPDATE ag.survey_question_response 
  SET chinese = '纽埃'
  WHERE survey_question_id = 110 AND
        display_index = 162;
UPDATE ag.survey_question_response 
  SET chinese = '诺福克岛'
  WHERE survey_question_id = 110 AND
        display_index = 163;
UPDATE ag.survey_question_response 
  SET chinese = '北马里亚纳群岛'
  WHERE survey_question_id = 110 AND
        display_index = 164;
UPDATE ag.survey_question_response 
  SET chinese = '挪威'
  WHERE survey_question_id = 110 AND
        display_index = 165;
UPDATE ag.survey_question_response 
  SET chinese = '阿曼'
  WHERE survey_question_id = 110 AND
        display_index = 166;
UPDATE ag.survey_question_response 
  SET chinese = '巴基斯坦'
  WHERE survey_question_id = 110 AND
        display_index = 167;
UPDATE ag.survey_question_response 
  SET chinese = 'u琉'
  WHERE survey_question_id = 110 AND
        display_index = 168;
UPDATE ag.survey_question_response 
  SET chinese = '被占领的巴勒斯坦领土'
  WHERE survey_question_id = 110 AND
        display_index = 169;
UPDATE ag.survey_question_response 
  SET chinese = '巴拿马'
  WHERE survey_question_id = 110 AND
        display_index = 170;
UPDATE ag.survey_question_response 
  SET chinese = '巴布亚新几内亚'
  WHERE survey_question_id = 110 AND
        display_index = 171;
UPDATE ag.survey_question_response 
  SET chinese = '巴拉圭'
  WHERE survey_question_id = 110 AND
        display_index = 172;
UPDATE ag.survey_question_response 
  SET chinese = '秘鲁'
  WHERE survey_question_id = 110 AND
        display_index = 173;
UPDATE ag.survey_question_response 
  SET chinese = '菲律宾'
  WHERE survey_question_id = 110 AND
        display_index = 174;
UPDATE ag.survey_question_response 
  SET chinese = '皮特凯恩'
  WHERE survey_question_id = 110 AND
        display_index = 175;
UPDATE ag.survey_question_response 
  SET chinese = '波兰'
  WHERE survey_question_id = 110 AND
        display_index = 176;
UPDATE ag.survey_question_response 
  SET chinese = '葡萄牙'
  WHERE survey_question_id = 110 AND
        display_index = 177;
UPDATE ag.survey_question_response 
  SET chinese = '波多黎各'
  WHERE survey_question_id = 110 AND
        display_index = 178;
UPDATE ag.survey_question_response 
  SET chinese = '卡塔尔'
  WHERE survey_question_id = 110 AND
        display_index = 179;
UPDATE ag.survey_question_response 
  SET chinese = '团圆'
  WHERE survey_question_id = 110 AND
        display_index = 180;
UPDATE ag.survey_question_response 
  SET chinese = '罗马尼亚'
  WHERE survey_question_id = 110 AND
        display_index = 181;
UPDATE ag.survey_question_response 
  SET chinese = '俄罗斯联邦'
  WHERE survey_question_id = 110 AND
        display_index = 182;
UPDATE ag.survey_question_response 
  SET chinese = '卢旺达'
  WHERE survey_question_id = 110 AND
        display_index = 183;
UPDATE ag.survey_question_response 
  SET chinese = '圣海伦娜'
  WHERE survey_question_id = 110 AND
        display_index = 184;
UPDATE ag.survey_question_response 
  SET chinese = '圣基茨和尼维斯'
  WHERE survey_question_id = 110 AND
        display_index = 185;
UPDATE ag.survey_question_response 
  SET chinese = '圣卢西亚'
  WHERE survey_question_id = 110 AND
        display_index = 186;
UPDATE ag.survey_question_response 
  SET chinese = '圣皮埃尔和密克隆群岛'
  WHERE survey_question_id = 110 AND
        display_index = 187;
UPDATE ag.survey_question_response 
  SET chinese = '圣文森特和格林纳丁斯'
  WHERE survey_question_id = 110 AND
        display_index = 188;
UPDATE ag.survey_question_response 
  SET chinese = '萨摩亚'
  WHERE survey_question_id = 110 AND
        display_index = 189;
UPDATE ag.survey_question_response 
  SET chinese = '圣马力诺'
  WHERE survey_question_id = 110 AND
        display_index = 190;
UPDATE ag.survey_question_response 
  SET chinese = '圣多美和普林西比'
  WHERE survey_question_id = 110 AND
        display_index = 191;
UPDATE ag.survey_question_response 
  SET chinese = '沙特阿拉伯'
  WHERE survey_question_id = 110 AND
        display_index = 192;
UPDATE ag.survey_question_response 
  SET chinese = '塞内加尔'
  WHERE survey_question_id = 110 AND
        display_index = 193;
UPDATE ag.survey_question_response 
  SET chinese = '塞尔维亚'
  WHERE survey_question_id = 110 AND
        display_index = 194;
UPDATE ag.survey_question_response 
  SET chinese = '塞舌尔'
  WHERE survey_question_id = 110 AND
        display_index = 195;
UPDATE ag.survey_question_response 
  SET chinese = '塞拉利昂'
  WHERE survey_question_id = 110 AND
        display_index = 196;
UPDATE ag.survey_question_response 
  SET chinese = '新加坡'
  WHERE survey_question_id = 110 AND
        display_index = 197;
UPDATE ag.survey_question_response 
  SET chinese = '斯洛伐克'
  WHERE survey_question_id = 110 AND
        display_index = 198;
UPDATE ag.survey_question_response 
  SET chinese = '斯洛文尼亚'
  WHERE survey_question_id = 110 AND
        display_index = 199;
UPDATE ag.survey_question_response 
  SET chinese = '所罗门群岛'
  WHERE survey_question_id = 110 AND
        display_index = 200;
UPDATE ag.survey_question_response 
  SET chinese = '索马里'
  WHERE survey_question_id = 110 AND
        display_index = 201;
UPDATE ag.survey_question_response 
  SET chinese = '南非'
  WHERE survey_question_id = 110 AND
        display_index = 202;
UPDATE ag.survey_question_response 
  SET chinese = '南乔治亚岛和南桑威奇群岛'
  WHERE survey_question_id = 110 AND
        display_index = 203;
UPDATE ag.survey_question_response 
  SET chinese = '西班牙'
  WHERE survey_question_id = 110 AND
        display_index = 204;
UPDATE ag.survey_question_response 
  SET chinese = '斯里兰卡'
  WHERE survey_question_id = 110 AND
        display_index = 205;
UPDATE ag.survey_question_response 
  SET chinese = '苏丹'
  WHERE survey_question_id = 110 AND
        display_index = 206;
UPDATE ag.survey_question_response 
  SET chinese = '苏里南'
  WHERE survey_question_id = 110 AND
        display_index = 207;
UPDATE ag.survey_question_response 
  SET chinese = '斯瓦尔巴和扬·马延'
  WHERE survey_question_id = 110 AND
        display_index = 208;
UPDATE ag.survey_question_response 
  SET chinese = '斯威士兰'
  WHERE survey_question_id = 110 AND
        display_index = 209;
UPDATE ag.survey_question_response 
  SET chinese = '瑞典'
  WHERE survey_question_id = 110 AND
        display_index = 210;
UPDATE ag.survey_question_response 
  SET chinese = '瑞士'
  WHERE survey_question_id = 110 AND
        display_index = 211;
UPDATE ag.survey_question_response 
  SET chinese = '阿拉伯叙利亚共和国'
  WHERE survey_question_id = 110 AND
        display_index = 212;
UPDATE ag.survey_question_response 
  SET chinese = '中国台湾省'
  WHERE survey_question_id = 110 AND
        display_index = 213;
UPDATE ag.survey_question_response 
  SET chinese = '塔吉克斯坦'
  WHERE survey_question_id = 110 AND
        display_index = 214;
UPDATE ag.survey_question_response 
  SET chinese = '坦桑尼亚联合共和国'
  WHERE survey_question_id = 110 AND
        display_index = 215;
UPDATE ag.survey_question_response 
  SET chinese = '泰国'
  WHERE survey_question_id = 110 AND
        display_index = 216;
UPDATE ag.survey_question_response 
  SET chinese = '东帝汶'
  WHERE survey_question_id = 110 AND
        display_index = 217;
UPDATE ag.survey_question_response 
  SET chinese = '多哥'
  WHERE survey_question_id = 110 AND
        display_index = 218;
UPDATE ag.survey_question_response 
  SET chinese = '托克劳'
  WHERE survey_question_id = 110 AND
        display_index = 219;
UPDATE ag.survey_question_response 
  SET chinese = '汤加'
  WHERE survey_question_id = 110 AND
        display_index = 220;
UPDATE ag.survey_question_response 
  SET chinese = '特立尼达和多巴哥'
  WHERE survey_question_id = 110 AND
        display_index = 221;
UPDATE ag.survey_question_response 
  SET chinese = '突尼斯'
  WHERE survey_question_id = 110 AND
        display_index = 222;
UPDATE ag.survey_question_response 
  SET chinese = '火鸡'
  WHERE survey_question_id = 110 AND
        display_index = 223;
UPDATE ag.survey_question_response 
  SET chinese = '土库曼斯坦'
  WHERE survey_question_id = 110 AND
        display_index = 224;
UPDATE ag.survey_question_response 
  SET chinese = '特克斯和凯科斯群岛'
  WHERE survey_question_id = 110 AND
        display_index = 225;
UPDATE ag.survey_question_response 
  SET chinese = '图瓦卢'
  WHERE survey_question_id = 110 AND
        display_index = 226;
UPDATE ag.survey_question_response 
  SET chinese = '乌干达'
  WHERE survey_question_id = 110 AND
        display_index = 227;
UPDATE ag.survey_question_response 
  SET chinese = '乌克兰'
  WHERE survey_question_id = 110 AND
        display_index = 228;
UPDATE ag.survey_question_response 
  SET chinese = '阿拉伯联合酋长国'
  WHERE survey_question_id = 110 AND
        display_index = 229;
UPDATE ag.survey_question_response 
  SET chinese = '英国'
  WHERE survey_question_id = 110 AND
        display_index = 230;
UPDATE ag.survey_question_response 
  SET chinese = '美国'
  WHERE survey_question_id = 110 AND
        display_index = 231;
UPDATE ag.survey_question_response 
  SET chinese = '美国本土外小岛屿'
  WHERE survey_question_id = 110 AND
        display_index = 232;
UPDATE ag.survey_question_response 
  SET chinese = '乌拉圭'
  WHERE survey_question_id = 110 AND
        display_index = 233;
UPDATE ag.survey_question_response 
  SET chinese = '乌兹别克斯坦'
  WHERE survey_question_id = 110 AND
        display_index = 234;
UPDATE ag.survey_question_response 
  SET chinese = '瓦努阿图'
  WHERE survey_question_id = 110 AND
        display_index = 235;
UPDATE ag.survey_question_response 
  SET chinese = '委内瑞拉'
  WHERE survey_question_id = 110 AND
        display_index = 236;
UPDATE ag.survey_question_response 
  SET chinese = '越南'
  WHERE survey_question_id = 110 AND
        display_index = 237;
UPDATE ag.survey_question_response 
  SET chinese = '英属维尔京群岛'
  WHERE survey_question_id = 110 AND
        display_index = 238;
UPDATE ag.survey_question_response 
  SET chinese = '美国维尔京群岛'
  WHERE survey_question_id = 110 AND
        display_index = 239;
UPDATE ag.survey_question_response 
  SET chinese = '瓦利斯和富图纳群岛'
  WHERE survey_question_id = 110 AND
        display_index = 240;
UPDATE ag.survey_question_response 
  SET chinese = '撒哈拉沙漠西部'
  WHERE survey_question_id = 110 AND
        display_index = 241;
UPDATE ag.survey_question_response 
  SET chinese = '也门'
  WHERE survey_question_id = 110 AND
        display_index = 242;
UPDATE ag.survey_question_response 
  SET chinese = '赞比亚'
  WHERE survey_question_id = 110 AND
        display_index = 243;
UPDATE ag.survey_question_response 
  SET chinese = '津巴布韦'
  WHERE survey_question_id = 110 AND
        display_index = 244;

UPDATE ag.survey_question SET chinese = '出生月：'
  WHERE survey_question_id = 111;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 111 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '一月'
  WHERE survey_question_id = 111 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '二月'
  WHERE survey_question_id = 111 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '游行'
  WHERE survey_question_id = 111 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '四月'
  WHERE survey_question_id = 111 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '可以'
  WHERE survey_question_id = 111 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '六月'
  WHERE survey_question_id = 111 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '七月'
  WHERE survey_question_id = 111 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '八月'
  WHERE survey_question_id = 111 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '九月'
  WHERE survey_question_id = 111 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET chinese = '十月'
  WHERE survey_question_id = 111 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET chinese = '十一月'
  WHERE survey_question_id = 111 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET chinese = '十二月'
  WHERE survey_question_id = 111 AND
        display_index = 12;

UPDATE ag.survey_question SET chinese = '出生年：'
  WHERE survey_question_id = 112;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 112 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '2018'
  WHERE survey_question_id = 112 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '2017'
  WHERE survey_question_id = 112 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '2016'
  WHERE survey_question_id = 112 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '2015'
  WHERE survey_question_id = 112 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '2014'
  WHERE survey_question_id = 112 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '2013'
  WHERE survey_question_id = 112 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '2012'
  WHERE survey_question_id = 112 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '2011'
  WHERE survey_question_id = 112 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '2010'
  WHERE survey_question_id = 112 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET chinese = '2009'
  WHERE survey_question_id = 112 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET chinese = '2008'
  WHERE survey_question_id = 112 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET chinese = '2007'
  WHERE survey_question_id = 112 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET chinese = '2006'
  WHERE survey_question_id = 112 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET chinese = '2005'
  WHERE survey_question_id = 112 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET chinese = '2004'
  WHERE survey_question_id = 112 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET chinese = '2003'
  WHERE survey_question_id = 112 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET chinese = '2002'
  WHERE survey_question_id = 112 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET chinese = '2001'
  WHERE survey_question_id = 112 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET chinese = '2000'
  WHERE survey_question_id = 112 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET chinese = '1999'
  WHERE survey_question_id = 112 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET chinese = '1998'
  WHERE survey_question_id = 112 AND
        display_index = 21;
UPDATE ag.survey_question_response 
  SET chinese = '1997'
  WHERE survey_question_id = 112 AND
        display_index = 22;
UPDATE ag.survey_question_response 
  SET chinese = '1996'
  WHERE survey_question_id = 112 AND
        display_index = 23;
UPDATE ag.survey_question_response 
  SET chinese = '1995'
  WHERE survey_question_id = 112 AND
        display_index = 24;
UPDATE ag.survey_question_response 
  SET chinese = '1994'
  WHERE survey_question_id = 112 AND
        display_index = 25;
UPDATE ag.survey_question_response 
  SET chinese = '1993'
  WHERE survey_question_id = 112 AND
        display_index = 26;
UPDATE ag.survey_question_response 
  SET chinese = '1992'
  WHERE survey_question_id = 112 AND
        display_index = 27;
UPDATE ag.survey_question_response 
  SET chinese = '1991'
  WHERE survey_question_id = 112 AND
        display_index = 28;
UPDATE ag.survey_question_response 
  SET chinese = '1990'
  WHERE survey_question_id = 112 AND
        display_index = 29;
UPDATE ag.survey_question_response 
  SET chinese = '1989'
  WHERE survey_question_id = 112 AND
        display_index = 30;
UPDATE ag.survey_question_response 
  SET chinese = '1988'
  WHERE survey_question_id = 112 AND
        display_index = 31;
UPDATE ag.survey_question_response 
  SET chinese = '1987'
  WHERE survey_question_id = 112 AND
        display_index = 32;
UPDATE ag.survey_question_response 
  SET chinese = '1986'
  WHERE survey_question_id = 112 AND
        display_index = 33;
UPDATE ag.survey_question_response 
  SET chinese = '1985'
  WHERE survey_question_id = 112 AND
        display_index = 34;
UPDATE ag.survey_question_response 
  SET chinese = '1984'
  WHERE survey_question_id = 112 AND
        display_index = 35;
UPDATE ag.survey_question_response 
  SET chinese = '1983'
  WHERE survey_question_id = 112 AND
        display_index = 36;
UPDATE ag.survey_question_response 
  SET chinese = '1982'
  WHERE survey_question_id = 112 AND
        display_index = 37;
UPDATE ag.survey_question_response 
  SET chinese = '1981'
  WHERE survey_question_id = 112 AND
        display_index = 38;
UPDATE ag.survey_question_response 
  SET chinese = '1980'
  WHERE survey_question_id = 112 AND
        display_index = 39;
UPDATE ag.survey_question_response 
  SET chinese = '1979'
  WHERE survey_question_id = 112 AND
        display_index = 40;
UPDATE ag.survey_question_response 
  SET chinese = '1978'
  WHERE survey_question_id = 112 AND
        display_index = 41;
UPDATE ag.survey_question_response 
  SET chinese = '1977'
  WHERE survey_question_id = 112 AND
        display_index = 42;
UPDATE ag.survey_question_response 
  SET chinese = '1976'
  WHERE survey_question_id = 112 AND
        display_index = 43;
UPDATE ag.survey_question_response 
  SET chinese = '1975'
  WHERE survey_question_id = 112 AND
        display_index = 44;
UPDATE ag.survey_question_response 
  SET chinese = '1974'
  WHERE survey_question_id = 112 AND
        display_index = 45;
UPDATE ag.survey_question_response 
  SET chinese = '1973'
  WHERE survey_question_id = 112 AND
        display_index = 46;
UPDATE ag.survey_question_response 
  SET chinese = '1972'
  WHERE survey_question_id = 112 AND
        display_index = 47;
UPDATE ag.survey_question_response 
  SET chinese = '1971'
  WHERE survey_question_id = 112 AND
        display_index = 48;
UPDATE ag.survey_question_response 
  SET chinese = '1970'
  WHERE survey_question_id = 112 AND
        display_index = 49;
UPDATE ag.survey_question_response 
  SET chinese = '1969'
  WHERE survey_question_id = 112 AND
        display_index = 50;
UPDATE ag.survey_question_response 
  SET chinese = '1968'
  WHERE survey_question_id = 112 AND
        display_index = 51;
UPDATE ag.survey_question_response 
  SET chinese = '1967'
  WHERE survey_question_id = 112 AND
        display_index = 52;
UPDATE ag.survey_question_response 
  SET chinese = '1966'
  WHERE survey_question_id = 112 AND
        display_index = 53;
UPDATE ag.survey_question_response 
  SET chinese = '1965'
  WHERE survey_question_id = 112 AND
        display_index = 54;
UPDATE ag.survey_question_response 
  SET chinese = '1964'
  WHERE survey_question_id = 112 AND
        display_index = 55;
UPDATE ag.survey_question_response 
  SET chinese = '1963'
  WHERE survey_question_id = 112 AND
        display_index = 56;
UPDATE ag.survey_question_response 
  SET chinese = '1962'
  WHERE survey_question_id = 112 AND
        display_index = 57;
UPDATE ag.survey_question_response 
  SET chinese = '1961'
  WHERE survey_question_id = 112 AND
        display_index = 58;
UPDATE ag.survey_question_response 
  SET chinese = '1960'
  WHERE survey_question_id = 112 AND
        display_index = 59;
UPDATE ag.survey_question_response 
  SET chinese = '1959'
  WHERE survey_question_id = 112 AND
        display_index = 60;
UPDATE ag.survey_question_response 
  SET chinese = '1958'
  WHERE survey_question_id = 112 AND
        display_index = 61;
UPDATE ag.survey_question_response 
  SET chinese = '1957'
  WHERE survey_question_id = 112 AND
        display_index = 62;
UPDATE ag.survey_question_response 
  SET chinese = '1956'
  WHERE survey_question_id = 112 AND
        display_index = 63;
UPDATE ag.survey_question_response 
  SET chinese = '1955'
  WHERE survey_question_id = 112 AND
        display_index = 64;
UPDATE ag.survey_question_response 
  SET chinese = '1954'
  WHERE survey_question_id = 112 AND
        display_index = 65;
UPDATE ag.survey_question_response 
  SET chinese = '1953'
  WHERE survey_question_id = 112 AND
        display_index = 66;
UPDATE ag.survey_question_response 
  SET chinese = '1952'
  WHERE survey_question_id = 112 AND
        display_index = 67;
UPDATE ag.survey_question_response 
  SET chinese = '1951'
  WHERE survey_question_id = 112 AND
        display_index = 68;
UPDATE ag.survey_question_response 
  SET chinese = '1950'
  WHERE survey_question_id = 112 AND
        display_index = 69;
UPDATE ag.survey_question_response 
  SET chinese = '1949'
  WHERE survey_question_id = 112 AND
        display_index = 70;
UPDATE ag.survey_question_response 
  SET chinese = '1948'
  WHERE survey_question_id = 112 AND
        display_index = 71;
UPDATE ag.survey_question_response 
  SET chinese = '1947'
  WHERE survey_question_id = 112 AND
        display_index = 72;
UPDATE ag.survey_question_response 
  SET chinese = '1946'
  WHERE survey_question_id = 112 AND
        display_index = 73;
UPDATE ag.survey_question_response 
  SET chinese = '1945'
  WHERE survey_question_id = 112 AND
        display_index = 74;
UPDATE ag.survey_question_response 
  SET chinese = '1944'
  WHERE survey_question_id = 112 AND
        display_index = 75;
UPDATE ag.survey_question_response 
  SET chinese = '1943'
  WHERE survey_question_id = 112 AND
        display_index = 76;
UPDATE ag.survey_question_response 
  SET chinese = '1942'
  WHERE survey_question_id = 112 AND
        display_index = 77;
UPDATE ag.survey_question_response 
  SET chinese = '1941'
  WHERE survey_question_id = 112 AND
        display_index = 78;
UPDATE ag.survey_question_response 
  SET chinese = '1940'
  WHERE survey_question_id = 112 AND
        display_index = 79;
UPDATE ag.survey_question_response 
  SET chinese = '1939'
  WHERE survey_question_id = 112 AND
        display_index = 80;
UPDATE ag.survey_question_response 
  SET chinese = '1938'
  WHERE survey_question_id = 112 AND
        display_index = 81;
UPDATE ag.survey_question_response 
  SET chinese = '1937'
  WHERE survey_question_id = 112 AND
        display_index = 82;
UPDATE ag.survey_question_response 
  SET chinese = '1936'
  WHERE survey_question_id = 112 AND
        display_index = 83;
UPDATE ag.survey_question_response 
  SET chinese = '1935'
  WHERE survey_question_id = 112 AND
        display_index = 84;
UPDATE ag.survey_question_response 
  SET chinese = '1934'
  WHERE survey_question_id = 112 AND
        display_index = 85;
UPDATE ag.survey_question_response 
  SET chinese = '1933'
  WHERE survey_question_id = 112 AND
        display_index = 86;
UPDATE ag.survey_question_response 
  SET chinese = '1932'
  WHERE survey_question_id = 112 AND
        display_index = 87;
UPDATE ag.survey_question_response 
  SET chinese = '1931'
  WHERE survey_question_id = 112 AND
        display_index = 88;
UPDATE ag.survey_question_response 
  SET chinese = '1930'
  WHERE survey_question_id = 112 AND
        display_index = 89;
UPDATE ag.survey_question_response 
  SET chinese = '1929'
  WHERE survey_question_id = 112 AND
        display_index = 90;
UPDATE ag.survey_question_response 
  SET chinese = '1928'
  WHERE survey_question_id = 112 AND
        display_index = 91;
UPDATE ag.survey_question_response 
  SET chinese = '1927'
  WHERE survey_question_id = 112 AND
        display_index = 92;
UPDATE ag.survey_question_response 
  SET chinese = '1926'
  WHERE survey_question_id = 112 AND
        display_index = 93;
UPDATE ag.survey_question_response 
  SET chinese = '1925'
  WHERE survey_question_id = 112 AND
        display_index = 94;
UPDATE ag.survey_question_response 
  SET chinese = '1924'
  WHERE survey_question_id = 112 AND
        display_index = 95;
UPDATE ag.survey_question_response 
  SET chinese = '1923'
  WHERE survey_question_id = 112 AND
        display_index = 96;
UPDATE ag.survey_question_response 
  SET chinese = '1922'
  WHERE survey_question_id = 112 AND
        display_index = 97;
UPDATE ag.survey_question_response 
  SET chinese = '1921'
  WHERE survey_question_id = 112 AND
        display_index = 98;
UPDATE ag.survey_question_response 
  SET chinese = '1920'
  WHERE survey_question_id = 112 AND
        display_index = 99;
UPDATE ag.survey_question_response 
  SET chinese = '1919'
  WHERE survey_question_id = 112 AND
        display_index = 100;
UPDATE ag.survey_question_response 
  SET chinese = '1918'
  WHERE survey_question_id = 112 AND
        display_index = 101;
UPDATE ag.survey_question_response 
  SET chinese = '1917'
  WHERE survey_question_id = 112 AND
        display_index = 102;
UPDATE ag.survey_question_response 
  SET chinese = '1916'
  WHERE survey_question_id = 112 AND
        display_index = 103;
UPDATE ag.survey_question_response 
  SET chinese = '1915'
  WHERE survey_question_id = 112 AND
        display_index = 104;
UPDATE ag.survey_question_response 
  SET chinese = '1914'
  WHERE survey_question_id = 112 AND
        display_index = 105;
UPDATE ag.survey_question_response 
  SET chinese = '1913'
  WHERE survey_question_id = 112 AND
        display_index = 106;
UPDATE ag.survey_question_response 
  SET chinese = '1912'
  WHERE survey_question_id = 112 AND
        display_index = 107;
UPDATE ag.survey_question_response 
  SET chinese = '1911'
  WHERE survey_question_id = 112 AND
        display_index = 108;
UPDATE ag.survey_question_response 
  SET chinese = '1910'
  WHERE survey_question_id = 112 AND
        display_index = 109;
UPDATE ag.survey_question_response 
  SET chinese = '1909'
  WHERE survey_question_id = 112 AND
        display_index = 110;
UPDATE ag.survey_question_response 
  SET chinese = '1908'
  WHERE survey_question_id = 112 AND
        display_index = 111;
UPDATE ag.survey_question_response 
  SET chinese = '1907'
  WHERE survey_question_id = 112 AND
        display_index = 112;
UPDATE ag.survey_question_response 
  SET chinese = '1906'
  WHERE survey_question_id = 112 AND
        display_index = 113;
UPDATE ag.survey_question_response 
  SET chinese = '1905'
  WHERE survey_question_id = 112 AND
        display_index = 114;
UPDATE ag.survey_question_response 
  SET chinese = '1904'
  WHERE survey_question_id = 112 AND
        display_index = 115;
UPDATE ag.survey_question_response 
  SET chinese = '1903'
  WHERE survey_question_id = 112 AND
        display_index = 116;
UPDATE ag.survey_question_response 
  SET chinese = '1902'
  WHERE survey_question_id = 112 AND
        display_index = 117;
UPDATE ag.survey_question_response 
  SET chinese = '1901'
  WHERE survey_question_id = 112 AND
        display_index = 118;
UPDATE ag.survey_question_response 
  SET chinese = '1900'
  WHERE survey_question_id = 112 AND
        display_index = 119;
UPDATE ag.survey_question_response 
  SET chinese = '1899'
  WHERE survey_question_id = 112 AND
        display_index = 120;
UPDATE ag.survey_question_response 
  SET chinese = '1898'
  WHERE survey_question_id = 112 AND
        display_index = 121;
UPDATE ag.survey_question_response 
  SET chinese = '1897'
  WHERE survey_question_id = 112 AND
        display_index = 122;
UPDATE ag.survey_question_response 
  SET chinese = '1896'
  WHERE survey_question_id = 112 AND
        display_index = 123;
UPDATE ag.survey_question_response 
  SET chinese = '1895'
  WHERE survey_question_id = 112 AND
        display_index = 124;
UPDATE ag.survey_question_response 
  SET chinese = '1894'
  WHERE survey_question_id = 112 AND
        display_index = 125;
UPDATE ag.survey_question_response 
  SET chinese = '1893'
  WHERE survey_question_id = 112 AND
        display_index = 126;
UPDATE ag.survey_question_response 
  SET chinese = '1892'
  WHERE survey_question_id = 112 AND
        display_index = 127;
UPDATE ag.survey_question_response 
  SET chinese = '1891'
  WHERE survey_question_id = 112 AND
        display_index = 128;
UPDATE ag.survey_question_response 
  SET chinese = '1890'
  WHERE survey_question_id = 112 AND
        display_index = 129;

UPDATE ag.survey_question SET chinese = '体重：'
  WHERE survey_question_id = 113;

UPDATE ag.survey_question SET chinese = '体重单位：'
  WHERE survey_question_id = 114;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 114 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '英镑'
  WHERE survey_question_id = 114 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '公斤'
  WHERE survey_question_id = 114 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '当前邮政编码：'
  WHERE survey_question_id = 115;

UPDATE ag.survey_question SET chinese = '请写下您认为可能影响个人微生物的任何其他事情。'
  WHERE survey_question_id = 116;

UPDATE ag.survey_question SET chinese = '您的猫住在室内/室外还是受限制（笼子/箱子）：'
  WHERE survey_question_id = 117;

UPDATE ag.survey_question SET chinese = '饮食限制：'
  WHERE survey_question_id = 118;

UPDATE ag.survey_question SET chinese = '旅行：'
  WHERE survey_question_id = 119;

UPDATE ag.survey_question SET chinese = '您是否遵循除上述以外的任何其他的特殊饮食限制？'
  WHERE survey_question_id = 12;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 12 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 12 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 12 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '在本研究中，对于自愿告知您其参与本研究的人，您与其关系是什么（例如伴侣、子女、室友）？如果是子女，请说明你们是否有遗传关系。请注意，我们只会使用双方均提供的信息。'
  WHERE survey_question_id = 120;

UPDATE ag.survey_question SET chinese = '与猫的接触程度：'
  WHERE survey_question_id = 122;

UPDATE ag.survey_question SET chinese = '使用的抗生素：'
  WHERE survey_question_id = 124;

UPDATE ag.survey_question SET chinese = '用于治疗：'
  WHERE survey_question_id = 126;

UPDATE ag.survey_question SET chinese = '您家里的饮用水源是什么？'
  WHERE survey_question_id = 13;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 13 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '城市水'
  WHERE survey_question_id = 13 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '井水'
  WHERE survey_question_id = 13 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '瓶装水'
  WHERE survey_question_id = 13 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '过滤水'
  WHERE survey_question_id = 13 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 13 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您的种族/族裔是什么？'
  WHERE survey_question_id = 14;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 14 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '白种人'
  WHERE survey_question_id = 14 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '亚洲人或太平洋岛民'
  WHERE survey_question_id = 14 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '非裔美国人'
  WHERE survey_question_id = 14 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '西班牙人'
  WHERE survey_question_id = 14 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 14 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您每周吃多少种不同的植物？ 例如，如果您吃一罐含有胡萝卜、土豆和洋葱的汤，您可以把它算作 3 种不同的植物；如果您吃多谷物面包，每种不同的谷物都算作植物。'
  WHERE survey_question_id = 146;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 146 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '小于 5 种'
  WHERE survey_question_id = 146 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '6 到 10 种'
  WHERE survey_question_id = 146 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '11 到 20 种'
  WHERE survey_question_id = 146 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '21 到 30 种'
  WHERE survey_question_id = 146 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '多于 30 种'
  WHERE survey_question_id = 146 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '居住国家：'
  WHERE survey_question_id = 148;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 148 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '阿富汗'
  WHERE survey_question_id = 148 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '奥兰群岛'
  WHERE survey_question_id = 148 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '阿尔巴尼亚'
  WHERE survey_question_id = 148 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '阿尔及利亚'
  WHERE survey_question_id = 148 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '美属萨摩亚'
  WHERE survey_question_id = 148 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '安道尔'
  WHERE survey_question_id = 148 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '安哥拉'
  WHERE survey_question_id = 148 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '安圭拉岛'
  WHERE survey_question_id = 148 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '南极洲'
  WHERE survey_question_id = 148 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET chinese = '安提瓜和巴布达'
  WHERE survey_question_id = 148 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET chinese = '阿根廷'
  WHERE survey_question_id = 148 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET chinese = '亚美尼亚'
  WHERE survey_question_id = 148 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET chinese = '阿鲁巴岛'
  WHERE survey_question_id = 148 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET chinese = '澳大利亚'
  WHERE survey_question_id = 148 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET chinese = '奥地利'
  WHERE survey_question_id = 148 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET chinese = '阿塞拜疆'
  WHERE survey_question_id = 148 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET chinese = '巴哈马'
  WHERE survey_question_id = 148 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET chinese = '巴林'
  WHERE survey_question_id = 148 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET chinese = '孟加拉国'
  WHERE survey_question_id = 148 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET chinese = '巴巴多斯'
  WHERE survey_question_id = 148 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET chinese = '白俄罗斯'
  WHERE survey_question_id = 148 AND
        display_index = 21;
UPDATE ag.survey_question_response 
  SET chinese = '比利时'
  WHERE survey_question_id = 148 AND
        display_index = 22;
UPDATE ag.survey_question_response 
  SET chinese = '伯利兹'
  WHERE survey_question_id = 148 AND
        display_index = 23;
UPDATE ag.survey_question_response 
  SET chinese = '贝宁'
  WHERE survey_question_id = 148 AND
        display_index = 24;
UPDATE ag.survey_question_response 
  SET chinese = '百慕大'
  WHERE survey_question_id = 148 AND
        display_index = 25;
UPDATE ag.survey_question_response 
  SET chinese = '不丹'
  WHERE survey_question_id = 148 AND
        display_index = 26;
UPDATE ag.survey_question_response 
  SET chinese = '玻利维亚'
  WHERE survey_question_id = 148 AND
        display_index = 27;
UPDATE ag.survey_question_response 
  SET chinese = '波斯尼亚和黑塞哥维那'
  WHERE survey_question_id = 148 AND
        display_index = 28;
UPDATE ag.survey_question_response 
  SET chinese = '博茨瓦纳'
  WHERE survey_question_id = 148 AND
        display_index = 29;
UPDATE ag.survey_question_response 
  SET chinese = '布维岛'
  WHERE survey_question_id = 148 AND
        display_index = 30;
UPDATE ag.survey_question_response 
  SET chinese = '巴西'
  WHERE survey_question_id = 148 AND
        display_index = 31;
UPDATE ag.survey_question_response 
  SET chinese = '英属印度洋领地'
  WHERE survey_question_id = 148 AND
        display_index = 32;
UPDATE ag.survey_question_response 
  SET chinese = '文莱达鲁萨兰国'
  WHERE survey_question_id = 148 AND
        display_index = 33;
UPDATE ag.survey_question_response 
  SET chinese = '保加利亚'
  WHERE survey_question_id = 148 AND
        display_index = 34;
UPDATE ag.survey_question_response 
  SET chinese = '布基纳法索'
  WHERE survey_question_id = 148 AND
        display_index = 35;
UPDATE ag.survey_question_response 
  SET chinese = '布隆迪'
  WHERE survey_question_id = 148 AND
        display_index = 36;
UPDATE ag.survey_question_response 
  SET chinese = '柬埔寨'
  WHERE survey_question_id = 148 AND
        display_index = 37;
UPDATE ag.survey_question_response 
  SET chinese = '喀麦隆'
  WHERE survey_question_id = 148 AND
        display_index = 38;
UPDATE ag.survey_question_response 
  SET chinese = '加拿大'
  WHERE survey_question_id = 148 AND
        display_index = 39;
UPDATE ag.survey_question_response 
  SET chinese = '佛得角'
  WHERE survey_question_id = 148 AND
        display_index = 40;
UPDATE ag.survey_question_response 
  SET chinese = '开曼群岛'
  WHERE survey_question_id = 148 AND
        display_index = 41;
UPDATE ag.survey_question_response 
  SET chinese = '中非共和国'
  WHERE survey_question_id = 148 AND
        display_index = 42;
UPDATE ag.survey_question_response 
  SET chinese = '乍得'
  WHERE survey_question_id = 148 AND
        display_index = 43;
UPDATE ag.survey_question_response 
  SET chinese = '智利'
  WHERE survey_question_id = 148 AND
        display_index = 44;
UPDATE ag.survey_question_response 
  SET chinese = '中国'
  WHERE survey_question_id = 148 AND
        display_index = 45;
UPDATE ag.survey_question_response 
  SET chinese = '圣诞岛'
  WHERE survey_question_id = 148 AND
        display_index = 46;
UPDATE ag.survey_question_response 
  SET chinese = '科科斯（基林）群岛'
  WHERE survey_question_id = 148 AND
        display_index = 47;
UPDATE ag.survey_question_response 
  SET chinese = '哥伦比亚'
  WHERE survey_question_id = 148 AND
        display_index = 48;
UPDATE ag.survey_question_response 
  SET chinese = '科摩罗'
  WHERE survey_question_id = 148 AND
        display_index = 49;
UPDATE ag.survey_question_response 
  SET chinese = '刚果'
  WHERE survey_question_id = 148 AND
        display_index = 50;
UPDATE ag.survey_question_response 
  SET chinese = '刚果民主共和国'
  WHERE survey_question_id = 148 AND
        display_index = 51;
UPDATE ag.survey_question_response 
  SET chinese = '库克群岛'
  WHERE survey_question_id = 148 AND
        display_index = 52;
UPDATE ag.survey_question_response 
  SET chinese = '哥斯达黎加'
  WHERE survey_question_id = 148 AND
        display_index = 53;
UPDATE ag.survey_question_response 
  SET chinese = '科特迪瓦'
  WHERE survey_question_id = 148 AND
        display_index = 54;
UPDATE ag.survey_question_response 
  SET chinese = '克罗地亚'
  WHERE survey_question_id = 148 AND
        display_index = 55;
UPDATE ag.survey_question_response 
  SET chinese = '古巴'
  WHERE survey_question_id = 148 AND
        display_index = 56;
UPDATE ag.survey_question_response 
  SET chinese = '塞浦路斯'
  WHERE survey_question_id = 148 AND
        display_index = 57;
UPDATE ag.survey_question_response 
  SET chinese = '捷克共和国'
  WHERE survey_question_id = 148 AND
        display_index = 58;
UPDATE ag.survey_question_response 
  SET chinese = '丹麦'
  WHERE survey_question_id = 148 AND
        display_index = 59;
UPDATE ag.survey_question_response 
  SET chinese = '吉布地'
  WHERE survey_question_id = 148 AND
        display_index = 60;
UPDATE ag.survey_question_response 
  SET chinese = '多米尼加'
  WHERE survey_question_id = 148 AND
        display_index = 61;
UPDATE ag.survey_question_response 
  SET chinese = '多明尼加共和国'
  WHERE survey_question_id = 148 AND
        display_index = 62;
UPDATE ag.survey_question_response 
  SET chinese = '厄瓜多尔'
  WHERE survey_question_id = 148 AND
        display_index = 63;
UPDATE ag.survey_question_response 
  SET chinese = '埃及'
  WHERE survey_question_id = 148 AND
        display_index = 64;
UPDATE ag.survey_question_response 
  SET chinese = '萨尔瓦多'
  WHERE survey_question_id = 148 AND
        display_index = 65;
UPDATE ag.survey_question_response 
  SET chinese = '赤道几内亚'
  WHERE survey_question_id = 148 AND
        display_index = 66;
UPDATE ag.survey_question_response 
  SET chinese = '厄立特里亚'
  WHERE survey_question_id = 148 AND
        display_index = 67;
UPDATE ag.survey_question_response 
  SET chinese = '爱沙尼亚'
  WHERE survey_question_id = 148 AND
        display_index = 68;
UPDATE ag.survey_question_response 
  SET chinese = '埃塞俄比亚'
  WHERE survey_question_id = 148 AND
        display_index = 69;
UPDATE ag.survey_question_response 
  SET chinese = '福克兰群岛（马尔维纳斯）'
  WHERE survey_question_id = 148 AND
        display_index = 70;
UPDATE ag.survey_question_response 
  SET chinese = '法罗群岛'
  WHERE survey_question_id = 148 AND
        display_index = 71;
UPDATE ag.survey_question_response 
  SET chinese = '斐济'
  WHERE survey_question_id = 148 AND
        display_index = 72;
UPDATE ag.survey_question_response 
  SET chinese = '芬兰'
  WHERE survey_question_id = 148 AND
        display_index = 73;
UPDATE ag.survey_question_response 
  SET chinese = '法国'
  WHERE survey_question_id = 148 AND
        display_index = 74;
UPDATE ag.survey_question_response 
  SET chinese = '法属圭亚那'
  WHERE survey_question_id = 148 AND
        display_index = 75;
UPDATE ag.survey_question_response 
  SET chinese = '法属波利尼西亚'
  WHERE survey_question_id = 148 AND
        display_index = 76;
UPDATE ag.survey_question_response 
  SET chinese = '法属南部领地'
  WHERE survey_question_id = 148 AND
        display_index = 77;
UPDATE ag.survey_question_response 
  SET chinese = '加蓬'
  WHERE survey_question_id = 148 AND
        display_index = 78;
UPDATE ag.survey_question_response 
  SET chinese = '冈比亚'
  WHERE survey_question_id = 148 AND
        display_index = 79;
UPDATE ag.survey_question_response 
  SET chinese = '佐治亚州'
  WHERE survey_question_id = 148 AND
        display_index = 80;
UPDATE ag.survey_question_response 
  SET chinese = '德国'
  WHERE survey_question_id = 148 AND
        display_index = 81;
UPDATE ag.survey_question_response 
  SET chinese = '加纳'
  WHERE survey_question_id = 148 AND
        display_index = 82;
UPDATE ag.survey_question_response 
  SET chinese = '直布罗陀'
  WHERE survey_question_id = 148 AND
        display_index = 83;
UPDATE ag.survey_question_response 
  SET chinese = '希腊'
  WHERE survey_question_id = 148 AND
        display_index = 84;
UPDATE ag.survey_question_response 
  SET chinese = '格陵兰'
  WHERE survey_question_id = 148 AND
        display_index = 85;
UPDATE ag.survey_question_response 
  SET chinese = '格林纳达'
  WHERE survey_question_id = 148 AND
        display_index = 86;
UPDATE ag.survey_question_response 
  SET chinese = '瓜德罗普岛'
  WHERE survey_question_id = 148 AND
        display_index = 87;
UPDATE ag.survey_question_response 
  SET chinese = '关岛'
  WHERE survey_question_id = 148 AND
        display_index = 88;
UPDATE ag.survey_question_response 
  SET chinese = '危地马拉'
  WHERE survey_question_id = 148 AND
        display_index = 89;
UPDATE ag.survey_question_response 
  SET chinese = '根西岛'
  WHERE survey_question_id = 148 AND
        display_index = 90;
UPDATE ag.survey_question_response 
  SET chinese = '几内亚'
  WHERE survey_question_id = 148 AND
        display_index = 91;
UPDATE ag.survey_question_response 
  SET chinese = '几内亚比绍'
  WHERE survey_question_id = 148 AND
        display_index = 92;
UPDATE ag.survey_question_response 
  SET chinese = '圭亚那'
  WHERE survey_question_id = 148 AND
        display_index = 93;
UPDATE ag.survey_question_response 
  SET chinese = '海地'
  WHERE survey_question_id = 148 AND
        display_index = 94;
UPDATE ag.survey_question_response 
  SET chinese = '希尔德岛和麦当劳群岛'
  WHERE survey_question_id = 148 AND
        display_index = 95;
UPDATE ag.survey_question_response 
  SET chinese = '罗马教廷（梵蒂冈城国）'
  WHERE survey_question_id = 148 AND
        display_index = 96;
UPDATE ag.survey_question_response 
  SET chinese = '洪都拉斯'
  WHERE survey_question_id = 148 AND
        display_index = 97;
UPDATE ag.survey_question_response 
  SET chinese = '香港'
  WHERE survey_question_id = 148 AND
        display_index = 98;
UPDATE ag.survey_question_response 
  SET chinese = '匈牙利'
  WHERE survey_question_id = 148 AND
        display_index = 99;
UPDATE ag.survey_question_response 
  SET chinese = '冰岛'
  WHERE survey_question_id = 148 AND
        display_index = 100;
UPDATE ag.survey_question_response 
  SET chinese = '印度'
  WHERE survey_question_id = 148 AND
        display_index = 101;
UPDATE ag.survey_question_response 
  SET chinese = '印度尼西亚'
  WHERE survey_question_id = 148 AND
        display_index = 102;
UPDATE ag.survey_question_response 
  SET chinese = '伊朗伊斯兰共和国'
  WHERE survey_question_id = 148 AND
        display_index = 103;
UPDATE ag.survey_question_response 
  SET chinese = '伊拉克'
  WHERE survey_question_id = 148 AND
        display_index = 104;
UPDATE ag.survey_question_response 
  SET chinese = '爱尔兰'
  WHERE survey_question_id = 148 AND
        display_index = 105;
UPDATE ag.survey_question_response 
  SET chinese = '马恩岛'
  WHERE survey_question_id = 148 AND
        display_index = 106;
UPDATE ag.survey_question_response 
  SET chinese = '以色列'
  WHERE survey_question_id = 148 AND
        display_index = 107;
UPDATE ag.survey_question_response 
  SET chinese = '意大利'
  WHERE survey_question_id = 148 AND
        display_index = 108;
UPDATE ag.survey_question_response 
  SET chinese = '牙买加'
  WHERE survey_question_id = 148 AND
        display_index = 109;
UPDATE ag.survey_question_response 
  SET chinese = '日本'
  WHERE survey_question_id = 148 AND
        display_index = 110;
UPDATE ag.survey_question_response 
  SET chinese = '泽西岛'
  WHERE survey_question_id = 148 AND
        display_index = 111;
UPDATE ag.survey_question_response 
  SET chinese = '约旦'
  WHERE survey_question_id = 148 AND
        display_index = 112;
UPDATE ag.survey_question_response 
  SET chinese = '哈萨克斯坦'
  WHERE survey_question_id = 148 AND
        display_index = 113;
UPDATE ag.survey_question_response 
  SET chinese = '肯尼亚'
  WHERE survey_question_id = 148 AND
        display_index = 114;
UPDATE ag.survey_question_response 
  SET chinese = '基里巴斯'
  WHERE survey_question_id = 148 AND
        display_index = 115;
UPDATE ag.survey_question_response 
  SET chinese = '韩国，朝鲜民主主义人民共和国'
  WHERE survey_question_id = 148 AND
        display_index = 116;
UPDATE ag.survey_question_response 
  SET chinese = '韩国'
  WHERE survey_question_id = 148 AND
        display_index = 117;
UPDATE ag.survey_question_response 
  SET chinese = '科威特'
  WHERE survey_question_id = 148 AND
        display_index = 118;
UPDATE ag.survey_question_response 
  SET chinese = '吉尔吉斯斯坦'
  WHERE survey_question_id = 148 AND
        display_index = 119;
UPDATE ag.survey_question_response 
  SET chinese = '老挝人民民主共和国'
  WHERE survey_question_id = 148 AND
        display_index = 120;
UPDATE ag.survey_question_response 
  SET chinese = '拉脱维亚'
  WHERE survey_question_id = 148 AND
        display_index = 121;
UPDATE ag.survey_question_response 
  SET chinese = '黎巴嫩'
  WHERE survey_question_id = 148 AND
        display_index = 122;
UPDATE ag.survey_question_response 
  SET chinese = '莱索托'
  WHERE survey_question_id = 148 AND
        display_index = 123;
UPDATE ag.survey_question_response 
  SET chinese = '利比里亚'
  WHERE survey_question_id = 148 AND
        display_index = 124;
UPDATE ag.survey_question_response 
  SET chinese = '阿拉伯利比亚民众国'
  WHERE survey_question_id = 148 AND
        display_index = 125;
UPDATE ag.survey_question_response 
  SET chinese = '列支敦士登'
  WHERE survey_question_id = 148 AND
        display_index = 126;
UPDATE ag.survey_question_response 
  SET chinese = '立陶宛'
  WHERE survey_question_id = 148 AND
        display_index = 127;
UPDATE ag.survey_question_response 
  SET chinese = '卢森堡'
  WHERE survey_question_id = 148 AND
        display_index = 128;
UPDATE ag.survey_question_response 
  SET chinese = '澳门'
  WHERE survey_question_id = 148 AND
        display_index = 129;
UPDATE ag.survey_question_response 
  SET chinese = '马其顿，前南斯拉夫共和国'
  WHERE survey_question_id = 148 AND
        display_index = 130;
UPDATE ag.survey_question_response 
  SET chinese = '马达加斯加'
  WHERE survey_question_id = 148 AND
        display_index = 131;
UPDATE ag.survey_question_response 
  SET chinese = '马拉维'
  WHERE survey_question_id = 148 AND
        display_index = 132;
UPDATE ag.survey_question_response 
  SET chinese = '马来西亚'
  WHERE survey_question_id = 148 AND
        display_index = 133;
UPDATE ag.survey_question_response 
  SET chinese = '马尔代夫'
  WHERE survey_question_id = 148 AND
        display_index = 134;
UPDATE ag.survey_question_response 
  SET chinese = '马里'
  WHERE survey_question_id = 148 AND
        display_index = 135;
UPDATE ag.survey_question_response 
  SET chinese = '马耳他'
  WHERE survey_question_id = 148 AND
        display_index = 136;
UPDATE ag.survey_question_response 
  SET chinese = '马绍尔群岛'
  WHERE survey_question_id = 148 AND
        display_index = 137;
UPDATE ag.survey_question_response 
  SET chinese = '马提尼克岛'
  WHERE survey_question_id = 148 AND
        display_index = 138;
UPDATE ag.survey_question_response 
  SET chinese = '毛里塔尼亚'
  WHERE survey_question_id = 148 AND
        display_index = 139;
UPDATE ag.survey_question_response 
  SET chinese = '毛里求斯'
  WHERE survey_question_id = 148 AND
        display_index = 140;
UPDATE ag.survey_question_response 
  SET chinese = '马约特岛'
  WHERE survey_question_id = 148 AND
        display_index = 141;
UPDATE ag.survey_question_response 
  SET chinese = '墨西哥'
  WHERE survey_question_id = 148 AND
        display_index = 142;
UPDATE ag.survey_question_response 
  SET chinese = '密克罗尼西亚联邦'
  WHERE survey_question_id = 148 AND
        display_index = 143;
UPDATE ag.survey_question_response 
  SET chinese = '摩尔多瓦共和国'
  WHERE survey_question_id = 148 AND
        display_index = 144;
UPDATE ag.survey_question_response 
  SET chinese = '摩纳哥'
  WHERE survey_question_id = 148 AND
        display_index = 145;
UPDATE ag.survey_question_response 
  SET chinese = '蒙古'
  WHERE survey_question_id = 148 AND
        display_index = 146;
UPDATE ag.survey_question_response 
  SET chinese = '黑山共和国'
  WHERE survey_question_id = 148 AND
        display_index = 147;
UPDATE ag.survey_question_response 
  SET chinese = '蒙特塞拉特'
  WHERE survey_question_id = 148 AND
        display_index = 148;
UPDATE ag.survey_question_response 
  SET chinese = '摩洛哥'
  WHERE survey_question_id = 148 AND
        display_index = 149;
UPDATE ag.survey_question_response 
  SET chinese = '莫桑比克'
  WHERE survey_question_id = 148 AND
        display_index = 150;
UPDATE ag.survey_question_response 
  SET chinese = '缅甸'
  WHERE survey_question_id = 148 AND
        display_index = 151;
UPDATE ag.survey_question_response 
  SET chinese = '纳米比亚'
  WHERE survey_question_id = 148 AND
        display_index = 152;
UPDATE ag.survey_question_response 
  SET chinese = '瑙鲁'
  WHERE survey_question_id = 148 AND
        display_index = 153;
UPDATE ag.survey_question_response 
  SET chinese = '尼泊尔'
  WHERE survey_question_id = 148 AND
        display_index = 154;
UPDATE ag.survey_question_response 
  SET chinese = '荷兰'
  WHERE survey_question_id = 148 AND
        display_index = 155;
UPDATE ag.survey_question_response 
  SET chinese = '荷属安的列斯'
  WHERE survey_question_id = 148 AND
        display_index = 156;
UPDATE ag.survey_question_response 
  SET chinese = '新喀里多尼亚'
  WHERE survey_question_id = 148 AND
        display_index = 157;
UPDATE ag.survey_question_response 
  SET chinese = '新西兰'
  WHERE survey_question_id = 148 AND
        display_index = 158;
UPDATE ag.survey_question_response 
  SET chinese = '尼加拉瓜'
  WHERE survey_question_id = 148 AND
        display_index = 159;
UPDATE ag.survey_question_response 
  SET chinese = '尼日尔'
  WHERE survey_question_id = 148 AND
        display_index = 160;
UPDATE ag.survey_question_response 
  SET chinese = '奈及利亚'
  WHERE survey_question_id = 148 AND
        display_index = 161;
UPDATE ag.survey_question_response 
  SET chinese = '纽埃'
  WHERE survey_question_id = 148 AND
        display_index = 162;
UPDATE ag.survey_question_response 
  SET chinese = '诺福克岛'
  WHERE survey_question_id = 148 AND
        display_index = 163;
UPDATE ag.survey_question_response 
  SET chinese = '北马里亚纳群岛'
  WHERE survey_question_id = 148 AND
        display_index = 164;
UPDATE ag.survey_question_response 
  SET chinese = '挪威'
  WHERE survey_question_id = 148 AND
        display_index = 165;
UPDATE ag.survey_question_response 
  SET chinese = '阿曼'
  WHERE survey_question_id = 148 AND
        display_index = 166;
UPDATE ag.survey_question_response 
  SET chinese = '巴基斯坦'
  WHERE survey_question_id = 148 AND
        display_index = 167;
UPDATE ag.survey_question_response 
  SET chinese = 'u琉'
  WHERE survey_question_id = 148 AND
        display_index = 168;
UPDATE ag.survey_question_response 
  SET chinese = '被占领的巴勒斯坦领土'
  WHERE survey_question_id = 148 AND
        display_index = 169;
UPDATE ag.survey_question_response 
  SET chinese = '巴拿马'
  WHERE survey_question_id = 148 AND
        display_index = 170;
UPDATE ag.survey_question_response 
  SET chinese = '巴布亚新几内亚'
  WHERE survey_question_id = 148 AND
        display_index = 171;
UPDATE ag.survey_question_response 
  SET chinese = '巴拉圭'
  WHERE survey_question_id = 148 AND
        display_index = 172;
UPDATE ag.survey_question_response 
  SET chinese = '秘鲁'
  WHERE survey_question_id = 148 AND
        display_index = 173;
UPDATE ag.survey_question_response 
  SET chinese = '菲律宾'
  WHERE survey_question_id = 148 AND
        display_index = 174;
UPDATE ag.survey_question_response 
  SET chinese = '皮特凯恩'
  WHERE survey_question_id = 148 AND
        display_index = 175;
UPDATE ag.survey_question_response 
  SET chinese = '波兰'
  WHERE survey_question_id = 148 AND
        display_index = 176;
UPDATE ag.survey_question_response 
  SET chinese = '葡萄牙'
  WHERE survey_question_id = 148 AND
        display_index = 177;
UPDATE ag.survey_question_response 
  SET chinese = '波多黎各'
  WHERE survey_question_id = 148 AND
        display_index = 178;
UPDATE ag.survey_question_response 
  SET chinese = '卡塔尔'
  WHERE survey_question_id = 148 AND
        display_index = 179;
UPDATE ag.survey_question_response 
  SET chinese = '团圆'
  WHERE survey_question_id = 148 AND
        display_index = 180;
UPDATE ag.survey_question_response 
  SET chinese = '罗马尼亚'
  WHERE survey_question_id = 148 AND
        display_index = 181;
UPDATE ag.survey_question_response 
  SET chinese = '俄罗斯联邦'
  WHERE survey_question_id = 148 AND
        display_index = 182;
UPDATE ag.survey_question_response 
  SET chinese = '卢旺达'
  WHERE survey_question_id = 148 AND
        display_index = 183;
UPDATE ag.survey_question_response 
  SET chinese = '圣海伦娜'
  WHERE survey_question_id = 148 AND
        display_index = 184;
UPDATE ag.survey_question_response 
  SET chinese = '圣基茨和尼维斯'
  WHERE survey_question_id = 148 AND
        display_index = 185;
UPDATE ag.survey_question_response 
  SET chinese = '圣卢西亚'
  WHERE survey_question_id = 148 AND
        display_index = 186;
UPDATE ag.survey_question_response 
  SET chinese = '圣皮埃尔和密克隆群岛'
  WHERE survey_question_id = 148 AND
        display_index = 187;
UPDATE ag.survey_question_response 
  SET chinese = '圣文森特和格林纳丁斯'
  WHERE survey_question_id = 148 AND
        display_index = 188;
UPDATE ag.survey_question_response 
  SET chinese = '萨摩亚'
  WHERE survey_question_id = 148 AND
        display_index = 189;
UPDATE ag.survey_question_response 
  SET chinese = '圣马力诺'
  WHERE survey_question_id = 148 AND
        display_index = 190;
UPDATE ag.survey_question_response 
  SET chinese = '圣多美和普林西比'
  WHERE survey_question_id = 148 AND
        display_index = 191;
UPDATE ag.survey_question_response 
  SET chinese = '沙特阿拉伯'
  WHERE survey_question_id = 148 AND
        display_index = 192;
UPDATE ag.survey_question_response 
  SET chinese = '塞内加尔'
  WHERE survey_question_id = 148 AND
        display_index = 193;
UPDATE ag.survey_question_response 
  SET chinese = '塞尔维亚'
  WHERE survey_question_id = 148 AND
        display_index = 194;
UPDATE ag.survey_question_response 
  SET chinese = '塞舌尔'
  WHERE survey_question_id = 148 AND
        display_index = 195;
UPDATE ag.survey_question_response 
  SET chinese = '塞拉利昂'
  WHERE survey_question_id = 148 AND
        display_index = 196;
UPDATE ag.survey_question_response 
  SET chinese = '新加坡'
  WHERE survey_question_id = 148 AND
        display_index = 197;
UPDATE ag.survey_question_response 
  SET chinese = '斯洛伐克'
  WHERE survey_question_id = 148 AND
        display_index = 198;
UPDATE ag.survey_question_response 
  SET chinese = '斯洛文尼亚'
  WHERE survey_question_id = 148 AND
        display_index = 199;
UPDATE ag.survey_question_response 
  SET chinese = '所罗门群岛'
  WHERE survey_question_id = 148 AND
        display_index = 200;
UPDATE ag.survey_question_response 
  SET chinese = '索马里'
  WHERE survey_question_id = 148 AND
        display_index = 201;
UPDATE ag.survey_question_response 
  SET chinese = '南非'
  WHERE survey_question_id = 148 AND
        display_index = 202;
UPDATE ag.survey_question_response 
  SET chinese = '南乔治亚岛和南桑威奇群岛'
  WHERE survey_question_id = 148 AND
        display_index = 203;
UPDATE ag.survey_question_response 
  SET chinese = '西班牙'
  WHERE survey_question_id = 148 AND
        display_index = 204;
UPDATE ag.survey_question_response 
  SET chinese = '斯里兰卡'
  WHERE survey_question_id = 148 AND
        display_index = 205;
UPDATE ag.survey_question_response 
  SET chinese = '苏丹'
  WHERE survey_question_id = 148 AND
        display_index = 206;
UPDATE ag.survey_question_response 
  SET chinese = '苏里南'
  WHERE survey_question_id = 148 AND
        display_index = 207;
UPDATE ag.survey_question_response 
  SET chinese = '斯瓦尔巴和扬·马延'
  WHERE survey_question_id = 148 AND
        display_index = 208;
UPDATE ag.survey_question_response 
  SET chinese = '斯威士兰'
  WHERE survey_question_id = 148 AND
        display_index = 209;
UPDATE ag.survey_question_response 
  SET chinese = '瑞典'
  WHERE survey_question_id = 148 AND
        display_index = 210;
UPDATE ag.survey_question_response 
  SET chinese = '瑞士'
  WHERE survey_question_id = 148 AND
        display_index = 211;
UPDATE ag.survey_question_response 
  SET chinese = '阿拉伯叙利亚共和国'
  WHERE survey_question_id = 148 AND
        display_index = 212;
UPDATE ag.survey_question_response 
  SET chinese = '中国台湾省'
  WHERE survey_question_id = 148 AND
        display_index = 213;
UPDATE ag.survey_question_response 
  SET chinese = '塔吉克斯坦'
  WHERE survey_question_id = 148 AND
        display_index = 214;
UPDATE ag.survey_question_response 
  SET chinese = '坦桑尼亚联合共和国'
  WHERE survey_question_id = 148 AND
        display_index = 215;
UPDATE ag.survey_question_response 
  SET chinese = '泰国'
  WHERE survey_question_id = 148 AND
        display_index = 216;
UPDATE ag.survey_question_response 
  SET chinese = '东帝汶'
  WHERE survey_question_id = 148 AND
        display_index = 217;
UPDATE ag.survey_question_response 
  SET chinese = '多哥'
  WHERE survey_question_id = 148 AND
        display_index = 218;
UPDATE ag.survey_question_response 
  SET chinese = '托克劳'
  WHERE survey_question_id = 148 AND
        display_index = 219;
UPDATE ag.survey_question_response 
  SET chinese = '汤加'
  WHERE survey_question_id = 148 AND
        display_index = 220;
UPDATE ag.survey_question_response 
  SET chinese = '特立尼达和多巴哥'
  WHERE survey_question_id = 148 AND
        display_index = 221;
UPDATE ag.survey_question_response 
  SET chinese = '突尼斯'
  WHERE survey_question_id = 148 AND
        display_index = 222;
UPDATE ag.survey_question_response 
  SET chinese = '火鸡'
  WHERE survey_question_id = 148 AND
        display_index = 223;
UPDATE ag.survey_question_response 
  SET chinese = '土库曼斯坦'
  WHERE survey_question_id = 148 AND
        display_index = 224;
UPDATE ag.survey_question_response 
  SET chinese = '特克斯和凯科斯群岛'
  WHERE survey_question_id = 148 AND
        display_index = 225;
UPDATE ag.survey_question_response 
  SET chinese = '图瓦卢'
  WHERE survey_question_id = 148 AND
        display_index = 226;
UPDATE ag.survey_question_response 
  SET chinese = '乌干达'
  WHERE survey_question_id = 148 AND
        display_index = 227;
UPDATE ag.survey_question_response 
  SET chinese = '乌克兰'
  WHERE survey_question_id = 148 AND
        display_index = 228;
UPDATE ag.survey_question_response 
  SET chinese = '阿拉伯联合酋长国'
  WHERE survey_question_id = 148 AND
        display_index = 229;
UPDATE ag.survey_question_response 
  SET chinese = '英国'
  WHERE survey_question_id = 148 AND
        display_index = 230;
UPDATE ag.survey_question_response 
  SET chinese = '美国'
  WHERE survey_question_id = 148 AND
        display_index = 231;
UPDATE ag.survey_question_response 
  SET chinese = '美国本土外小岛屿'
  WHERE survey_question_id = 148 AND
        display_index = 232;
UPDATE ag.survey_question_response 
  SET chinese = '乌拉圭'
  WHERE survey_question_id = 148 AND
        display_index = 233;
UPDATE ag.survey_question_response 
  SET chinese = '乌兹别克斯坦'
  WHERE survey_question_id = 148 AND
        display_index = 234;
UPDATE ag.survey_question_response 
  SET chinese = '瓦努阿图'
  WHERE survey_question_id = 148 AND
        display_index = 235;
UPDATE ag.survey_question_response 
  SET chinese = '委内瑞拉'
  WHERE survey_question_id = 148 AND
        display_index = 236;
UPDATE ag.survey_question_response 
  SET chinese = '越南'
  WHERE survey_question_id = 148 AND
        display_index = 237;
UPDATE ag.survey_question_response 
  SET chinese = '英属维尔京群岛'
  WHERE survey_question_id = 148 AND
        display_index = 238;
UPDATE ag.survey_question_response 
  SET chinese = '美国维尔京群岛'
  WHERE survey_question_id = 148 AND
        display_index = 239;
UPDATE ag.survey_question_response 
  SET chinese = '瓦利斯和富图纳群岛'
  WHERE survey_question_id = 148 AND
        display_index = 240;
UPDATE ag.survey_question_response 
  SET chinese = '撒哈拉沙漠西部'
  WHERE survey_question_id = 148 AND
        display_index = 241;
UPDATE ag.survey_question_response 
  SET chinese = '也门'
  WHERE survey_question_id = 148 AND
        display_index = 242;
UPDATE ag.survey_question_response 
  SET chinese = '赞比亚'
  WHERE survey_question_id = 148 AND
        display_index = 243;
UPDATE ag.survey_question_response 
  SET chinese = '津巴布韦'
  WHERE survey_question_id = 148 AND
        display_index = 244;

UPDATE ag.survey_question SET chinese = '您有其他宠物吗？'
  WHERE survey_question_id = 149;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 149 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 149 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 149 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您什么时候搬到目前的居住地？'
  WHERE survey_question_id = 15;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 15 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '在过去的一个月内'
  WHERE survey_question_id = 15 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '在过去的 3 个月内'
  WHERE survey_question_id = 15 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '在过去的 6 个月内'
  WHERE survey_question_id = 15 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '在过去的一年内'
  WHERE survey_question_id = 15 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '我居住在目前的居住地超过一年。'
  WHERE survey_question_id = 15 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '请列出宠物'
  WHERE survey_question_id = 150;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有心理健康疾病吗？'
  WHERE survey_question_id = 153;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 153 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 153 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 153 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '请从以下列表中选出该疾病：'
  WHERE survey_question_id = 154;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 154 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '抑郁症'
  WHERE survey_question_id = 154 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '双相情感障碍'
  WHERE survey_question_id = 154 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = 'PTSD（创伤后应激障碍）'
  WHERE survey_question_id = 154 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '精神分裂症'
  WHERE survey_question_id = 154 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '神经性厌食症'
  WHERE survey_question_id = 154 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '神经性贪食症'
  WHERE survey_question_id = 154 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '药物滥用'
  WHERE survey_question_id = 154 AND
        display_index = 7;

UPDATE ag.survey_question SET chinese = '哪一类型的糖尿病？'
  WHERE survey_question_id = 155;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 155 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = 'I 型糖尿病'
  WHERE survey_question_id = 155 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = 'II 型糖尿病'
  WHERE survey_question_id = 155 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '妊娠期糖尿病'
  WHERE survey_question_id = 155 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您有逼真和/或可怕的梦吗？'
  WHERE survey_question_id = 156;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 156 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 156 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 156 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 156 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 156 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 156 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '是否饮用含甜味剂的饮料？'
  WHERE survey_question_id = 157;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 157 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 157 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 157 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 157 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 157 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 157 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有癌症吗？'
  WHERE survey_question_id = 158;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 158 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 158 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 158 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 158 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 158 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '如果您曾经被诊断出患有癌症，是如何治疗的呢？'
  WHERE survey_question_id = 159;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 159 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '没有治疗'
  WHERE survey_question_id = 159 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '仅应用手术治疗'
  WHERE survey_question_id = 159 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '化疗'
  WHERE survey_question_id = 159 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '放疗'
  WHERE survey_question_id = 159 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '我在过去的 _________内曾到我居住国家之外的地区旅行。'
  WHERE survey_question_id = 16;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 16 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '1 个月'
  WHERE survey_question_id = 16 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '3 个月'
  WHERE survey_question_id = 16 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '6 个月'
  WHERE survey_question_id = 16 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '1 年'
  WHERE survey_question_id = 16 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '我在过去的一年内未曾到我居住国家之外的地区旅行。'
  WHERE survey_question_id = 16 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有胃酸反流或 GERD（胃食管反流病）吗？'
  WHERE survey_question_id = 160;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 160 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 160 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 160 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 160 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 160 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '哪种类型的炎症性肠病（IBD）？'
  WHERE survey_question_id = 161;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 161 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '溃疡性结肠炎'
  WHERE survey_question_id = 161 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '克罗恩病'
  WHERE survey_question_id = 161 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您应用特定的饮食吗?（选择所有适用项目）'
  WHERE survey_question_id = 162;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 162 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '旧石器时代饮食或远古饮食'
  WHERE survey_question_id = 162 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '改良的旧石器时代饮食'
  WHERE survey_question_id = 162 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '生食饮食'
  WHERE survey_question_id = 162 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = 'FODMAP'
  WHERE survey_question_id = 162 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = 'Weston-Price 或其他低谷物、低加工饮食'
  WHERE survey_question_id = 162 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '犹太食物'
  WHERE survey_question_id = 162 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '清真食物'
  WHERE survey_question_id = 162 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '排除茄属植物'
  WHERE survey_question_id = 162 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '排除乳制品'
  WHERE survey_question_id = 162 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET chinese = '排除精制糖'
  WHERE survey_question_id = 162 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET chinese = '此处未描述的其他限制'
  WHERE survey_question_id = 162 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET chinese = '我不吃特定的饮食'
  WHERE survey_question_id = 162 AND
        display_index = 12;

UPDATE ag.survey_question SET chinese = '喝酒时通常会喝多少单位酒精饮料？'
  WHERE survey_question_id = 163;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 163 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '1'
  WHERE survey_question_id = 163 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '1-2'
  WHERE survey_question_id = 163 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '2-3'
  WHERE survey_question_id = 163 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '3-4'
  WHERE survey_question_id = 163 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '4+'
  WHERE survey_question_id = 163 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '我不喝酒'
  WHERE survey_question_id = 163 AND
        display_index = 6;

UPDATE ag.survey_question SET chinese = '您患有哪一种类型的炎性肠病（IBD）'
  WHERE survey_question_id = 164;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 164 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '回肠克罗恩病'
  WHERE survey_question_id = 164 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '结肠克罗恩病'
  WHERE survey_question_id = 164 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '回肠和结肠克罗恩病'
  WHERE survey_question_id = 164 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '溃疡性结肠炎'
  WHERE survey_question_id = 164 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '显微镜结肠炎'
  WHERE survey_question_id = 164 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您有多少非家庭成员的室友？'
  WHERE survey_question_id = 17;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 17 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '无'
  WHERE survey_question_id = 17 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '一个'
  WHERE survey_question_id = 17 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '两个'
  WHERE survey_question_id = 17 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '三个'
  WHERE survey_question_id = 17 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '多于三个'
  WHERE survey_question_id = 17 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您的室友中是否有人参加了这项研究？'
  WHERE survey_question_id = 18;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 18 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 18 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 18 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 18 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您是否与本研究中的任何其他参与者有亲属关系或生活在一起？'
  WHERE survey_question_id = 19;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 19 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 19 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 19 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 19 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您每天服用多种维生素吗？'
  WHERE survey_question_id = 2;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 2 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 2 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 2 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您养狗吗?'
  WHERE survey_question_id = 20;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 20 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 20 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 20 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您养猫吗？'
  WHERE survey_question_id = 21;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 21 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 21 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 21 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您的优势手是哪一只？'
  WHERE survey_question_id = 22;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 22 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我的右手是优势手'
  WHERE survey_question_id = 22 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '我的左手是优势手'
  WHERE survey_question_id = 22 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '我的两只手都是优势手'
  WHERE survey_question_id = 22 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您的最高学历是什么？'
  WHERE survey_question_id = 23;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 23 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '没上完高中'
  WHERE survey_question_id = 23 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '高中或高中同等学历（GED）'
  WHERE survey_question_id = 23 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '大学或技术学校'
  WHERE survey_question_id = 23 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '副学士学位'
  WHERE survey_question_id = 23 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '学士学位'
  WHERE survey_question_id = 23 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '研究生院或专业教育'
  WHERE survey_question_id = 23 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '研究生或专业学位'
  WHERE survey_question_id = 23 AND
        display_index = 7;

UPDATE ag.survey_question SET chinese = '您多久锻炼一次？'
  WHERE survey_question_id = 24;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 24 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 24 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 24 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 24 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 24 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 24 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您通常在室内还是在室外锻炼？'
  WHERE survey_question_id = 25;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 25 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '室内'
  WHERE survey_question_id = 25 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '室外'
  WHERE survey_question_id = 25 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '两者都有'
  WHERE survey_question_id = 25 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '取决于季节'
  WHERE survey_question_id = 25 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '以上都不是'
  WHERE survey_question_id = 25 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您咬指甲吗？'
  WHERE survey_question_id = 26;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 26 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 26 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 26 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您多久使用一次游泳池/热水浴缸？'
  WHERE survey_question_id = 27;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 27 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 27 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 27 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 27 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 27 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 27 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您吸烟的频率是多少？'
  WHERE survey_question_id = 28;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 28 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 28 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 28 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 28 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 28 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 28 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您多久喝一次酒？'
  WHERE survey_question_id = 29;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 29 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 29 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 29 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 29 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 29 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 29 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您多久食用一次益生菌？'
  WHERE survey_question_id = 3;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 3 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 3 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 3 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次 /周）'
  WHERE survey_question_id = 3 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 3 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 3 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您通常饮用哪种类型的酒精（选择所有适用项）？'
  WHERE survey_question_id = 30;

UPDATE ag.survey_question_response 
  SET chinese = '啤酒/苹果酒'
  WHERE survey_question_id = 30 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '酸啤酒'
  WHERE survey_question_id = 30 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '白酒'
  WHERE survey_question_id = 30 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '红酒'
  WHERE survey_question_id = 30 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '烈酒饮料/烈酒'
  WHERE survey_question_id = 30 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 30 AND
        display_index = 999;

UPDATE ag.survey_question SET chinese = '您多久刷一次牙齿？'
  WHERE survey_question_id = 31;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 31 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 31 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（每天不到一次）'
  WHERE survey_question_id = 31 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '经常（每天 1-2 次）'
  WHERE survey_question_id = 31 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '频繁（每天 2 次以上）'
  WHERE survey_question_id = 31 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 31 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您多久用牙线剔牙一次？'
  WHERE survey_question_id = 32;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 32 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 32 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 32 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 32 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 32 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 32 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您多久应用一次面部化妆品？'
  WHERE survey_question_id = 33;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 33 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 33 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 33 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 33 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 33 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 33 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您应用除臭剂或止汗剂（止汗剂通常含有铝）吗？'
  WHERE survey_question_id = 34;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 34 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我用除臭剂'
  WHERE survey_question_id = 34 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '我用止汗剂'
  WHERE survey_question_id = 34 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '不确定，但我使用某种类型的除臭剂/止汗剂'
  WHERE survey_question_id = 34 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '我不使用除臭剂或止汗剂'
  WHERE survey_question_id = 34 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您平均每晚睡多少个小时？'
  WHERE survey_question_id = 35;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 35 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '少于 5 个小时'
  WHERE survey_question_id = 35 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '5-6 个小时'
  WHERE survey_question_id = 35 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '6-7 个小时'
  WHERE survey_question_id = 35 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '7-8 个小时'
  WHERE survey_question_id = 35 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '8 个小时或以上'
  WHERE survey_question_id = 35 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '烘干衣服时是否使用织物柔软剂？'
  WHERE survey_question_id = 36;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 36 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 36 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 36 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您平均每天排便多少次？'
  WHERE survey_question_id = 37;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 37 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '少于一次'
  WHERE survey_question_id = 37 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '一次'
  WHERE survey_question_id = 37 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '两次'
  WHERE survey_question_id = 37 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '三次'
  WHERE survey_question_id = 37 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '四次'
  WHERE survey_question_id = 37 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '五次或更多'
  WHERE survey_question_id = 37 AND
        display_index = 6;

UPDATE ag.survey_question SET chinese = '描述您的排便质量。使用下面的图表作为参考：'
  WHERE survey_question_id = 38;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 38 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我容易发生便秘（粪便难以排出） -  1 型和 2 型'
  WHERE survey_question_id = 38 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '我容易发生腹泻（水样便） -  5 型、6 型和 7 型'
  WHERE survey_question_id = 38 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '我的大便形态通常为正常 - 3 型和 4 型'
  WHERE survey_question_id = 38 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '我不知道，我没有参照物'
  WHERE survey_question_id = 38 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '我在过去的 ____________内服用过抗生素。'
  WHERE survey_question_id = 39;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 39 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '1 周'
  WHERE survey_question_id = 39 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '1 个月'
  WHERE survey_question_id = 39 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '6 个月'
  WHERE survey_question_id = 39 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '1 年'
  WHERE survey_question_id = 39 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '我在过去的一年里没有服用过抗生素。'
  WHERE survey_question_id = 39 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您多久服用一次维生素 B 复合物或叶酸？'
  WHERE survey_question_id = 4;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 4 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 4 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 4 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次 /周）'
  WHERE survey_question_id = 4 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 4 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 4 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '我在过去的 ____________内接种过流感疫苗。'
  WHERE survey_question_id = 40;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 40 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '1 周'
  WHERE survey_question_id = 40 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '1 个月'
  WHERE survey_question_id = 40 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '6 个月'
  WHERE survey_question_id = 40 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '1 年'
  WHERE survey_question_id = 40 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '我在过去的一年内没有接种流感疫苗。'
  WHERE survey_question_id = 40 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您目前正在使用某种形式的荷尔蒙避孕措施吗？'
  WHERE survey_question_id = 41;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 41 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是的，我正在服用“避孕药”'
  WHERE survey_question_id = 41 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '是的，我使用注射避孕药（DMPA）'
  WHERE survey_question_id = 41 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '是的，我使用避孕贴片（Ortho-Evra）'
  WHERE survey_question_id = 41 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '是的，我使用阴道环（NuvaRing）'
  WHERE survey_question_id = 41 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '是的，我使用荷尔蒙宫内节育器（Mirena）'
  WHERE survey_question_id = 41 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 41 AND
        display_index = 6;

UPDATE ag.survey_question SET chinese = '您现在怀孕了吗？'
  WHERE survey_question_id = 42;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 42 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 42 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 42 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 42 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '我在过去 6 个月内的体重 _________ 。'
  WHERE survey_question_id = 43;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 43 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '增加超过 10 磅'
  WHERE survey_question_id = 43 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '降低超过 10 磅'
  WHERE survey_question_id = 43 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '保持稳定'
  WHERE survey_question_id = 43 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您接受过扁桃体摘除术吗？'
  WHERE survey_question_id = 44;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 44 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 44 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 44 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 44 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您接受过阑尾切除术吗？'
  WHERE survey_question_id = 45;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 45 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 45 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 45 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 45 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您得过水痘吗？'
  WHERE survey_question_id = 46;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 46 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 46 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 46 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 46 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您目前正服用处方药治疗面部痤疮吗？'
  WHERE survey_question_id = 47;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 47 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 47 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 47 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您使用非处方产品来控制面部痤疮吗？'
  WHERE survey_question_id = 48;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 48 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 48 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 48 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您目前是否应用非处方药或处方药治疗其他病症？'
  WHERE survey_question_id = 49;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 49 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 49 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 49 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您多久服用一次维生素 D 补充剂？'
  WHERE survey_question_id = 5;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 5 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 5 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 5 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次 /周）'
  WHERE survey_question_id = 5 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 5 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 5 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您是通过剖腹产（剖宫产）出生的吗？'
  WHERE survey_question_id = 50;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 50 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 50 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 50 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 50 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您在婴儿时的喂养食物是什么？'
  WHERE survey_question_id = 51;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 51 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '主要是母乳'
  WHERE survey_question_id = 51 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '主要是婴儿配方奶粉'
  WHERE survey_question_id = 51 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '母乳和配方奶粉的混合'
  WHERE survey_question_id = 51 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '不确定'
  WHERE survey_question_id = 51 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您是否愿意与我们联系以回答有关上述病症的其他问题？'
  WHERE survey_question_id = 52;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 52 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 52 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 52 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您有季节性过敏吗？'
  WHERE survey_question_id = 53;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 53 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 53 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 53 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您是否有以下任何的非食物性过敏？ （标出所有适用项目）'
  WHERE survey_question_id = 54;

UPDATE ag.survey_question_response 
  SET chinese = '药物（如青霉素）'
  WHERE survey_question_id = 54 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '宠物皮屑'
  WHERE survey_question_id = 54 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '蜂蜇'
  WHERE survey_question_id = 54 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '毒藤/橡树'
  WHERE survey_question_id = 54 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '日光'
  WHERE survey_question_id = 54 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 54 AND
        display_index = 999;

UPDATE ag.survey_question SET chinese = '您在婴儿期从母乳或配方奶粉中获得大部分营养吗？或成人时从营养奶昔（即 Ensure）中获得大部分营养（75% 以上每日卡路里）吗？'
  WHERE survey_question_id = 55;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 55 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 55 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 55 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '我同时吃固体食物和配方奶粉/母乳'
  WHERE survey_question_id = 55 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您平均每周多久吃一次肉/鸡蛋？'
  WHERE survey_question_id = 56;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 56 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 56 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 56 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 56 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 56 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 56 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内烹饪和进食在家里烹饪的食物的频率是多少？（不包括即食食品，如盒装通心粉和奶酪、日本拉面、瘦身特餐）'
  WHERE survey_question_id = 57;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 57 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 57 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 57 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 57 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 57 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 57 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内吃即食食品（如盒装通心粉和奶酪、日本拉面、瘦身特餐）的频率是多少？'
  WHERE survey_question_id = 58;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 58 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 58 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 58 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 58 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 58 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 58 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内吃餐厅制作的食物（包括外卖食物）的频率是多少？'
  WHERE survey_question_id = 59;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 59 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 59 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 59 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 59 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 59 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 59 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您在服用任何其他营养/草药补充剂吗？'
  WHERE survey_question_id = 6;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 6 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 6 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 6 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有肾病吗？'
  WHERE survey_question_id = 60;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 60 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 60 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）诊断'
  WHERE survey_question_id = 60 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 60 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 60 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内每天至少进食 2-3 份水果的频率是多少？ （1 份= 1/2 杯水果；1 个中等大小的水果；4 盎司 100% 果汁。）'
  WHERE survey_question_id = 61;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 61 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 61 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 61 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 61 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 61 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 61 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内每天至少进食 2-3 份蔬菜（包括土豆）的频率是多少？（1 份= 1/2 杯蔬菜/土豆；1 杯生的有叶蔬菜）'
  WHERE survey_question_id = 62;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 62 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 62 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 62 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 62 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 62 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 62 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内每天食用一份或多份发酵蔬菜或植物产品的频率是多少？ （1 份= 1/2 杯酸菜、泡菜或发酵蔬菜或 1 杯红茶菌）'
  WHERE survey_question_id = 63;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 63 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 63 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 63 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 63 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 63 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 63 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内每天至少食用 2 份牛奶或奶酪的频率是多少？ （1 份= 1 杯牛奶或酸奶；1 1/2  -  2 盎司奶酪）'
  WHERE survey_question_id = 64;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 64 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 64 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 64 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 64 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 64 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 64 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您在一周内多久吃一次代乳品（豆浆、无乳糖牛奶、杏仁奶等）？'
  WHERE survey_question_id = 65;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 65 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 65 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 65 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 65 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 65 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 65 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您多久吃一次冷冻甜点（冰淇淋/意式冰激凌/奶昔、果子露/冰糕、冷冻酸奶等）？'
  WHERE survey_question_id = 66;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 66 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 66 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 66 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 66 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 66 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 66 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您平均每周多久吃一次红肉？'
  WHERE survey_question_id = 67;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 67 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 67 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 67 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 67 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 67 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 67 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内多久吃一次高脂肪红肉，如牛排、丁骨牛排、汉堡包、排骨、培根等？'
  WHERE survey_question_id = 68;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 68 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 68 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 68 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 68 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 68 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 68 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内每天至少吃一次家禽（鸡肉、火鸡等）的频率是多少？'
  WHERE survey_question_id = 69;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 69 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 69 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 天/周）'
  WHERE survey_question_id = 69 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 天/周）'
  WHERE survey_question_id = 69 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 天/周）'
  WHERE survey_question_id = 69 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 69 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您有乳糖不耐受症吗？'
  WHERE survey_question_id = 7;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 7 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '是'
  WHERE survey_question_id = 7 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 7 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '平均而言，您每周吃海鲜（鱼、虾、龙虾、螃蟹等）的天数是多少？'
  WHERE survey_question_id = 70;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 70 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 70 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 天/周）'
  WHERE survey_question_id = 70 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 天/周）'
  WHERE survey_question_id = 70 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 天/周）'
  WHERE survey_question_id = 70 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 70 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您每周内有多少天会吃咸味零食（薯片、墨西哥玉米片、玉米片、黄油爆米花、炸薯条等）？'
  WHERE survey_question_id = 71;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 71 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 71 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 天/周）'
  WHERE survey_question_id = 71 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 天/周）'
  WHERE survey_question_id = 71 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 天/周）'
  WHERE survey_question_id = 71 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 71 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您每周内吃含糖甜食（蛋糕、饼干、糕点、甜甜圈、松饼、巧克力等）的天数是多少？'
  WHERE survey_question_id = 72;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 72 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 72 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 天/周）'
  WHERE survey_question_id = 72 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 天/周）'
  WHERE survey_question_id = 72 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 天/周）'
  WHERE survey_question_id = 72 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 72 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '平均而言，您每周内应用橄榄油（包括沙拉酱）烹饪的天数是多少？'
  WHERE survey_question_id = 73;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 73 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 73 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 天/周）'
  WHERE survey_question_id = 73 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 天/周）'
  WHERE survey_question_id = 73 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 天/周）'
  WHERE survey_question_id = 73 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 73 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '食用全蛋（不包括 egg beaters 或仅食用蛋白）。'
  WHERE survey_question_id = 74;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 74 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 74 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 74 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 74 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 74 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 74 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '一天内饮用 16 盎司或更多的含糖饮料（如非健怡苏打水或果汁饮料/潘趣酒 [但不包括 100% 果汁] ）的频率是多少？（1 罐苏打水= 12 盎司）'
  WHERE survey_question_id = 75;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 75 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 75 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 天/周）'
  WHERE survey_question_id = 75 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 天/周）'
  WHERE survey_question_id = 75 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 75 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 75 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '一天饮用至少 1 升（约 32 盎司）的水？'
  WHERE survey_question_id = 76;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 76 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 76 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 76 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 76 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 76 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 76 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有自闭症或自闭症谱系障碍吗？'
  WHERE survey_question_id = 77;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 77 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 77 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 77 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 77 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 77 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有小肠细菌过度生长（SIBO）吗？'
  WHERE survey_question_id = 78;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 78 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 78 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 78 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 78 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 78 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有肠易激综合征（IBS）吗？'
  WHERE survey_question_id = 79;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 79 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 79 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 79 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 79 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 79 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您有麸质不耐受症吗？'
  WHERE survey_question_id = 8;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 8 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我被诊断出患有乳糜泻'
  WHERE survey_question_id = 8 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '我被诊断出患有麸质过敏症（谷蛋白抗体），但不是乳糜泻'
  WHERE survey_question_id = 8 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '我不吃麸质，因为会让我感觉不适'
  WHERE survey_question_id = 8 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '否'
  WHERE survey_question_id = 8 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您是否曾被诊断出患有艰难梭菌（C. diff）感染？'
  WHERE survey_question_id = 80;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 80 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 80 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 80 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 80 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 80 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有其他相关的临床病症吗？'
  WHERE survey_question_id = 81;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 81 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 81 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 81 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 81 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 81 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有糖尿病吗？'
  WHERE survey_question_id = 82;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 82 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 82 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 82 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 82 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 82 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有炎症性肠病（IBD）吗？'
  WHERE survey_question_id = 83;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 83 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 83 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 83 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 83 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 83 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有阿尔茨海默病/老年痴呆症吗？'
  WHERE survey_question_id = 84;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 84 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 84 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 84 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 84 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 84 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有注意力缺陷障碍/注意力缺陷多动障碍（ADD/ADHD）吗？'
  WHERE survey_question_id = 85;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 85 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 85 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 85 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 85 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 85 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有肝病吗？'
  WHERE survey_question_id = 86;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 86 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 86 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 86 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 86 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 86 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有下列自身免疫性疾病吗？如狼疮（系统性红斑狼疮）、R.A（类风湿性关节炎）、MS（多发性硬化症）、桥本氏甲状腺炎或任何其他自身免疫性疾病。'
  WHERE survey_question_id = 87;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 87 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 87 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 87 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 87 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 87 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有皮肤病吗？'
  WHERE survey_question_id = 88;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 88 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 88 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 88 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 88 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 88 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有冠状动脉疾病、心脏病或曾经发生心脏病发作和/或卒中吗？'
  WHERE survey_question_id = 89;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 89 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 89 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 89 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 89 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 89 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '我对 __________ 过敏（标出所有适用项目）'
  WHERE survey_question_id = 9;

UPDATE ag.survey_question_response 
  SET chinese = '花生'
  WHERE survey_question_id = 9 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '木本坚果'
  WHERE survey_question_id = 9 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '贝类'
  WHERE survey_question_id = 9 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 9 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '据我所知，我没有食物过敏。'
  WHERE survey_question_id = 9 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 9 AND
        display_index = 999;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有癫痫或癫痫发作吗？'
  WHERE survey_question_id = 90;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 90 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 90 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 90 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 90 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 90 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内每天至少吃 2 份全谷物的频率是多少？'
  WHERE survey_question_id = 91;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 91 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 91 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（小于 1 次/周）'
  WHERE survey_question_id = 91 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 91 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 91 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 91 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有偏头痛吗？'
  WHERE survey_question_id = 92;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 92 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 92 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 92 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 92 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 92 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有哮喘、囊性纤维化或 COPD（慢性阻塞性肺病）吗？'
  WHERE survey_question_id = 93;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 93 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 93 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 93 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 93 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 93 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有苯丙酮酸尿症吗？'
  WHERE survey_question_id = 94;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 94 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 94 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 94 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 94 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 94 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有肠道念珠菌或真菌过度生长吗？'
  WHERE survey_question_id = 95;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 95 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 95 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 95 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 95 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 95 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有甲状腺疾病吗？'
  WHERE survey_question_id = 96;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 96 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 96 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 96 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 96 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 96 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您曾经被诊断出患有抑郁症、双相情感障碍或精神分裂症吗？'
  WHERE survey_question_id = 97;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 97 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '我没有患过该病症'
  WHERE survey_question_id = 97 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '由医疗专业人员（医生、医师助理）做出诊断'
  WHERE survey_question_id = 97 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '由另类医学从业者诊断'
  WHERE survey_question_id = 97 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '自我诊断'
  WHERE survey_question_id = 97 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '预产期：'
  WHERE survey_question_id = 98;

UPDATE ag.survey_question SET chinese = '非处方和处方药物：'
  WHERE survey_question_id = 99;

UPDATE ag.survey_question SET chinese = '平均而言，您一周内每天食用一份或多份发酵蔬菜或植物产品的频率是多少？ （1 份= 1/2 杯酸菜、泡菜或发酵蔬菜或 1 杯红茶菌）'
  WHERE survey_question_id = 165;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 165 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 165 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '很少（几次/月）'
  WHERE survey_question_id = 165 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '偶尔（1-2 次/周）'
  WHERE survey_question_id = 165 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '经常（3-5 次/周）'
  WHERE survey_question_id = 165 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '每天'
  WHERE survey_question_id = 165 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '不包括啤酒、葡萄酒和酒精，我在最近____内在频率或数量上显著增加（即多于一倍）了发酵食品摄入量。'
  WHERE survey_question_id = 166;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 166 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '1 周'
  WHERE survey_question_id = 166 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '1 个月'
  WHERE survey_question_id = 166 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '6 个月'
  WHERE survey_question_id = 166 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '1 年'
  WHERE survey_question_id = 166 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '我没有增加摄入量'
  WHERE survey_question_id = 166 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '以下哪种发酵食品/饮料您每周食用超过一次？勾选所有适用项目'
  WHERE survey_question_id = 167;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 167 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '泡菜'
  WHERE survey_question_id = 167 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '酸菜'
  WHERE survey_question_id = 167 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '发酵豆/味噌/纳豆'
  WHERE survey_question_id = 167 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '酱菜'
  WHERE survey_question_id = 167 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '丹贝'
  WHERE survey_question_id = 167 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '发酵豆腐'
  WHERE survey_question_id = 167 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '开菲尔（水）'
  WHERE survey_question_id = 167 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '开菲尔（牛奶）'
  WHERE survey_question_id = 167 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '干酪'
  WHERE survey_question_id = 167 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET chinese = '酸奶/lassi'
  WHERE survey_question_id = 167 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET chinese = '酸奶油/鲜奶油'
  WHERE survey_question_id = 167 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET chinese = '发酵鱼'
  WHERE survey_question_id = 167 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET chinese = '鱼露'
  WHERE survey_question_id = 167 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET chinese = '发酵面包/酸面包/injera'
  WHERE survey_question_id = 167 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET chinese = '红茶菌'
  WHERE survey_question_id = 167 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET chinese = '吉开酒'
  WHERE survey_question_id = 167 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET chinese = '啤酒'
  WHERE survey_question_id = 167 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET chinese = '苹果酒'
  WHERE survey_question_id = 167 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET chinese = '葡萄酒'
  WHERE survey_question_id = 167 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET chinese = '蜂蜜酒'
  WHERE survey_question_id = 167 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 167 AND
        display_index = 21;

UPDATE ag.survey_question SET chinese = '请在“其他”栏中写出未列出的任何食用食品'
  WHERE survey_question_id = 168;

UPDATE ag.survey_question SET chinese = '您是否在家中制作以下的任何发酵食品/饮料供个人食用？勾选所有适用项目。'
  WHERE survey_question_id = 169;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 169 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '泡菜'
  WHERE survey_question_id = 169 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '酸菜'
  WHERE survey_question_id = 169 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '发酵豆/味噌/纳豆'
  WHERE survey_question_id = 169 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '酱菜'
  WHERE survey_question_id = 169 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '丹贝'
  WHERE survey_question_id = 169 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '发酵豆腐'
  WHERE survey_question_id = 169 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '开菲尔（水）'
  WHERE survey_question_id = 169 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '开菲尔（牛奶）'
  WHERE survey_question_id = 169 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '干酪'
  WHERE survey_question_id = 169 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET chinese = '酸奶/lassi'
  WHERE survey_question_id = 169 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET chinese = '酸奶油/奶油冰淇淋'
  WHERE survey_question_id = 169 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET chinese = '发酵鱼'
  WHERE survey_question_id = 169 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET chinese = '鱼露'
  WHERE survey_question_id = 169 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET chinese = '发酵面包/酸面包/injera'
  WHERE survey_question_id = 169 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET chinese = '红茶菌'
  WHERE survey_question_id = 169 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET chinese = '吉开酒'
  WHERE survey_question_id = 169 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET chinese = '啤酒'
  WHERE survey_question_id = 169 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET chinese = '苹果酒'
  WHERE survey_question_id = 169 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET chinese = '葡萄酒'
  WHERE survey_question_id = 169 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET chinese = '蜂蜜酒'
  WHERE survey_question_id = 169 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 169 AND
        display_index = 21;

UPDATE ag.survey_question SET chinese = '请在“其他”栏中写出未列出的任何个人制作的食品'
  WHERE survey_question_id = 170;

UPDATE ag.survey_question SET chinese = '您是否制作以下任何发酵食品/饮料用于商业用途？勾选所有适用项目。'
  WHERE survey_question_id = 171;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 171 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '泡菜'
  WHERE survey_question_id = 171 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '酸菜'
  WHERE survey_question_id = 171 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '发酵豆/味噌/纳豆'
  WHERE survey_question_id = 171 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '酱菜'
  WHERE survey_question_id = 171 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '丹贝'
  WHERE survey_question_id = 171 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '发酵豆腐'
  WHERE survey_question_id = 171 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '开菲尔（水）'
  WHERE survey_question_id = 171 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '开菲尔（牛奶）'
  WHERE survey_question_id = 171 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '干酪'
  WHERE survey_question_id = 171 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET chinese = '酸奶/lassi'
  WHERE survey_question_id = 171 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET chinese = '酸奶油/奶油冰淇淋'
  WHERE survey_question_id = 171 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET chinese = '发酵鱼'
  WHERE survey_question_id = 171 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET chinese = '鱼露'
  WHERE survey_question_id = 171 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET chinese = '发酵面包/酸面包/injera'
  WHERE survey_question_id = 171 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET chinese = '红茶菌'
  WHERE survey_question_id = 171 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET chinese = '吉开酒'
  WHERE survey_question_id = 171 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET chinese = '啤酒'
  WHERE survey_question_id = 171 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET chinese = '苹果酒'
  WHERE survey_question_id = 171 AND
        display_index = 18;
UPDATE ag.survey_question_response 
  SET chinese = '葡萄酒'
  WHERE survey_question_id = 171 AND
        display_index = 19;
UPDATE ag.survey_question_response 
  SET chinese = '蜂蜜酒'
  WHERE survey_question_id = 171 AND
        display_index = 20;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 171 AND
        display_index = 21;

UPDATE ag.survey_question SET chinese = '请在“其他”栏中写出未列出的任何商业制作的食品'
  WHERE survey_question_id = 172;

UPDATE ag.survey_question SET chinese = '自愿提供更多有关该事项的信息。'
  WHERE survey_question_id = 173;

UPDATE ag.survey_question SET chinese = '名称'
  WHERE survey_question_id = 127;

UPDATE ag.survey_question SET chinese = '动物类型'
  WHERE survey_question_id = 128;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 128 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '狗'
  WHERE survey_question_id = 128 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '猫'
  WHERE survey_question_id = 128 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '小型哺乳动物'
  WHERE survey_question_id = 128 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '大型哺乳动物'
  WHERE survey_question_id = 128 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '鱼'
  WHERE survey_question_id = 128 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '鸟'
  WHERE survey_question_id = 128 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '爬行动物'
  WHERE survey_question_id = 128 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '两栖动物'
  WHERE survey_question_id = 128 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 128 AND
        display_index = 9;

UPDATE ag.survey_question SET chinese = '来源'
  WHERE survey_question_id = 129;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 129 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '培育者'
  WHERE survey_question_id = 129 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '收容中心'
  WHERE survey_question_id = 129 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '家庭'
  WHERE survey_question_id = 129 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '野生'
  WHERE survey_question_id = 129 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '年龄'
  WHERE survey_question_id = 130;

UPDATE ag.survey_question SET chinese = '性别'
  WHERE survey_question_id = 131;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 131 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '雄性'
  WHERE survey_question_id = 131 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '雌性'
  WHERE survey_question_id = 131 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '环境'
  WHERE survey_question_id = 132;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 132 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '城市'
  WHERE survey_question_id = 132 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '郊区'
  WHERE survey_question_id = 132 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '乡村'
  WHERE survey_question_id = 132 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '体重类别'
  WHERE survey_question_id = 133;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 133 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '体重过轻'
  WHERE survey_question_id = 133 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '较瘦'
  WHERE survey_question_id = 133 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '正常'
  WHERE survey_question_id = 133 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '较胖'
  WHERE survey_question_id = 133 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '超重'
  WHERE survey_question_id = 133 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '饮食分类'
  WHERE survey_question_id = 134;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 134 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '肉食'
  WHERE survey_question_id = 134 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '杂食'
  WHERE survey_question_id = 134 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '草食'
  WHERE survey_question_id = 134 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '食物来源'
  WHERE survey_question_id = 135;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 135 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '宠物店的食物'
  WHERE survey_question_id = 135 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '人类食物'
  WHERE survey_question_id = 135 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '野生食物'
  WHERE survey_question_id = 135 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '食物类型'
  WHERE survey_question_id = 136;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 136 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '干性食物'
  WHERE survey_question_id = 136 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '湿性食物'
  WHERE survey_question_id = 136 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '两者都有'
  WHERE survey_question_id = 136 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '食物特殊属性'
  WHERE survey_question_id = 137;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 137 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '有机'
  WHERE survey_question_id = 137 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '无谷物'
  WHERE survey_question_id = 137 AND
        display_index = 2;

UPDATE ag.survey_question SET chinese = '生活状态'
  WHERE survey_question_id = 138;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 138 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '独自与人类共同生活'
  WHERE survey_question_id = 138 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '独自生活，不与人类共同生活/极少与人类共同生活（收容所）'
  WHERE survey_question_id = 138 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '与其他动物和人类共同生活'
  WHERE survey_question_id = 138 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '与其他动物共同生活/极少与人类共同生活'
  WHERE survey_question_id = 138 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '呆在室外的时间'
  WHERE survey_question_id = 139;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 139 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '无'
  WHERE survey_question_id = 139 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '小于 2 小时'
  WHERE survey_question_id = 139 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '2-4 小时'
  WHERE survey_question_id = 139 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '4-8 小时'
  WHERE survey_question_id = 139 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '8 小时以上'
  WHERE survey_question_id = 139 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '接触马桶水'
  WHERE survey_question_id = 140;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 140 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '经常'
  WHERE survey_question_id = 140 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '有时'
  WHERE survey_question_id = 140 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 140 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '食粪动物'
  WHERE survey_question_id = 141;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 141 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '大量'
  WHERE survey_question_id = 141 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '中量'
  WHERE survey_question_id = 141 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '少量'
  WHERE survey_question_id = 141 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 141 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '请写下您认为可能影响该动物的微生物的相关其他事宜。'
  WHERE survey_question_id = 142;

UPDATE ag.survey_question SET chinese = '请输入动物类型'
  WHERE survey_question_id = 143;

UPDATE ag.survey_question SET chinese = '请输入其他动物类型'
  WHERE survey_question_id = 144;

UPDATE ag.survey_question SET chinese = '请输入目前与动物一起生活的任何人类的年龄（以年为单位）和性别'
  WHERE survey_question_id = 145;

UPDATE ag.survey_question SET chinese = '您当地的冲浪地点在哪里？'
  WHERE survey_question_id = 174;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 174 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '美国加利福尼亚州圣地亚哥市 Point Loma/海洋沙滩'
  WHERE survey_question_id = 174 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '美国加利福尼亚州圣地亚哥市 La Jolla'
  WHERE survey_question_id = 174 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '美国加利福尼亚州 Encinitas'
  WHERE survey_question_id = 174 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '美国南加州'
  WHERE survey_question_id = 174 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '美国中部加州'
  WHERE survey_question_id = 174 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '北加州'
  WHERE survey_question_id = 174 AND
        display_index = 6;
UPDATE ag.survey_question_response 
  SET chinese = '美国太平洋西北地区'
  WHERE survey_question_id = 174 AND
        display_index = 7;
UPDATE ag.survey_question_response 
  SET chinese = '美国夏威夷'
  WHERE survey_question_id = 174 AND
        display_index = 8;
UPDATE ag.survey_question_response 
  SET chinese = '美国东北部'
  WHERE survey_question_id = 174 AND
        display_index = 9;
UPDATE ag.survey_question_response 
  SET chinese = '美国东南部'
  WHERE survey_question_id = 174 AND
        display_index = 10;
UPDATE ag.survey_question_response 
  SET chinese = '南美洲'
  WHERE survey_question_id = 174 AND
        display_index = 11;
UPDATE ag.survey_question_response 
  SET chinese = '欧洲'
  WHERE survey_question_id = 174 AND
        display_index = 12;
UPDATE ag.survey_question_response 
  SET chinese = '非洲'
  WHERE survey_question_id = 174 AND
        display_index = 13;
UPDATE ag.survey_question_response 
  SET chinese = '澳大利亚'
  WHERE survey_question_id = 174 AND
        display_index = 14;
UPDATE ag.survey_question_response 
  SET chinese = '新西兰'
  WHERE survey_question_id = 174 AND
        display_index = 15;
UPDATE ag.survey_question_response 
  SET chinese = '东南亚'
  WHERE survey_question_id = 174 AND
        display_index = 16;
UPDATE ag.survey_question_response 
  SET chinese = '亚洲'
  WHERE survey_question_id = 174 AND
        display_index = 17;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 174 AND
        display_index = 18;

UPDATE ag.survey_question SET chinese = '您多久在当地冲浪一次？'
  WHERE survey_question_id = 175;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 175 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '一天多次'
  WHERE survey_question_id = 175 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '一天一次'
  WHERE survey_question_id = 175 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '一周多次'
  WHERE survey_question_id = 175 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '一周一次'
  WHERE survey_question_id = 175 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '一个月多次'
  WHERE survey_question_id = 175 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您多久冲浪一次？'
  WHERE survey_question_id = 176;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 176 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '一天多次'
  WHERE survey_question_id = 176 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '一天一次'
  WHERE survey_question_id = 176 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '一周多次'
  WHERE survey_question_id = 176 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '一周一次'
  WHERE survey_question_id = 176 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '一个月多次'
  WHERE survey_question_id = 176 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您到其他冲浪地点旅行并冲浪的频率如何？'
  WHERE survey_question_id = 177;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 177 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '一天多次'
  WHERE survey_question_id = 177 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '一天一次'
  WHERE survey_question_id = 177 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '一周多次'
  WHERE survey_question_id = 177 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '一周一次'
  WHERE survey_question_id = 177 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '一个月多次'
  WHERE survey_question_id = 177 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您在（家/工作/出差）时，会离这个海滩多远？'
  WHERE survey_question_id = 178;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 178 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '<1 km'
  WHERE survey_question_id = 178 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '5-10km'
  WHERE survey_question_id = 178 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '>10km'
  WHERE survey_question_id = 178 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您使用什么类型的潜水服？'
  WHERE survey_question_id = 179;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 179 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '无'
  WHERE survey_question_id = 179 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '<1mm'
  WHERE survey_question_id = 179 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '2-3mm'
  WHERE survey_question_id = 179 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '3-4mm'
  WHERE survey_question_id = 179 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '4-5mm'
  WHERE survey_question_id = 179 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您使用什么类型的防晒霜？'
  WHERE survey_question_id = 180;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 180 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '<SPF25'
  WHERE survey_question_id = 180 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = 'SPF 25-50'
  WHERE survey_question_id = 180 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = 'SPF 50+'
  WHERE survey_question_id = 180 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 180 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您多久用一次防晒霜？'
  WHERE survey_question_id = 181;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 181 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '每次冲浪都用'
  WHERE survey_question_id = 181 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '频繁'
  WHERE survey_question_id = 181 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '很少'
  WHERE survey_question_id = 181 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 181 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您冲浪后洗澡的频率是多少？'
  WHERE survey_question_id = 182;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 182 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '每次冲浪后'
  WHERE survey_question_id = 182 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '频繁'
  WHERE survey_question_id = 182 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '很少'
  WHERE survey_question_id = 182 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '从来没有'
  WHERE survey_question_id = 182 AND
        display_index = 4;

UPDATE ag.survey_question SET chinese = '您的姿态是什么？'
  WHERE survey_question_id = 183;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 183 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '自然'
  WHERE survey_question_id = 183 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '右脚在前站在冲浪板上'
  WHERE survey_question_id = 183 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '俯卧冲浪'
  WHERE survey_question_id = 183 AND
        display_index = 3;

UPDATE ag.survey_question SET chinese = '您更喜欢什么类型的冲浪板？'
  WHERE survey_question_id = 184;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 184 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = '长板'
  WHERE survey_question_id = 184 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = '短板'
  WHERE survey_question_id = 184 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = '冲浪趴板'
  WHERE survey_question_id = 184 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = '无冲浪板'
  WHERE survey_question_id = 184 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = '无偏好'
  WHERE survey_question_id = 184 AND
        display_index = 5;

UPDATE ag.survey_question SET chinese = '您使用什么类型的蜡？'
  WHERE survey_question_id = 185;

UPDATE ag.survey_question_response 
  SET chinese = '未指明'
  WHERE survey_question_id = 185 AND
        display_index = 0;
UPDATE ag.survey_question_response 
  SET chinese = 'Sex Wax'
  WHERE survey_question_id = 185 AND
        display_index = 1;
UPDATE ag.survey_question_response 
  SET chinese = 'Sticky Bumps'
  WHERE survey_question_id = 185 AND
        display_index = 2;
UPDATE ag.survey_question_response 
  SET chinese = 'Mrs. Palmers'
  WHERE survey_question_id = 185 AND
        display_index = 3;
UPDATE ag.survey_question_response 
  SET chinese = 'Bubble Gum'
  WHERE survey_question_id = 185 AND
        display_index = 4;
UPDATE ag.survey_question_response 
  SET chinese = 'Famous'
  WHERE survey_question_id = 185 AND
        display_index = 5;
UPDATE ag.survey_question_response 
  SET chinese = '其他'
  WHERE survey_question_id = 185 AND
        display_index = 6;

