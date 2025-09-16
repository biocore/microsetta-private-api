-- Consent documents have an account_id associated, with the idea that there may eventually be an administrative feature to update the contents.
-- Until that's built, we use a stable dummy account whose ID is 000fc4cd-8fa4-db8b-e050-8a800c5d81b7, established in patch 0118.sql.

-- First, we need to clone the contents of the consent documents's we're _not_ changing into a new version, which in this case will be the child_data and child_biospecimen consents.
-- We made a conscious design decision to keep all consent documents at the same version, so we'll just do an INSERT INTO...SELECT FROM... statement for those types.

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    SELECT consent_type, locale, date_time, consent_content, 'true', account_id, 2
    FROM ag.consent_documents
    WHERE consent_type IN ('child_data', 'child_biospecimen');

-- Then, we'll insert the contents of the new documents

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adolescent_data', 'en_US', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Assent to Act as a Research Subject<br />
    (Ages 13-17 years)
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
    Dr. Rob Knight from the University of California San Diego (UC San Diego) is conducting a research study to find out more about all the many bacteria and other microorganisms (called your microbiome) that live on and within your body. We are inviting you to participate in this study because you live in a place where you can receive a sampling kit. There will be approximately 500,000 participants in total in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
    Why is this study being done and what will happen to you?
</p>
<p class="consent_content">
    Every person has a unique microbiome and the more people we study, the more we will understand about the microorganisms that live in and on us. The purpose of this research study is to assess more accurately the differences among people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. If you agree to take part in this study, you will be asked to complete online surveys/questionnaires. This survey/questionnaire will ask questions about you, such as your age, weight, height, lifestyle, diet, and  if you have certain medical or health conditions. You should expect to spend an average of 5-10 minutes on each survey, but some may take up to 30 minutes to complete.
</p>
<p class="consent_header">
    What benefits can be reasonably expected?
</p>
<p class="consent_content">
    There is no direct benefit for participating in this study. If you complete one of the questionnaires called the Food Frequency Questionnaire (FFQ), you may receive a nutritional report evaluating your eating pattern and nutrient intake with an overall diet score. The investigator(s), however, may learn more about relevant topics, such as gut-related health conditions.  
</p>
<p class="consent_header">
    What risks and confidentiality are associated with this study?
</p>
<p class="consent_content">
    Participation in this study can involve some added minimal risks or discomforts. While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
    What are the alternatives to participating in this study and can you withdraw?
</p>
<p class="consent_content">
    Your participation in this study is completely voluntary and you are free to skip any question that you choose. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
    You can refuse to participate or withdraw at any time by deleting your online profile. Our researchers will still use the data about you that was collected before you withdrew. These data will not include any personal information that could directly identify you. After you withdraw, no further data will be collected from you.
</p>
<p class="consent_header">
    Know what we will collect
</p>
<p class="consent_content">
    As part of this research study, we will create and obtain information related to you and your participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
</p>
<p class="consent_header">
    How we will use your Personal Data
</p>
<p class="consent_content">
    The Personal Data you provide will be used for the following purposes:
    <ul>
        <li>To share with members of the research team so they can properly conduct the research.</li>
        <li>For future research studies or additional research by other researchers.</li>
        <li>To contact you for the purpose of receiving alerts of your participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s).</li>
        <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research.</li>
        <li>To confirm proper conduct of the study and research integrity.</li>
    </ul>
</p>
<p class="consent_content">
    If you are part of a specific sub-study, and enrollment in the Microsetta Initiative is an add-on for participation in a separate companion study, your data may be shared with the investigators of that study.
</p>
<p class="consent_header">
    Retention of your Personal Data
</p>
<p class="consent_content">
    We may retain your Personal Data for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your Personal Data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your information will be retained as necessary to comply with legal or regulatory requirements.
</p>
<p class="consent_header">
    Your Privacy Rights
</p>
<p class="consent_content">
    The General Data Protection Regulation ("GDPR") requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your Personal Data, including the right to access, correct, restrict, and withdraw your personal information. 
</p>
<p class="consent_content">
    The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as countries in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Personal Data. Additional information about the protections we will use is included in this consent document and in our Privacy Statement.  
</p>
<p class="consent_header">
    Who can you call if you have questions?
</p>
<p class="consent_content">
    If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_content">
    If you have questions or complaints about our treatment of your Personal Data, or about our privacy practices more generally, please feel free to contact the UC San Diego Privacy Official by email at ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
    Your Signature and Consent
</p>
<p class="consent_content">
    You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject"s Bill of Rights</a>" to keep. 
</p>
<p class="consent_content">
    Your consent is entirely voluntary, but declining to provide it may impede your ability to participate in this research.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adolescent_data', 'es_MX', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 13-17 años)
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Le invitamos a participar en este estudio porque vive en un lugar donde puede recibir un kit de muestreo.Habrá aproximadamente 500000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se está llevando a cabo este estudio?
</p>
<p class="consent_content">
    Cada persona tiene un microbioma único y cuanto más personas estudiemos, más comprenderemos sobre los microorganismos que viven dentro y sobre nosotros. El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta participar en este estudio, se le pedirá que complete encuestas/cuestionarios en línea. Estas encuestas/cuestionarios harán preguntas sobre usted, como su edad, peso, altura, estilo de vida, dieta y si tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas le pueden tomar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
    ¿Qué beneficios se pueden esperar razonablemente?
</p>
<p class="consent_content">
    No hay ningún beneficio directo por participar en este estudio. Si completa uno de los cuestionarios llamado Cuestionario de frecuencia de alimentos (FFQ), puede recibir un informe nutricional que evalúe su patrón de alimentación y la ingesta de nutrientes con una puntuación general de la dieta. Sin embargo, los investigadores pueden aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué riesgos y confidencialidad están asociados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Mientras responde encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas.Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas para participar en este estudio y puede retirarse?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria y usted es libre de omitir cualquier pregunta que elija. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento eliminando su perfil en línea o solicitando la eliminación de su cuenta. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Estos datos no incluirán ninguna información personal que pueda identificarle directamente. Después de retirarse, no se recopilarán más datos sobre usted. 
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    Conoce lo que recopilaremos
</p>
<p class="consent_content">
    Como parte de este estudio de investigación, crearemos y obtendremos información relacionada a usted y su participación en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
    Cómo utilizaremos sus datos personales
</p>
<p class="consent_content">
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:
    <ul>
        <li>Para compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
        <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
        <li>Para comunicarnos con usted con el fin de recibir alertas sobre su estado de participación, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
        <li>Para cumplir con los requisitos legales y reglamentarios, incluidos los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
        <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
    </ul>
</p>
<p class="consent_content">
    Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, sus datos pueden ser compartidos con los investigadores de ese estudio.
</p>
<p class="consent_header">
    Conservación de sus datos personales
</p>
<p class="consent_content">
    Podemos retener sus Datos personales durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Eliminaremos sus Datos personales cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, su información se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
    Sus derechos de privacidad
</p>
<p class="consent_content">
    El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con sus Datos personales, incluido el derecho a acceder, corregir, restringir y retirar su información personal.
</p>
<p class="consent_content">
    El equipo de investigación almacenará y procesará sus Datos personales en nuestro sitio de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger sus Datos personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos Personales. En este documento de consentimiento y en nuestra Declaración de privacidad se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
    Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_content">
    Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adolescent_data', 'es_ES', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 13-17 años)
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Le invitamos a participar en este estudio porque vive en un lugar donde puede recibir un kit de muestreo.Habrá aproximadamente 500000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se está llevando a cabo este estudio?
</p>
<p class="consent_content">
    Cada persona tiene un microbioma único y cuanto más personas estudiemos, más comprenderemos sobre los microorganismos que viven dentro y sobre nosotros. El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta participar en este estudio, se le pedirá que complete encuestas/cuestionarios en línea. Estas encuestas/cuestionarios harán preguntas sobre usted, como su edad, peso, altura, estilo de vida, dieta y si tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas le pueden tomar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
    ¿Qué beneficios se pueden esperar razonablemente?
</p>
<p class="consent_content">
    No hay ningún beneficio directo por participar en este estudio. Si completa uno de los cuestionarios llamado Cuestionario de frecuencia de alimentos (FFQ), puede recibir un informe nutricional que evalúe su patrón de alimentación y la ingesta de nutrientes con una puntuación general de la dieta. Sin embargo, los investigadores pueden aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué riesgos y confidencialidad están asociados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Mientras responde encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas.Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas para participar en este estudio y puede retirarse?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria y usted es libre de omitir cualquier pregunta que elija. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento eliminando su perfil en línea o solicitando la eliminación de su cuenta. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Estos datos no incluirán ninguna información personal que pueda identificarle directamente. Después de retirarse, no se recopilarán más datos sobre usted. 
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    Conoce lo que recopilaremos
</p>
<p class="consent_content">
    Como parte de este estudio de investigación, crearemos y obtendremos información relacionada a usted y su participación en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
    Cómo utilizaremos sus datos personales
</p>
<p class="consent_content">
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:
    <ul>
        <li>Para compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
        <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
        <li>Para comunicarnos con usted con el fin de recibir alertas sobre su estado de participación, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
        <li>Para cumplir con los requisitos legales y reglamentarios, incluidos los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
        <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
    </ul>
</p>
<p class="consent_content">
    Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, sus datos pueden ser compartidos con los investigadores de ese estudio.
</p>
<p class="consent_header">
    Conservación de sus datos personales
</p>
<p class="consent_content">
    Podemos retener sus Datos personales durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Eliminaremos sus Datos personales cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, su información se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
    Sus derechos de privacidad
</p>
<p class="consent_content">
    El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con sus Datos personales, incluido el derecho a acceder, corregir, restringir y retirar su información personal.
</p>
<p class="consent_content">
    El equipo de investigación almacenará y procesará sus Datos personales en nuestro sitio de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger sus Datos personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos Personales. En este documento de consentimiento y en nuestra Declaración de privacidad se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
    Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_content">
    Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adolescent_biospecimen', 'en_US', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Assent to Act as a Research Subject<br />
    (Ages 13-17 years)
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong><br />
    Biospecimen and Future Use Research
</p>
<p class="consent_header">
    Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
    Dr. Rob Knight from the University of California San Diego (UC San Diego) is conducting a research study to find out more about all the many bacteria and other microorganisms (called your microbiome) that live on and within your body. We are inviting you to participate in this study because you live in a place where you can receive a sampling kit. There will be approximately 500,000 participants in total in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
    Why is this study being done?
</p>
<p class="consent_content">
    Every person has a unique microbiome and the more people we study, the more we will understand about the microorganisms that live in and on us. The purpose of this study is to assess more accurately the microbial differences between people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. Biospecimens are samples from your body such as stool, skin, urine, or blood which are used for research purposes. This study involves the collection, storage, and use of your information and biospecimens for the purpose of processing your biospecimens and for future research. The results will be used to create a database of DNA sequence and other data from various body sites, as well as details about you (the participant supplying the sample). Researchers can then use that data while studying relevant topics, such as gut-related health conditions
</p>
<p class="consent_header">
    What will happen to you in this study and which procedures are standard of care and which are experimental?
</p>
<p class="consent_content">
    If you agree to participate in this study, the following will happen to you:
</p>
<p class="consent_content">
    You will sample yourself using the kit that was provided to you.  Instructions are included in the kit so you know what to do.  The most common sample is of your poop (stool) where you apply a small smear to the tips of a swab from used toilet tissue or to a card (called an FOBT card). You may also be asked to scoop some poop using a small spoon-like tool, place used toilet paper into a special receptacle we provide, or poop into a plastic container that you place under the toilet seat. You may also need to sample a small area of skin, your tongue or mouth, your nostrils, ear wax, or vagina.  We may also ask someone (like your mom or dad) to take a small sample of blood by pricking your finger and then collecting the blood on 2 small swabs. None of these samples or investigations will allow us to make a diagnosis of disease and we are not looking at anything in your own DNA that can also be found in your poop, skin, or saliva.
</p>
<p class="consent_header">
    How much time will each study procedure take, what is your total time commitment, and how long will the study last?
</p>
<p class="consent_content">
    Each sample you send can be obtained in 5 minutes or less.  We expect the study to continue for many years, but your results will be available to you before the end of the study.
</p>
<p class="consent_header">
    What risks are associated with this study?
</p>
<p class="consent_content">
    Participation in this study may involve some added risks or discomforts. These include the following:
    <ol>
        <li>You may experience temporary pain or a bruise at the site of the needle-stick if you take the blood test.</li>
        <li>There is a risk of loss of confidentiality.</li>
    </ol>
</p>
<p class="consent_content">
    Because this is a research study, there may be some unknown risks that are currently unforeseeable. You and your parents will be informed of any significant new findings.
</p>
<p class="consent_header">
    What are the alternatives to participating in this study? Can you withdraw from the study or be withdrawn?
</p>
<p class="consent_content">
    Your participation in this study is completely voluntary. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
    You can refuse to participate or withdraw at any time by deleting your online profile, or by requesting the deletion of your account. Our researchers will still use the data about you that was collected before you withdrew. These data will not include any personal information that could directly identify you. After you withdraw, no further data will be collected from you.
</p>
<p class="consent_content">
    You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
</p>
<p class="consent_header">
    What benefits can be reasonably expected?
