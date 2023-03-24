#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from microsetta_private_api.config_manager import AMGUT_CONFIG

# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The American Gut Project Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

# Any media specific localizations
HELP_EMAIL = "info@%(email)s.org" % \
    {'email': AMGUT_CONFIG.locale.replace('_', '')}

_SITEBASE = AMGUT_CONFIG.sitebase

media_locale = {
    'ADDENDUM_CERT_ABUNDANT_MICROBES': _SITEBASE + "/static/img/Michael_Pollan_mod-13.png",
    'ADDENDUM_CERT_BARCHART': _SITEBASE + "/static/img/Michael_Pollan_mod-11.png",
    'ADDENDUM_CERT_BARCHART_LEGEND': _SITEBASE + "/static/img/Michael_Pollan_mod-12.png",
    'ADDENDUM_CERT_ENRICHED_MICROBES': _SITEBASE + "/static/img/Michael_Pollan_mod-14.png",
    'ADDENDUM_CERT_HEADER': _SITEBASE + "/static/img/Michael_Pollan_mod-02.png",
    'ADDENDUM_CERT_HEADER_PCOA': _SITEBASE + "/static/img/Michael_Pollan_mod-03.png",
    'ADDENDUM_CERT_NAME': _SITEBASE + "/static/img/Michael_Pollan_mod-01b.png",
    'ADDENDUM_CERT_PCOA_AGES_POP': _SITEBASE + "/static/img/Michael_Pollan_mod-09.png",
    'ADDENDUM_CERT_PCOA_AG_POPULATION': _SITEBASE + "/static/img/Michael_Pollan_mod-10.png",
    'ADDENDUM_CERT_PCOA_BODYSITES': _SITEBASE + "/static/img/Michael_Pollan_mod-08.png",
    'ADDENDUM_CERT_PCOA_LEGEND': _SITEBASE + "/static/img/Michael_Pollan_mod-04.png",
    'ADDENDUM_CERT_RARE_MICROBES': _SITEBASE + "/static/img/Michael_Pollan_mod-15.png",
    'ADDENDUM_CERT_TITLE': _SITEBASE + "/static/img/Michael_Pollan_mod-01.png",
    'ADDENDUM_PCOA_AGES_POPS': _SITEBASE + "/static/img/PCoA2.png",
    'ADDENDUM_PCOA_AG_POPULATION': _SITEBASE + "/static/img/PCoA3.png",
    'ADDENDUM_PCOA_BODYSITES': _SITEBASE + "/static/img/PCoA1.png",
    'ADDENDUM_TAX_BARCHART': _SITEBASE + "/static/img/TaxFig.png",
    'ADD_PARTICIPANT': "https://player.vimeo.com/video/63931218",
    'ADD_PARTICIPANT_IMG_1': _SITEBASE + "/static/img/add_participant.png",
    'ADD_PARTICIPANT_IMG_MENU': _SITEBASE + "/static/img/add_participant_menu.png",
    'ADD_SAMPLE_HIGHLIGHT': _SITEBASE + "/static/img/add_sample_highlight.png",
    'ADD_SAMPLE_OVERVIEW': _SITEBASE + "/static/img/add_sample_overview.png",
    'ALT_GUT_SITE': 'https://microbio.me',
    'AMERICAN_GUT_PROJECT': 'http://americangut.org',
    'BRITISH_GUT_PROJECT': 'http://britishgut.org',
    'EMAIL_ERROR': "There was a problem sending your email. Please contact us directly at <a href='mailto:%(help_email)s'>%(help_email)s</a>" % {'help_email': HELP_EMAIL},
    'EMAIL_SENT': 'Your message has been sent. We will reply shortly',
    'FAQ_AMBIGUOUS_PASS': _SITEBASE + "/static/img/creds_example.png",
    'FAVICON': _SITEBASE + "/static/img/favicon.ico",
    'FOBT_PDF': _SITEBASE + '/static/img/FOBT_instructions.pdf',
    'GUT_PROJECT_SHORTHANDS': ['American Gut', 'British Gut'],
    'HELP_EMAIL': HELP_EMAIL,
    'LOCALE': AMGUT_CONFIG.locale,
    'LOG_SAMPLE_OPTS': _SITEBASE + "/static/img/log_sample_options.png",
    'NAV_ADDENDUM': "How do I interpret results?",
    'NAV_ADD_ANIMAL': "Add Animal Source",
    'NAV_ADD_HUMAN': "Add Human Source",
    'NAV_ALT_GUT': ' Participant Site',
    'NAV_AMERICAN_GUT_PROJECT': 'American Gut Project',
    'NAV_ANIMAL_SAMPLES': "Animal Samples",
    'NAV_BRITISH_GUT_PROJECT': 'British Gut Project',
    'NAV_CHANGE_PASSWORD': "Change Password",
    'NAV_CONTACT_US': "Contact Us",
    'NAV_ENV_SAMPLES': "Environmental Samples",
    'NAV_FAQ': "FAQ",
    'NAV_REGISTER_KIT': 'Register Kit',
    'NAV_FORGOT_KITID': "I forgot my kit ID",
    'NAV_FORGOT_PASSWORD': "I forgot my password",
    'NAV_HOME': "Home",
    'NAV_HUMAN_SAMPLES': "Human Samples",
    'NAV_JOIN_PROJECT': "Join The Project",
    'NAV_KIT_INSTRUCTIONS': "Kit Instructions",
    'NAV_LOGOUT': "Log out",
    'NAV_LOG_SAMPLE': "Assign Sample",
    'NAV_MICROBIOME_101': "%(project_shorthand)s 101" % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'NAV_MICROBIOME_FAQ': "Human Microbiome FAQ",
    'NAV_OTHER_SITES': 'Other Sites',
    'NAV_PARTICIPANT_LOGIN': "Participant Log In",
    'NAV_PARTICIPANT_RESOURCES': "Participant Resources",
    'NAV_PRELIM_RESULTS': "Preliminary Results!",
    'NAV_RECEIVED': "(Received)",
    'PORTAL_DIET_QUESTIONS': _SITEBASE + "/static/img/diet_questions.png",
    'PROJECT_TITLE': AMGUT_CONFIG.project_name,
    'RAW_DATA_1': _SITEBASE + '/static/img/raw_data_instructions_1.png',
    'RAW_DATA_2': _SITEBASE + '/static/img/raw_data_instructions_2.png',
    'SAMPLE_BARCODE': _SITEBASE + "/static/img/sample_barcode.jpg",
    'SHORTHAND': AMGUT_CONFIG.project_shorthand,
    'SITEBASE': _SITEBASE,
    'STEPS_VIDEO': "https://player.vimeo.com/video/63542787",
    'SWAB_HANDLING': "https://player.vimeo.com/video/62393487"
}

_HANDLERS = {
    'ADD_BARCODE_ERROR': "Could not add barcode to database. Did you hit the back button while registering and press 'register user' again?",
    'ADD_KIT_ERROR': 'Could not add kit to database. Did you hit the back button while registering and press "Register Kit" again?',
    'AUTH_REGISTER_BODY': "Thank you for registering with the %(project_name)s! Your verification code is:\n\n{0}\n\nYou will need this code to verifiy your kit on the %(project_shorthand)s webstite. To get started, please log into:\n\nhttps://microbio.me%(sitebase)s\n\nEnter the kit_id and password found inside your kit, verify the contents of your kit, and enter the verification code found in this email.{1}\n\nSincerely,\nThe %(project_shorthand)s Team" % {'project_shorthand': AMGUT_CONFIG.project_shorthand, 'project_name': AMGUT_CONFIG.project_name, 'sitebase': media_locale['SITEBASE']},
    'AUTH_REGISTER_PGP': "\n\nFor the PGP cohort, we are requesting that you collect one sample from each of the following sites:\n\nLeft hand\nRight hand\nForehead\nMouth\nFecal\n\nThis is important to ensure that we have the same types of samples for all PGP participants which, in turn, could be helpful in downstream analysis when looking for relationships between the microbiome and the human genome\n\n.",
    'AUTH_REGISTER_SUBJECT': "%(project_shorthand)s Verification Code" % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'AUTH_SUBJECT': "You have registered your kit!  Your verification code is below.",
    'BARCODE_ERROR': "ERROR: No barcode was requested",
    'CHANGE_PASS_BODY': 'This is a courtesy email to confirm that you have changed your password for your kit with ID %s. If you did not request this change, please email us immediately at {0}'.format(media_locale['HELP_EMAIL']),
    'CHANGE_PASS_SUBJECT': '%(project_shorthand)s Password Reset' % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'INVALID_KITID': "Invalid Kit ID or Password",
    'KIT_IDS_BODY': 'Your {1} Kit IDs are %s. You are receiving this email because you requested your Kit ID from the {1} web page If you did not request your Kit ID please email {0} Thank you,\n The {1} Team\n'.format(media_locale['HELP_EMAIL'], AMGUT_CONFIG.project_shorthand),
    'KIT_IDS_SUBJECT': '%(project_shorthand)s Kit ID' % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'KIT_REG_SUCCESS': 'Kit registered successfully.',
    'MESSAGE_SENT': "Your message has been sent. We will reply shortly",
    'MINOR_PARENTAL_BODY': "Thank you for your interest in this study. Because of your status as a minor, we will contact you within 48 hours to verify parent/guardian consent.",
    'MISSING_NAME_EMAIL': 'Missing participant name or email. Please retry, adding all required information.',
    'PARTICIPANT_EXISTS': 'Participant %s already exists! This means we already have a survey on file under this name. Try using a variation of the name (such as substituting an initial for the first or last name).',
    'REGISTER_KIT': 'Kit has not been registered. Please click "Register Kit" link.',
    'RESET_PASS_BODY': 'The password on {1} Kit ID %s has been reset please click the link below within two hours\n\nhttps://microbio.me{0}/change_pass_verify/?email=%s&kitid=%s&passcode=%s'.format(media_locale['SITEBASE'], AMGUT_CONFIG.project_shorthand),
    'SUCCESSFULLY_ADDED': 'Successfully added %s!',
    'SUCCESSFULLY_EDITED': 'Successfully edited %s!'
}