</p>
<p class="consent_content">
    There is no direct benefit to you for participating in this study. You will get access to your data that will give you and your parents an idea of what kinds of microorganisms are in your sample and how it compares with other people like you (age, sex).
</p>
<p class="consent_header">
    Will you be compensated for participating in this study?
</p>
<p class="consent_content">
    If you are a general participant, meaning that your parent or guardian enrolled you through the Microsetta Initiative crowd-sourcing site, you will not be financially compensated for taking part in this study.
</p>
<p class="consent_content">
    If you are a part of a specific sub-study, and enrollment in the Microsetta Initiative is an add-on for participation in a separate companion study, you or your parent/guardian may receive compensation if you complete all the required steps as explained to you by study personnel. You or your parent/guardian will be provided a separate document that explains the compensation options.
</p>
<p class="consent_header">
    Are there any costs associated with participating in this study?
</p>
<p class="consent_content">
    There may be costs associated with obtaining a kit. Once you receive your kit, there will be no additional cost to you for participating in this sampling procedure. 
</p>
<p class="consent_header">
    What about your confidentiality?
</p>
<p class="consent_content">
    Research records will be kept confidential to the extent allowed by law.  As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical study personnel.  The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
    How we will use your Sample
</p>
<p class="consent_content">
    Information from analyses of your data and biospecimen(s) will be used to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including yours) may be analyzed and published in scientific articles. If you are part of a specific sub-study, and enrollment in the Microsetta Initiative is an add-on for participation in a separate companion study, your data may be shared with the investigators of that study.
</p>
<p class="consent_content">
    We may save some of your sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your data and/or sample(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use. We may contact you if additional information or action is needed in order to process your sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
    Biospecimens (such as stool, saliva, mucus, skin, urine, or blood) collected from you for this study and information obtained from your biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your biospecimens and/or information obtained from them.
</p>
<p class="consent_content">
    <strong>Please Note:</strong><br />
    Please be aware that no human DNA will be analyzed as part of this or any future studies. Furthermore, the methods we use for identifying microorganisms in your sample cannot be used to diagnose disease or infection.
</p>
<p class="consent_header">
    Who can you call if you have questions?
</p>
<p class="consent_content">
    If you have questions or research-related problems, you may reach us by emailing our help account microsetta@ucsd.edu or Rob Knight at 858-246-1184.
</p>
<p class="consent_content">
    You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_header">
    Your Signature and Assent
</p>
<p class="consent_content">
    You may download a copy of this assent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adolescent_biospecimen', 'es_MX', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 13-17 años)
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong><br />
    Bioespecímenes e investigación de uso futuro
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Le invitamos a participar en este estudio porque vive en un lugar donde puede recibir un kit de muestreo. Habrá aproximadamente 500000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se está llevando a cabo este estudio?
</p>
<p class="consent_content">
    Cada persona tiene un microbioma único y cuanto más personas estudiemos, más comprenderemos sobre los microorganismos que viven dentro y sobre nosotros. El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Las muestras biológicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de su información y muestras biológicas con el fin de procesar sus muestras biológicas y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podrán usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué le sucederá en este estudio y qué procedimientos son el estándar de atención y cuáles son experimentales?
</p>
<p class="consent_content">
    Si usted acepta participar en este estudio, le ocurrirá lo siguiente:
</p>
<p class="consent_content">
    Usted mismo tomará la muestra usando el kit que se le proporcionó. Las instrucciones están incluidas en el kit para que sepa qué hacer. La muestra más común es de heces (fecal) donde se recoge una pequeña muestra insertando las puntas de un hisopo en el papel higiénico usado o en una tarjeta (tarjeta llamada FOBT). También se le puede pedir que saque un trozo de materia fecal con una pequeña herramienta similar a una cuchara, que coloque papel higiénico usado en un receptáculo especial que le proporcionaremos o que defeque en un recipiente de plástico que se coloca debajo del asiento del baño. También es posible que deba tomar muestras de una pequeña área de la piel, la lengua o la boca, las fosas nasales, la cera del oído o la vagina. También podemos pedirle a alguien (como su mamá o papá) que tome una pequeña muestra de sangre pinchando su dedo y luego recolectando la sangre en 2 hisopos pequeños. Ninguna de estas muestras o investigaciones nos permitirá hacer un diagnóstico de enfermedad y no estamos buscando nada en su propio ADN que también se pueda encontrar en sus heces, piel o saliva.
</p>
<p class="consent_header">
    ¿Cuánto tiempo es necesario para realizar cada procedimiento del estudio, cuánto tiempo debe dedicar en total y cuánto durará el estudio?
</p>
<p class="consent_content">
    Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero sus resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
    ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
    <ol>
        <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el análisis de sangre.</li>
        <li>Existe el riesgo de pérdida de confidencialidad.</li>
    </ol>
</p>
<p class="consent_content">
    Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres serán informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio? ¿Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento eliminando su perfil en línea o solicitando la eliminación de su cuenta. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Estos datos no incluirán ninguna información personal que pueda identificarle directamente. Después de retirarse, no se recopilarán más datos sobre usted. 
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo para usted por participar en este estudio. Usted tendrá acceso a sus datos que le darán a usted y a sus padres una idea de lo que hay en su muestra y cómo se compara con otras personas como usted (edad, sexo).
</p>
<p class="consent_header">
    ¿Se le pagará por participar en este estudio?
</p>
<p class="consent_content">
    Si es un participante general, es decir, si su padre o tutor lo inscribió a través del sitio de colaboración colectiva de The Microsetta Initiative, no recibirá una compensación económica por participar en este estudio.
</p>
<p class="consent_content">
    Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, usted o su padre/tutor podrían recibir una compensación si completan todos los pasos requeridos, tal como le explicó el personal del estudio. Se les entregará a usted o a su padre/tutor un documento aparte que explica las opciones de compensación.
</p>
<p class="consent_header">
    ¿Hay algún costo vinculado con la participación en el estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos su Muestra
</p>
<p class="consent_content">
    La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, sus datos pueden ser compartidos con los investigadores de ese estudio.
</p>
<p class="consent_content">
    Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
    <strong>Tenga en cuenta:</strong><br />
    Tenga en cuenta que no se analizará ADN humano como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra no pueden usarse para diagnosticar enfermedades o infecciones.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
    Si tiene alguna duda o problemas relacionados con la investigación, usted puede comunicarse con nosotros enviando un correo electrónico a nuestra cuenta de ayuda microsetta@ucsd.edu o llamando a Rob Knight al 858-246-1184.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar  problemas relacionados con la investigación.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adolescent_biospecimen', 'es_ES', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento para participar como sujeto de investigación<br />
    (Edades 13-17 años)
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong><br />
    Bioespecímenes e investigación de uso futuro
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Le invitamos a participar en este estudio porque vive en un lugar donde puede recibir un kit de muestreo. Habrá aproximadamente 500000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se está llevando a cabo este estudio?
</p>
<p class="consent_content">
    Cada persona tiene un microbioma único y cuanto más personas estudiemos, más comprenderemos sobre los microorganismos que viven dentro y sobre nosotros. El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Las muestras biológicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de su información y muestras biológicas con el fin de procesar sus muestras biológicas y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podrán usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué le sucederá en este estudio y qué procedimientos son el estándar de atención y cuáles son experimentales?
</p>
<p class="consent_content">
    Si usted acepta participar en este estudio, le ocurrirá lo siguiente:
</p>
<p class="consent_content">
    Usted mismo tomará la muestra usando el kit que se le proporcionó. Las instrucciones están incluidas en el kit para que sepa qué hacer. La muestra más común es de heces (fecal) donde se recoge una pequeña muestra insertando las puntas de un hisopo en el papel higiénico usado o en una tarjeta (tarjeta llamada FOBT). También se le puede pedir que saque un trozo de materia fecal con una pequeña herramienta similar a una cuchara, que coloque papel higiénico usado en un receptáculo especial que le proporcionaremos o que defeque en un recipiente de plástico que se coloca debajo del asiento del baño. También es posible que deba tomar muestras de una pequeña área de la piel, la lengua o la boca, las fosas nasales, la cera del oído o la vagina. También podemos pedirle a alguien (como su mamá o papá) que tome una pequeña muestra de sangre pinchando su dedo y luego recolectando la sangre en 2 hisopos pequeños. Ninguna de estas muestras o investigaciones nos permitirá hacer un diagnóstico de enfermedad y no estamos buscando nada en su propio ADN que también se pueda encontrar en sus heces, piel o saliva.
</p>
<p class="consent_header">
    ¿Cuánto tiempo es necesario para realizar cada procedimiento del estudio, cuánto tiempo debe dedicar en total y cuánto durará el estudio?
</p>
<p class="consent_content">
    Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero sus resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
    ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
    <ol>
        <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el análisis de sangre.</li>
        <li>Existe el riesgo de pérdida de confidencialidad.</li>
    </ol>
</p>
<p class="consent_content">
    Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres serán informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio? ¿Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento eliminando su perfil en línea o solicitando la eliminación de su cuenta. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Estos datos no incluirán ninguna información personal que pueda identificarle directamente. Después de retirarse, no se recopilarán más datos sobre usted. 
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo para usted por participar en este estudio. Usted tendrá acceso a sus datos que le darán a usted y a sus padres una idea de lo que hay en su muestra y cómo se compara con otras personas como usted (edad, sexo).
</p>
<p class="consent_header">
    ¿Se le pagará por participar en este estudio?
</p>
<p class="consent_content">
    Si es un participante general, es decir, si su padre o tutor lo inscribió a través del sitio de colaboración colectiva de The Microsetta Initiative, no recibirá una compensación económica por participar en este estudio.
</p>
<p class="consent_content">
    Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, usted o su padre/tutor podrían recibir una compensación si completan todos los pasos requeridos, tal como le explicó el personal del estudio. Se les entregará a usted o a su padre/tutor un documento aparte que explica las opciones de compensación.
</p>
<p class="consent_header">
    ¿Hay algún costo vinculado con la participación en el estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos su Muestra
</p>
<p class="consent_content">
    La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, sus datos pueden ser compartidos con los investigadores de ese estudio.
</p>
<p class="consent_content">
    Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
    <strong>Tenga en cuenta:</strong><br />
    Tenga en cuenta que no se analizará ADN humano como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra no pueden usarse para diagnosticar enfermedades o infecciones.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
    Si tiene alguna duda o problemas relacionados con la investigación, usted puede comunicarse con nosotros enviando un correo electrónico a nuestra cuenta de ayuda microsetta@ucsd.edu o llamando a Rob Knight al 858-246-1184.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar  problemas relacionados con la investigación.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adult_biospecimen', 'en_US', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consent to Act as a Research Subject
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong><br />
    Biospecimen and Future Use Research
</p>
<p class="consent_header">
    Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
    Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called your microbiome) that live in and on your body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  We are inviting you to participate in this study because you live in a location where you can receive a sampling kit. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
    Why is this study being done?
</p>
<p class="consent_content">
    Every person has a unique microbiome and the more people we study, the more we will understand about the microorganisms that live in and on us. The purpose of this study is to assess more accurately the microbial differences among people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. Biospecimens are samples from your body such as stool, skin, urine, or blood which are used for research purposes. This study involves the collection, storage, and use of your information and biospecimens for the purpose of processing your biospecimens and for future research. The results will be used to create a database of DNA sequence and other data from various body sites, as well as details about you (the participant supplying the sample). Researchers can then use that data while studying relevant topics, such as gut-related health conditions.  
</p>
<p class="consent_header">
    What will happen to you in this study?
</p>
<p class="consent_content">
    If you agree to the collection and processing of your biospecimen(s), the following will happen to you:
</p>
<p class="consent_content">
    You have received or will receive a sample kit. The kit contains devices used to collect samples and instructions for use. The collection device may also include 95% ethanol to preserve the sample and make it non-infectious. You will then collect a sample of yourself (e.g. feces, skin, mouth, nostril, ear, vagina), pet, or environment as described in the kit instructions or in the instructions provided to you by study coordinators. You will also be asked to provide general collection information such as the date and time your sample was collected. All samples should be returned to us in the included containers according to the instructions provided.
</p>
<p class="consent_content">
    If collecting from stool, you will be asked to sample in one of a variety of ways, such as the following:
    <ol>
        <li>By inserting swab tip(s) into used toilet tissue and returning the swab(s) in the provided plastic container;</li>
        <li>By inserting swab tip(s) into used toilet tissue and applying the tips to the surface of a Fecal Occult Blood Test (FOBT) card, then returning the card to us.  The FOBT card is the same device used by your doctor to check for blood in your stool.  The FOBT card stabilizes the stool material for later analysis.  We will not check if there is blood in the stool for diagnostic purposes because we are not a clinical laboratory;</li>
        <li>By using a scooper device to scoop a part of the fecal material into the provided tube;</li>
        <li>Depositing soiled toilet paper into the provided receptacle;</li>
        <li>Submitting a whole stool sample in a shipping container we will provide.  This container will have ice packs that reliably cool the sample to -20 degrees Celsius/-4 degrees Fahrenheit.</li>
    </ol>
</p>
<p class="consent_content">
    If you received a blood collection kit, it contains materials and instructions on how to collect a blood sample at home.  It is similar to the test used to test glucose levels by pricking your finger.
</p>
<p class="consent_content">
    Once your sample has been analyzed, we will upload results to your account and send you an email with a link to log in and view them.  It can take several months for you to learn the results of your microbiome analysis. If you are a part of a specific sub-study, it may take longer, depending on the duration of the study. 