_NEW_PARTICIPANT = {
    'ADD_HUMAN_TITLE': 'Add a New Human Source',
    'SEL_AGE_RANGE': 'Select age range of participant:',
    'ADD_HUMAN_HELP_SUGGESTION': 'If you need help with the website, please use the contact mechanism in the menu to the left. Please do not email the people listed in this form for help, unless it has to do with an injury. ',
    'AGE_0_6': '3 months - 6 years',
    'AGE_7_12': '7-12 years',
    'AGE_13_17': '13-17 years',
    'AGE_18': '18+ years',
    'ASSENT_7_12': '''
        <p style="text-align: center; font-weight: bold;">University of California, San Diego<br />
        Assent to Act as a Research Subject<br />
        (Ages 7-12 years)</p>
        <p style="text-align: center; font-weight: bold;">The Microsetta Initiative (a study about microbes)</p>
        <p>
            Dr. Rob Knight and his research team are doing a research study to find out more about the trillions of  tiny living things like bacteria and viruses that live in you or on you. These tiny things are called microbes, and you are being asked if you want to be in this study because the kinds of microbes you have is unique - not the same as anyone else on earth. We may be able to tell if you have been infected with something (like the virus that causes COVID-19) but we can’t tell you that because we are not allowed to do that.
        </p>
        <p>
            If you decide you want to be in this research study, this is what will happen to you:<br />
            We will ask you or your mom or dad to sample some place on your body (like skin or mouth) or your poop (from toilet paper) with something that looks like 2 Q-tips.  Sometimes we need more poop for our research and then we will ask you to poop into a plastic bowl that is under the seat of the toilet and catches the poop as it comes out.  Your mom or dad will send it to us in the bowl. We may also ask your mom or dad to prick your finger so that we can get a little bit of your blood.
        </p>
        <p>
            Sometimes kids don’t feel good while being in this study. You might feel a little bit sore where your skin is rubbed with the Q-tip and you will feel it if they prick your finger to get blood. Most people don’t mind these feelings.
        </p>
        <p>
            If you feel any of these things, or other things, be sure to tell your mom or dad.
        </p>
        <p>
            You don’t have to be in this research study if you don’t want to. Nobody will be mad at you if you say no. Even if you say yes now and change your mind after you start doing this study, you can stop and no one will be mad.
        </p>
        <p>
            Be sure to ask your parents if you have questions.  You can also ask them to call Dr. Knight or his research team so they can tell you more about anything you don’t understand. 
        </p>
    ''',
    'ASSENT_13_17': '''
        <p style="text-align: center; font-weight: bold;">University of California, San Diego<br />
        Assent to Act as a Research Subject<br />
        (Ages 13-17 years)</p>
        <p style="text-align: center; font-weight: bold;">The Microsetta Initiative</p>
        <p>
            <strong><i>Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?</i></strong><br />
            Dr. Rob Knight is conducting a research study to find out more about all the many bacteria and other microorganisms (called your microbiome) that live on and within your body. You have been asked to participate in this study because you, and everyone else on earth, have a unique microbiome, and the more people we study of all ages, the more we will understand about how the microorganisms may help or harm us. There will be approximately 100,000 participants in total in the study from across the USA and from other countries around the world.
        </p>
        <p>
            <strong><i>Why is this study being done?</i></strong><br />
            The purpose of this study is to assess more accurately the differences between people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases.  The results will be used to create a database of sequence data and metabolites from various body sites (e.g. skin, mouth, gut, blood), as well as details about you (the participant supplying the sample). Researchers can then use that data while studying relevant topics, such as gut-related health conditions.
        </p>
        <p>
            <strong><i>What will happen to you in this study and which procedures are standard of care and which are experimental?</i></strong><br />
            If you agree to participate in this study, the following will happen to you:<br/><br />
            You will fill in a questionnaire online that asks questions about you, such as age, weight, height, what you eat, if you have taken antibiotics, if you have certain diseases and if you take supplements like vitamins.  You will also be asked to answer questions about how the COVID-19 pandemic is affecting how you sleep and how you feel.  There are also other types of questions that are about specific topics which you can choose to answer if you think they apply to you. Then you will sample yourself using the kit that was provided to you .  Instructions are included in the kit so you know what to do.  The most common sample is of your poop (stool) where you apply a small smear to the tips of a swab from used toilet tissue or to a card (called an FOBT card). You may also be asked to scoop some poop using a small spoon-like tool, place used toilet paper into a special receptacle we provide, or poop into a plastic container that you place under the toilet seat. You may also need to sample a small area of skin, your tongue or mouth, your nostrils, ear wax, or vagina.  We may also ask someone (like your mom or dad) to take a small sample of blood by pricking your finger and then collecting the blood on 2 small swabs. None of these samples or investigations will allow us to make a diagnosis of disease and we are not looking at anything in your own DNA that can also be found in your poop,skin, or saliva.
        </p>
        <p>
            <strong><i>How much time will each study procedure take, what is your total time commitment, and how long will the study last?</i></strong><br />
            To complete the online questionnaire should take 30-45 minutes or less.  Each sample you send can be obtained in 5 minutes or less.  We expect the study to continue for many years but your results will be available to you before the end of the study (usually within a few months of us receiving the sample).
        </p>
        <p>
            <strong><i>What risks are associated with this study?</i></strong><br />
            Participation in this study may involve some added risks or discomforts. These include the following:<br />
            <blockquote>
                <ol>
                    <li>While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom.</li>
                    <li>You may experience temporary pain or a bruise at the site of the needle-stick if you take the blood test.</li>
                    <li>There is a risk of loss of confidentiality.</li>
                </ol>
            </blockquote>
            Because this is a research study, there may be some unknown risks that are currently unforeseeable. You and your parents will be informed of any significant new findings.
        </p>
        <p>
            <strong><i>What are the alternatives to participating in this study?</i></strong><br />
            You do not have to participate.
        </p>
        <p>
            <strong><i>What benefits can be reasonably expected?</i></strong><br />
            There is no direct benefit to you for participating in this study. You will get access to your data that will give you and your parents an idea of what is in your sample and how it compares with other people like you (age, sex).
        </p>
        <p>
            <strong><i>Can you choose to not participate or withdraw from the study without penalty or loss of benefits?</i></strong><br />
            Participation in research is entirely voluntary. You may refuse to participate or withdraw at any time without penalty or loss of benefits to which you are entitled. If you decide that you no longer wish to continue in this study, you may withdraw your consent by requesting the deletion of your source and/or account through your online account. Our researchers will still use the data about you that was collected before you withdrew. After you withdraw, no further data will be collected from you.<br /><br />
            We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
        </p>
        <p>
            <strong><i>Can you be withdrawn from the study without your assent?</i></strong><br />
            You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
        </p>
        <p>
            <strong><i>Will you be compensated for participating in this study?</i></strong><br />
            You will not be financially compensated in this study.
        </p>
        <p>
            <strong><i>Are there any costs associated with participating in this study?</i></strong><br />
            After you have signed up for the project and mailed in your sample there will be no costs to you for participating in the study.
        </p>
        <p>
            <strong><i>What if you are injured as a direct result of being in this study?</i></strong><br />
            If you are injured or become ill as a direct result of this research study, you will be provided with medical care.
        </p>
        <p>
            <strong><i>What about your confidentiality?</i></strong><br />
            Research records will be kept confidential to the extent allowed by law.  As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego's infrastructure and directly identifying information is accessible only to critical study personnel. The code key (that relates participant personal information to sample barcodes) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.
        </p>
        <p>
            <strong><i>Know what we will collect </i></strong><br />
            As part of this research study, we will create and obtain information related to you and your participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include: contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
        </p>
        <p>
            <strong><i>How we will use your Sample</i></strong><br />
            We will use the sample you provide to study the non-human DNA (e.g. bacterial DNA) in it. We may save some of your sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. We may contact you if additional information or action is needed in order to process your sample(s) and/or for re-consenting purposes.
        </p>
        <p>
            <strong><i>How we will use your Personal Data</i></strong><br />
            The Personal Data you provide will be used for the following purposes:<br />
            <blockquote>
                <ul>
                    <li>To share with members of the research team so they can properly conduct the research</li>
                    <li>For future research studies or additional research by other researchers</li>
                    <li>To contact you for the purpose of receiving alerts of your participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s)</li>
                    <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research</li>
                    <li>To confirm proper conduct of the study and research integrity</li>
                </ul>
            </blockquote>
        </p>
        <p>
            <strong><i>Retention of your Personal Data</i></strong><br />
            We may retain your personal data for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your personal data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your information will be retained as necessary to comply with legal or regulatory requirements.
        </p>
        <p>
            <strong><i>Your Privacy Rights</i></strong><br />
            The General Data Protection Regulation (“GDPR”) requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your Personal Data, including the right to access, correct, restrict, and withdraw your personal information.<br /><br />
            The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as States in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Study Data. Additional information about the protections we will use is included in this consent document.
        </p>
        <p>
            <strong><i>Who can you call if you have questions?</i></strong><br />
            If you have questions or research-related problems, you may reach us by emailing our help account microsetta@ucsd.edu or Rob Knight at 858-246-1184.<br /><br />
            You may call the Office of IRB Administration at 858-246-4777 to inquire about your rights as a research subject or to report research-related problems.<br /><br />
            If you have questions or complaints about our treatment of your Personal Data, or about our privacy practices more generally, please feel free to contact the UC San Diego Privacy Official by email at ucsdprivacy@ucsd.edu.
        </p>
        <p>
            <strong><i>Your Signature and Assent</i></strong><br />
            You may download a copy of  this assent document and a copy of the “Experimental Subject's Bill of Rights” to keep.
        </p>
    ''',
    'CONSENT_18': '''
        <p style="text-align: center; font-weight: bold;">University of California, San Diego<br />
        Consent to Act as a Research Subject</p>
        <p style="text-align: center; font-weight: bold;">The Microsetta Initiative</p>
        <p>
            <strong><i>Who is conducting the study, why have you been asked to participate, how were you selected, and what is the approximate number of participants in the study?</i></strong><br />
            Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called your microbiome) that live in and on your body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  You have been asked to participate in this study because your microbiome is unique – not the same as anyone else’s on earth. There will be approximately 100,000 participants in the study from across the USA and from other countries around the world.
        </p>
        <p>
            <strong><i>Why is this study being done?</i></strong><br />
            The purpose of this study is to assess more accurately the differences among people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases.  The results will be used to create a database of sequence data and metabolites from various body sites (e.g. skin, mouth, gut, blood), as well as details about the person supplying the sample. Researchers can then use that data while studying relevant topics, such as gut-related health conditions.
        </p>
        <p>
            <strong><i>What will happen to you in this study?</i></strong><br />
            If you agree to be in this study, the following will happen to you:<br /><br />
            You have received or will receive a sample kit.  The kit contains devices used to collect samples and instructions for use.  The collection device may also include 95% ethanol to preserve the sample and make it non-infectious.<br /><br />
            We will ask you to complete an online questionnaire about you (e.g. age, weight, height), your lifestyle, and what you eat.  There are also other questionnaires that are more topic-focused, which you can choose to complete if they apply to you.   These may include questions related to the following topics, among others: COVID-19, Autism-Spectrum Disorder, migraines, surfing, consumption of fermented foods, consumption of foods containing polyphenols. You should complete these if they're applicable and you want to provide additional information that may assist our research.<br />
            You will then collect a sample of yourself (e.g. stool, skin, mouth, nostril, ear, vagina), pet, or environment as described in the kit instructions or in the instructions provided to you by study coordinators. If collecting from stool, you will be asked to sample in one of a variety of ways, such as the following:<br />
            <blockquote>
                <ol>
                    <li>By inserting the tips of the swab into used toilet tissue and returning the sample in the provided plastic container;</li>
                    <li>By inserting the tips of the swab into used toilet tissue and applying the tips to the surface of a Fecal Occult Blood Test (FOBT) card, then returning the card to us.  The FOBT card is the same device used by your doctor to check for blood in your stool.  The FOBT card stabilizes the stool material for later analysis.  We will not check if there is blood in the stool for diagnostic purposes because we are not a clinical laboratory;</li>
                    <li>By using the scooper device to scoop a part of the fecal material into the provided tube;</li>
                    <li>Depositing soiled toilet paper into the provided receptacle;</li>
                    <li>Submitting a whole stool sample in a shipping container we will provide.  This container will have ice packs that reliably cool the sample to -20 degrees Celsius/-4 degrees Fahrenheit.</li>
                </ol>
            </blockquote>
            If you received a blood collection kit, it contains materials and instructions on how to collect a blood sample at home.  It is similar to the test used to test glucose levels by pricking your finger. <br /><br />
            All samples should be returned to us in the included containers according to the instructions provided.<br /><br />
            We would like you to understand what you will receive in return for your participation, and what we will do with your sample.<br /><br />
            The samples in the project (including yours) may be analyzed and published in scientific articles. DNA and RNA will be extracted from the sample and amplified by PCR (polymerase chain reaction), and then sequenced to see what microorganisms are present in your sample and in what proportions. We may also use the remaining sample to look more carefully at specific microorganisms present, or to investigate other chemical compounds such as metabolites or proteins.  Please be aware that <strong>no human DNA</strong> will be analyzed as part of this or any future studies.  We estimate that it will take 2-3 months for you to learn the results of the initial bacterial diversity estimation. If you are a part of a specific sub-study, it  may take longer, depending on the duration of the study.We will upload results to your account when available and send you an email with a link to log in and view them.<br /><br />
            We also want you to understand that the methods we use for identifying microorganisms in your sample <strong>cannot be used to diagnose disease or infection</strong>.  The results are not medically actionable. The report includes a notation of the rare types of microorganisms for  your interest only. The techniques we use to identify the organisms cannot be used for species- level resolution.<br /><br />
            <strong><u>Please Note</u></strong>: The sequencing is <strong>not for diagnostic purposes and does not target human DNA</strong>.
        </p>
        <p>
            <strong><i>How much time will each study procedure take, what is your total time commitment, and how long will the study last?</i></strong><br />
            Completing the main online questionnaire should take 30 - 45 minutes or less. Each additional survey may take up to an additional 30 minutes to complete. Each sample you send can be obtained in 5 minutes or less.  We expect the study to continue for many years but your results will be available to you before the end of the study (usually within a few months of us receiving the sample).  
        </p>
        <p>
            <strong><i>What risks are associated with this study?</i></strong><br />
            Participation in this study may involve some added risks or discomforts. These include the following:<br />
            <blockquote>
                <ol>
                    <li>While answering surveys, you may feel frustration, emotional discomfort, fatigue, and/or boredom.</li>
                    <li>If using the blood collection device, you may experience temporary pain or a bruise at the site of the needle-stick.</li>
                    <li>There is a risk of loss of confidentiality.</li>
                </ol>
            </blockquote>
            Because this is a research study, there may be some unknown risks that are currently unforeseeable. You will be informed of any significant new findings.
        </p>
        <p>
            <strong><i>What are the alternatives to participating in this study?</i></strong><br />
            You do not have to participate.
        </p>
        <p>
            <strong><i>What benefits can be reasonably expected?</i></strong><br />
            There is no monetary or direct benefit for participating in this study. You will receive a report detailing the results of our analysis on your sample, as well as facts and figures comparing your microbiome's composition to that of other study participants.
        </p>
        <p>
            <strong><i>Can you choose to not participate or withdraw from the study without penalty or loss of benefits?</i></strong><br />
            Participation in research is entirely voluntary. You may refuse to participate or withdraw at any time without penalty or loss of benefits to which you are entitled. If you decide that you no longer wish to continue in this study, you may withdraw your consent by requesting the deletion of your source and/or account through your online account. We will inform you if any important new information is found during the course of this study that may affect your wanting to continue.
        </p>
        <p>
            <strong><i>Can you be withdrawn from the study without your consent?</i></strong><br />
            You may be withdrawn from the study if you do not follow the instructions given to you by the study personnel.
        </p>
        <p>
            <strong><i>Will you be compensated for participating in this study?</i></strong><br />
            You will not be financially compensated in this study.
        </p>
        <p>
            <strong><i>Are there any costs associated with participating in this study?</i></strong><br />
            After you have signed up for the project and mailed in your sample there will be no costs to you for participating in the study. 
        </p>
        <p>
            <strong><i>What if you are injured as a direct result of being in this study?</i></strong><br />
            If you are injured as a direct result of participation in this research, the University of California will provide any medical care you need to treat those injuries. The University will not provide any other form of compensation to you if you are injured. You may call the Office of IRB Administration at (858) 246-4777 for more information about this, to inquire about your rights as a research subject or to report research-related problems.
        </p>
        <p>
            <strong><i>What about your confidentiality?</i></strong><br />
            Research records will be kept confidential to the extent allowed by law. As part of your participation in the study, you will provide personal and/or sensitive information that could allow you to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you provide is stored on secure systems within UC San Diego's infrastructure and directly identifying information is accessible only to critical research personnel. The code key (that relates participant personal information to sample barcodes) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board.<br /><br />
            We may need to report information about known or reasonably suspected incidents of abuse or neglect of a child, dependent adult or elder including physical, sexual, emotional, and financial abuse or neglect. If any investigator has or is given such information, he or she may report such information to the appropriate authorities.<br /><br />
            (Federal and State laws generally make it illegal for health insurance companies, group health plans, and most employers to discriminate against you based on your genetic information. This law generally will protect you in the following ways: a) Health insurance companies and group health plans may not request your genetic information that we get from this research. b) Health insurance companies and group health plans may not use your genetic information when making decisions regarding your eligibility or premiums. c) Employers with 5 or more employees may not use your genetic information that we get from this research when making a decision to hire, promote, or fire you or when setting the terms of your employment.<br /><br />
            Be aware that these laws do not protect you against genetic discrimination by companies that sell life insurance, disability insurance, or long-term care insurance.)
        </p>
        <p>
            <strong><i>Know what we will collect </i></strong><br />
            As part of this research study, we will create and obtain information related to you and your participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include: contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
        </p>
        <p>
            <strong><i>How we will use your Sample</i></strong><br />
            We will use the sample you provide to study the non-human DNA (e.g. bacterial DNA) in it. We may save some of your sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. We may contact you if additional information or action is needed in order to process your sample(s) and/or for re-consenting purposes.
        </p>
        <p>
            <strong><i>How we will use your Personal Data</i></strong><br />
            The Personal Data you provide will be used for the following purposes:<br />
            <blockquote>
                <ul>
                    <li>To share with members of the research team so they can properly conduct the research</li>
                    <li>For future research studies or additional research by other researchers</li>
                    <li>To contact you for the purpose of receiving alerts of your participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s)</li>
                    <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research</li>
                    <li>To confirm proper conduct of the study and research integrity</li>
                </ul>
            </blockquote>
        </p>
        <p>
            <strong><i>Retention of your Personal Data</i></strong><br />
            We may retain your Personal Data for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your Personal Data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your information will be retained as necessary to comply with legal or regulatory requirements.
        </p>
        <p>
            <strong><i>Your Privacy Rights</i></strong><br />
            The General Data Protection Regulation (“GDPR”) requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your Personal Data, including the right to access, correct, restrict, and withdraw your personal information. <br /><br />
            The research team will store and process your Personal Data at our research site in the United States. The United States does not have the same laws to protect your Personal Data as countries in the EU/EEA. However, the research team is committed to protecting the confidentiality of your Study Data. Additional information about the protections we will use is included in this consent document.  
        </p>
        <p>
            <strong><i>Who can you call if you have questions?</i></strong><br />
            If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.<br /><br />
            You may call the Office of IRB Administration at 858-246-4777 to inquire about your rights as a research subject or to report research-related problems.<br /><br />
            If you have questions or complaints about our treatment of your Personal Data, or about our privacy practices more generally, please feel free to contact the UC San Diego Privacy Official by email at ucsdprivacy@ucsd.edu.
        </p>
        <p>
            <strong><i>Your Signature and Consent</i></strong><br />
            You may download a copy of this consent document and a copy of the “Experimental Subject's Bill of Rights” to keep.<br /><br />
            Your consent is entirely voluntary, but declining to provide it may materially impede your ability to participate in this research and receive a kit.
        </p>
    ''',
    'CONSENT_YOUR_CHILD': '''
        <p style="text-align: center; font-weight: bold;">University of California, San Diego<br />
        Parent Consent for Child to Act as a Research Subject</p>
        <p style="text-align: center; font-weight: bold;">The Microsetta Initiative</p>
        <p>
            <strong><i>Who is conducting the study, why has your child been asked to participate, how was your child selected, and what is the approximate number of participants in the study?</i></strong><br />
            Dr. Rob Knight is conducting a research study to find out more about the trillions of bacteria and other microorganisms (called the microbiome) that live in and on the body. This includes eukaryotes like fungi and parasites, prokaryotes like bacteria and archaea, and viruses.  You are volunteering your child for this study because you want to know more about the microbiome of your child. Children like all humans have a unique microbiome and including them in the study will help elucidate the development of the microbiome. There will be approximately 100,000 participants in the study from across the USA and from other countries around the world.
        </p>
        <p>
            <strong><i>Why is this study being done?</i></strong><br />
            The purpose of this study is to assess more accurately the differences between people and whether these differences can be attributed to factors such as lifestyle, diet, body type, age or the presence of associated diseases. The results will be used to create a database of sequence data and metabolites from various body sites (e.g. skin, mouth, gut) as well as details about the child participant supplying the sample. Researchers can then use that data while studying relevant topics, such as gut-related health conditions. 
        </p>
        <p>
            <strong><i>What will happen to your child in this study and which procedures are standard of care and which are experimental?</i></strong><br />
            If you agree to allow your child to participate in this study, the following will happen to your child:<br /><br />
            You have received or will receive a sample kit.  The kit contains devices used to collect samples and instructions for use.  The collection device may also include 95% ethanol to preserve the sample and make it non-infectious.<br /><br />
            We will ask you to complete an online questionnaire about your child (e.g. age, weight, height), your child’s lifestyle, and what your child eats. There are also other questionnaires that are more topic-focused, which you can choose to complete if they apply to your child.  These may include questions related to the following topics, among others: COVID-19, Autism-Spectrum Disorder, migraines, surfing, consumption of fermented foods, consumption of foods containing polyphenols. You should complete these if they apply to your child and you want to provide additional information that may assist our research.<br /><br />
            You will then sample a part of your child’s body (e.g. stool, skin, mouth, nostril, ear, vagina) as described in the kit instructions. If collecting from stool, you will be asked to sample in one of a variety of ways, such as the following:<br />
            <blockquote>
                <ol>
                    <li>By inserting the tips of a Q-tip like swab into used toilet tissue and returning the sample in the provided plastic container;</li>
                    <li>By inserting the tips of the swab into used toilet tissue and applying the tips to the surface of a Fecal Occult Blood Test (FOBT) card, then returning the card to us.  The FOBT card is the same device used by your doctor to check for blood in your stool.  The FOBT card stabilizes the stool material for later analysis.  We will not check if there is blood in the stool for diagnostic purposes because we are not a clinical laboratory;</li>
                    <li>By using the scooper device to scoop a part of the fecal material into the provided tube;</li>
                    <li>Depositing soiled toilet paper into the provided receptacle;</li>
                    <li>Submitting a whole stool sample in a shipping container we will provide.  This container will have ice packs that reliably cool the sample to -20 degrees Celsius/-4 degrees Fahrenheit.</li>
                </ol>
            </blockquote>
            If you received a blood collection kit, it contains materials and instructions on how to collect a blood sample at home.  It is similar to the test used to test glucose levels by pricking your child’s finger.<br /><br />
            All samples should be returned to us in the included containers according to the instructions provided. <br /><br />
            We would like you to understand what you will receive in return for your child’s participation, and what we will do with your child’s sample.<br /><br />
            The samples in the project (including your child’s) may be analyzed and published in scientific articles. DNA and RNA will be extracted from the sample and amplified by PCR (polymerase chain reaction) and then sequenced to see what microorganisms (including viruses like SARS-CoV-2 that causes COVID-19 disease) are present in your child’s sample and in what proportions.  We may also use the remaining sample to look more carefully at specific microorganisms present, or to investigate other chemical compounds such as metabolites or proteins.  Please be aware that <strong>no human DNA</strong> will be analyzed as part of this or any future studies.  We estimate that it will take 2-3 months for you to learn the results of the initial bacterial diversity estimation. If your child is a part of a specific sub-study, it may take longer, depending on the duration of the study.<br /><br />
            We will upload results to your account when available and send you an email with a link to log in and view them.<br /><br />
            We also want you to understand that the methods we use for identifying microorganisms in your sample <strong>cannot be used to diagnose disease or infection</strong>.  The results are not medically actionable. The report includes a notation of the rare types of microorganisms for  your interest only. The techniques we use to identify the organisms cannot be used for species- level resolution.<br /><br />
            <strong><u>Please Note</u></strong>: The sequencing is <strong>not for diagnostic purposes and does not target human DNA</strong>.
        </p>
        <p>
            <strong><i>How much time will each study procedure take, what is your child’s total time commitment, and how long will the study last?</i></strong><br />
            Completing the main online questionnaire should take 30-45 minutes or less.  Each additional survey may take up to an additional 30 minutes to complete. Each sample you send can be obtained in 5 minutes or less.  We expect the study to continue for many years but the results will be available to you before the end of the study (usually within a few months of us receiving the sample). 
        </p>
        <p>
            <strong><i>What risks are associated with this study?</i></strong><br />
            Participation in this study may involve some added risks or discomforts. These include the following:<br />
            <blockquote>
                <ol>
                    <li>While answering surveys, you or your child may feel frustration, emotional discomfort, fatigue, and/or boredom.</li>
                    <li>If using the blood collection device, your child may experience temporary pain or a bruise at the site of the needle-stick.</li>
                    <li>There is a risk of loss of confidentiality.</li>
                </ol>
            </blockquote>
            Because this is a research study, there may be some unknown risks that are currently unforeseeable. You will be informed of any significant new findings.
        </p>
        <p>
            <strong><i>What are the alternatives to participating in this study?</i></strong><br />
            Participation is voluntary.
        </p>
        <p>
            <strong><i>What benefits can be reasonably expected?</i></strong><br />
            There is no direct benefit to your child for participating in this study. You will receive a report detailing the results of our analysis on your child’s sample, as well as facts and figures comparing your child’s microbial composition to that of other study participants. The investigator, however, may learn more about the human microbiome in health and disease and provide a valuable resource for other researchers.
        </p>
        <p>
            <strong><i>Can you choose to not have your child participate or withdraw from the study without penalty or loss of benefits?</i></strong><br />
            Participation in research is entirely voluntary. You may refuse to have your child participate or withdraw your child at any time without penalty or loss of benefits to which you or your child are entitled. If you decide that you no longer wish your child to continue in this study, you may withdraw your consent by requesting the deletion of your child’s source and/or account through your online account. We will inform you and your child if any important new information is found during the course of this study that may affect your wanting to continue.
        </p>
        <p>
            <strong><i>Can your child be withdrawn from the study without your consent?</i></strong><br />
            Your child may be withdrawn from the study if the instructions given to you by the study personnel are not followed.
        </p>
        <p>
            <strong><i>Will you be compensated for participating in this study?</i></strong><br />
            You will not be financially compensated in this study.
        </p>
        <p>
            <strong><i>Are there any costs associated with participating in this study?</i></strong><br />
            After you have signed your child up for the project and mailed in your child’s sample there will be no costs to you for their participation in the study.
        </p>
        <p>
            <strong><i>What if your child is injured as a direct result of being in this study?</i></strong><br />
            If your child is injured as a direct result of participation in this research, the University of California will provide any medical care you need to treat those injuries. The University will not provide any other form of compensation to you if your child is injured. You or your child may call the Office of IRB Administration at 858-246-4777 for more information about this, to inquire about your rights as a research subject or to report research-related problems.
        </p>
        <p>
            <strong><i>What about your or your child’s confidentiality?</i></strong><br />
            Research records will be kept confidential to the extent allowed by law. As part of your child’s participation in the study, you or your child will provide personal and/or sensitive information that could allow your child to be identified if it was made public, such as name, date of birth, or address. We take every precaution to protect your identity. All data you or your child provide are stored on secure systems within UC San Diego's infrastructure and directly identifying information is accessible only to critical study personnel. The code key (that relates participant personal information to sample barcodes) is retained on a separate password-protected server that is accessible only to relevant staff such as the Dr. Knight, Co-Investigators, project and sample coordinators, IT administrator and the database coders. Sample analysis is performed using data from which directly identifying information has been removed, and all data shared with public repositories also undergo this treatment. Research records may be reviewed by the UC San Diego Institutional Review Board. <br /><br />
            We may need to report information about known or reasonably suspected incidents of abuse or neglect of a child, dependent adult or elder including physical, sexual, emotional, and financial abuse or neglect. If any investigator has or is given such information, he or she may report such information to the appropriate authorities.<br /><br />
            (Federal and State laws generally make it illegal for health insurance companies, group health plans, and most employers to discriminate against you based on your genetic information. This law generally will protect you in the following ways: a) Health insurance companies and group health plans may not request your genetic information that we get from this research. b) Health insurance companies and group health plans may not use your genetic information when making decisions regarding your eligibility or premiums. c) Employers with 5 or more employees may not use your genetic information that we get from this research when making a decision to hire, promote, or fire you or when setting the terms of your employment.<br /><br />
            Be aware that these laws do not protect you against genetic discrimination by companies that sell life insurance, disability insurance, or long-term care insurance.)
        </p>
        <p>
            <strong><i>Know what we will collect </i></strong><br />
            As part of this research study, we will create and obtain information related to your child’s participation in the study from you or from collaborators so we can properly conduct this research. Research study data will include: contact information, demographic information, personal experiences, lifestyle preferences, health information, date of birth, opinions or beliefs.
        </p>
        <p>
            <strong><i>How we will use your child’s Sample</i></strong><br />
            We will use the sample your child provides to study the non-human DNA (e.g. bacterial DNA) in it. We may save some of your child’s sample to be accessible to researchers so they can conduct additional studies using the other compounds from it, such as RNA, proteins or metabolites. We may contact you if additional information or action is needed in order to process your child’s sample(s) and/or for re-consenting purposes.
        </p>
        <p>
            <strong><i>How we will use your child’s Personal Data</i></strong><br />
            The Personal Data you provide will be used for the following purposes:<br />
            <blockquote>
                <ul>
                    <li>To share with members of the research team so they can properly conduct the research</li>
                    <li>For future research studies or additional research by other researchers</li>
                    <li>To contact you for the purpose of receiving alerts of your child’s participation status, general program updates, opportunities to take part in new or future research, and/or as a follow-up to questions you have responded to in the questionnaire(s)</li>
                    <li>To comply with legal and regulatory requirements, including requirements to share data with regulatory agencies overseeing the research</li>
                    <li>To confirm proper conduct of the study and research integrity</li>
                </ul>
            </blockquote>
        </p>
        <p>
            <strong><i>Retention of your Personal Data</i></strong><br />
            We may retain the Personal Data you provide for as long as necessary to fulfill the objectives of the research and to ensure the integrity of the research. We will delete your child’s Personal Data when it is no longer needed for the study or if you withdraw your consent provided such deletion does not render impossible or seriously impair the achievement of the objectives of the research project. However, your child’s information will be retained as necessary to comply with legal or regulatory requirements. 
        </p>
        <p>
            <strong><i>Your Privacy Rights</i></strong><br />
            The General Data Protection Regulation (“GDPR”) requires researchers to provide information to you when we collect and use research data if you are located within the European Union (EU) or the European Economic Area (EEA). The GDPR gives you rights relating to your child’s Personal Data, including the right to access, correct, restrict, and withdraw your child’s personal information.<br /><br />
            The research team will store and process your child’s Personal Data at our research site in the United States. The United States does not have the same laws to protect your child’s Personal Data as States in the EU/EEA. However, the research team is committed to protecting the confidentiality of your child’s Study Data. Additional information about the protections we will use is included in this consent document.  
        </p>
        <p>
            <strong><i>Who can you call if you have questions?</i></strong><br />
            If you have questions or research-related problems, you may reach Rob Knight at 858-246-1184 or email our help account: microsetta@ucsd.edu.<br /><br />
            You may call the Office of IRB Administration at 858-246-4777 to inquire about your rights as a research subject or to report research-related problems.<br /><br />
            If you have questions or complaints about our treatment of your Personal Data, or about our privacy practices more generally, please feel free to contact the UC San Diego Privacy Official by email at ucsdprivacy@ucsd.edu.
        </p>
        <p>
            <strong><i>Your Signature and Consent</i></strong><br />
            You may download a copy of this consent document and a copy of the “Experimental Subject's Bill of Rights” to keep.<br /><br />
            Your consent is entirely voluntary, but declining to provide it may materially impede your child’s ability to participate in this research and receive a kit.
        </p>
    ''',
    'PARTICIPATION_AGREEMENT': '''
<p style="text-align: center; font-weight: bold;">THE MICROSETTA INITIATIVE</p>
<p style="text-align: center; font-weight: bold;">University of California, San Diego</p>
<p style="text-align: center; font-weight: bold;">PARTICIPATION AGREEMENT</p>
<ol>
<li><strong>Indemnification</strong>. Each party shall defend, indemnify and hold the other party, its officers, employees, and agents harmless from and against any and all liability, loss, expense (including attorneys' fees), and claims for injury or damages arising out of the performance of this Agreement, but only in proportion to and to the extent such liability, loss, expense, attorneys' fees, or claims for injury (including death) or damages are caused by or result from the negligent or intentional acts or omissions of the indemnifying party, its officers, employees, or agents.</li>
<li><strong>Patent Infringement Indemnification</strong>. The Individual shall indemnify, defend, and hold harmless UCSD, its officers, agents, and employees against all losses, damages, liabilities, costs, and expenses (including but not limited to attorneys' fees) resulting from any judgment or proceeding in which it is determined, or any settlement agreement arising out of the allegation, that the Individual's furnishing or supplying UCSD with parts, goods, components, programs, practices, or methods under this Agreement or UCSD's use of such parts, materials, goods, components, programs, practices, or methods supplied by the Individual under this Agreement constitutes an infringement of any patent, copyright, trademark, trade name, trade secret, or other proprietary or contractual right of any third party. UCSD retains the right to participate in the defense against any such suit or action.</li>
<li><strong>Limitation of Liability</strong>. EXCEPT WITH REGARD TO ITS INDEMNIFICATION OBLIGATIONS, NEITHER PARTY WILL BE LIABLE TO THE OTHER PARTY FOR ANY INDIRECT, SPECIAL, INCIDENTAL, EXEMPLARY OR CONSEQUENTIAL DAMAGES, OR COSTS, INCLUDING, BUT NOT LIMITED TO, ANY LOST PROFITS OR REVENUES, EVEN IF SUCH PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES AND REGARDLESS OF THE LEGAL THEORY UNDER WHICH SUCH DAMAGES ARE SOUGHT. UCSD DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT SHALL UCSD'S TOTAL LIABILITY UNDER THIS AGREEMENT EXCEED THE AMOUNT PAID BY THE INDIVIDUAL FOR THE SERVICES. UCSD DOES NOT GUARANTEE A SPECIFIC RESULT OR DELIVERABLE FOR PARTICIPATING IN THIS PROJECT.</li>
<li><strong>UCSD's Ownership of Materials</strong>. UCSD will own the deliverables upon receipt of the materials from Individual.</li>
<li><strong>Use of UCSD Name</strong>. California Education Code Section 92000 prohibits use of the University of California, San Diego's name to suggest that UCSD endorses a product or service. The Individual will not use The University of California's name, or any acronym thereof publically, including UCSD, without UCSD's prior written approval.</li>
<li><strong>Excusable Delay</strong>. In the event of a delay caused by inclement weather, fire, flood, strike or other labor dispute, acts of God, acts of Governmental officials or agencies, or any other cause beyond the control of UCSD, UCSD's performance is excused hereunder for the periods of time attributable to such a delay, which may extend beyond the time lost due to one or more of the causes mentioned above. The Company's duty to pay for past or continuing costs is not suspended hereunder.</li>
<li><strong>Non-Interference</strong>. Notwithstanding any other provision contained herein, the use of UCSD facilities and/or UCSD personnel in support of this Agreement can only be authorized to the extent that it will not interfere with work related to the prime missions of UCSD and/or the Department (e.g., education and research). Accordingly, Individual's exclusive remedy for failure by either UCSD or persons acting on its behalf to perform services or furnish information or data hereunder at any particular time or in any specific manner, is limited to reimbursement of any unexpended payments under this Agreement.</li>
<li><strong>Non-Exclusive Nature of Services</strong>. The Services herein are being offered to Individual on a non-exclusive basis. Nothing herein shall be construed as granting Company any exclusive right(s) to the Service(s) referenced herein, and UCSD retains the right to offer and perform similar or identical Services for others.</li>
<li><strong>Notice</strong>. Any notice or communication required by this Agreement shall be in writing and shall be deemed to have been duly given if delivered personally, or sent by overnight mail, or prepaid registered mail, email, or confirmed facsimile transmission, addressed to the other party at the address set forth on kit registration, or at such other address as such party hereto may hereafter specify in writing to the other party.</li>
<li><strong>Status of Parties</strong>. This Agreement is not intended to create, nor shall it be construed to be, a joint venture, association, partnership, franchise, or other form of business relationship. Neither party shall have, nor hold itself out as having, any right, power or authority to assume, create, or incur any expenses, liability, or obligation on behalf of the other party, except as expressly provided herein.</li>
<li><strong>Third-Party Beneficiary</strong>. There are no intended third-party beneficiaries to this Agreement.</li>
<li><strong>Severability</strong>. If any provision of this Agreement is held invalid, illegal or unenforceable in any respect, such provision shall be treated as severable, leaving the remaining provisions unimpaired, provided that such does not materially prejudice either party in their respective rights and obligations contained in the valid terms, covenants, or conditions.</li>
<li><strong>Non-Waiver</strong>. The failure of either party to require the performance of any of the terms of this Agreement or the waiver by either party of any default under this Agreement shall not prevent a subsequent enforcement of such term, nor be deemed a waiver of any subsequent breach.</li>
<li><strong>Modification of Agreement</strong>. This Agreement shall be changed only by written agreement of the parties.</li>
<li><strong>Applicable Law</strong>. This Agreement shall be governed by the laws of the State of California without regard to its conflict of laws provisions.</li>
<li><strong>Signatures, Counterparts and Copies</strong>. This Agreement may be executed in counterparts, all of which, when taken together, shall constitute one contract with the same force and effect as if all signatures had been entered on one document. Signatures may be made electronically, by clicking "I Agree" and such electronic signatures shall be valid and binding upon the parties making them, and shall serve in all respects as original signatures. Upon clicking "I Agree" this agreement shall be considered fully-executed by both parties. Signatures may be delivered among and between the parties by facsimile or electronic means. Thereafter, the parties further agree that electronic copies of this Agreement may be used for any and all purposes for which the original may have been used.</li>
<li><strong>Arbitration</strong>. In the event of any dispute, claim, question, or disagreement arising from or relating to this Agreement or the breach thereof, the parties hereto shall use their best efforts to settle the dispute, claim, question, or disagreement. To this effect, they shall consult and negotiate with each other in good faith and recognizing their mutual interests, attempt to reach a just and equitable solution satisfactory to both parties. If they do not reach a solution within a period of sixty (60) days, then upon notice by either party to the other, all disputes, claims, questions, or disagreements shall be finally settled in accordance with the provisions of the American Arbitration Association ("AAA") and proceed under the provisions of Title 9 of the California Code of Civil Procedure Sections 1280 through and including 1294.2. The discovery provisions of the California Code of Civil Procedure Section 1283.05 shall be applicable to this Agreement. Each party shall bear its own costs.</li>
<li><strong>Export Control</strong>. No ITAR or export controlled materials shall be delivered to UCSD pursuant to this agreement.</li>
<li><strong>Entire Agreement</strong>. This Agreement, including Exhibit A made a part hereof, sets forth the entire agreement of the parties with respect to the subject matter herein and supersedes any prior agreements, oral and written, and all other communications between the parties with respect to such subject matter.</li>
</ol>
    ''',

    'EXHIBIT_A': '''<p style="text-align: center; font-weight: bold;">EXHIBIT A</p>
<p style="text-align: center; font-weight: bold;">THE MICROSETTA INITIATIVE STATEMENT OF SERVICES</p>
<ol>
<li><strong>SCOPE OF WORK</strong>:<br />
The Services will be performed as set forth below or in accordance with the attachment hereto and incorporated by reference herein.<br /><br />
When you sign up for the study, you may claim a package of research analyses based on your contribution level. You are mailed a kit with sampling instructions, and directions on how to sign into the website to complete the consent form and submit the questionnaire. Any sample that is received in the laboratory without a completed consent form online is not sequenced. You be able to view, download and print a high-resolution certificate suitable for framing of your results and access to more detailed taxa report of your results - which can be viewed online and downloaded into Excel.<br /><br />
I have accepted this Scope of Work on behalf of UCSD and the responsibility for administering and monitoring the agreement.</li>
<li><strong>DELIVERABLES</strong>:<br />
Approximately 2-4 months after we have received your sample you will be notified of your results electronically.</li>
<li><strong>COST</strong>: Cost is variable based on the contribution level that was elected.</li>
<li><strong>PAYMENT</strong>:<br />
<ol>
<li><strong>SCHEDULE</strong>: 100% of cost due upon clicking "I Accept"</li>
<li><strong>REMITTANCE</strong>: Payment will be submitted through PayPal via the FundRazr website. No payment is required if participation is through a sponsored study.</li>
</ol>
</li>
<li><strong>TERM OF AGREEMENT</strong>: This Agreement will be effective as of the date of remittance of payment to FundRazr.</li> 
<li><strong>UCSD CONTRACTS OFFICE CONTACT</strong>:<br />
University of California, San Diego<br />
9500 Gilman Drive Mail Stop 0934<br />
La Jolla, California 92093-0934<br />
Telephone: (858) 822-5180<br />
Email: researchadmin@ucsd.edu</li>
</ol>
''',
    'BILL_OF_RIGHTS': '''Experimental Subject's Bill of Rights''',
    'TEXT_I_HAVE_READ_1': 'I have read (or someone has read to me) this form. I am aware that I am being asked to be in a research study, and I voluntarily agree to participate in this study. I understand how my personal data will be processed, my related rights, and that I consent to the processing of my sample and data as provided in this document.',
    'TEXT_I_HAVE_READ_SIMPLIFIED': 'Yes, you will be in this research study.',
    'PERSON_ATTAINING_ASSENT': 'Signature Of Person Obtaining Assent',
    'TEXT_ASSENT_WITNESS': 'In my judgment, the participant is voluntarily and knowingly giving assent and possesses the legal capacity to give assent to participate in the study.',
    'ASSENT_OBTAINER': 'Name of person obtaining assent',
    'TEXT_I_HAVE_READ_PARENT': 'I have read (or someone has read to me) this form. I am aware that I am being asked to provide consent for my child to be in a research study. I voluntarily agree to allow my child to participate in this study. I understand how my child’s personal data will be processed, my related rights, and that I consent to the processing of my child’s sample and data as provided in this document.',
    'PARTICIPANT_NAME': 'Participant name',
    'PARTICIPANT_PARENT_1': 'Parent/Guardian name',
    'PARTICIPANT_PARENT_2': 'Parent/Guardian name of second parent',
    'PARTICIPANT_DECEASED_PARENTS': 'One parent/guardian is deceased or unable to consent',
    'DATE_SIGNED': 'Date Signed',
    'PARTICIPANT_ADDRESS': 'Participant Address',
    'PARTICIPANT_CITY': 'Participant City',
    'PARTICIPANT_STATE': 'Participant State',
    'PARTICIPANT_ZIPCODE': 'Participant Zipcode',
    'PARTICIPANT_COUNTRY': 'Participant Country'
}