</p>
<p class="consent_header">
    How much time will each study procedure take, what is your total time commitment, and how long will the study last?
</p>
<p class="consent_content">
    Each sample you send can be obtained in 5 minutes or less.  We expect the study to continue for many years but your results will be available to you before the end of the study.
</p>
<p class="consent_header">
    What risks are associated with this study?
</p>
<p class="consent_content">
    Participation in this study may involve some added risks or discomforts. These include the following:
    <ol>
        <li>If using the blood collection device, you may experience temporary pain or a bruise at the site of the needle-stick.</li>
        <li>There is a risk of loss of confidentiality.</li>
    </ol>
</p>
<p class="consent_content">
    Because this is a research study, there may be some unknown risks that are currently unforeseeable. You will be informed of any significant new findings.
</p>
<p class="consent_header">
    What are the alternatives to participating in this study? Can you withdraw from the study or be withdrawn?
</p>
<p class="consent_content">
    Your participation in this study is completely voluntary. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
    You can refuse to participate or withdraw at any time by deleting your online profile, or by requesting the deletion of your account. Our researchers will still use the data about you that was collected before you withdrew. These data will not include any personal information that could directly identify you. After you withdraw, no further data will be collected from you. 
</p>
<p class="consent_content">
    You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
</p>
<p class="consent_header">
    What benefits can be reasonably expected?
</p>
<p class="consent_content">
    There is no direct benefit for participating in this study. You will receive a report detailing the results of our analysis on your biospecimen(s), as well as facts and figures comparing your microbiome''s composition to that of other study participants. The investigator, however, may learn more about the human microbiome in health and disease and provide a valuable resource for other researchers.
</p>
<p class="consent_header">
    Are there any costs associated with participating in the collection of your biospecimen(s)?
</p>
<p class="consent_content">
    There may be costs associated with obtaining a kit. Once you receive your kit, there will be no additional cost to you for participating in this sampling procedure.
</p>
<p class="consent_header">
    What about your confidentiality?
</p>
<p class="consent_content">
    Research records will be kept confidential to the extent allowed by law. As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The professionally maintained database server has several layers of security: it is password protected, firewalled, only allows network connectivity from defined UC San Diego managed systems, employs access control lists, and is physically housed in a key card controlled UC San Diego facility. Nightly backups of the database are taken and maintained on a separate co-located system with additional security measures in place. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_header">
    How we will use your Sample
</p>
<p class="consent_content">
    Information from analyses of your data and biospecimen(s) will be used  to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including yours) may be analyzed and published in scientific articles. If you are part of a specific sub-study, and enrollment in the Microsetta Initiative is an add-on for participation in a separate companion study, your data may be shared with the investigators of that study.
</p>
<p class="consent_content">
    We may save some of your sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your data and/or biospecimen(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use.We may contact you if additional information or action is needed in order to process your sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
    Biospecimens (such as stool, saliva, mucus, skin, urine, or blood) collected from you for this study and information obtained from your biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your biospecimens and/or information obtained from them.
</p>
<p class="consent_content">
    <strong>Please Note:</strong><br />
    Please be aware that no human DNA will be analyzed as part of this or any future studies. Furthermore, the methods we use for identifying microorganisms in your sample cannot be used to diagnose disease or infection.
</p>
<p class="consent_header">
    Who can you call if you have questions?
</p>
<p class="consent_content">
    If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_header">
    Your Signature and Consent
</p>
<p class="consent_content">
    You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep. 
</p>
<p class="consent_content">
    Your consent is entirely voluntary, but declining to provide it may impede your ability to participate in this research and have your sample(s) processed.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adult_biospecimen', 'es_MX', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento para participar como sujeto de investigación
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong><br />
    Bioespecímenes e investigación de uso futuro
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Le invitamos a participar en este estudio porque vive en un lugar donde puede recibir un kit de muestreo. Habrá aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se está llevando a cabo este estudio?
</p>
<p class="consent_content">
    Cada persona tiene un microbioma único y cuanto más personas estudiemos, más comprenderemos sobre los microorganismos que viven dentro y sobre nosotros. El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Las muestras biológicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de su información y muestras biológicas con el fin de procesar sus muestras biológicas y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podrán usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué le sucederá durante el estudio?
</p>
<p class="consent_content">
    Si acepta la recolección y el procesamiento de su(s) muestra(s) biológica(s), le ocurrirá lo siguiente:
</p>
<p class="consent_content">
    Usted ha recibido o recibirá un kit de muestra. El kit contiene dispositivos utilizados para recolectar muestras e instrucciones de uso. El dispositivo de recolección también puede incluir etanol al 95% para preservar la muestra y hacerla no infecciosa. Luego, recolectará una muestra de usted mismo (por ejemplo, heces, piel, boca, orificio nasal, oído, vagina), mascota o entorno, como se describe en las instrucciones del kit o en las instrucciones que le proporcionaron los coordinadores del estudio. También se le pedirá que proporcione información general sobre la recolección, como la fecha y la hora en que se recolectó su muestra. Todas las muestras deben devolverse en los contenedores incluidos de acuerdo con las instrucciones proporcionadas.
</p>
<p class="consent_content">
    Si se recolecta muestra de heces, se le pedirá que tome muestras en una variedad de formas, como las siguientes:
    <ol>
        <li>Insertando las punta(s) del hisopo en papel higiénico usado y devolviendo el hisopo(s) en el recipiente de plástico suministrado;</li>
        <li>Insertando las puntas del hisopo en el papel higiénico usado y pasando las puntas por la superficie de una tarjeta para pruebas de sangre oculta en heces, y luego devuélvanos la tarjeta. La tarjeta para pruebas de sangre oculta en heces es el mismo instrumento que usa su médico para verificar si hay sangre en sus heces. La tarjeta para pruebas de sangre oculta en heces permite estabilizar las heces para su posterior análisis. No verificaremos si hay sangre en las heces con fines diagnósticos, puesto que no somos un laboratorio clínico;</li>
        <li>Usando el instrumento de cuchara para recoger una parte de la materia fecal en el tubo suministrado;</li>
        <li>Depositando papel higiénico sucio en el receptáculo suministrado;</li>
        <li>Enviando una muestra completa de heces en el recipiente de envío que le suministraremos. Dicho recipiente contiene una serie de compresas de hielo que enfriarán la muestra de manera fiable a -20 °C/-4 °F.</li>
    </ol>
</p>
<p class="consent_content">
    Si recibió un kit de recolección de sangre, este contiene materiales e instrucciones sobre cómo recolectar una muestra de sangre en casa. Es similar a la prueba que se usa para medir los niveles de glucosa pinchando el dedo. 
</p>
<p class="consent_content">
    Una vez que se haya analizado su muestra, cargaremos los resultados en su cuenta y le enviaremos un correo electrónico con un enlace para iniciar sesión y verlos. Pueden pasar varios meses conocer los resultados de su análisis del microbioma. Si forma parte de un subestudio específico, puede llevar más tiempo, según la duración del estudio.
</p>
<p class="consent_header">
    ¿Cuánto tiempo es necesario para realizar cada procedimiento del estudio, cuánto tiempo debe dedicar en total y cuánto durará el estudio?
</p>
<p class="consent_content">
    Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero sus resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
    ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
    <ol>
        <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el análisis de sangre.</li>
        <li>Existe el riesgo de pérdida de confidencialidad.</li>
    </ol>
</p>
<p class="consent_content">
    Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres serán informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio? ¿Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar. 
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento eliminando su perfil en línea o solicitando la eliminación de su cuenta. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Estos datos no incluirán ninguna información personal que pueda identificarle directamente. Después de retirarse, no se recopilarán más datos sobre usted. 
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo por participar en este estudio. Usted recibirá un informe que detalla los resultados de nuestro análisis en su(s) muestra(s) biológica(s), así como datos y cifras que comparan la composición de su microbioma con la de otros participantes del estudio.
</p>
<p class="consent_header">
    ¿Hay algún costo vinculado con la participación en el estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas.Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos su Muestra
</p>
<p class="consent_content">
    La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, sus datos pueden ser compartidos con los investigadores de ese estudio.
</p>
<p class="consent_content">
    Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, piel, orina o sangre) recolectadas de usted para este estudio y la información obtenida de sus muestras biológicas pueden usarse en esta investigación u otra investigación, y compartirse con otras organizaciones. Usted no participará en ningún valor comercial o beneficio derivado del uso de sus muestras biológicas y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong>Tenga en cuenta:</strong><br />
    Tenga en cuenta que no se analizará ADN humano como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra no pueden usarse para diagnosticar enfermedades o infecciones.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
    Si tiene alguna duda o problemas relacionados con la investigación, puede llamar a Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación y procesar su(s) muestra(s).
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adult_biospecimen', 'es_ES', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento para participar como sujeto de investigación
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong><br />
    Bioespecímenes e investigación de uso futuro
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight de la University of California San Diego (UC San Diego) está realizando un estudio de investigación para obtener más información sobre todas las bacterias y otros microorganismos (llamado su microbioma) que viven sobre y dentro de su cuerpo. Le invitamos a participar en este estudio porque vive en un lugar donde puede recibir un kit de muestreo. Habrá aproximadamente 500,000 participantes en total en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se está llevando a cabo este estudio?
</p>
<p class="consent_content">
    Cada persona tiene un microbioma único y cuanto más personas estudiemos, más comprenderemos sobre los microorganismos que viven dentro y sobre nosotros. El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Las muestras biológicas son muestras de su cuerpo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de su información y muestras biológicas con el fin de procesar sus muestras biológicas y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre usted (el participante que proporciona la muestra). Luego, los investigadores podrán usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué le sucederá durante el estudio?
</p>
<p class="consent_content">
    Si acepta la recolección y el procesamiento de su(s) muestra(s) biológica(s), le ocurrirá lo siguiente:
</p>
<p class="consent_content">
    Usted ha recibido o recibirá un kit de muestra. El kit contiene dispositivos utilizados para recolectar muestras e instrucciones de uso. El dispositivo de recolección también puede incluir etanol al 95% para preservar la muestra y hacerla no infecciosa. Luego, recolectará una muestra de usted mismo (por ejemplo, heces, piel, boca, orificio nasal, oído, vagina), mascota o entorno, como se describe en las instrucciones del kit o en las instrucciones que le proporcionaron los coordinadores del estudio. También se le pedirá que proporcione información general sobre la recolección, como la fecha y la hora en que se recolectó su muestra. Todas las muestras deben devolverse en los contenedores incluidos de acuerdo con las instrucciones proporcionadas.
</p>
<p class="consent_content">
    Si se recolecta muestra de heces, se le pedirá que tome muestras en una variedad de formas, como las siguientes:
    <ol>
        <li>Insertando las punta(s) del hisopo en papel higiénico usado y devolviendo el hisopo(s) en el recipiente de plástico suministrado;</li>
        <li>Insertando las puntas del hisopo en el papel higiénico usado y pasando las puntas por la superficie de una tarjeta para pruebas de sangre oculta en heces, y luego devuélvanos la tarjeta. La tarjeta para pruebas de sangre oculta en heces es el mismo instrumento que usa su médico para verificar si hay sangre en sus heces. La tarjeta para pruebas de sangre oculta en heces permite estabilizar las heces para su posterior análisis. No verificaremos si hay sangre en las heces con fines diagnósticos, puesto que no somos un laboratorio clínico;</li>
        <li>Usando el instrumento de cuchara para recoger una parte de la materia fecal en el tubo suministrado;</li>
        <li>Depositando papel higiénico sucio en el receptáculo suministrado;</li>
        <li>Enviando una muestra completa de heces en el recipiente de envío que le suministraremos. Dicho recipiente contiene una serie de compresas de hielo que enfriarán la muestra de manera fiable a -20 °C/-4 °F.</li>
    </ol>
</p>
<p class="consent_content">
    Si recibió un kit de recolección de sangre, este contiene materiales e instrucciones sobre cómo recolectar una muestra de sangre en casa. Es similar a la prueba que se usa para medir los niveles de glucosa pinchando el dedo. 
</p>
<p class="consent_content">
    Una vez que se haya analizado su muestra, cargaremos los resultados en su cuenta y le enviaremos un correo electrónico con un enlace para iniciar sesión y verlos. Pueden pasar varios meses conocer los resultados de su análisis del microbioma. Si forma parte de un subestudio específico, puede llevar más tiempo, según la duración del estudio.
</p>
<p class="consent_header">
    ¿Cuánto tiempo es necesario para realizar cada procedimiento del estudio, cuánto tiempo debe dedicar en total y cuánto durará el estudio?
</p>
<p class="consent_content">
    Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero sus resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
    ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:
    <ol>
        <li>Es posible que experimente un dolor temporal o un hematoma en el lugar del pinchazo si se hace el análisis de sangre.</li>
        <li>Existe el riesgo de pérdida de confidencialidad.</li>
    </ol>
</p>
<p class="consent_content">
    Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted y sus padres serán informados de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio? ¿Puede retirarse del estudio o ser retirado?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar. 