_FAQ = {
    'ADD_PARTICIPANT': '<a href="%(add_participant_vid)s">%(project_shorthand)s - How to Add a Participant</a> from <a href="https://vimeo.com/user16100300">shelley schlender</a> on <a href="https://vimeo.com">Vimeo</a>.' % {'project_shorthand': AMGUT_CONFIG.project_shorthand, 'add_participant_vid': media_locale['ADD_PARTICIPANT']},
    'ADDITIONAL_QUESTIONS': 'If you are not able to get your question answered, please email us at <a href="mailto:%(help_email)s">%(help_email)s</a> and we will do our best to assist you.' % {"help_email": media_locale["HELP_EMAIL"]},
    'ANOTHER_COPY_RESULTS': 'Am I able to get another copy of my results?',
    'ANOTHER_COPY_RESULTS_ANS': 'You can download a copy from our website. Log in with your account name and password, go to the left side bar, move your mouse to Human Samples -> PARTICIPANT NAME -> SAMPLE NUMBER, and then click on SAMPLE NUMBER.pdf to download it.',
    'BETTER_OR_WORSE': 'How can I tell if my gut microbiome is better or worse than other people in my category?',
    'BETTER_OR_WORSE_ANS': "Right now, you can't. We're still trying to understand what constitutes a normal or average gut microbiome, and we have a lot to learn about the functions of many of the microbes that inhabit the gut. Therefore, it's difficult to know what combinations of microbes are best for nutrition and health. That's one reason collecting data from so many people is important - hopefully we can start to learn more about this.",
    'COMBINE_RESULTS': 'My whole family participated, can we combine the results somehow?',
    'COMBINE_RESULTS_ANS': "We're still evaluating how best to present the data for samples that represent a family. We are posting individual results now and will provide updated results through the web site later.",
    'DIFFERENT_WHATS_WRONG_WITH_ME': "I'm different than other people in my category. Does that mean something is wrong with me?",
    'DIFFERENT_WHATS_WRONG_WITH_ME_ANS': "No! Your gut microbiome is as unique as your fingerprint so you should expect to see some differences. Many factors can affect your gut microbiome, and any differences you see are likely to be the result of one of these factors. Maybe your diet is different than most people your age. Maybe you just travelled somewhere exotic. Different does not necessarily mean bad.",
    'FAQ_HEADER': "%(project_shorthand)s FAQ" % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'FAQ_SECTION_1': "The %(shorthand)s general questions and information" % {"shorthand": AMGUT_CONFIG.project_shorthand},
    'FAQ_SECTION_2': "I'm having trouble logging in",
    'FAQ_SECTION_3': "I have a question about the submission process/instruction packet",
    'FAQ_SECTION_4': "I have a question about my sample results",
    'FAQ_SECTION_5': "I have a question about my raw data and the analysis process",
    'FAQ_SECTION_6': "Miscellaneous questions",
    'FECAL_NO_RESULTS_ANS': "On any given sequencing run (not just the %(project_shorthand)s), a small percentage of the samples fail for unknown reasons - our methods are good but not perfect. This is one of the reasons the sample kits have two Q-tips. It allows us to perform a second microbial DNA extraction and re-sequence if the first attempt failed. We will be doing this for all of the samples that failed. If there was a technical problem with the sample itself (e.g. not enough microbes on the swab) that prevents us from producing data for you, we will be re-contacting you about collecting another sample." % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'FIND_DETAILED_INFO': "Where can I find more detailed information about my sample?",
    'FIND_DETAILED_INFO_ANS': 'You can find the raw data from <a href="https://www.ebi.ac.uk/">European Bioinformatics Institute</a> or download the copy of your result from our website (instructions for both options found further below in FAQ).',
    'HANDLING_SWABS': "%(project_shorthand)s - Handling Your SWABS</a> from" % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'HOW_CHANGE_GUT': "How can I change my gut microbiome?",
    'HOW_CHANGE_GUT_ANS': "Although we still don't have a predictable way to change the gut microbiome in terms of increasing or decreasing the abundances of specific bacteria, we do know that a variety of factors influence gut microbial community composition. Diet is a major factor affecting the gut microbiome so by changing your diet, you may be able to affect your gut microbiome. We still don't fully understand probiotics but know that they can influence your gut microbiome while you are actively taking them. Factors such as stress can also influence the gut microbiome. However, it is important to remember that there are factors we can't change, such as age or genetics, that can affect the gut microbiome.",
    'HOW_PROCESS_SAMPLES': "How are the samples and data processed?",
    'HOW_PROCESS_SAMPLES_ANS_1': 'The majority of the samples in the %(project_name)s are run through a processing pipeline designed to amplify a small region of a gene that is believed to be common to all Bacteria and Archaea. This gene, the 16S ribosomal RNA gene is like a barcode you find on your groceries, and serves as a marker for different organisms. There are quite a few different ways to assess the types of Bacteria and Archaea in a sample, including a variety of techniques even to look at this single gene. Every method has its biases, and comparing data between different methods is <a href="http://www.ncbi.nlm.nih.gov/pubmed/23861384">non-trivial</a> and can sometimes be nearly impossible. One of the primary goals of the Gut Project is to provide data that can be used and reused by researchers worldwide, we have opted to use the standard protocols adopted by the <a href="http://earthmicrobiome.org">Earth Microbiome Project</a>, (<a href="http://www.ncbi.nlm.nih.gov/pubmed/22402401">Caporaso et al 2012</a>, and more detailed description of the <a href="http://www.earthmicrobiome.org/emp-standard-protocols/16s/">protocol</a>). This ensures that the data generated by the project can be combined with the other 80,000 samples so far indexed by the EMP (as scientists, we get giddy about things like this).' % {'project_name': AMGUT_CONFIG.project_name},
    'HOW_PROCESS_SAMPLES_ANS_2': 'DNA sequencing is a complex challenge that involves an army of robots, ultra pure water that costs $75 per 10ml, and an amazing <a href="http://www.illumina.com/systems/miseq.ilmn">digital camera</a> that actually determines individual sequences one nucleotide at a time. The number of stunningly brilliant minds whose footprints exist in these methods is astounding. However, the challenges don\'t end once you get the DNA sequence - some might say they are just beginning. It turns out that figuring out what actually is in your sample, that is, what organisms these sequences correspond to, requires cutting edge computational approaches, supercomputers and caffeine for the people operating them. The questions being asked of the data are themselves complex, and volume of data being processed is simply phenomenal. To give you some idea, for each sample sequenced we obtain around 6 million nucleotides which we represent as letters (A, T, G or C, see <a href="http://en.wikipedia.org/wiki/Nucleotide">here</a> for more info), whereas Shakespeare\'s Hamlet only contains around 150,000 letters (ignoring spaces).',
    'HOW_PROCESS_SAMPLES_ANS_3': 'The primary software package we use for processing 16S sequence data is called Quantitative Insights into Microbial Ecology (<a href="http://www.qiime.org">QIIME</a>; <a href="http://www.ncbi.nlm.nih.gov/pubmed/20383131">Caporaso et al. 2010</a>). Using this package, we are able to start with raw sequence data and process it to so that we end up be able to explore the relationships within and between samples using a variety of statistical methods and metrics. To help in the process, we leverage a standard and comprehensive (to date) reference database called Greengenes (<a href="http://www.ncbi.nlm.nih.gov/pubmed/22134646">McDonald  et al. 2011</a>; <a href="http://www.ncbi.nlm.nih.gov/pubmed/16820507">DeSantis et al. 2006</a>) that includes information on a few hundred thousand Bacteria and Archaea (it is likely that there are millions or more species of bacteria). Due to the molecular limitations of our approach, and the lack of a complete reference database (because the total diversity of microbes on Earth is still unknown), our ability to determine whether a specific organism is present has a margin of error on the order of millions of years, which limits our ability to assess specific strains or even species using this inexpensive technique (more expensive techniques, such as some of the higher-level contributions, can provide this information). But all is not lost! By using the evolutionary history of the organisms as inferred by the small pieces of DNA that we have, we can begin to ask broad questions about the diversity within (see <a href="http://www.ncbi.nlm.nih.gov/pubmed/7972354">Faith 1994</a>) and between samples (see <a href="http://www.ncbi.nlm.nih.gov/pubmed/16332807">Lozupone and Knight 2005</a>), and whether the patterns observed relate to study variables (e.g., BMI, exercise frequency, etc).',
    'HOW_PROCESS_SAMPLES_ANS_4': 'The specifics on how the %(project_shorthand)s sequence data are processed can be found <a href="http://nbviewer.ipython.org/github/biocore/American-Gut/blob/master/ipynb/module2_v1.0.ipynb">here</a>, and are written up in an executable <a href="http://ipython.org/notebook">IPython Notebook</a>, which provides all the relevant processing steps in an open-source format. Be warned, processing the full %(project_shorthand)s datasets takes over 5,000 CPU hours right now (i.e. if you do it on your laptop it might take 7 months, even if you don\'t run out of memory: this might put the time it takes to get your results in perspective). This is the processing pipeline that we use on your data. As this project is a work in progress, we are versioning the processing pipeline as there will continue to be improvements to the process as the project moves forward.' % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'HOW_PROCESS_SAMPLES_ANS_5': 'Additional information about the tools used in the %(project_name)s and our contributions to the microbiome community can be found in the following publications:' % {'project_name': AMGUT_CONFIG.project_name},
    'HOW_PROCESS_SAMPLES_ANS_7': 'More detail on our work on the effects of storage conditions can be found in these publications:',
    'HOW_PROCESS_SAMPLES_ANS_9': 'And more detail on our work on sequencing and data analysis protocols can be found in these publications:',
    'INFORMATION_IDENTIFY_ME': 'Can data describing my gut microbiome be used to identify me or a medical condition I have?',
    'LOG_IN_WHAT_NOW': "I'm logged in, what do I do now?",
    'LOG_IN_WHAT_NOW_ANS_1': 'You need to follow the add participant workflow. Click on the "Add Source & Survey" tab located at the top of the page.',
    'LOG_IN_WHAT_NOW_ANS_2': '<p>During this workflow you (or whomever is being sampled) will:</p><ol>   <li>Add a participant</li><li>Provide electronic consent</li><li>Answer survey questions (including the diet questions)</li><li>Upon completion, become eligible to associate samples</li>          </ol><p>When participants are eligible,  you will then see their name under the corresponding menu on the left, in this example we have just added the participant "test":</p>',
    'LOG_IN_WHAT_NOW_ANS_3': 'You can assign a sample by clicking the "Assign Sample" link in the menu. If you do not see the "Assign Sample" link, then all of your barcodes have been assigned.',
    'LOG_IN_WHAT_NOW_ANS_4': "The generic add sample page looks like this:",
    'LOG_IN_WHAT_NOW_ANS_5': "When adding a sample, please be sure to select the barcodes that matches the barcode on the sampling tube of the sample that you are logging",
    'LOOK_BELOW': "If you're still experiencing issues, look for your problem in the FAQ below",
    'MISSING_METADATA': "What are missing metadata?",
    'MISSING_METADATA_ANS': "Metadata are information describing your age, gender, diet, etc. Missing metadata mean that this person did not provide us with this information.",
    'MULTIPLE_KITS_DIFFERENT_TIMES': "I have a 2+ sample kit, and would like to collect and send them in at different times",
    'MULTIPLE_KITS_DIFFERENT_TIMES_ANS': 'You are welcome to do that!  If you plan to wait to use another sample tube at a later date, store the tube in a dry, cool location at room temperature.  An ideal location would be a cabinet or closet.<p><strong>Do not take a sample unless you plan to send it within 48 hours of collecting.</strong></p>',
    'NOT_A_BUSINESS': 'Is the %(shorthand)s a business?' % {"shorthand": AMGUT_CONFIG.project_shorthand},
    'NOT_A_BUSINESS_ANS': 'We have had many enquiries about our "service" or "business". %(project_shorthand)s is a contribution-supported academic project that is a collaboration between the <a href="http://www.earthmicrobiome.org">Earth Microbiome Project</a> and the <a href="http://humanfoodproject.com/">Human Food Project</a>, primarily run out of the <a href="https://knightlab.ucsd.edu/">Knight Lab</a> at the University of California San Diego, and is not a business or service.  In particular, the project is not a diagnostic test (although the information gained through the project may in future contribute to the development of diagnostic tests). All data except for information that needs to be kept confidential for privacy reasons is openly and freely released into public databases, and the project is not intended to make a profit (any surplus funds would be recycled back into furthering human microbiome research).' % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'PARTICIPATE_WITH_DIAGNOSIS': "Can I participate in the project if I am diagnosed with ...?",
    'PARTICIPATE_WITH_DIAGNOSIS_ANS': "Of course! The only exclusion criteria are: you must be more than 3 months old and cannot be in prison. Please keep in mind that, for legal and ethical reasons, the %(project_name)s does not provide medically actionable results or advice." % {'project_name': AMGUT_CONFIG.project_name},
    'PASSWORD_DOESNT_WORK': "My password doesn't work!",
    'PASSWORD_DOESNT_WORK_ANS': '<p>The passwords have some ambiguous characters in them, so we have this guide to help you decipher which characters are in your password.</p><p class="ambig">abcdefghijklmnopqrstuvwxyz<br>ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>1234567890<br>1 = the number 1<br>l = the letter l as in Lima<br>0 = the number 0<br>O = the letter O as in Oscar<br>g = the letter g as in golf<br>q = the letter q as in quebec</p>',
    'PASSWORD_SAME_VERIFICATION': "Is my password the same as my verification code?",
    'PASSWORD_SAME_VERIFICATION_ANS': 'No. Your <strong>password</strong> is printed on the sheet that you received with your kit in the mail. That sheet looks like this:</p><img src="%(sitebase)s/static/img/creds_example.png"/>'
                                      '<p>Your <strong>verification code</strong> is emailed to you. Look for the email: <br /><br /><strong>FROM:</strong>  %(project_name)s (%(help_email)s)<br /><strong>SUBJECT:</strong>  %(project_shorthand)s Kit ID & Verification Code' % {'sitebase': media_locale['SITEBASE'], 'project_shorthand': AMGUT_CONFIG.project_shorthand, 'project_name': AMGUT_CONFIG.project_name, 'help_email': media_locale['HELP_EMAIL']},
    'RAW_DATA': "How can I get the raw data?",
    'RAW_DATA_ANS_1': '<P>The raw data can be fetched from the <a href=http://www.ebi.ac.uk/>European Bioinformatics Institute</a>. EBI is part of <a href=http://www.insdc.org/>The International Nucleotide Sequence Database Collaboration</a> and is a public warehouse for sequence data. The deposited %(project)s accession is <a href="http://www.ebi.ac.uk/ena/data/view/ERP012803&display=html">ERP012803</a>. You will need your sample barcode number to access your raw data. If you cannot find your sample barcode number, then it likely has not completed processing yet.  If you are still unable to locate it and your results are currently available, please email us to inquire.' % {"project": AMGUT_CONFIG.project_name},
    'RAW_DATA_STEPS': 'Click on the <a href="http://www.ebi.ac.uk/ena/data/view/ERP012803&display=html">ERP012803</a> accession link above and follow these instructions:',
    'RAW_DATA_STEP_1': 'Wait until the "Read Files" tab appears',
    'RAW_DATA_STEP_2': 'Click on the "TEXT" link. A text file will download (it\'s a large file, so it\'ll take a while to download)',
    'RAW_DATA_STEP_3': 'Open up the text file with Notepad/TextEdit/a simplified text editor program. There should be one pre-installed on your computer',
    'RAW_DATA_STEP_4': 'Use the find shortcut (CTRL+F or COMMAND+F) and search the text file using your barcode number',
    'RAW_DATA_STEP_5': 'Four lines above your barcode number, you\'ll find a string of letters and numbers that read "SAMEA[XXXXXXX]". Copy that number',
    'RAW_DATA_STEP_6': 'Back on the EBI page in the URL address, replace "PRJEB11419" with the copied string from the text file. Press ENTER/RETURN on your computer',
    'RAW_DATA_STEP_7': 'You can now access your sample\'s raw data! You can download the various files found on the page to explore more',
    'STEPS_TO_FOLLOW': '<a href="%(steps_vid)s">%(project_shorthand)s - Steps to Follow When Your Kit Arrives</a> from <a href="https://vimeo.com/user16100300">shelley schlender</a> on <a href="https://vimeo.com">Vimeo</a>.' % {'project_shorthand': AMGUT_CONFIG.project_shorthand, 'steps_vid': media_locale['STEPS_VIDEO']},
    'TAKES_SIX_MONTHS': "Does it really take up to four months to get my results?",
    'TAKES_SIX_MONTHS_ANS': "Yes. It takes about six weeks for extractions, six weeks for the remainder of the processing, and two weeks to do the actual sequencing. This is before any analysis and if everything goes as planned, with no delays - equipment down, run failures, reagents or other consumables back ordered. There are also added transit times for your sample to travel between the UK and the US. Things do sometimes go wrong, so we say up to four months, although we are working to improve these.",
    'WATCH_VIDEOS': "Watch these helpful videos created by our colleagues at the American Gut about what to do once you've received your kit!",
    'WHAT_FORMS': "What are the forms you talk about on the sampling instructions?",
    'WHAT_FORMS_ANS': 'The instruction on the sampling instructions that requires you to "place your forms and the sample tube in preaddressed envelope" is leftover from a previous version of the sampling instructions. There are no forms for you to include inside the envelope with your sample.</p>',
    'WHERE_SEND_SAMPLE': "Where do I send my sample?",
    'WHO_MICHAEL_POLLAN': "Who is Michael Pollan?",
    'WHO_MICHAEL_POLLAN_ANS': 'Michael Pollan is a New York Times Best Seller for his books on diet and nutrition. Further information about Michael can be found <a href="http://michaelpollan.com/">here</a>.',
    'WHY_TWO_SWABS': "Why are there 2 swabs inside the tube?",
    'WHY_TWO_SWABS_ANS_1': "Each sampling tube contains two swabs and looks like this:",
    'WHY_TWO_SWABS_ANS_2': "<p>Each tube is used for <strong>one sample</strong>. The tube has two swabs in it because one is a backup in case the DNA does not amplify on the first swab.</p>"
                           "<p>Here's a video of Rob Knight talking about swab handling:</p><iframe src='%(swab_handle_vid)s' width=''500'' height=''281'' frameborder=''0'' webkitallowfullscreen='' mozallowfullscreen='' allowfullscreen=''></iframe>" % {'swab_handle_vid': media_locale['SWAB_HANDLING']}
}

_INTRODUCTION = {
    'PROJECT_101': '%(shorthand)s 101' % {"shorthand": AMGUT_CONFIG.project_shorthand},
    'INTRODUCTION_BEGINNING': '<a href="http://www.robrdunn.com">Rob Dunn</a> has provided this excellent introduction to some of the basics that every curious reader should check out!<br/>&nbsp;<br/>Rob is the author of the <a href="http://www.yourwildlife.org/the-wild-life-of-our-bodies/">Wild Life of Our Bodies</a>. He is an evolutionary biologist and writer at North Carolina State University. For more about your gut and all of your other parts, read more from Rob at <a href="http://www.robrdunn.com">www.robrdunn.com</a>.</p>',
    'INTRODUCTION_WHAT_IS_GUT_HEAD': "What is a Gut?",
    'INTRODUCTION_WHAT_IS_GUT': "Your gut is a hole that runs through your body. Your gut is actually, developmentally speaking, the outside of your body, but it has evolved many intricacies that make it seem like the inside. Your gut starts with your mouth and ends with your anus. In between food is changed into energy, feces, bacteria, viruses and a few other things. Your gut exacts a kind of metamorphosis on everything you eat, turning hotdog or grilled cheese, miraculously, into energy and, ultimately, cells, signals and even thoughts. We are only beginning to understand this process, a process in which microbes play (or fail to play) a major role.",
    'INTRODUCTION_WHAT_IS_PROJECT_HEAD': "What is the %(project_name)s?" % {'project_name': AMGUT_CONFIG.project_name},
    'INTRODUCTION_WHAT_IS_16S_HEAD': "What is 16S rRNA?",
    'INTRODUCTION_ROBOTS_HEAD': "Do you really have a robot?",
    'INTRODUCTION_ROBOTS': "Look, here is the deal. Robots. Microbiologists use robots. Personally, I think the fact that microbiologists study the dominant fraction of life on Earth, a fraction that carries out most of the important process (and a fair bit of inexplicable magic) makes microbiologists cool. I am not a microbiologist; I am an evolutionary biologist and a writer, but I think that microbiologists are hipsters cloaked in scientists clothing (and language). But if the outrageousness of their quarry does not convince you they are hip, well, then, let me remind you, they have robots.<br/>&nbsp;<br/>The robots enable the scientists to rapidly extract the DNA and RNA from thousands of samples simultaneously. Specifically, they can load your samples into small plastic plates each with 96 little wells. The robot then loads chemicals into the wells and heats the chemically-laced wells enough to break open the bacterial cells in the sample, BAM! This releases the cell's DNA and RNA. The robots then decode the specific letters (nucleotides) of the 16S gene using the nucleotides dumped out of the broken microbial cells into these plates.",
    'INTRODUCTION_TREE_HEAD': "Tree of life",
    'INTRODUCTION_TREE': "There is an evolutionary tree inside you. Well, sort of. When scientists study the microbes in your gut (and from the same samples we could also study viruses, bacteriophages&mdash; the viruses that attack bacteria&mdash;, fungi or even the presence of animals such as worms of various sorts) they do so by looking at the 16s or other genetic code of the RNA on the swabs you send us. We compare the code of each bit of RNA we find to the code of species other people have collected and also the code of the other bits of RNA in your sample. As a result, we can actually use the results of your sample to map the species living in you onto an evolutionary tree. Your own genes occupy one tiny branch on the tree of life, but the species inside of you come from all over the evolutionary tree. In fact, in some people we find species from each of the major branches of the tree of life (archaea, bacteria, eukaryotes) and then also many of the smaller branches. Inside you, in other words, are the consequences of many different and ancient evolutionary stories.",
    'INTRODUCTION_MICROBIOME_HEAD': "What is a microbiome?",
    'INTRODUCTION_MICROBIOME': "A biome, as ecologists and evolutionary biologists like me historically used it is a self-contained ecosystem, where all the organisms can interact with each other and the environment in which they live, for example a rain forest is a biome, but it is made of smaller biomes, for example a tree is a biome for insects, then a single insect is a biome for bacteria. Therefore, these smaller biomes are often called microbiomes, in the case of you, it's your gut!&hellip; A microbiome is a small (micro) version of this larger phenomenon, a whole world within you.",
    'INTRODUCTION_EAT_HEAD': "What do my microbes eat?",
    'INTRODUCTION_EAT': "Everyplace you have ever set your hand or any other part of your body is covered in microbes. This is true of your gut, but also everything else. Microbes live in clouds. They live in ice. They live deep in the Earth. They also live in your colon, on your skin, and so on. It is reasonable to wonder what they eat. The short answer is everything. Microbes are thousands of times more variable when it comes to their diets than are animals, plants or even fungi. Some microbes can get their nitrogen out of the air; they can, in other words, eat air. Ain't that cool. Others, like us, eat other species, munching them in the world's coolest and most ubiquitous game of packman. The bacteria in your gut are also diverse in terms of their diets. If there are two hundred species of bacteria in your gut (and there probably are at least that many) then there are at least that many different combinations of things that they are eating.",
    'INTRODUCTION_MICROBES_COME_FROM_HEAD': "Where do my microbes come from?",
    'INTRODUCTION_DISCOVER_HEAD': "What will we discover in your gut?",
    'INTRODUCTION_DISCOVER': "When the early meetings were going on about this project, everyone sat around talking about what we might see from colon samples. One scientist was sure that we would see bacteria that looked like Elvis. Another though we would find Shakespeare's great lost play. But the truth is all that we are going to see from your gut are lists of nucleotides. Let me explain&hellip;<br/>&nbsp;<br/>Nucleotides are those building blocks out of which DNA and RNA are made. They come in different forms to which scientists have assigned names and letters. When the robots are done with the work, what they produce are lists of the nucleotides in all of 16S genes from all of the cells in your sample. These nucleotides tell the scientists which kinds of life are in your sample (and in you). But because we will only have samples of little stretches of the 16S genes, we won't know exactly which species are in you, just which lineages they are from. You might have the bacterial equivalent of a chimpanzee and a gorilla in you, but all we'll know from your sample is that there was an ape. Knowing you have a bacterial ape in your gut will, on its own, not tell you so much. The real information will come from context, statistical context. I know, that sounds boring, but I promise it is not.<br/>&nbsp;<br/>We think that hundreds of different things you do during your life, in addition to what your mother and father did (let's try not to think about that), your genes and even just where you grew up influence which species of microbes are found inside you. But we don't really know. The problem is humans are so darn complicated. What we need to be able to do is to compare large numbers of people, people who differ in many ways, to be able to sort out which variables are sometimes a little important and which ones are the big deal. Is a vegan gut very different from a vegetarian one? Does eating yoghurt make a big difference? Do the effects of a c-section birth last forever? These questions require us to compare many people, which is where you come in. Your sample, gives us context and it gives you context too. It won't be terribly exciting on its own (you will know which ancient lineages you have dividing and thriving inside you. OK, that is pretty cool on second thought), but it will be very exciting in context. Where do you fall relative to fish eaters, sick people healthy people, hunter gatherers, or even your dog? You will know and we will know. And this is not all.<br/>&nbsp;<br/>All of the questions I have mentioned so far are what I might call first order questions. How does this thing compare to that thing. But what we'd love to be able to answer are second order questions, contingent questions, questions such as whether the effect of your diet depends on your ethnicity (it probably does), whether the effect of having a dog depends on whether or not you live in the city (again, I bet it does) and so on. These questions are exactly the sort of question we have failed to be able to answer well when it comes to diet, because we don't have big enough samples sizes. We can see the forest for all of humans. Well, that isn't quite right, but you get the idea, we will be able to understand elaborate effects of multiple variables on the wilderness between your pie hole and the other hole and that, to us, is exciting.",
    'INTRODUCTION_STORIES_HEAD': "A few of the stories of the evolutionary tree in your gut",
    'INTRODUCTION_STORIES': "Some people have least favorite bacteria. Salmonella, for example, seems to have inspired some haters. But microbiologists also have favorite bacteria, as well they should. The stories of bacteria (and those who chase and study them) are among the most important of humanities stories and include the tales of many species without which we could not live, or whose presence or absence affects how we live. These species are as fascinating and, dare I say, lovely as pandas or koala bears, just harder to see and far more significant. I have begun to compile a book of the stories of some of the most common and interesting species you are likely to encounter&mdash; whether in your own gut, on your lettuce or the next time you sink your fingers into the soil. These stories will be available online here at <a href=\"http://invisiblelife.yourwildlife.org/\">Invisible Life</a> as they are compiled as a book, a book written by some of the very best science writers AND scientists out there. For starters, you might be interested to know that <a href=\"http://invisiblelife.yourwildlife.org/mycoplasma/\">the smallest species on Earth</a> is sometimes found inside humans and, once we look at your 16S, we will even know whether it lives in you. As more of these stories are written, they will appear here, eventually as an ebook, an ebook that you can reference when you find out what lives inside you to know whether your constant companion is a species we know everything about or, as is more typical, no one has ever studied. Like Charlie Chaplin once said&hellip; Wait, Charlie Chaplin was the one who didn't say anything wasn't he."
}