</p>
<p class="consent_content">
    Puede negarse a participar o retirarse en cualquier momento eliminando su perfil en línea o solicitando la eliminación de su cuenta. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Estos datos no incluirán ninguna información personal que pueda identificarle directamente. Después de retirarse, no se recopilarán más datos sobre usted. 
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Cuáles podrían ser los beneficios de participar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo por participar en este estudio. Usted recibirá un informe que detalla los resultados de nuestro análisis en su(s) muestra(s) biológica(s), así como datos y cifras que comparan la composición de su microbioma con la de otros participantes del estudio.
</p>
<p class="consent_header">
    ¿Hay algún costo vinculado con la participación en el estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit. Una vez que reciba su kit, no habrá ningún costo adicional para usted por participar en este procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de su participación en el estudio, usted proporcionará información personal y/o confidencial que podría permitir su identificación si se hiciera pública, como nombre, fecha de nacimiento o dirección. Nosotros tomamos todas las precauciones para proteger su identidad.Toda la información proporcionada se almacena en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas.Los registros de investigación pueden ser revisados por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos su Muestra
</p>
<p class="consent_content">
    La información de los análisis de sus datos y muestras biológicas se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el suyo) pueden ser analizados y publicados en artículos científicos. Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, sus datos pueden ser compartidos con los investigadores de ese estudio.
</p>
<p class="consent_content">
    Es posible que guardemos parte de su muestra para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir sus datos y/o muestra(s) en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar su(s) muestra(s) y/o para propósitos de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, piel, orina o sangre) recolectadas de usted para este estudio y la información obtenida de sus muestras biológicas pueden usarse en esta investigación u otra investigación, y compartirse con otras organizaciones. Usted no participará en ningún valor comercial o beneficio derivado del uso de sus muestras biológicas y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong>Tenga en cuenta:</strong><br />
    Tenga en cuenta que no se analizará ADN humano como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra no pueden usarse para diagnosticar enfermedades o infecciones.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
    Si tiene alguna duda o problemas relacionados con la investigación, puede llamar a Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación y procesar su(s) muestra(s).
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adult_data', 'en_US', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consent to Act as a Research Subject
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
    You are being invited to participate in a research study titled The Microsetta Initiative. This study is being done by Dr. Rob Knight from the University of California San Diego (UC San Diego). We are inviting you to participate in this study because you live in a location where you can receive a sampling kit. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
    Why is this study being done and what will happen to you?
</p>
<p class="consent_content">
    Every person has a unique microbiome and the more people we study, the more we will understand about the microorganisms that live in and on us. The purpose of this research study is to assess more accurately the microbial differences among people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. If you agree to take part in this study, you will be asked to complete online surveys/questionnaires. These surveys/questionnaires are categorized by content type and will ask questions about you, such as your age, weight, height, lifestyle, diet, and if you have certain medical or health conditions. You should expect to spend an average of 5-10 minutes on each survey, but some may take up to 30 minutes to complete.
</p>
<p class="consent_header">
    What benefits can be reasonably expected?
</p>
<p class="consent_content">
    There is no direct benefit for participating in this study. If you complete one of the questionnaires, called a Food Frequency Questionnaire (FFQ), you may receive a nutritional report evaluating your eating pattern and nutrient intake with an overall diet score. The investigator(s), however, may learn more about relevant topics, such as gut-related health conditions.  
</p>
<p class="consent_header">
    What risks and confidentiality are associated with this study?
</p>
<p class="consent_content">
    Participation in this study may involve some added minimal risks or discomforts. While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you provide is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The professionally maintained database server has several layers of security: it is password protected, firewalled, only allows network connectivity from defined UC San Diego managed systems, employs access control lists, and is physically housed in a key card controlled UC San Diego facility. Nightly backups of the database are taken and maintained on a separate co-located system with additional security measures in place. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_content">
    We may need to report information about known or reasonably suspected incidents of abuse or neglect of a child, dependent adult or elder including physical, sexual, emotional, and financial abuse or neglect. If any investigator has or is given such information, they may report such information to the appropriate authorities.
</p>
<p class="consent_content">
Federal and State laws generally make it illegal for health insurance companies, group health plans, and most employers to discriminate against you based on your genetic information. This law generally will protect you in the following ways: a) Health insurance companies and group health plans may not request your genetic information that we get from this research. b) Health insurance companies and group health plans may not use your genetic information when making decisions regarding your eligibility or premiums. c) Employers with 5 or more employees may not use your genetic information that we get from this research when making a decision to hire, promote, or fire you or when setting the terms of your employment.
</p>
<p class="consent_content">
    Be aware that these laws do not protect you against genetic discrimination by companies that sell life insurance, disability insurance, or long-term care insurance.
</p>
<p class="consent_header">
    What are the alternatives to participating in this study? Can you withdraw from the study or be withdrawn?
</p>
<p class="consent_content">
    Your participation in this study is completely voluntary and you are free to skip any question that you choose. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
</p>
<p class="consent_content">
    You can withdraw at any time by deleting your online profile, or by requesting the deletion of your account. Our researchers will still use the data about you that was collected before you withdrew. These data will not include any personal information that could directly identify you. After you withdraw, no further data will be collected from you. 
</p>
<p class="consent_content">
    You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
</p>
<p class="consent_header">
    Will you be compensated for participating in this study?
</p>
<p class="consent_content">
    If you are a general participant, meaning that you enrolled on your own through the Microsetta Initiative  crowd-sourcing site, you will not be financially compensated for taking part in this study.
</p>
<p class="consent_content">
    If you are a part of a specific sub-study, and enrollment in the Microsetta Initiative is an add-on for participation in a separate companion study, you may receive compensation if you complete all the required steps as explained to you by study personnel. You will be provided a separate document that explains the compensation options.
</p>
<p class="consent_header">
    Are there any costs associated with participating in this study?
</p>
<p class="consent_content">
    There will be no cost to you for completing the standard survey/questionnaire(s). However, there may be costs associated with having certain diet assessment tools made available to you, such as the Food Frequency Questionnaire (FFQ).
</p>
<p class="consent_header">
    Know what we will collect
</p>
<p class="consent_content">
    As part of this research study, we will create and obtain information related to you and your participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
</p>
<p class="consent_header">
    How we will use your Personal Data
</p>
<p class="consent_content">
    The Personal Data you provide will be used for the following purposes:<br />
    <ul>
        <li>To share with members of the research team so they can properly conduct the research.</li>
        <li>For future research studies or additional research by other researchers.</li>
        <li>To contact you for the purpose of receiving alerts of your participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s).</li>
        <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research.</li>
        <li>To confirm proper conduct of the study and research integrity.</li>
    </ul>
</p>
<p class="consent_content">
    If you are part of a specific sub-study, and enrollment in the Microsetta Initiative is an add-on for participation in a separate companion study, your data may be shared with the investigators of that study.
</p>
<p class="consent_header">
    Retention of your Personal Data
</p>
<p class="consent_content">
    We may retain your Personal Data for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your Personal Data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your information will be retained as necessary to comply with legal or regulatory requirements. 
</p>
<p class="consent_header">
    Your Privacy Rights
</p>
<p class="consent_content">
    The General Data Protection Regulation ("GDPR") requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your Personal Data, including the right to access, correct, restrict, and withdraw your personal information. 
</p>
<p class="consent_content">
    The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as countries in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Personal Data. Additional information about the protections we will use is included in this consent document and in our Privacy Statement.  
</p>
<p class="consent_header">
    Who can you call if you have questions?
</p>
<p class="consent_content">
    If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_content">
    If you have questions or complaints about our treatment of your Personal Data, or about our privacy practices more generally, please feel free to contact the UC San Diego Privacy Official by email at ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
    Your Signature and Consent
</p>
<p class="consent_content">
    You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
    Your consent is entirely voluntary, but declining to provide it may impede your ability to participate in this research.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adult_data', 'es_MX', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento para participar como sujeto de investigación
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    Usted ha sido invitado a participar en un estudio de investigación titulado La Iniciativa Microsetta. Este estudio está siendo realizado por el Dr. Rob Knight de la University of California San Diego (UC San Diego). Le invitamos a participar en este estudio porque vive en un lugar donde puede recibir un kit de muestreo. Habrá aproximadamente 500000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se está llevando a cabo este estudio y qué le sucederá a usted durante el estudio?
</p>
<p class="consent_content">
    Cada persona tiene un microbioma único y cuanto más personas estudiemos, más comprenderemos sobre los microorganismos que viven dentro y sobre nosotros. El propósito de este estudio de investigación es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta participar en este estudio, se le pedirá que complete encuestas/cuestionarios en línea. Estas encuestas/cuestionarios se clasifican por tipo de contenido y le harán preguntas sobre usted, como su edad, peso, altura, estilo de vida, dieta y si tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas pueden tardar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
    ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo por participar en este estudio. Si completa uno de los cuestionarios, llamado Cuestionario de frecuencia de alimentos (FFQ), usted podrá recibir un reporte nutricional que evalúa su patrón de alimentación y la ingesta de nutrientes con una puntuación general de la dieta. Sin embargo, los investigadores podrían aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué riesgos y confidencialidad están asociados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas adicionales. Mientras responde las encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero nosotros tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_content">
    Es posible que necesitemos reportar información sobre incidentes conocidos o sospechados de abuso o negligencia de un niño, adulto dependiente o anciano, incluido el abuso o negligencia física, sexual, emocional y financiera. Si algún investigador tiene o recibe dicha información, puede reportar dicha información a las autoridades correspondientes.
</p>
<p class="consent_content">
    Las leyes federales y estatales generalmente hacen que sea ilegal que las compañías de seguros de salud, los planes de salud grupales y la mayoría de los empleadores lo discriminen en función de su información genética. Esta ley generalmente lo protegerá de las siguientes maneras: a) Las compañías de seguros de salud y los planes de salud grupales no pueden solicitar su información genética que obtengamos de esta investigación. b) Las compañías de seguros de salud y los planes de salud grupales no pueden usar su información genética al tomar decisiones con respecto a su elegibilidad o primas. c) Los empleadores con 5 o más empleados no pueden usar su información genética que obtengamos de esta investigación al tomar una decisión para contratarlo, ascenderlo o despedirlo o al establecer los términos de su empleo.
</p>
<p class="consent_content">
    Tenga en cuenta que estas leyes no lo protegen contra la discriminación genética por parte de compañías que venden seguros de vida, seguros por discapacidad o seguros de atención a largo plazo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio y puede usted retirarse del estudio?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria y usted es libre de omitir cualquier pregunta que elija. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede retirarse en cualquier momento eliminando su perfil en línea o solicitando la eliminación de su cuenta. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Estos datos no incluirán ninguna información personal que pueda identificarle directamente. Después de retirarse, no se recopilarán más datos sobre usted.
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Se le compensará por participar en este estudio?
</p>
<p class="consent_content">
    Si es un participante general, es decir, si se inscribió por su cuenta a través del sitio web de colaboración colectiva de The Microsetta Initiative, no recibirá compensación económica por participar en este estudio.
</p>
<p class="consent_content">
    Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, podría recibir una compensación si completa todos los pasos requeridos, tal como le explicó el personal del estudio. Se le proporcionará un documento aparte que explica las opciones de compensación.
</p>
<p class="consent_header">
    ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
    No habrá ningún costo para usted por completar la encuesta/cuestionario(s) estándar. Sin embargo, puede haber costos asociados al tener a su disposición ciertas herramientas para la evaluación de la dieta, como el Cuestionario de frecuencia de alimentos (FFQ por sus siglas en inglés).
</p>
<p class="consent_header">
    Conoce lo que recopilaremos
</p>
<p class="consent_content">
    Como parte de este estudio de investigación, nosotros crearemos y obtendremos información relacionada con usted y su participación en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
    Cómo utilizaremos sus datos personales
</p>
<p class="consent_content">
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
    <ul>
        <li>Compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
        <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
        <li>Para comunicarnos con usted con el fin de recibir alertas sobre su estado de participación, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
        <li>Para cumplir con los requisitos legales y reglamentarios, incluyendo los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
        <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
    </ul>
</p>
<p class="consent_content">
    Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, sus datos pueden ser compartidos con los investigadores de ese estudio.
</p>
<p class="consent_header">
    Conservación de sus datos personales
</p>
<p class="consent_content">
    Nosotros podemos retener sus Datos personales durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Nosotros eliminaremos sus Datos personales cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, su información se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
    Sus derechos de privacidad
</p>
<p class="consent_content">
    El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con sus Datos Personales, incluido el derecho a acceder, corregir, restringir y retirar su información personal.
</p>
<p class="consent_content">
    El equipo de investigación almacenará y procesará sus Datos Personales en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tiene las mismas leyes para proteger sus Datos Personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos Personales. En este documento de consentimiento y en nuestra Declaración de privacidad se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
    Si tiene alguna duda o problemas relacionados con la investigación, puede llamar a Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_content">
    Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos Personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu. 
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('adult_data', 'es_ES', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento para participar como sujeto de investigación
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién realiza el estudio, por qué se le ha pedido que participe, cómo fue seleccionado y cuál es la cifra aproximada de participantes en el estudio?
</p>
<p class="consent_content">
    Usted ha sido invitado a participar en un estudio de investigación titulado La Iniciativa Microsetta. Este estudio está siendo realizado por el Dr. Rob Knight de la University of California San Diego (UC San Diego). Le invitamos a participar en este estudio porque vive en un lugar donde puede recibir un kit de muestreo. Habrá aproximadamente 500000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se está llevando a cabo este estudio y qué le sucederá a usted durante el estudio?
</p>
<p class="consent_content">
    Cada persona tiene un microbioma único y cuanto más personas estudiemos, más comprenderemos sobre los microorganismos que viven dentro y sobre nosotros. El propósito de este estudio de investigación es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Si usted acepta participar en este estudio, se le pedirá que complete encuestas/cuestionarios en línea. Estas encuestas/cuestionarios se clasifican por tipo de contenido y le harán preguntas sobre usted, como su edad, peso, altura, estilo de vida, dieta y si tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas pueden tardar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
    ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo por participar en este estudio. Si completa uno de los cuestionarios, llamado Cuestionario de frecuencia de alimentos (FFQ), usted podrá recibir un reporte nutricional que evalúa su patrón de alimentación y la ingesta de nutrientes con una puntuación general de la dieta. Sin embargo, los investigadores podrían aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué riesgos y confidencialidad están asociados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas adicionales. Mientras responde las encuestas, puede sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero nosotros tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que proporciona se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas. Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_content">
    Es posible que necesitemos reportar información sobre incidentes conocidos o sospechados de abuso o negligencia de un niño, adulto dependiente o anciano, incluido el abuso o negligencia física, sexual, emocional y financiera. Si algún investigador tiene o recibe dicha información, puede reportar dicha información a las autoridades correspondientes.
</p>
<p class="consent_content">
    Las leyes federales y estatales generalmente hacen que sea ilegal que las compañías de seguros de salud, los planes de salud grupales y la mayoría de los empleadores lo discriminen en función de su información genética. Esta ley generalmente lo protegerá de las siguientes maneras: a) Las compañías de seguros de salud y los planes de salud grupales no pueden solicitar su información genética que obtengamos de esta investigación. b) Las compañías de seguros de salud y los planes de salud grupales no pueden usar su información genética al tomar decisiones con respecto a su elegibilidad o primas. c) Los empleadores con 5 o más empleados no pueden usar su información genética que obtengamos de esta investigación al tomar una decisión para contratarlo, ascenderlo o despedirlo o al establecer los términos de su empleo.
</p>
<p class="consent_content">
    Tenga en cuenta que estas leyes no lo protegen contra la discriminación genética por parte de compañías que venden seguros de vida, seguros por discapacidad o seguros de atención a largo plazo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio y puede usted retirarse del estudio?
</p>
<p class="consent_content">
    Su participación en este estudio es completamente voluntaria y usted es libre de omitir cualquier pregunta que elija. Le informaremos si se encuentra nueva información importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede retirarse en cualquier momento eliminando su perfil en línea o solicitando la eliminación de su cuenta. Nuestros investigadores seguirán utilizando los datos sobre usted que se recopilaron antes de que se retirara. Estos datos no incluirán ninguna información personal que pueda identificarle directamente. Después de retirarse, no se recopilarán más datos sobre usted.
</p>
<p class="consent_content">
    Puede ser retirado del estudio si no sigue las instrucciones que le ha dado el personal del estudio.
</p>
<p class="consent_header">
    ¿Se le compensará por participar en este estudio?
</p>
<p class="consent_content">
    Si es un participante general, es decir, si se inscribió por su cuenta a través del sitio web de colaboración colectiva de The Microsetta Initiative, no recibirá compensación económica por participar en este estudio.
</p>
<p class="consent_content">
    Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, podría recibir una compensación si completa todos los pasos requeridos, tal como le explicó el personal del estudio. Se le proporcionará un documento aparte que explica las opciones de compensación.
</p>
<p class="consent_header">
    ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
    No habrá ningún costo para usted por completar la encuesta/cuestionario(s) estándar. Sin embargo, puede haber costos asociados al tener a su disposición ciertas herramientas para la evaluación de la dieta, como el Cuestionario de frecuencia de alimentos (FFQ por sus siglas en inglés).
</p>
<p class="consent_header">
    Conoce lo que recopilaremos
</p>
<p class="consent_content">
    Como parte de este estudio de investigación, nosotros crearemos y obtendremos información relacionada con usted y su participación en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
    Cómo utilizaremos sus datos personales
</p>
<p class="consent_content">
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
    <ul>
        <li>Compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
        <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
        <li>Para comunicarnos con usted con el fin de recibir alertas sobre su estado de participación, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
        <li>Para cumplir con los requisitos legales y reglamentarios, incluyendo los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
        <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
    </ul>
</p>
<p class="consent_content">
    Si participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, sus datos pueden ser compartidos con los investigadores de ese estudio.
</p>
<p class="consent_header">
    Conservación de sus datos personales
</p>
<p class="consent_content">
    Nosotros podemos retener sus Datos personales durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Nosotros eliminaremos sus Datos personales cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, su información se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
    Sus derechos de privacidad
</p>
<p class="consent_content">
    El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con sus Datos Personales, incluido el derecho a acceder, corregir, restringir y retirar su información personal.
</p>
<p class="consent_content">
    El equipo de investigación almacenará y procesará sus Datos Personales en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tiene las mismas leyes para proteger sus Datos Personales que los países de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de sus Datos Personales. En este documento de consentimiento y en nuestra Declaración de privacidad se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene alguna duda?
</p>
<p class="consent_content">
    Si tiene alguna duda o problemas relacionados con la investigación, puede llamar a Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_content">
    Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos Personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu. 
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir su capacidad para participar en esta investigación.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('parent_biospecimen', 'en_US', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Parent Consent for Child to Act as a Research Subject
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative </strong><br />
    Biospecimen and Future Use Research
</p>
<p class="consent_header">
    Who is conducting the study, why has your child been asked to participate, how was your child selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
    Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called the microbiome) that live in and on the body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  We are inviting you to volunteer your child for this study because you live in a location where you can receive a sampling kit for your child.There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
    Why is this study being done?
</p>
<p class="consent_content">
    The purpose of this study is to assess more accurately the microbial differences between people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. Children, like all humans, have a unique microbiome and including them in the study will help elucidate the development of the microbiome. Biospecimens are samples from your child''s body such as stool, skin, urine, or blood, which are used for research purposes. This study involves the collection, storage, and use of your child''s information and biospecimens for the purpose of processing your child''s biospecimens and for future research. The results will be used to create a database of DNA sequence and other data from various body sites, as well as details about the child participant supplying the sample. Researchers can then use that data while studying relevant topics, such as gut-related health conditions. 
</p>
<p class="consent_header">
    What will happen to your child in this study?
</p>
<p class="consent_content">
    If you agree to the collection and processing of your child''s biospecimen(s), the following will happen to your child:
</p>
<p class="consent_content">
    You have received or will receive a sample kit.  The kit contains devices used to collect samples and instructions for use.  The collection device may also include 95% ethanol to preserve the sample and make it non-infectious.
</p>
<p class="consent_content">
    You will sample a part of your child''s body (e.g. feces, skin, mouth, nostril, ear, vagina) as described in the kit instructions. You will also be asked to provide general collection information such as the date and time your child''s sample was collected. All samples should be returned to us in the included containers according to the instructions provided.
</p>
<p class="consent_content">
    If collecting from your child''s stool, you will be asked to sample in one of a variety of ways, such as the following:
    <ol>
        <li>By inserting swab tips into used toilet tissue or diaper and returning the sample in the provided plastic container;</li>
        <li>By inserting swab tips into used toilet tissue and applying the tips to the surface of a Fecal Occult Blood Test (FOBT) card, then returning the card to us.  The FOBT card is the same device used by your doctor to check for blood in your stool.  The FOBT card stabilizes the stool material for later analysis.  We will not check if there is blood in the stool for diagnostic purposes because we are not a clinical laboratory;</li>
        <li>By using a scooper device to scoop a part of the fecal material into the provided tube;</li>
        <li>Depositing soiled toilet paper into the provided receptacle;</li>
        <li>Submitting a whole stool sample in a shipping container we will provide.  This container will have ice packs that reliably cool the sample to -20 degrees Celcius/-4 degrees Fahrenheit.</li>
    </ol>
</p>
<p class="consent_content">
    If you received a blood collection kit, it contains materials and instructions on how to collect a blood sample at home.  It is similar to the test used to test glucose levels by pricking your child''s finger.  
</p>
<p class="consent_content">
    Once your child''s sample has been analyzed, we will upload results to your account and send you an email with a link to log in and view them. It can take several months for you to learn the results of your child''s microbiome analysis. If your child is a part of a specific sub-study, it may take longer, depending on the duration of the study.
</p>
<p class="consent_header">
    How much time will each study procedure take, what is your child''s total time commitment, and how long will the study last?
</p>
<p class="consent_content">
    Each sample you send can be obtained in 5 minutes or less.  We expect the study to continue for many years but the results will be available to you before the end of the study. 
</p>
<p class="consent_header">
    What risks are associated with this study?
</p>
<p class="consent_content">
    Participation in this study may involve some added risks or discomforts. These include the following:<br />
    <ol>
        <li>If using the blood collection device, your child may experience temporary pain or a bruise at the site of the needle-stick.</li>
        <li>There is a risk of loss of confidentiality.</li>
    </ol>
</p>
<p class="consent_content">
    Because this is a research study, there may be some unknown risks that are currently unforeseeable. You will be informed of any significant new findings.
</p>
<p class="consent_header">
    What are the alternatives to participating in this study? Can your child withdraw or be withdrawn from the study?
</p>
<p class="consent_content">
    Participation in research is entirely voluntary. We will inform you if any important new information is found during the course of this study that may affect your child wanting to continue.
</p>
<p class="consent_content">
    You may refuse to have your child participate or withdraw your child at any time by deleting your child''s online profile or by requesting the deletion of your account. Our researchers will still use the data about your child that was collected before they were withdrawn. These data will not include any personal information that could directly identify your child. After your child withdraws, no further data will be collected from them. 
</p>
<p class="consent_content">
    Your child may be withdrawn from the study if the instructions given by the study personnel are not followed.
</p>
<p class="consent_header">
    What benefits can be reasonably expected?
</p>
<p class="consent_content">
    There is no direct benefit to your child for participating in this study. You will receive a report detailing the results of our analysis on your child''s sample, as well as facts and figures comparing your child''s microbial composition to that of other study participants. The investigator, however, may learn more about the human microbiome in health and disease and provide a valuable resource for other researchers.
</p>
<p class="consent_header">
    Will you be compensated for participating in this study?
</p>
<p class="consent_content">
    If your child is a general participant, meaning that you enrolled your child through the Microsetta Initiative crowd-sourcing site, you will not be financially compensated for their taking part in this study.
</p>
<p class="consent_content">
    If your child is a part of a specific sub-study, and enrollment in the Microsetta Initiative is an add-on for participation in a separate companion study, you may receive compensation for their participation if you complete all the required steps as explained to you by study personnel. You will be provided a separate document that explains the compensation options.
</p>
<p class="consent_header">
    Are there any costs associated with participating in this study?
</p>
<p class="consent_content">
    There may be costs associated with obtaining a kit but there will be no cost for participating in the sampling procedure.
</p>
<p class="consent_header">
    What about your or your child''s confidentiality?
</p>
<p class="consent_content">
    Research records will be kept confidential to the extent allowed by law. As part of your child''s participation in the study, you or your child will provide personal and/or sensitive information that could allow your child to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you or your child provide are stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical study personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The professionally maintained database server has several layers of security: it is password protected, firewalled, only allows network connectivity from defined UC San Diego managed systems, employs access control lists, and is physically housed in a key card controlled UC San Diego facility. Nightly backups of the database are taken and maintained on a separate co-located system with additional security measures in place. Research records may be reviewed by the UC San Diego Institutional Review Board. 
</p>
<p class="consent_header">
    How we will use your child''s Sample
</p>
<p class="consent_content">
    Information from analyses of your child''s data and biospecimen(s) will be used to study the non-human DNA (e.g. bacterial DNA) in it. The data from the samples in the project (including your child''s) may be analyzed and published in scientific articles. If your child is part of a specific sub-study, and enrollment in the Microsetta Initiative is an add-on for participation in a separate companion study, your child''s data may be shared with the investigators of that study.