_TAXA_SUMMARY = {
    'DOWNLOAD_LINK': "Download the table",
    'RESOLUTION_NOTE': "Note: Where there are blanks in the table below, the taxonomy could not be resolved in finer detail."
}

_BASIC_REPORT = {
    'TITLE': "Basic Report for %(barcode)s"
}

_INTERACTIVE_REPORT = {
    'TITLE': "Interactive Report for %(barcode)s"
}

_HELP_REQUEST = {
    'CONTACT_HEADER': "Contact the %(project_shorthand)s" % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'EMAIL_ADDRESS': "Email address",
    'FIRST_NAME': "First name",
    'LAST_NAME': "Last name",
    'NOTE': "Note that all inquiries are directed to the American Gut help account, which will be responding to the request",
    'PROBLEM_PROMPT': "Enter information related to your problem",
    'RESPONSE_TIMING': "We will send a response to the email address you supply within 48 hours.",
}

_DB_ERROR = {
    'HEADER': 'Oops! There seems to be a database error.',
    'MESSAGE': 'Please help us to debug by emailing us at <a href="mailto:%(help_email)s">%(help_email)s</a> and tell us exactly what happend before you got this error.' % {"help_email": media_locale["HELP_EMAIL"]},
    'SIGNOFF': 'Thanks, <br /> The American Gut Team'
}

_404 = {
    'HELP_TEXT': 'Click <a href="mailto:%(help_email)s">HERE</a> to email us about the issue. Please include the URL you were trying to access:' % {'help_email': media_locale['HELP_EMAIL']},
    'MAIN_WARNING': '404: Page not found!'
}

_403 = {
    'HELP_TEXT': 'Click <a href="mailto:%(help_email)s">HERE</a> to email us about the issue. Please include the URL you were trying to access:' % {'help_email': media_locale['HELP_EMAIL']}
}

_PARTICIPANT_OVERVIEW = {
    'COMPLETED_CONSENT': "Completed consent",
    'COMPLETED_SURVEY': "Completed survey",
    'OVERVIEW_FOR_PARTICPANT': "Overview for participant",
    'SAMPLES_ASSIGNED': "Samples assigned",
    'VIOSCREEN_CONTINUE': '<a href="%s"><button>Continue your Food Frequency Questionnaire</button></a>',
    'VIOSCREEN_COMPLETE': 'Food Frequency Questionnaire completed',
    'VIOSCREEN_START': '<a href="%s"><button>Start the Food Frequency Questionnaire</button></a>'
}

_ADD_SAMPLE_OVERVIEW = {
    'ADD_SAMPLE_1': 'If you don\'t see the sample source you want here, you need to add it. You can do this in ',
    'ADD_SAMPLE_2': 'Step 2',
    'ADD_SAMPLE_3': 'on the main page when you log in.',
    'ADD_SAMPLE_TITLE': 'Choose your sample source ',
    'ADD_SAMPLE_TITLE_HELP': 'The sample source is the person, animal or environment that the sample you are currently logging came from. If you took the sample from yourself, you should select yourself as the sample source.',
    'ANIMAL_SOURCE': 'Animal Source',
    'ENVIRONMENTAL': 'Environmental',
    'HUMAN_SOURCE': 'Human Source'
}

_SAMPLE_OVERVIEW = {
    'BARCODE_RECEIVED': "Sample %(barcode)s. This sample has been received by the sequencing center!",
    'BASIC_REPORT_TITLE': 'Basic Report',
    'BIOM_TABLE_TITLE': 'Summarised data (<a href="http://biom-format.org">biom-format.org</a>)',
    'EXCEL_TABLE_TITLE': 'Summarised data',
    'DATA_NOT_AVAILABLE': 'These data are not available yet for download.',
    'DISPLAY_BARCODE': "Sample %(barcode)s",
    'INTERACTIVE_REPORT_TITLE': 'Interactive Report',
    'RAW_SEQUENCE_TITLE': 'Raw sequences',
    'REMOVE_BARCODE': "Remove barcode %(barcode)s",
    'SAMPLE_DATE': "Sample Date",
    'SAMPLE_NOTES': "Notes",
    'SAMPLE_NOT_PROCESSED': "This sample has not yet been processed. Please check back later.",
    'SAMPLE_SITE': "Sample Site",
    'SAMPLE_STATUS': "Sample Status",
    'SAMPLE_TIME': "Sample Time",
    'sequence_url': 'Download FASTQ from EBI',
    'TAXA_SUM_TITLE': "Taxa Summary",
    'VIEW_TAXA_SUMMARY': "View Taxa Summary",
    'VIEW_BASIC_REPORT': 'View Basic Report',
    'VIEW_INTERACTIVE_REPORT': 'View Interactive Report'
}

_NEW_PARTICIPANT_OVERVIEW = {
    'ADD_NEW': "Add a New Human Sample Source",
    'CONTINUE': "Continue",
    'EXPLANATION': "You have entered the add human source workflow. During this workflow you will add a human source that represents whoever is being sampled. You be asked for consent to join the project and then asked survey questions.",
    'ONCE_ADDED': "Once you have added a human source, you will then see the name of that source in the left menu, and you will also have an option for adding a sample to that source. When you click that, you will be able to select the appropriate barcode and add sample metadata.",
    'ELECTRONIC_SIG_CONSENT': 'I consent to using an electronic signature'
}

_MAP = {
    'MAP_TITLE': "Map Key",
    'MAP_KIT': "Kit Verified",
    'MAP_PARTICIPANT': "Participant",
    'MAP_SAMPLE': "Sample(s) Logged",
    'SEP1': '1-10 kits',
    'SEP2': '11-100 kits',
    'SEP3': '101-1000 kits',
    'SEP4': '1001-10000 kits',
    'SEP5': '>10000 kits'
}

_FORGOT_PASSWORD = {
    'EMAIL': "E-mail",
    'EMAIL_FAILED': '<p>There was a problem sending you the password reset code. Please contact us directly at <a href="mailto:%(help_email)s" target="_blank">%(help_email)s</a>.</p><p>Email contained: </p>' % {'help_email': media_locale['HELP_EMAIL']},
    'EMAIL_RESET_PASSWORD': 'You will receive an email shortly with instructions to reset your password. Please check your email because you need to reset your password within two hours. If you are unable to find the email within 5 minutes, you may need to check your spam folder.<p>Additionally, attempting to access the email\'s link through your mobile device will not work and you will unfortunately have to use a computer.</p>',
    'ENTER_ID_EMAIL': "Enter your Kit ID and email",
    'KIT_ID': "Kit ID:",
    'NO_RECORD': '<p style="color:red;">This information does not match our records</p><p>Please email <a href="mailto:%(help_email)s">directly</a> for further assistance<p>',
    'SEND_EMAIL': "Send email"
}

_ERROR = {
    'ERROR_CONTACT': "The error has been logged and we will look into it. Please go back to the main page.",
    'ERROR_OCCURED': "AN ERROR HAS OCCURRED!"
}

_RETREIVE_KITID = {
    'EMAIL_CANTSEND': "Mail can be sent only from microbio.me domain.",
    'EMAIL_EXCEPTION': 'There was a problem sending you the kit ID. Please contact us directly at <a href="mailto:%(help_email)s">%(help_email)s</a>.' % {'help_email': media_locale['HELP_EMAIL']},
    'EMAIL_PROMPT': "Email:",
    'EMAIL_SUCCESS': "Your kit ID has been emailed to you. Please check your email.",
    'ENTER_EMAIL': "Please Enter Your Email",
    'SEND_EMAIL': "Send Kit ID Email",
    'UNKNOWN_EMAIL': "This email address is not in our system"
}

_ADD_SAMPLE = {
    'DATE': 'Date',
    'DATE_EXAMPLE': 'mm/dd/yyyy (Example: May 7th, 2013 is 05/07/2013)',
    'NEW_SAMPLE_DESCRIPTION_1': 'Choose the barcode from your kit that corresponds to the sample you are logging.',
    'NEW_SAMPLE_DESCRIPTION_2': 'It is very important that the sample barcode matches <strong>exactly</strong> for downstream analysis steps.',
    'NEW_SAMPLE_TITLE': 'Assign a new sample for',
    'NOTES': 'Additional Notes (optional)',
    'SITE_SAMPLED': 'Site Sampled',
    'TIME': 'Time',
    'TIME_EXAMPLE': 'hh:mm AM/PM (Example: 04:35 PM)'
}

_REGISTER_USER = {
    'ADDRESS': "Address",
    'CITY': "City",
    'COUNTRY': "Country",
    'EMAIL': "Email",
    'EMAIL2': 'Re-enter email',
    'ENTER_KIT_ID': "Please enter your kit ID",
    'ENTER_PASSWORD': 'Please enter your kit password',
    'ENTER_ADDRESS': "Please enter your address",
    'ENTER_CITY': "Please enter your city",
    'ENTER_COUNTRY': "Please enter your country",
    'ENTER_EMAIL': "Please enter your email",
    'ENTER_NAME': "Please enter your name",
    'ENTER_STATE': "Please enter your state",
    'INVALID_ID_OR_PW': "Invalid kit ID or password",
    'NAME': "Name",
    'REQUIRED_EMAIL': "You must supply a valid email",
    'MATCHING_EMAIL': 'Emails do not match',
    'STATE': "State",
    'PASSWORD': 'Password',
    'SUBMIT': "Submit My Information",
    'KIT_ID': 'Kit ID'
}