</p>
<p class="consent_content">
    We may save some of your child''s sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. If we do so, we will remove all directly identifiable information before use or sharing. Once identifiers have been removed, we will not ask for your consent for the use or sharing of your child''s data and/or biospecimen(s) in other research. In addition, data that has been removed of directly identifying information will be uploaded to the European Bioinformatics Institute (http://www.ebi.ac.uk) and Qiita (https://qiita.ucsd.edu) for other researchers to access and use. We may contact you if additional information or action is needed in order to process your child''s sample(s) and/or for re-consenting purposes.
</p>
<p class="consent_content">
    Biospecimens (such as stool, saliva, mucus, skin, urine, or blood) collected from your child for this study and information obtained from your child''s biospecimens may be used in this research or other research, and shared with other organizations. You will not share in any commercial value or profit derived from the use of your child''s biospecimens and/or information obtained from them.
</p>
<p class="consent_content">
    <strong>Please Note:</strong><br />
    Please be aware that no human DNA will be analyzed as part of this or any future studies. Furthermore, the methods we use for identifying microorganisms in your sample cannot be used to diagnose disease or infection. 
</p>
<p class="consent_header">
    Who can you call if you have questions?
</p>
<p class="consent_content">
    If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_header">
    Your Signature and Consent
</p>
<p class="consent_content">
    You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
    Your consent is entirely voluntary, but declining to provide it may impede your child''s ability to participate in this research and have your child''s sample(s) processed.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('parent_biospecimen', 'es_MX', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong><br />
    Bioespecímenes e Investigación de Uso Futuro
</p>
<p class="consent_header">
    ¿Quién está realizando el estudio, por qué se le pidió a su hijo que participara, cómo se seleccionó a su hijo y cuál es el número aproximado de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamado el microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y los virus. Lo invitamos a voluntariar a su hijo para este estudio porque vive en un lugar donde puede recibir un kit de muestreo para su hijo.Habrá aproximadamente 500000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se realiza este estudio?
</p>
<p class="consent_content">
    El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Los niños, como todos los seres humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Las muestras biológicas son muestras  del cuerpo de su hijo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de la información y las muestras biológicas de su hijo con el fin de procesar las muestras biológicas de su hijo y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre el niño participante que proporciona la muestra. Luego, los investigadores pueden usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué le pasará a su hijo(a) en este estudio?
</p>
<p class="consent_content">
    Si acepta la recolección y el procesamiento de las muestras biológicas de su hijo, le sucederá lo siguiente a su hijo:
</p>
<p class="consent_content">
    Usted ha recibido o recibirá un kit de muestra. El kit contiene dispositivos utilizados para recolectar muestras e instrucciones de uso. El dispositivo de recolección también puede incluir etanol al 95% para preservar la muestra y hacerla no infecciosa.
</p>
<p class="consent_content">
    Tomará muestras de una parte del cuerpo de su hijo (p. ej., heces, piel, boca, orificios nasales, orejas, vagina) como se describe en las instrucciones del kit. También se le pedirá que proporcione información general sobre la recolección, como la fecha y la hora en que se recolectó la muestra de su hijo. Todas las muestras deben devolverse en los contenedores incluidos de acuerdo con las instrucciones proporcionadas.
</p>
<p class="consent_content">
    Si se recolecta muestra de heces de su hijo, se le pedirá que tome una muestra de una variedad de formas, como las siguientes:<br />
    <ol>
        <li>Insertando las punta(s) del hisopo en papel higiénico usado y devolviendo el hisopo(s) en el recipiente de plástico suministrado;</li>
        <li>Insertando las puntas del hisopo en el papel higiénico usado y pasando las puntas por la superficie de una tarjeta para pruebas de sangre oculta en heces, y luego devuélvanos la tarjeta. La tarjeta para pruebas de sangre oculta en heces es el mismo instrumento que usa su médico para verificar si hay sangre en sus heces. La tarjeta para pruebas de sangre oculta en heces permite estabilizar las heces para su posterior análisis. No verificaremos si hay sangre en las heces con fines diagnósticos, puesto que no somos un laboratorio clínico;</li>
        <li>Usando el instrumento de cuchara para recoger una parte de la materia fecal en el tubo suministrado;</li>
        <li>Depositando papel higiénico sucio en el receptáculo suministrado;</li>
        <li>Enviando una muestra completa de heces en el recipiente de envío que le suministraremos. Dicho recipiente contiene una serie de compresas de hielo que enfriarán la muestra de manera fiable a -20 °C/-4 °F.</li>
    </ol>
</p>
<p class="consent_content">
    Si recibió un kit de recolección de sangre, este contiene materiales e instrucciones sobre cómo recolectar una muestra de sangre en casa. Es similar a la prueba que se usa para medir los niveles de glucosa pinchando el dedo. 
</p>
<p class="consent_content">
    Una vez que se haya analizado la muestra de su hijo, cargaremos los resultados en su cuenta y le enviaremos un correo electrónico con un enlace para iniciar sesión y verlos. Pueden pasar varios meses conocer los resultados del análisis del microbioma de su hijo. Si su hijo es parte de un subestudio específico, puede tomar más tiempo, según la duración del estudio.
</p>
<p class="consent_header">
    ¿Cuánto tiempo llevará cada procedimiento del estudio, cuánto tiempo debe dedicar en total su hijo y cuánto durará el estudio?
</p>
<p class="consent_content">
    Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero los resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
    ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:<br />
    <ol>
        <li>Si usa el dispositivo de recolección de sangre, su hijo puede experimentar un dolor temporal o un hematoma en el lugar del pinchazo de la aguja.</li>
        <li>Existe el riesgo de pérdida de confidencialidad.</li>
    </ol>
</p>
<p class="consent_content">
    Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted será informado de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio? ¿Puede su hijo retirarse o ser retirado del estudio?
</p>
<p class="consent_content">
    La participación en la investigación es totalmente voluntaria. Le informaremos a usted y a su hijo si se encuentra alguna información nueva importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a que su hijo participe o retirar a su hijo en cualquier momento eliminando el perfil en línea de su hijo, o solicitando la eliminación de su cuenta.. Nuestros investigadores seguirán utilizando los datos sobre usted o su hijo que se recopilaron antes de que se retiraran. Estos datos no incluirán ninguna información personal que pueda identificar directamente a su hijo. Después de que su hijo retire, no se recopilarán más datos sobre su hijo
</p>
<p class="consent_content">
    Su hijo puede ser retirado del estudio si no se siguen las instrucciones que le dio el personal del estudio.
</p>
<p class="consent_header">
    ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo para su hijo por participar en este estudio. Usted recibirá un informe que detalla los resultados de nuestro análisis de la muestra de su hijo, así como datos y cifras que comparan la composición microbiana de su hijo con la de otros participantes del estudio. Sin embargo, el investigador puede aprender más sobre el microbioma humano en la salud y la enfermedad y proporcionar un recurso valioso para otros investigadores.
</p>
<p class="consent_header">
    ¿Se le compensará por participar en este estudio?
</p>
<p class="consent_content">
    Si su hijo participa en el estudio general, es decir, si lo inscribió a través del sitio web de colaboración colectiva de The Microsetta Initiative, no recibirá compensación económica por su participación.
</p>
<p class="consent_content">
    Si su hijo participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, podría recibir una compensación por su participación si completa todos los pasos requeridos, tal como le explicó el personal del estudio. Se le proporcionará un documento aparte que explica las opciones de compensación.
</p>
<p class="consent_header">
    ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit, pero no habrá ningún costo por participar en el procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de la participación de su hijo en el estudio, usted o su hijo proporcionarán información personal y/o confidencial que podría permitir identificar a su hijo si se hiciera pública, como el nombre, la fecha de nacimiento o la dirección. Nosotros tomamos todas las precauciones para proteger su identidad. Todos los datos que usted o su hijo proporcionan se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal crítico del estudio. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas.Los registros de investigación pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos la muestra de su hijo
</p>
<p class="consent_content">
    La información de los análisis de los datos y muestras biológicas de su hijo se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el de su hijo) pueden analizarse y publicarse en artículos científicos. Es posible que guardemos parte de la muestra de su hijo para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir los datos y/o muestras biológicas de su hijo en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar la(s) muestra(s) de su hijo y/o para fines de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, piel, orina o sangre) recolectadas de su hijo para este estudio y la información obtenida de las muestras biológicas de su hijo pueden usarse en esta investigación u otra investigación y compartirse con otras organizaciones. No participará en ningún valor comercial o beneficio derivado del uso de las muestras biológicas de su hijo y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong>Tenga en cuenta:</strong><br />
    Tenga en cuenta que no se analizará ADN humano como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra no pueden usarse para diagnosticar enfermedades o infecciones.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
    Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir que su hijo participe en esta investigación y que se procesen la(s) muestra(s) de su hijo.
</p>', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('parent_biospecimen', 'es_ES', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong><br />
    Bioespecímenes e Investigación de Uso Futuro
</p>
<p class="consent_header">
    ¿Quién está realizando el estudio, por qué se le pidió a su hijo que participara, cómo se seleccionó a su hijo y cuál es el número aproximado de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamado el microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y los virus. Lo invitamos a voluntariar a su hijo para este estudio porque vive en un lugar donde puede recibir un kit de muestreo para su hijo.Habrá aproximadamente 500000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se realiza este estudio?
</p>
<p class="consent_content">
    El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Los niños, como todos los seres humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Las muestras biológicas son muestras  del cuerpo de su hijo, como heces, piel, orina o sangre, que se utilizan con fines de investigación. Este estudio implica la recopilación, el almacenamiento y el uso de la información y las muestras biológicas de su hijo con el fin de procesar las muestras biológicas de su hijo y para futuras investigaciones. Los resultados se utilizarán para crear una base de datos de secuencias de ADN y otros datos de varios sitios del cuerpo, así como detalles sobre el niño participante que proporciona la muestra. Luego, los investigadores pueden usar esos datos mientras estudian temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué le pasará a su hijo(a) en este estudio?
</p>
<p class="consent_content">
    Si acepta la recolección y el procesamiento de las muestras biológicas de su hijo, le sucederá lo siguiente a su hijo:
</p>
<p class="consent_content">
    Usted ha recibido o recibirá un kit de muestra. El kit contiene dispositivos utilizados para recolectar muestras e instrucciones de uso. El dispositivo de recolección también puede incluir etanol al 95% para preservar la muestra y hacerla no infecciosa.
</p>
<p class="consent_content">
    Tomará muestras de una parte del cuerpo de su hijo (p. ej., heces, piel, boca, orificios nasales, orejas, vagina) como se describe en las instrucciones del kit. También se le pedirá que proporcione información general sobre la recolección, como la fecha y la hora en que se recolectó la muestra de su hijo. Todas las muestras deben devolverse en los contenedores incluidos de acuerdo con las instrucciones proporcionadas.
</p>
<p class="consent_content">
    Si se recolecta muestra de heces de su hijo, se le pedirá que tome una muestra de una variedad de formas, como las siguientes:<br />
    <ol>
        <li>Insertando las punta(s) del hisopo en papel higiénico usado y devolviendo el hisopo(s) en el recipiente de plástico suministrado;</li>
        <li>Insertando las puntas del hisopo en el papel higiénico usado y pasando las puntas por la superficie de una tarjeta para pruebas de sangre oculta en heces, y luego devuélvanos la tarjeta. La tarjeta para pruebas de sangre oculta en heces es el mismo instrumento que usa su médico para verificar si hay sangre en sus heces. La tarjeta para pruebas de sangre oculta en heces permite estabilizar las heces para su posterior análisis. No verificaremos si hay sangre en las heces con fines diagnósticos, puesto que no somos un laboratorio clínico;</li>
        <li>Usando el instrumento de cuchara para recoger una parte de la materia fecal en el tubo suministrado;</li>
        <li>Depositando papel higiénico sucio en el receptáculo suministrado;</li>
        <li>Enviando una muestra completa de heces en el recipiente de envío que le suministraremos. Dicho recipiente contiene una serie de compresas de hielo que enfriarán la muestra de manera fiable a -20 °C/-4 °F.</li>
    </ol>
</p>
<p class="consent_content">
    Si recibió un kit de recolección de sangre, este contiene materiales e instrucciones sobre cómo recolectar una muestra de sangre en casa. Es similar a la prueba que se usa para medir los niveles de glucosa pinchando el dedo. 
</p>
<p class="consent_content">
    Una vez que se haya analizado la muestra de su hijo, cargaremos los resultados en su cuenta y le enviaremos un correo electrónico con un enlace para iniciar sesión y verlos. Pueden pasar varios meses conocer los resultados del análisis del microbioma de su hijo. Si su hijo es parte de un subestudio específico, puede tomar más tiempo, según la duración del estudio.
</p>
<p class="consent_header">
    ¿Cuánto tiempo llevará cada procedimiento del estudio, cuánto tiempo debe dedicar en total su hijo y cuánto durará el estudio?
</p>
<p class="consent_content">
    Cada muestra que envíe se puede obtener en 5 minutos o menos. Esperamos que el estudio continúe durante muchos años, pero los resultados estarán disponibles para usted antes de que finalice el estudio.
</p>
<p class="consent_header">
    ¿Cuáles son los riesgos relacionados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias adicionales. Estos incluyen los siguientes:<br />
    <ol>
        <li>Si usa el dispositivo de recolección de sangre, su hijo puede experimentar un dolor temporal o un hematoma en el lugar del pinchazo de la aguja.</li>
        <li>Existe el riesgo de pérdida de confidencialidad.</li>
    </ol>
</p>
<p class="consent_content">
    Debido a que este es un estudio de investigación, puede haber algunos riesgos desconocidos que actualmente son imprevisibles. Usted será informado de cualquier nuevo hallazgo significativo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio? ¿Puede su hijo retirarse o ser retirado del estudio?
</p>
<p class="consent_content">
    La participación en la investigación es totalmente voluntaria. Le informaremos a usted y a su hijo si se encuentra alguna información nueva importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Puede negarse a que su hijo participe o retirar a su hijo en cualquier momento eliminando el perfil en línea de su hijo, o solicitando la eliminación de su cuenta.. Nuestros investigadores seguirán utilizando los datos sobre usted o su hijo que se recopilaron antes de que se retiraran. Estos datos no incluirán ninguna información personal que pueda identificar directamente a su hijo. Después de que su hijo retire, no se recopilarán más datos sobre su hijo
</p>
<p class="consent_content">
    Su hijo puede ser retirado del estudio si no se siguen las instrucciones que le dio el personal del estudio.
</p>
<p class="consent_header">
    ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo para su hijo por participar en este estudio. Usted recibirá un informe que detalla los resultados de nuestro análisis de la muestra de su hijo, así como datos y cifras que comparan la composición microbiana de su hijo con la de otros participantes del estudio. Sin embargo, el investigador puede aprender más sobre el microbioma humano en la salud y la enfermedad y proporcionar un recurso valioso para otros investigadores.
</p>
<p class="consent_header">
    ¿Se le compensará por participar en este estudio?
</p>
<p class="consent_content">
    Si su hijo participa en el estudio general, es decir, si lo inscribió a través del sitio web de colaboración colectiva de The Microsetta Initiative, no recibirá compensación económica por su participación.
</p>
<p class="consent_content">
    Si su hijo participa en un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, podría recibir una compensación por su participación si completa todos los pasos requeridos, tal como le explicó el personal del estudio. Se le proporcionará un documento aparte que explica las opciones de compensación.
</p>
<p class="consent_header">
    ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
    Puede haber costos asociados con la obtención de un kit, pero no habrá ningún costo por participar en el procedimiento de muestreo.
</p>
<p class="consent_header">
    ¿Y su confidencialidad?
</p>
<p class="consent_content">
    Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley. Como parte de la participación de su hijo en el estudio, usted o su hijo proporcionarán información personal y/o confidencial que podría permitir identificar a su hijo si se hiciera pública, como el nombre, la fecha de nacimiento o la dirección. Nosotros tomamos todas las precauciones para proteger su identidad. Todos los datos que usted o su hijo proporcionan se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa solo es accesible para el personal crítico del estudio. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas.Los registros de investigación pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_header">
    Cómo usaremos la muestra de su hijo
</p>
<p class="consent_content">
    La información de los análisis de los datos y muestras biológicas de su hijo se utilizará para estudiar el ADN no humano (por ejemplo, ADN bacteriano) que contiene. Los datos de las muestras del proyecto (incluido el de su hijo) pueden analizarse y publicarse en artículos científicos. Es posible que guardemos parte de la muestra de su hijo para que los investigadores puedan acceder a ella y puedan realizar estudios adicionales utilizando los otros compuestos de la misma, como ARN, proteínas o metabolitos. Si lo hacemos, eliminaremos toda la información directamente identificable antes de usarla o compartirla. Una vez que se hayan eliminado los identificadores, no le pediremos su consentimiento para usar o compartir los datos y/o muestras biológicas de su hijo en otras investigaciones. Además, los datos que se hayan eliminado de la información de identificación directa se cargarán en el Instituto Europeo de Bioinformática (http://www.ebi.ac.uk) y Qiita (https://qiita.ucsd.edu) para que otros investigadores tengan acceso y uso. Es posible que nos comuniquemos con usted si se necesita información o acción adicional para procesar la(s) muestra(s) de su hijo y/o para fines de re-consentimiento.
</p>
<p class="consent_content">
    Las muestras biológicas (como heces, piel, orina o sangre) recolectadas de su hijo para este estudio y la información obtenida de las muestras biológicas de su hijo pueden usarse en esta investigación u otra investigación y compartirse con otras organizaciones. No participará en ningún valor comercial o beneficio derivado del uso de las muestras biológicas de su hijo y/o la información obtenida de ellas.
</p>
<p class="consent_content">
    <strong>Tenga en cuenta:</strong><br />
    Tenga en cuenta que no se analizará ADN humano como parte de este ni de ningún estudio futuro. Además, los métodos que usamos para identificar microorganismos en su muestra no pueden usarse para diagnosticar enfermedades o infecciones.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
    Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para reportar problemas relacionados con la investigación.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir que su hijo participe en esta investigación y que se procesen la(s) muestra(s) de su hijo.
</p>', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('parent_data', 'en_US', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Parent Consent for Child to Act as a Research Subject
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    Who is conducting the study, why has your child been asked to participate, how was your child selected, and what is the approximate number of participants in the study?
</p>
<p class="consent_content">
    Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called the microbiome) that live in and on the body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  We are inviting you to volunteer your child for this study because you live in a location where you can receive a sampling kit for your child. There will be approximately 500,000 participants in the study from across the USA and from other countries around the world.
</p>
<p class="consent_header">
    Why is this study being done and what will happen to your child?
</p>
<p class="consent_content">
    The purpose of this study is to assess more accurately the microbial differences between people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. Children, like all humans, have a unique microbiome and including them in the study will help elucidate the development of the microbiome. If you agree to allow your child to take part in this study, we will ask you to complete online surveys/questionnaires about your child such as their age, weight, height, lifestyle, diet, and if your child has certain medical or health conditions. You should expect to spend an average of 5-10 minutes on each survey, but some may take up to 30 minutes to complete. 
</p>
<p class="consent_header">
    What benefits can be reasonably expected?
</p>
<p class="consent_content">
    There is no direct benefit to your child for participating in this study.  If you complete one of the questionnaires called Food Frequency Questionnaire (FFQ) for your child, you may receive a nutritional report evaluating your child''s eating pattern and nutrient intake with an overall diet score. The investigator(s), however, may learn more about relevant topics, such as gut-related health conditions.  
</p>
<p class="consent_header">
    What risks are associated with this study?
</p>
<p class="consent_content">
    Participation in this study may involve some added minimal risks or discomforts. While answering surveys, you or your child may feel frustration, emotional discomfort, fatigue, and/or boredom.  There is also a risk of loss of confidentiality, but we take every precaution to protect your identity and minimize the risks. All data you or your child provides is stored on secure systems within UC San Diego''s infrastructure and directly identifying information is accessible only to critical research personnel. The database that stores participant personal and sample information runs on a password-protected server that is accessible only to relevant staff such as Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. The professionally maintained database server has several layers of security: it is password protected, firewalled, only allows network connectivity from defined UC San Diego managed systems, employs access control lists, and is physically housed in a key card controlled UC San Diego facility. Nightly backups of the database are taken and maintained on a separate co-located system with additional security measures in place. Research records will be kept confidential to the extent allowed by law and may be reviewed by the UC San Diego Institutional Review Board.
</p>
<p class="consent_content">
    We may need to report information about known or reasonably suspected incidents of abuse or neglect of a child, dependent adult or elder including physical, sexual, emotional, and financial abuse or neglect. If any investigator has or is given such information, they may report such information to the appropriate authorities.
</p>
<p class="consent_content">
    Federal and State laws generally make it illegal for health insurance companies, group health plans, and most employers to discriminate against you based on your genetic information. This law generally will protect you in the following ways: a) Health insurance companies and group health plans may not request your genetic information that we get from this research. b) Health insurance companies and group health plans may not use your genetic information when making decisions regarding your eligibility or premiums. c) Employers with 5 or more employees may not use your genetic information that we get from this research when making a decision to hire, promote, or fire you or when setting the terms of your employment.
</p>
<p class="consent_content">
    Be aware that these laws do not protect you against genetic discrimination by companies that sell life insurance, disability insurance, or long-term care insurance.
</p>
<p class="consent_header">
    What are the alternatives to participating in this study and can you withdraw?
</p>
<p class="consent_content">
    Participation in this study is completely voluntary and your child is free to skip any question that they choose. We will inform you if any important new information is found during the course of this study that may affect your child wanting to continue. 
</p>
<p class="consent_content">
    You or your child can withdraw at any time by deleting your child''s online profile, or by requesting the deletion of your account. Our researchers will still use the data about your child that was collected before they withdrew. These data will not include any personal information that could directly identify your child. After your child withdraws, no further data will be collected from them.
</p>
<p class="consent_content">
    Your child may be withdrawn from the study if the instructions given by the study personnel are not followed.
</p>
<p class="consent_header">
    Are there any costs associated with participating in this study?
</p>
<p class="consent_content">
    There will be no cost to you or your child for completing the standard survey/questionnaire(s). However, there may be costs associated with having certain diet assessment tools made available to your child, such as the Food Frequency Questionnaire (FFQ).
</p>
<p class="consent_header">
    Know what we will collect
</p>
<p class="consent_content">
    As part of this research study, we will create and obtain information related to you or your child''s participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
</p>
<p class="consent_header">
    How we will use your child''s Personal Data
</p>
<p class="consent_content">
    The Personal Data you provide will be used for the following purposes:<br />
    <ul>
        <li>To share with members of the research team so they can properly conduct the research.</li>
        <li>For future research studies or additional research by other researchers.</li>
        <li>To contact you for the purpose of receiving alerts of your child''s participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s).</li>
        <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research.</li>
        <li>To confirm proper conduct of the study and research integrity.</li>
    </ul>
</p>
<p class="consent_content">
    If your child is part of a specific sub-study, and enrollment in the Microsetta Initiative is an add-on for participation in a separate companion study, your child''s data may be shared with the investigators of that study.
</p>
<p class="consent_header">
    Retention of your child''s Personal Data
</p>
<p class="consent_content">
    We may retain the Personal Data you provide for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your child''s Personal Data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your child''s information will be retained as necessary to comply with legal or regulatory requirements. 
</p>
<p class="consent_header">
    Your Privacy Rights
</p>
<p class="consent_content">
    The General Data Protection Regulation ("GDPR") requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your child''s Personal Data, including the right to access, correct, restrict, and withdraw your child''s personal information.
</p>
<p class="consent_content">
    The research team will store and process your child''s Personal Data at our research site in the United States. The United States does not have the same laws to protect your child''s Personal Data as States in the EU/EEA. However, the research team is committed to protecting the confidentiality of your child''s Personal Data. Additional information about the protections we will use is included in this consent document and in our Privacy Statement.  
</p>
<p class="consent_header">
    Who can you call if you have questions?
</p>
<p class="consent_content">
    If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    You may contact UC San Diego Office of IRB Administration at 858-246-4777 or email at irb@ucsd.edu to inquire about your rights as a research subject or to report research-related problems.
</p>
<p class="consent_content">
    If you have questions or complaints about our treatment of your Personal Data, or about our privacy practices more generally, please feel free to contact the UC San Diego Privacy Official by email at ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
    Your Signature and Consent
</p>
<p class="consent_content">
    You may download a copy of this consent document and a copy of the "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Experimental Subject''s Bill of Rights</a>" to keep.
</p>
<p class="consent_content">
    Your consent is entirely voluntary, but declining to provide it may impede your child''s ability to participate in this research.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('parent_data', 'es_MX', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién está realizando el estudio, por qué se le pidió a su hijo que participara, cómo se seleccionó a su hijo y cuál es el número aproximado de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamados microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y virus. Lo invitamos a voluntariar a su hijo para este estudio porque vive en un lugar donde puede recibir un kit de muestreo para su hijo. Habrá aproximadamente 500000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se realiza este estudio y qué le pasará a su hijo en este estudio?
</p>
<p class="consent_content">
    El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Los niños, como todos los seres humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Si usted acepta permitir que su hijo participe en este estudio, le pediremos que complete encuestas/cuestionarios en línea sobre su hijo, como su edad, peso, altura, estilo de vida, dieta y si su hijo tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas pueden tardar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
    ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo para su hijo por participar en este estudio. Si completa uno de los cuestionarios llamado Cuestionario de frecuencia de alimentos (FFQ) por su hijo, puede recibir un informe nutricional que evalúe el patrón de alimentación y la ingesta de nutrientes de su hijo con una puntuación general de la dieta. Sin embargo, los investigadores pueden aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué riesgos están asociados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Al responder encuestas, usted o su hijo pueden sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que usted o su hijo proporcionen se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas.Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_content">
    Es posible que necesitemos reportar información sobre incidentes conocidos o sospechados de abuso o negligencia de un niño, adulto dependiente o anciano, incluido abuso o negligencia física, sexual, emocional y financiera. Si algún investigador tiene o recibe dicha información, puede reportar dicha información a las autoridades correspondientes.
</p>
<p class="consent_content">
    Las leyes federales y estatales generalmente hacen que sea ilegal que las compañías de seguros de salud, los planes de salud grupales y la mayoría de los empleadores lo discriminen en función de su información genética. Esta ley generalmente lo protegerá de las siguientes maneras: a) Las compañías de seguros de salud y los planes de salud grupales no pueden solicitar su información genética que obtengamos de esta investigación. b) Las compañías de seguros de salud y los planes de salud grupales no pueden usar su información genética al tomar decisiones con respecto a su elegibilidad o primas. c) Los empleadores con 5 o más empleados no pueden usar su información genética que obtengamos de esta investigación al tomar una decisión para contratarlo, ascenderlo o despedirlo o al establecer los términos de su empleo.
</p>
<p class="consent_content">
    Tenga en cuenta que estas leyes no lo protegen contra la discriminación genética por parte de compañías que venden seguros de vida, seguros por discapacidad o seguros de atención a largo plazo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio y puede usted retirarse?
</p>
<p class="consent_content">
    La participación en este estudio es completamente voluntaria y usted es libre de omitir cualquier pregunta que elija. Le informaremos a usted y a su hijo si se encuentra alguna información nueva importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Usted o su hijo pueden retirarse en cualquier momento eliminando el perfil en línea de su hijo, o solicitando la eliminación de su cuenta.  Nuestros investigadores seguirán utilizando los datos sobre usted o su hijo que se recopilaron antes de que se retiraran. Estos datos no incluirán ninguna información personal que pueda identificar directamente a su hijo. Después de que su hijo retire, no se recopilarán más datos sobre su hijo.
</p>
<p class="consent_content">
    Su hijo puede ser retirado del estudio si no se siguen las instrucciones que le dio el personal del estudio.
</p>
<p class="consent_header">
    ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
    No habrá ningún costo para usted o su hijo por completar la encuesta/cuestionario(s) estándar. Sin embargo, puede haber costos asociados con tener ciertas herramientas de evaluación de la dieta disponibles para su hijo, como el Cuestionario de frecuencia de alimentos (FFQ).