_ADDENDUM = {
    'ABUNDANT': "Abundant Microbes",
    'AG_POPULATION': "The American Gut Population",
    'BACTAX_LINK': "For more information on bacterial taxonomy, please refer to the following link: ",
    'CHIMP_TAXONOMY': "Chimpanzee",
    'CHIMP_TAXONOMY_CLASS': "Class: Mammalia",
    'CHIMP_TAXONOMY_FAMILY': "Family: Hominidae",
    'CHIMP_TAXONOMY_GENUS': "Genus: <em>Pan</em>",
    'CHIMP_TAXONOMY_KINGDOM': "Kingdom: Animalia",
    'CHIMP_TAXONOMY_ORDER': "Order: Primates",
    'CHIMP_TAXONOMY_PHYLUM': "Phylum: Chordata",
    'CHIMP_TAXONOMY_SPECIES': "Species: <em>troglodytes</em>",
    'COLLABORATORS': "Collaborators",
    'COMPARE_TEXT_1': 'Here, we present three Principle Coordinates Plots. Each point on these plots represents the bacterial composition of one sample from one person. We take all of the information about the abundances of all the bacteria in each sample and compare them to each other using this type of plot. When two points are very close to each other, it means that the types of bacteria in those two samples are very similar. Points that are farther apart represent samples that are less similar to each other. The axes mean nothing in this context. It doesn\'t matter how high or low a point is on the plot. The only thing that matters is how close it is to other points.',
    'COMPARE_TEXT_2': "The large point represents your sample on each plot. This allows you to see how similar (close to) or different (far from) your sample is from others.",
    'CONTRIB': "Contributors",
    'DIFFERENT_AGES_POPS': "Different Ages and Populations",
    'DIFFERENT_BODY_SITES': "Different Body Sites",
    'DIFFERENT_BODY_SITES_ALT': "PCoA by body site for AGP and HMP",
    'ENRICHED': "Enriched Microbes",
    'ENRICHED_EXP_1': "The second table shows four microbes that you had more of compared to other people. It is likely that other participants also have these microbes in their sample, but we found substantially higher abundances of them in your sample relative to others. The percentages on the right tell you how many of your total bacteria (under \"Sample\") or of the total bacteria in an average person\'s sample (under \"Population\") belong to these taxa. Since you have more of these bacteria than most other people, the percentage under \"Sample\" should be higher than the percentage under \"Population\".",
    'ENRICHED_EXP_2': "The fold change tells you how many more of these bacteria you have than the average participant. For example, if you have 20% Bacteria A and the average person in the population has 10% Bacteria A, you have twice as many Bacteria A. This would be a twofold (2x) difference. Please note that because the percentages we report on this sheet are rounded (e.g., 0.05% rounded to 0.1%), and your fold differences are calculated from values that are not rounded, the fold differences you see may be slightly distinct than what you would calculate based on the numbers you see.",
    'HUMAN_TAXONOMY': "Human",
    'HUMAN_TAXONOMY_CLASS': "Class: Mammalia",
    'HUMAN_TAXONOMY_FAMILY': "Family: Hominidae",
    'HUMAN_TAXONOMY_GENUS': "Genus: <em>Homo</em>",
    'HUMAN_TAXONOMY_KINGDOM': "Kingdom: Animalia",
    'HUMAN_TAXONOMY_ORDER': "Order: Primates",
    'HUMAN_TAXONOMY_PHYLUM': "Phylum: Chordata",
    'HUMAN_TAXONOMY_SPECIES': "Species: <em>sapiens</em>",
    'INTRO': 'We\'d like to note that in general these data allow you to understand how similar or different you are to other people in terms of the bacterial composition of the sample you sent. The information about the microbes is at as fine level of a taxonomic resolution as we were able to achieve with our sequencing methods, and varies for different groups of microbes. Currently, we cannot tell you what it means if you have more or less of a certain bacteria than other people. Gut microbiome research is still new, and we have a lot to learn. Your participation in the American Gut Project will allow us to learn more, and we hope to update you with new findings as they emerge.<br><br>The data discussed in this addendum are for illustrative purposes, and do not reflect a specific participant\'s sample.',
    'LACTO_TAXONOMY': "Here is the same list for a common yogurt bacterium (<em>Lactobacillus delbrueckii</em>):",
    'LACTO_TAXONOMY_CLASS': "Bacilli",
    'LACTO_TAXONOMY_FAMILY': "Lactobacillaceae",
    'LACTO_TAXONOMY_GENUS': "<em>Lactobacillus</em>",
    'LACTO_TAXONOMY_KINGDOM': "Bacteria",
    'LACTO_TAXONOMY_ORDER': "Lactobacillales",
    'LACTO_TAXONOMY_PHYLUM': "Firmicutes",
    'LACTO_TAXONOMY_SPECIES': "<em>delbrueckii</em>",
    'LEARN_MORE': "Learn more about your certificate by clicking on a plot or table",
    'MAJOR_PHYLA': "Major Bacterial Phyla",
    'MAJOR_PHYLA_ACTINOBACTERIA_HEADER': "Actinobacteria",
    'MAJOR_PHYLA_BACTEROIDETES_HEADER': "Bacteroidetes",
    'MAJOR_PHYLA_CYANOBACTERIA_HEADER': "Cyanobacteria",
    'MAJOR_PHYLA_CYANOBACTERIA_TEXT': "A phylum of photosynthetic (plant-like) bacteria. The name comes from their blue pigment (in Greek <em>kyanos</em> - blue). They can grow as single cells or form filamentous colonies. They are extremely successful in every imaginable environment including places where other organisms are extremely limited like hot springs or cold Antarctic bare rocks. Through their incredible diversity and abundance, they contribute significantly to the global cycle of oxygen.",
    'MAJOR_PHYLA_FIRMICUTES_HEADER': "Firmicutes",
    'MAJOR_PHYLA_FUSOBACTERIA_HEADER': "Fusobacteria",
    'MAJOR_PHYLA_FUSOBACTERIA_TEXT': "A phylum of rod-shaped Gram-negative bacteria. Known primarily as fermentative species but some can be pathogens. Can occur in anoxic (no oxygen) sediments as well as intestinal habitats of animals including humans.",
    'MAJOR_PHYLA_PROTEOBACTERIA_HEADER': "Proteobacteria",
    'MAJOR_PHYLA_TENERICUTES_HEADER': "Tenericutes",
    'MAJOR_PHYLA_VERRUCOMICROBIA_HEADER': "Verrucomicrobia",
    'MAJOR_PHYLA_VERRUCOMICROBIA_TEXT': "A relatively new phylum with only a handful of described species. Although not the most abundant, they seem to be always present in soil, aquatic environments, and feces. Most likely they are involved in the decomposition of organic matter, with no known pathogens. While some may be autotrophs, others can be internal symbionts of microscopic eukaryotes such as protists or nematodes. Their name is derived from a wart-like appearance (<em>verruca</em> means wart) but they do not cause warts.",
    'MOD01ALT': "Your %(project_shorthand)s Sample" % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'MOD01bALT': "Michael Pollan",
    'MOD02ALT': "What's in your sample?",
    'MOD03ALT': "How do your gut microbes compare to others?",
    'MOD08ALT': "PCoA of BodySites with HMP",
    'MOD09ALT': "PCoA of diets and age",
    'MOD10ALT': "PCoA of %(project_shorthand)s Data" % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'MOD11ALT': "Taxonomy Bar Charts",
    'MOD12ALT': "Major Phyla",
    'MOD13ALT': "Abundant Microbes",
    'MOD14ALT': "Enriched Microbes",
    'MOD15ALT': "Rare Microbes",
    'NOTE': 'Note that the results below act as an example of what our reports look like (we use Michael Pollan’s as a sample).  These are not a reflection of your own results.',
    'OBSERVED_TAXON_1': "<td class = 'taxa'>Family Prevotella</td><td class = 'row'>24.9%</td>",
    'OBSERVED_TAXON_2': "<td class = 'taxa'>Family Ruminococcaceae</td><td class = 'row'>13.4%</td>",
    'OBSERVED_TAXON_3': "<td class = 'taxa'>Family Lachnospiraceae</td><td class = 'row'>10.1%</td>",
    'OBSERVED_TAXON_4': "<td class = 'taxa'>Genus <em>Bacteroides</em></td><td class = 'row'>8.1%</td>",
    'RARE': "Rare Taxa",
    'RARE_TEXT_1': "This sample included the following rare taxa: Genus <em>Varibaculum</em>, Genus <em>Neisseria</em>, Genus <em>Campylobacter</em>, Unclassified Order ML615J-28.",
    'RARE_TEXT_2': "This line shows four microbes that you have that are not commonly found in the type of sample you provided. Some other people may have them, but most people do not.",
    'RESULTS_CAPTION': "Your certificate is designed to help you determine what was found in your sample, and how you compare to other people. Click on a graph or table to learn more.",
    'SAMPLE_TITLE': "What's in your %(project_name)s sample?" % {'project_name': AMGUT_CONFIG.project_name},
    'SPONSORS': "Sponsors",
    'SUPPORTERS': "Supporters",
    'TAXONOMY': "Taxonomy",
    'TAX_BARCHART': "Taxonomy Bar Chart",
    'TAX_BARCHART_EXP': "The first table shows the four most abundant groups of microbes in your sample. Although you had other bacteria, these are the ones that you have the most of. The percentages on the right (under \"Sample\") tell you what percent of all of your bacteria belong to these taxa.",
    'TAX_BARCHART_TEXT_1': "The taxonomy bar chart shows the abundances of bacterial types at the phylum level in your sample and compares it to other samples. Specifically, it shows you what percentage of all your bacteria belonged to each phyla. We also calculated the average percentage of each bacterial phylum across all samples, across samples from people with a similar diet to the one you reported, across samples from people of the same gender as you, across samples from everyone with a similar BMI to you, across samples from everyone with the same age as you, and for one specific person, Michael Pollan. You can compare the percentage of bacterial phyla in your sample (first bar) to all of these values to get an idea of how similar or different you are.",
    'TAX_BARCHART_TEXT_2': '<strong>Firmicutes and Bacteroidetes are the two most abundant bacterial phyla in the human gut, but others are also present.</strong> Please see <a href = "#phyla">Major Bacterial Phyla</a> below for basic descriptions of these phyla.',
    'TITLE': "%(project_shorthand)s Addendum" % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'TOP': "Back to the top",
    'YOUR_ABUNDANT': "Your most abundant microbes:",
    'YOUR_ABUNDANT_TABLE_HEADER': "<th>Taxonomy</th><th>Sample</th>",
    'YOUR_COMPARE': "How do your gut microbes compare to others?",
    'YOUR_ENRICHED': "Your most enriched microbes:",
    'YOUR_ENRICHED_1': "<td class = 'taxa'>Genus <em>Clostridium</em></td><td class = 'row'>2.5%</td><td class = 'row'>0.3%</td><td class = 'row'>7x</td>",
    'YOUR_ENRICHED_2': "<td class = 'taxa'>Genus <em>Finegoldia</em></td><td class = 'row'>0.7%</td><td class = 'row'>0.0%</td><td class = 'row'>17x</td>",
    'YOUR_ENRICHED_3': "<td class = 'taxa'>Genus <em>Prevotella</em></td><td class = 'row'>24.9%</td><td class = 'row'>2.6%</td><td class = 'row'>9x</td>",
    'YOUR_ENRICHED_4': "<td class = 'taxa'>Genus <em>Collinsella</em></td><td class = 'row'>0.9%</td><td class = 'row'>0.1%</td><td class = 'row'>8x</td>",
    'YOUR_ENRICHED_TABLE_HEADER': "<th>Taxonomy</th><th>Sample</th><th>Population</th><th>Fold</th>"
}

_PORTAL = {
    'ADD_SOURCE_TAB': "Add Source <br>Survey",
    'DOMESTIC_HEADER_1': "Domestic Shipping",
    'DOMESTIC_TEXT_2': "This is the shipping address:",
    'FOBT_INSTRUCTIONS': '<strong>If you have a FOBT card, please follow <a href="%s" target="_blank">these sampling instructions</a> instead and <a href="#" onclick="selectTab(\'log\')">assign it</a>.</strong>' % media_locale['FOBT_PDF'],
    'GREETING': "Hi %(user_name)s! Please follow the steps below.",
    'LOG_SAMPLE_HEADER_1': "Assigning Samples",
    'LOG_SAMPLE_TAB': "Assign a Sample",
    'LOG_SAMPLE_TEXT_1': "Please write the sample site, date, and time on the sampling tube.",
    'LOG_SAMPLE_TEXT_2': 'After writing the information on the sampling tube tube, <a href="%(sitebase)s/authed/add_sample_overview/">assign the sample</a> to a source.' % {'sitebase': media_locale['SITEBASE']},
    'LOG_SAMPLE_TEXT_3': '<strong>We require samples to be assigned</strong> so that we can process each sample and later upload the results based on each sample\'s barcode and corresponding profile.',
    'LOG_SAMPLE_NEW': 'You have samples to be assigned:',
    'LOG_SAMPLE_NO_SAMPLES': 'You\'ve assigned all of your samples. You\'re good to go!',
    'MAILING_HEADER_1': "Mailing samples",
    'MAILING_TEXT_1': "Once you have added a <a href=\"#\" onclick=\"selectTab('source')\">sample source, completed the relevant survey</a> (if applicable), <a href=\"#\" onclick=\"selectTab('sample')\">taken</a> and <a href=\"#\" onclick=\"selectTab('log')\">assigned your samples</a>, you should then mail the samples back to us.",
    'MAILING_TEXT_2': "Wrap the sample tube in absorbent tissue, such as facial tissue or paper towels, and mail it back as soon as possible. The absorbent tissue will help to keep the relative humidity within the package low.",
    'MAILING_TEXT_3': "We also recommend using a reinforced envelope to reduce the chance of losing your sample due to damaged packaging.",
    'MAILING_TEXT_4': "The sooner we receive your sample, the sooner we can get it stored in our -80C freezers and ready for processing!",
    'MAILING_TEXT_5': "<strong>Do not refrigerate or freeze the samples</strong> if they cannot be shipped immediately.",
    'MAIL_TAB': "Mail Samples <br>to Us",
    'RESULTS_HEADER_1': "Sequencing &amp; Results",
    'RESULTS_READY_HEADER_1': "Your results are ready!",
    'RESULTS_READY_TEXT_2': 'To access your available results, hover over "Human Samples" in the menu on the left, hover over your name, then click on your sample to view your results, or click one of the links below. <b>For help interpreting results, <a href="%s/authed/addendum/">click here</a></b>. The following barcodes are ready:' % _SITEBASE,
    'RESULTS_READY_TEXT_3': "You will be able to view your results here on this website once they are available.",
    'RESULTS_TEXT_1': 'Once you have added a <a href="#" onclick="selectTab(\'source\')">sample source, completed the relevant survey</a> (if applicable), <a href="#" onclick="selectTab(\'sample\')">taken</a> and <a href="#" onclick="selectTab(\'log\')">assigned your samples</a> and you have <a href="#" onclick="selectTab(\'mail\')">mailed the samples back to us</a>, we will then perform sequencing and analysis on your samples.',
    'SAMPLE_SOURCE_HEADER_1': "Sample Source",
    'SAMPLE_SOURCE_TEXT_1': "There are three different sample sources that you can choose from for the %(project)s. The sources are human, animal and environmental. The buttons below will allow you to add a new sample source.",
    'SAMPLE_SOURCE_TEXT_2': "If you add a <strong>human</strong> or <strong>animal</strong> source, you will be asked to complete a survey",
    'SAMPLE_SOURCE_TYPE_ANIMAL': "Animal",
    'SAMPLE_SOURCE_TYPE_ENVIRONMENTAL': "Environmental",
    'SAMPLE_SOURCE_TYPE_HUMAN': "Human",
    'SAMPLE_STEPS_HEADER_1': "Before Taking Your Samples",
    'SAMPLE_STEPS_HEADER_2': "Taking Your Samples",
    'SAMPLE_STEPS_TEXT_1': 'These sample collection instructions are very important, please read through them <strong>before</strong> beginning to take your sample. Deviations will cause issues with sample processing, sequencing, and data analysis. We cannot guarantee that we will be able to process your sample if the instructions are not followed, and <strong>we cannot offer replacements if instructions were not followed</strong>. Please do not hesitate to ask us questions at <a href="%(sitebase)s/authed/help_request/">%(help_email)s</a>.' % {'help_email': media_locale['HELP_EMAIL'], 'sitebase': media_locale['SITEBASE']},
    'SAMPLE_STEPS_TEXT_2': "These are the steps involved in taking a sample:",
    'SAMPLE_STEPS_TEXT_3': '<li>Make sure you have <a href="#" onclick="selectTab(\'source\')">added your sample source and complete the required survey(s)</a></li><li>Remove the sample swabs from the sample tube</li><li>Collect your sample following the guidelines below</li><li>Place sample swabs into the sample tube</li>',
    'SAMPLE_STEPS_TEXT_4': "Once you have removed the sample tube, only handle the sample swab by the red cap.",
    'SAMPLE_STEPS_TEXT_6': "For an <strong>oral sample</strong>, firmly rub both sides of both cotton tips on the surface of the tongue for 20 seconds. Take great caution not to touch the cheeks, teeth, or lips.",
    'SAMPLE_STEPS_TEXT_7': "For a <strong>skin sample</strong>, firmly rub both sides of both cotton tips over the skin surface being sampled for 20 seconds.",
    'SAMPLE_STEPS_TEXT_8': "For an <strong>other/environmental sample</strong>, firmly rub both sides of both cotton tips over the surface being sampled for 20 seconds.",
    'SAMPLE_STEPS_TEXT_9': 'After you have finished taking your sample, return the swabs to the sample tube and push the red cap on firmly. Then, immediately move on to <a href="#" onclick="selectTab(\'log\')"><strong>assign your sample</strong></a>.',
    'SEQ_TAB': "Sequencing &amp;<br>Results",
    'UNCONSENTED_HEADER': 'Samples received but missing association with consent',
    'UNCONSENTED_EXPLANATION': 'The following samples have been received but have not been associated with a consent document. Please complete a survey if you have not, then <a href="%(sitebase)s/authed/add_sample_overview/">associate the sample</a>. <span style="font-weight:bold;color:red">We cannot process these samples until they are associated with a consent.</span>' % {'sitebase': media_locale['SITEBASE']},
    'SURVEY_HEADER_1': "Survey",
    'SURVEY_TEXT_1': "If you are taking a human or animal sample, we ask that you complete a survey.",
    'SURVEY_TEXT_2': "The survey will take <strong>30-45 minutes</strong> for a human subject, or <strong>10 minutes</strong> for an animal subject. You <strong>cannot</strong> save in the middle of the survey, so please set aside enough time to complete the entire survey.",
    'SURVEY_TEXT_3': "If you are taking a human sample, the survey includes demographic, lifestyle, medical and diet questions. All survey questions are optional.",
    'SURVEY_TEXT_4': 'The diet questions do not require a food diary, but please be prepared to answer questions about your eating habits. A screenshot of the dietary questions is shown below.',
    'TAKE_SAMPLE_TAB': "Take a Sample",
    'VERIFICATION_CODE_ERROR': "The kit verification code you entered does not match our records. Please double-check the code you entered. If you continue to experience difficulties, please <a href=/authed/help_request/>contact us</a>.",
    'VERIFICATION_CODE_PROMPT': 'Please enter the verification code sent to your email address <a href="#" class="help" title="If you did not recieve a verification code in your email from %(project_shorthand)s, please check your spam folder. If you still cannot find it, contact %(help_email)s">(?)</a>' % {'project_shorthand': AMGUT_CONFIG.project_shorthand, 'help_email': media_locale['HELP_EMAIL']},
    'VERIFICATION_HEADER_1': "Verification",
    'VERIFICATION_HEADER_2': "Verify your identity and kit barcode(s)",
    'VERIFICATION_TEXT_1': "We ask you to verify that you received the correct sample tubes and kit. Using a <strong>Verification Code</strong> helps us ensure that you receive the correct barcodes and Credentials Sheet.",
    'VERIFICATION_TEXT_2': 'Our <strong>Verification Code</strong> will be sent to you via email to the address that you entered when you made your contribution; if you made an anonymous contribution, please <a href="%(sitebase)s/authed/help_request/">contact us directly</a>.' % {'sitebase': media_locale['SITEBASE']},
    'VERIFICATION_TEXT_3': 'If you cannot find your <strong>Verification Code</strong>, please make sure to check your spam folder. If you still cannot find the code, please <a href="%(sitebase)s/authed/help_request/">contact us</a>.' % {'sitebase': media_locale['SITEBASE']},
    'RESEND_VERIFICATION': 'Resend verification code',
    'VERIFY_BARCODES': "Please verify that the barcode(s) you received in the mail match the barcode(s) here",
    'VERIFY_BARCODES_POPUP': "The barcode you need to verify is located on the outside of your sample tube.",
    'VERIFY_TAB': "Verify Your Kit"
}