</p>
<p class="consent_header">
    Conoce lo que recopilaremos
</p>
<p class="consent_content">
    Como parte de este estudio de investigación, crearemos y obtendremos información relacionada con su participación o la de su hijo en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
    Cómo utilizaremos los datos personales de su hijo
</p>
<p class="consent_content">
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
    <ul>
        <li>Compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
        <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
        <li>Para comunicarnos con usted con el fin de recibir alertas sobre el estado de participación de su hijo, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
        <li>Para cumplir con los requisitos legales y reglamentarios, incluidos los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
        <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
    </ul>
</p>
<p class="consent_content">
    Si su hijo es parte de un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, los datos de su hijo pueden compartirse con los investigadores de ese estudio.
</p>
<p class="consent_header">
    Conservación de los datos personales de su hijo
</p>
<p class="consent_content">
    Podemos retener los Datos Personales que nos proporcione durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Eliminaremos los Datos Personales de su hijo cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, la información de su hijo se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
    Sus derechos de privacidad
</p>
<p class="consent_content">
    El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con los Datos personales de su hijo, incluido el derecho a acceder, corregir, restringir y retirar la información personal de su hijo.
</p>
<p class="consent_content">
    El equipo de investigación almacenará y procesará los Datos Personales de su hijo en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger los Datos Personales de su hijo que los estados de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de los Datos Personales de su hijo. En este documento de consentimiento y en nuestra Declaración de privacidad se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
    Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_content">
    Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos Personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de Privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir que su hijo participe en esta investigación.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);

INSERT INTO ag.consent_documents (consent_type, locale, date_time, consent_content, reconsent_required, account_id, version)
    VALUES ('parent_data', 'es_ES', NOW(), '<p class="consent_title">
    <strong>University of California San Diego</strong><br />
    Consentimiento de los padres para que el niño actúe como sujeto de investigación
</p>
<p class="consent_title">
    <strong>The Microsetta Initiative</strong>
</p>
<p class="consent_header">
    ¿Quién está realizando el estudio, por qué se le pidió a su hijo que participara, cómo se seleccionó a su hijo y cuál es el número aproximado de participantes en el estudio?
</p>
<p class="consent_content">
    El Dr. Rob Knight está realizando un estudio de investigación para obtener más información sobre los trillones de bacterias y otros microorganismos (llamados microbioma) que viven dentro y sobre el cuerpo. Esto incluye eucariotas como hongos y parásitos, procariotas como bacterias y arqueas y virus. Lo invitamos a voluntariar a su hijo para este estudio porque vive en un lugar donde puede recibir un kit de muestreo para su hijo. Habrá aproximadamente 500000 participantes en el estudio de todos los EE. UU. y de otros países alrededor del mundo.
</p>
<p class="consent_header">
    ¿Por qué se realiza este estudio y qué le pasará a su hijo en este estudio?
</p>
<p class="consent_content">
    El propósito de este estudio es evaluar con mayor precisión las diferencias microbianas entre las personas y si estas diferencias pueden atribuirse a factores como el estilo de vida, la dieta, la constitución corporal, la edad o la presencia de enfermedades asociadas. Los niños, como todos los seres humanos, tienen un microbioma único e incluirlos en el estudio ayudará a dilucidar el desarrollo del microbioma. Si usted acepta permitir que su hijo participe en este estudio, le pediremos que complete encuestas/cuestionarios en línea sobre su hijo, como su edad, peso, altura, estilo de vida, dieta y si su hijo tiene ciertas condiciones médicas o de salud. Le tomará alrededor de 5 a 10 minutos en cada encuesta, pero algunas pueden tardar hasta 30 minutos en completarse.
</p>
<p class="consent_header">
    ¿Qué beneficios se pueden esperar?
</p>
<p class="consent_content">
    No hay ningún beneficio directo para su hijo por participar en este estudio. Si completa uno de los cuestionarios llamado Cuestionario de frecuencia de alimentos (FFQ) por su hijo, puede recibir un informe nutricional que evalúe el patrón de alimentación y la ingesta de nutrientes de su hijo con una puntuación general de la dieta. Sin embargo, los investigadores pueden aprender más sobre temas relevantes, como las condiciones de salud relacionadas con el intestino.
</p>
<p class="consent_header">
    ¿Qué riesgos están asociados con este estudio?
</p>
<p class="consent_content">
    La participación en este estudio puede implicar algunos riesgos o molestias mínimas. Al responder encuestas, usted o su hijo pueden sentir frustración, incomodidad emocional, fatiga y/o aburrimiento. También existe el riesgo de pérdida de confidencialidad, pero tomamos todas las precauciones para proteger su identidad y minimizar los riesgos. Todos los datos que usted o su hijo proporcionen se almacenan en sistemas seguros dentro de la infraestructura de UC San Diego y la información de identificación directa sólo es accesible para el personal de investigación crítico. La base de datos que almacena la información personal y de muestras de los participantes se ejecuta en un servidor protegido con contraseña al que solo puede acceder el personal pertinente, como el Dr. Knight, los coinvestigadores, los coordinadores de proyectos y de muestras, el administrador de TI y los codificadores de la base  de datos. El servidor de la base de datos mantenido profesionalmente tiene varias capas de seguridad: está protegido con contraseña, usa protección firewall, solo permite la conectividad de red desde definidos sistemas administrados de UC San Diego, emplea listas de control de acceso y está alojado físicamente en una instalación de UC San Diego controlada con tarjeta de acceso. Se realizan copias de seguridad nocturnas de la base de datos y se mantienen en un sistema separado ubicado en el mismo lugar con medidas de seguridad adicionales implementadas.Los registros de investigación se mantendrán confidenciales en la medida permitida por la ley y pueden ser revisados ​​por la Junta de Revisión Institucional de UC San Diego.
</p>
<p class="consent_content">
    Es posible que necesitemos reportar información sobre incidentes conocidos o sospechados de abuso o negligencia de un niño, adulto dependiente o anciano, incluido abuso o negligencia física, sexual, emocional y financiera. Si algún investigador tiene o recibe dicha información, puede reportar dicha información a las autoridades correspondientes.
</p>
<p class="consent_content">
    Las leyes federales y estatales generalmente hacen que sea ilegal que las compañías de seguros de salud, los planes de salud grupales y la mayoría de los empleadores lo discriminen en función de su información genética. Esta ley generalmente lo protegerá de las siguientes maneras: a) Las compañías de seguros de salud y los planes de salud grupales no pueden solicitar su información genética que obtengamos de esta investigación. b) Las compañías de seguros de salud y los planes de salud grupales no pueden usar su información genética al tomar decisiones con respecto a su elegibilidad o primas. c) Los empleadores con 5 o más empleados no pueden usar su información genética que obtengamos de esta investigación al tomar una decisión para contratarlo, ascenderlo o despedirlo o al establecer los términos de su empleo.
</p>
<p class="consent_content">
    Tenga en cuenta que estas leyes no lo protegen contra la discriminación genética por parte de compañías que venden seguros de vida, seguros por discapacidad o seguros de atención a largo plazo.
</p>
<p class="consent_header">
    ¿Cuáles son las alternativas a participar en este estudio y puede usted retirarse?
</p>
<p class="consent_content">
    La participación en este estudio es completamente voluntaria y usted es libre de omitir cualquier pregunta que elija. Le informaremos a usted y a su hijo si se encuentra alguna información nueva importante durante el curso de este estudio que pueda afectar su deseo de continuar.
</p>
<p class="consent_content">
    Usted o su hijo pueden retirarse en cualquier momento eliminando el perfil en línea de su hijo, o solicitando la eliminación de su cuenta.  Nuestros investigadores seguirán utilizando los datos sobre usted o su hijo que se recopilaron antes de que se retiraran. Estos datos no incluirán ninguna información personal que pueda identificar directamente a su hijo. Después de que su hijo retire, no se recopilarán más datos sobre su hijo.
</p>
<p class="consent_content">
    Su hijo puede ser retirado del estudio si no se siguen las instrucciones que le dio el personal del estudio.
</p>
<p class="consent_header">
    ¿Hay algún costo asociado con la participación en este estudio?
</p>
<p class="consent_content">
    No habrá ningún costo para usted o su hijo por completar la encuesta/cuestionario(s) estándar. Sin embargo, puede haber costos asociados con tener ciertas herramientas de evaluación de la dieta disponibles para su hijo, como el Cuestionario de frecuencia de alimentos (FFQ).
</p>
<p class="consent_header">
    Conoce lo que recopilaremos
</p>
<p class="consent_content">
    Como parte de este estudio de investigación, crearemos y obtendremos información relacionada con su participación o la de su hijo en el estudio de usted o de sus colaboradores para que podamos realizar esta investigación de manera adecuada. Los datos del estudio de investigación incluirán información de contacto, información demográfica, experiencias personales, preferencias de estilo de vida, información de salud, fecha de nacimiento, opiniones o creencias.
</p>
<p class="consent_header">
    Cómo utilizaremos los datos personales de su hijo
</p>
<p class="consent_content">
    Los Datos Personales que nos proporcione serán utilizados para las siguientes finalidades:<br />
    <ul>
        <li>Compartir con los miembros del equipo de investigación para que puedan realizar adecuadamente la investigación.</li>
        <li>Para futuros estudios de investigación o investigaciones adicionales realizadas por otros investigadores.</li>
        <li>Para comunicarnos con usted con el fin de recibir alertas sobre el estado de participación de su hijo, actualizaciones generales del programa, oportunidades para participar en investigaciones nuevas o futuras y/o como seguimiento de las preguntas que ha respondido en los cuestionarios.</li>
        <li>Para cumplir con los requisitos legales y reglamentarios, incluidos los requisitos para compartir datos con las agencias reguladoras que supervisan la investigación.</li>
        <li>Para confirmar la conducta adecuada del estudio y la integridad de la investigación.</li>
    </ul>
</p>
<p class="consent_content">
    Si su hijo es parte de un subestudio específico y la inscripción en The Microsetta Initiative es una extensión para participar en un estudio complementario, los datos de su hijo pueden compartirse con los investigadores de ese estudio.
</p>
<p class="consent_header">
    Conservación de los datos personales de su hijo
</p>
<p class="consent_content">
    Podemos retener los Datos Personales que nos proporcione durante el tiempo que sea necesario para cumplir con los objetivos de la investigación y garantizar la integridad de la investigación. Eliminaremos los Datos Personales de su hijo cuando ya no sean necesarios para el estudio o si retira su consentimiento, siempre que dicha eliminación no imposibilite o perjudique gravemente el logro de los objetivos del proyecto de investigación. Sin embargo, la información de su hijo se conservará según sea necesario para cumplir con los requisitos legales o reglamentarios.
</p>
<p class="consent_header">
    Sus derechos de privacidad
</p>
<p class="consent_content">
    El Reglamento general de protección de datos ("GDPR" por sus siglas en inglés) requiere que los investigadores le proporcionen información cuando recopilamos y usamos datos de investigación si se encuentra dentro de la Unión Europea (UE) o el Espacio Económico Europeo (EEE). El GDPR le otorga derechos relacionados con los Datos personales de su hijo, incluido el derecho a acceder, corregir, restringir y retirar la información personal de su hijo.
</p>
<p class="consent_content">
    El equipo de investigación almacenará y procesará los Datos Personales de su hijo en nuestro centro de investigación en los Estados Unidos. Los Estados Unidos no tienen las mismas leyes para proteger los Datos Personales de su hijo que los estados de la UE/EEE. Sin embargo, el equipo de investigación se compromete a proteger la confidencialidad de los Datos Personales de su hijo. En este documento de consentimiento y en nuestra Declaración de privacidad se incluye información adicional sobre las protecciones que utilizaremos.
</p>
<p class="consent_header">
    ¿A quién puede llamar si tiene preguntas?
</p>
<p class="consent_content">
    Si tiene preguntas o problemas relacionados con la investigación, puede comunicarse con Rob Knight al 858-246-1184 o enviar un correo electrónico a nuestra cuenta de ayuda: microsetta@ucsd.edu.
</p>
<p class="consent_content">
    Puede comunicarse con la Oficina de Administración del IRB de UC San Diego al 858-246-4777 o enviar un correo electrónico a irb@ucsd.edu para consultar sobre sus derechos como sujeto de investigación o para informar problemas relacionados con la investigación.
</p>
<p class="consent_content">
    Si tiene preguntas o quejas sobre nuestro tratamiento de sus Datos Personales, o sobre nuestras prácticas de privacidad en general, no dude en comunicarse con el Funcionario de Privacidad de UC San Diego por correo electrónico a ucsdprivacy@ucsd.edu.
</p>
<p class="consent_header">
    Firma y Consentimiento
</p>
<p class="consent_content">
    Usted puede descargar una copia de este documento de consentimiento y una copia de la "<a href="https://oag.ca.gov/sites/all/files/agweb/pdfs/research/bill_of_rights.pdf" target="_blank">Declaración de derechos del sujeto experimental</a>" para que las conserve.
</p>
<p class="consent_content">
    Su consentimiento es completamente voluntario, pero negarse a brindarlo puede impedir que su hijo participe en esta investigación.
</p>
', 'true', '000fc4cd-8fa4-db8b-e050-8a800c5d81b7', 2);