_CHANGE_PASS_VERIFY = {
    'BUTTON_TEXT': "Change Password",
    'CONFIRM_PASSWORD': "Confirm Password",
    'HELP_CONFIRM_PASSWORD': "Repeat your New Password again, exactly as before. We ask you to repeat it here so that you don't accidentally change your password to something you did not intend.",
    'HELP_NEW_PASSWORD': "The new password you would like to use to log in from now on.",
    'NEW_PASSWORD': "New Password",
    'NO_EMAIL_1': "Could not send Email",
    'NO_EMAIL_2': "We attempted to email the message below:",
    'NO_EMAIL_3': "This is a courtesy email to confirm that you have changed your password for your kit with ID %(kitid)s If you did not request this change, please email us immediately at %(help_email)s.",
    'NO_VALID_CODE': 'Your password change code is not valid. If you wish to change your password please <a href="%(sitebase)s/forgot_password/">start over</a>' % {'sitebase': media_locale['SITEBASE']},
    'SUCCESS': "Your password has been changed",
    'TITLE': "Please enter new password"
}

_SURVEY_MAIN = {
    'ONCE_YOU_START': 'Once you start this survey, you must complete it. Your answers will <strong>not</strong> be saved unless you complete the entire survey.',
    'OTHER_SURVEYS': 'Following the questionnaire, you will be presented with a few other focused surveys. As with everything, those surveys are optional but your responses could help improve our understanding of the microbiome.',
    'TIME_COMMITMENT': 'We anticipate that participant time commitment for completing the questionnaire online will take no more than <strong>45 minutes</strong>.',
    'TITLE': 'Survey',
    'TYPES_OF_QUESTIONS': 'You will be asked questions about your general personal information (name, age, sex, height, weight, ethnicity, place of birth, and current ZIP or equivalent code). We will ask if you recently moved and where you moved from. We will ask questions about general diet information (including whether you follow a special diet, if you have food allergies, whether you have cultural or religious food restrictions). Other questions address whether you have pets and the type of contact you have with these pets and your relationship to other people in this study. There is a section on health information including a history of allergies/asthma, if you suffer from migraines and if you have a history of irritable bowel disease.',
    'YOU_MAY_DECLINE': 'You may decline to answer any question by not selecting an answer.',
}

_HUMAN_SURVEY_COMPLETED = {
    'AVAILABLE_SURVEYS': 'Below are a few additional surveys that you may be interested in completing. There is no requirement to take these surveys, and your decision does not affect your involvement in the project in any way.',
    'COMPLETED_HEADER': 'Congratulations!',
    'COMPLETED_SAMPLE_ASSIGNED_HEADER': 'Thank you for logging your sample!',
    'COMPLETED_TEXT': 'You are now an enrolled participant in the %(PROJECT_TITLE)s! As a reminder, you still need to associate your sample(s) with the survey to complete the process. If your sample(s) are not associated with a survey, we will not be able to process them.' % media_locale,
    'SURVEY_ASD': '<h3 style="text-align: center"><a href="%s" target="_blank">ASD-Cohort survey</a></h3><a href="http://www.anl.gov/contributors/jack-gilbert">Dr. Jack Gilbert</a> is exploring the relationship between gut dysbiosis and Autism Spectrum Disorders, and in conjunction with the {0}, we started an ASD-Cohort study. This additional survey contains questions specific to that cohort, but it is open to any participant to take if they so choose.'.format(AMGUT_CONFIG.project_name),
    'SURVEY_VIOSCREEN': '<h3 style="text-align: center"><a href="%s">Dietary Survey</a></h3>The {0} and its sister projects are very interested in diet. If you\'d like to provide additional detail about your diet, please click above to take a detailed diet survey (known as an Food Frequency Questionnaire). This is a validated FFQ, and is the one used by the Mayo Clinic.'.format(AMGUT_CONFIG.project_name),
    'SURVEY_FERMENTED': '<h3 style="text-align: center"><a href="%s" target="_blank">Fermented Foods Survey</a></h3>As part of our onging research into what drive changes in the human gut microbiome, we are looking at fermented foods and the microbiomes of fermented food eaters. Please click the link above if you would like to participate in this survey.',
    'SURVEY_SURF': '<h3 style="text-align: center"><a href="%s" target="_blank">Surfing Survey</a></h3>As part of our study, we are interested in the effects of frequent and prolonged exposure to salt water and the ocean, as it pertains to surfing and surfers. If you are interested in participating, you can click the link above and take the survey.'
}

_NO_RESPONSE_CHOICE = "Unspecified"
_YES_NO_CHOICES = (_NO_RESPONSE_CHOICE, 'Yes', 'No')
_YES_NO_NOTSURE_CHOICES = (_NO_RESPONSE_CHOICE, 'Yes', 'No', 'Not sure')
_FREQUENCY_MONTH_CHOICES = (_NO_RESPONSE_CHOICE,
                            'Never',
                            'Rarely (a few times/month)',
                            'Occasionally (1-2 times/week)',
                            'Regularly (3-5 times/week)',
                            'Daily')
_FREQUENCY_WEEK_CHOICES = (_NO_RESPONSE_CHOICE,
                           'Never',
                           'Rarely (less than once/week)',
                           'Occasionally (1-2 times/week)',
                           'Regularly (3-5 times/week)',
                           'Daily')
_DIAGNOSIS_CHOICE = (_NO_RESPONSE_CHOICE,
                     'I do not have this condition',
                     'Diagnosed by a medical professional (doctor, physician assistant)',
                     'Diagnosed by an alternative medicine practitioner',
                     'Self-diagnosed')
_ANIMAL_SURVEY = {
    'GENERAL_TITLE': 'General',
    'GENERAL_QUESTION_1': 'Animal type?',
    'GENERAL_QUESTION_1_CHOICES': (_NO_RESPONSE_CHOICE,
                                   'Dog',
                                   'Cat',
                                   'Small mammal',
                                   'Large mammal',
                                   'Fish',
                                   'Bird',
                                   'Reptile',
                                   'Amphibian',
                                   'Other'),

    'GENERAL_QUESTION_2': 'Origin?',
    'GENERAL_QUESTION_2_CHOICES': (_NO_RESPONSE_CHOICE,
                                   'Breeder',
                                   'Shelter',
                                   'Home',
                                   'Wild'),

    'GENERAL_QUESTION_3': 'Age?',
    'GENERAL_QUESTION_3_CHOICES': None,

    'GENERAL_QUESTION_4': 'Gender?',
    'GENERAL_QUESTION_4_CHOICES': (_NO_RESPONSE_CHOICE,
                                   'Male',
                                   'Female',
                                   'Unknown'),

    'GENERAL_QUESTION_5': 'Setting?',
    'GENERAL_QUESTION_5_CHOICES': (_NO_RESPONSE_CHOICE,
                                   'Urban',
                                   'Suburban',
                                   'Rural'),

    'GENERAL_QUESTION_6': 'Weight category?',
    'GENERAL_QUESTION_6_CHOICES': (_NO_RESPONSE_CHOICE,
                                   'Underweight',
                                   'Skinny',
                                   'Normal',
                                   'Chubby',
                                   'Overweight'),

    'GENERAL_QUESTION_7': 'Diet classification?',
    'GENERAL_QUESTION_7_CHOICES': (_NO_RESPONSE_CHOICE,
                                   'Carnivore',
                                   'Omnivore',
                                   'Herbivore'),

    'GENERAL_QUESTION_8': 'Food source?',
    'GENERAL_QUESTION_8_CHOICES': (_NO_RESPONSE_CHOICE,
                                   'Pet store food',
                                   'Human food',
                                   'Wild food'),

    'GENERAL_QUESTION_9': 'Food type?',
    'GENERAL_QUESTION_9_CHOICES': (_NO_RESPONSE_CHOICE,
                                   'dry',
                                   'wet',
                                   'both'),

    'GENERAL_QUESTION_10': 'Food special attributes?',
    'GENERAL_QUESTION_10_CHOICES': (_NO_RESPONSE_CHOICE,
                                    'Organic',
                                    'Grain free'),

    'GENERAL_QUESTION_11': 'Social?',
    'GENERAL_QUESTION_11_CHOICES': (_NO_RESPONSE_CHOICE,
                                    'Lives alone with humans',
                                    'Lives alone no/limited humans (shelter)',
                                    'Lives with other animals and humans',
                                    'Lives with other animals/limited humans'),

    'GENERAL_QUESTION_12': 'Any pets the current animal lives with?',
    'GENERAL_QUESTION_12_CHOICES': None,

    'GENERAL_QUESTION_13': 'Add the age of any human that the current animal lives with',
    'GENERAL_QUESTION_13_CHOICES': None,

    'GENERAL_QUESTION_14': 'Add the gender of any human that the current animal lives with',
    'GENERAL_QUESTION_14_CHOICES': (_NO_RESPONSE_CHOICE,
                                    'Male',
                                    'Female',
                                    'Other'),

    'GENERAL_QUESTION_15': 'Hours spent outside?',
    'GENERAL_QUESTION_15_CHOICES': (_NO_RESPONSE_CHOICE,
                                    'None',
                                    'Less than 2',
                                    '2-4',
                                    '4-8',
                                    '8+'),

    'GENERAL_QUESTION_16': 'Toilet water access?',
    'GENERAL_QUESTION_16_CHOICES': (_NO_RESPONSE_CHOICE,
                                    'Regular',
                                    'Sometimes',
                                    'Never'),

    'GENERAL_QUESTION_17': 'Coprophage?',
    'GENERAL_QUESTION_17_CHOICES': (_NO_RESPONSE_CHOICE,
                                    'High',
                                    'Moderate',
                                    'Low',
                                    'Never'),

    'SUPPLEMENTAL_COMMENTS': 'Please write anything else about this animal that you think might affect its microorganisms.'
}

_PERSONAL_MICROBIOME = {
    'HEADER': 'Online Survey Consent Form',
    'CONSENT_1': 'You are being invited to participate in a research study titled "Impact of Personal Microbiome Information on American Gut Study Volunteers." This study is being done by Dr. Cinnamon Bloss, Professor from the University of California - San Diego (UCSD) School of Medicine. You are being invited to participate in this research because you took part in the American Gut Project study.',
    'CONSENT_2': "The purpose of this research study is to better understand how participation in the American Gut Project may have impacted people's health views, health behaviors, or communication with their healthcare provider. If you agree to take part in this study the following will happen to you:",
    'CONSENT_LIST_1': 'You will complete an online survey. This survey will ask questions about how you feel about your experience in the American Gut Project, about the impact receiving your personal microbiome results has on you, and some demographic questions about you. It will take about 5-10 minutes to complete the survey.',
    'CONSENT_LIST_2': 'Information that you provided as part of the American Gut Project will be collected and used in this study.',
    'CONSENT_LIST_3': "The study may also involve follow up interviews at a later date to collect more detailed and specific information about how participation in the American Gut Project has impacted participant's health. If you would like to participate in the possible follow-up interviews to share more of your thoughts, you can provide your contact information at the end of the survey. However, you should note that, even if you agree to be interviewed it is possible that you will not be contacted.",
    'CONSENT_3': "The data collected as part of this study may also be used in studies by other researchers from UCSD and other Universities. Dr. Bloss will be responsible for deciding how your data will be used. Dr. Bloss, her associates, or her successors in these studies will keep your data and the information derived from it for an indefinite period. By consenting to participate in this study you are indicating that you consent to the use of your data in other studies. If you do not consent to such use you should not participate in this study.",
    'CONSENT_4': "There will not be any direct benefit to you from this research. The investigator(s), however, may better understand how participating in the American Gut Project impacts people's health views, health behaviors, and communication with their healthcare providers.",
    'CONSENT_5': "There are minimal risks associated with this research study. Taking surveys can produce feelings of stress, frustration, discomfort, fatigue, and boredom.  To limit these risks, the questions have been written in a clear manner. There is a risk of loss of confidentiality. To protect against such a loss research records will be kept confidential to the extent allowed by law. Your survey data will be stored on a password protected secure computer will be identified by a study subject ID number.  If you decide to provide your name and contact information for potential follow-up, your name and contact information will be kept separate from your survey responses and will not be linked to your survey responses.  All analysis of the survey data will be done on data that is de-identified (e.g. does not contain your name). Research records may be reviewed by the UCSD Institutional Review Board and the National Institutes of Health. Results of this study may be reported in scientific journals, meeting, and news media, but none of these reports will use your name or use data that can point to any person who took part in the study.",
    'CONSENT_6': "Your participation in this study is completely voluntary and you can withdraw at any time by simply exiting the survey. Choosing not to participate or withdrawing will result in no penalty or loss of benefits to which you are entitled. You are free to skip any question that you choose.",
    'CONSENT_7': "If you have questions about this project or if you have a research-related problem, you may contact the researcher(s), Dr. Cinnamon Bloss at 858-534-9550. If you have any questions concerning your rights as a research subject, you may contact the UCSD Human Research Protections Program Office at (858) 246-7444.",
    'CONSENT_8': 'By clicking "You agree" below you are indicating that you are at least 18 years old, have read this consent form, and agree to participate in this research study. Please print a copy of this page for your records.',
    'AGREE': 'You Agree',
    'DISAGREE': 'You Do Not Agree'
}
