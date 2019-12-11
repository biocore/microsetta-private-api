#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from amgut.lib.config_manager import AMGUT_CONFIG
from amgut.lib.locale_data import english_gut as ENG

# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The American Gut Project Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

# Any media specific localizations
_SITEBASE = AMGUT_CONFIG.sitebase

media_locale = {
    'ANALYTICS_ID': 'UA-55355651-1',
    'FUNDRAZR_URL': "https://fundrazr.com/campaigns/4sSf3",
    'KIT_INSTRUCTIONS': _SITEBASE + '/static/img/bg_kit_instructions.pdf',
    'LATITUDE': 54.5,
    'LOGO': _SITEBASE + '/static/img/bg_logo.png',
    'LONGITUDE': -3.5,
    'SHIPPING_ADDRESS': 'Gabriela Surdulescu<br/>Department of Twin Research<br/>St. Thomas’ Hospital Campus<br>The Rayne Institute, Lambeth Wing, 4th Floor<br/>Westminster Bridge Road, London SE1 7EH',
    'ZOOM': 6
}
media_locale.update(ENG.media_locale)

_HANDLERS = ENG._HANDLERS

_NEW_PARTICIPANT = ENG._NEW_PARTICIPANT

_FAQ = {
    'FECAL_NO_RESULTS': "I sent in a faecal sample but did not get any results, what happened to them?",
    'HOW_PROCESS_SAMPLES_ANS_6': '<ul> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/21552244">Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/24280061">EMPeror: a tool for visualising high-throughput microbial community data.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/16332807">UniFrac: a new phylogenetic method for comparing microbial communities.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/16893466">UniFrac--an online tool for comparing microbial community diversity in a phylogenetic context.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/17220268">Quantitative and qualitative beta diversity measures lead to different insights into factors that structure microbial communities.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/19710709">Fast UniFrac: facilitating high-throughput phylogenetic analyses of microbial communities including analysis of pyrosequencing and PhyloChip data.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/20827291">UniFrac: an effective distance metric for microbial community comparison.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/21885731">Linking long-term dietary patterns with gut microbial enterotypes.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/23326225">A guide to enterotypes across the human body: meta-analysis of microbial community structures in human microbiome datasets.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/22699609">Structure, function and diversity of the healthy human microbiome.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/22699610">A framework for human microbiome research.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/23587224">The Biological Observation Matrix (BIOM) format or: how I learned to stop worrying and love the ome-ome.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/22134646">An improved Greengenes taxonomy with explicit ranks for ecological and evolutionary analyses of bacteria and archaea.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/21304728">The Earth Microbiome Project: Meeting report of the "1 EMP meeting on sample selection and acquisition" at Argonne National Laboratory October 6 2010.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/21304727">Meeting report: the terabase metagenomics workshop and the vision of an Earth microbiome project.</a></li> </ul>' % {'project_name': AMGUT_CONFIG.project_name},
    'HOW_PROCESS_SAMPLES_ANS_10': '<ul> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/17881377">Short pyrosequencing reads suffice for accurate microbial community analysis.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/18723574">Accurate taxonomy assignments from 16S rRNA sequences produced by highly parallel pyrosequencers.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/18264105">Error-correcting barcoded primers for pyrosequencing hundreds of samples in multiplex.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/22237546">Selection of primers for optimal taxonomic classification of environmental 16S rRNA gene sequences.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/22170427">Comparison of Illumina paired-end and single-direction sequencing for microbial 16S rRNA gene amplicon surveys.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/21716311">Impact of training sets on classification of high-throughput bacterial 16s rRNA gene surveys.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/21349862">PrimerProspector: de novo design and taxonomic analysis of barcoded polymerase chain reaction primers.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/20383131">QIIME allows analysis of high-throughput community sequencing data.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/22161565">Using QIIME to analyse 16S rRNA gene sequences from microbial communities.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/23861384">Meta-analyses of studies of the human microbiota.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/24060131">Advancing our understanding of the human microbiome using QIIME.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/20534432">Global patterns of 16S rRNA diversity at a depth of millions of sequences per sample.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/22402401">Ultra-high-throughput microbial community analysis on the Illumina HiSeq and MiSeq platforms.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/23202435">Quality-filtering vastly improves diversity estimates from Illumina amplicon sequencing.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/22699611">Human gut microbiome viewed across age and geography.</a></li> </ul>',
    'HOW_PROCESS_SAMPLES_ANS_8': '<ul> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/20412303">Effect of storage conditions on the assessment of bacterial community structure in soil and human-associated samples.</a></li> <li><a href="http://www.ncbi.nlm.nih.gov/pubmed/20673359">Sampling and pyrosequencing methods for characterising bacterial communities in the human gut using 16S sequence tags.</a></li> </ul>',
    'INFORMATION_IDENTIFY_ME_ANS': "No. First, all of your personal information is anonymous in our database as mandated by institutional guidelines. Second, although each person has a unique gut microbiome, many of the unique qualities are at the species or strain level of bacteria. Our sequencing methods currently do not allow us to describe your gut microbiome in that much detail. Finally, for most medical conditions, there are no known, predictable patterns in gut microbial community composition. Research simply hasn't gotten that far yet.</p>"
                                   "<p>We should also mention that since we are only interested in your microbes, we do not sequence human genomic DNA in our typical analyses. Where it is possible for human DNA to be sequenced (e.g., the Beyond Bacteria kits), we remove the human DNA using the same bioinformatics approaches undertaken in the NIH-funded Human Microbiome Project and approved by NIH bioethicists. Additionally, there is so little human DNA in faecal, skin and mucus samples that the chances of us being able to sequence your entire human genome are almost none, even if we tried.",
    'ONLY_FECAL_RESULTS': "I sent more than one kind of sample, but I only received data for my faecal sample. What happened to my other samples?",
    'ONLY_FECAL_RESULTS_ANS': 'Results are only available for faecal, oral, and skin samples. We are in the process of evaluating how best to present the other sample types. Please see <a href="#faq16">the previous question </a>',
    'PROJECT_RELATION': 'What is the British Gut’s relation to the American Gut?',
    'PROJECT_RELATION_ANS': "The British Gut is considered a “sister site” to the American Gut--so while it has a separate site of operations at <a href='http://www.twinsuk.ac.uk/'>King's College London</a> with TwinsUK, some of the operations tie back to the American Gut framework (examples include samples being processed at American Gut’s site at the University of California San Diego, emails being directed to the American Gut help account).<p>The British Gut was set up as a unique collaboration in order to be able to extend and collect samples from European participants.  By having a site set up in Europe, the time and cost for sending out kits, receiving samples, and sending samples back for analysis are greatly reduced.</p><p>Ultimately, both the American Gut and British Gut tie back to a larger umbrella known as <a href='http://microsetta.ucsd.edu'>The Microsetta Initiative</a>, which was an effort started in 2018 that wishes to collect microbiome samples and rich phenotypic data across the world’s populations.</p>",
    'RAW_DATA_ANS_2': 'Processed sequence data and open-access descriptions of the bioinformatic processing can be found at our <a href="https://github.com/qiime/American-Gut">Github repository</a>.</p>'
                      '<p>Sequencing of %(project_shorthand)s samples is an on-going project, as are the bioinformatic analyses. These resources will be updated as more information is added and as more open-access descriptions are finalised.' % {'project_shorthand': AMGUT_CONFIG.project_shorthand},
    'WHEN_RESULTS_NON_FECAL': "I sent in a non-faecal sample and have not received any results, when should I expect results?",
    'WHEN_RESULTS_NON_FECAL_ANS': "The vast majority of the samples we've received are faecal, which was why we prioritised those samples. Much of the analysis and results infrastructure we've put in place is applicable to other sample types, but we do still need to assess what specific representations of the data make the most sense to return to participants. We apologise for the delay.",
    'WHERE_SEND_SAMPLE_ANS': '<p>This is the shipping address:</p>%(shipping)s' % {'shipping': media_locale['SHIPPING_ADDRESS']}
}
_FAQ.update(ENG._FAQ)

_INTRODUCTION = {
    'INTRODUCTION_WHAT_IS_PROJECT': "<p>The %(project_name)s is a project in which scientists aim to work with non-scientists both to help them (AKA, you) understand the life inside their own guts and to do science. Science is coolest when it is informs our daily lives and what could possibly be more daily than what goes on in your gut? One of the big questions the %(project_shorthand)s scientists hope to figure out is what characterises healthy and sick guts (or even just healthier and sicker guts) and how one might move from the latter to the former. Such is the sort of big lofty goal these scientists dream about at night (spirochetes rather than sugarplums dancing through their heads), but even the more ordinary goals are exciting. Even just beginning to know how many and which species live in our guts will be exciting, particularly since most of these species have never been studied, which is to say there are almost certainly new species inside you, though until you sample yourself (and all the steps that it takes to look at a sample happen&mdash; the robots, the swirling, the head scratching, the organising of massive datasets), we won't know which ones. Not many people get to go to the rainforest to search for, much less discover, a new kind of monkey, but a new kind of bacteria, well, it is within (your toilet paper's) reach." % {'project_shorthand': AMGUT_CONFIG.project_shorthand, 'project_name': AMGUT_CONFIG.project_name},
    'INTRODUCTION_WHAT_IS_16S': "16S rRNA is a sort of telescope through which we see species that would otherwise be invisible. Let me explain. Historically, microbiologists studied bacteria and other microscopic species by figuring out what they ate and growing them, on petri dishes, in labs, in huge piles and stacks. On the basis of this approach&mdash; which required great skill and patience&mdash; thousands, perhaps hundreds of thousands, of studies were done. But then&hellip; in the 1960s, biologists including the wonderful radical <a href=\"http://www.robrdunn.com/2012/12/chapter-8-grafting-the-tree-of-life/\">Carl Woese</a>, began to wonder if the RNA and DNA of microbes could be used to study features of their biology. The work of Woese and others led to the study of the evolutionary biology of microbes but it also eventually led to the realisation that most of the microbes around us were not culturable&mdash; we didn't know what they ate or what conditions they needed. This situation persists. No one knows how to grow the vast majority of kinds of organisms living on your body and so the only way to even know they are there is to look at their RNA. There are many bits of RNA and DNA that one might look at, but a bit called 16S has proven particularly useful.",
    'INTRODUCTION_MICROBES_COME_FROM': "If you had asked this question a few years ago, we would have had to say the stork. But increasingly we are beginning to understand more about where the specific zoo of species in you come from and it is a little grosser than the stork. If you were born vaginally, some of your gut microbes came from your mother's feces (birth, my friend, is messy). Some came from her vagina. Others came, if you were breast fed, from her milk. It is easiest for bacteria, it seems, to colonise our guts in the first moments of life. As we age, our stomachs become acidic. We tend to think of the acid of our stomachs as aiding in digestion; it does that but another key role of our stomachs is to prevent pathogenic species from getting into our guts. The trouble with this, well, there are a couple of problems. One is c-section birth. During c-section birth, microbes need to come from somewhere other than the mother's vagina and feces. The most readily available microbes tend to be those in the hospital. As a result, the microbes in c-section babies tend to, at least initially, resemble those of the hospital more than they resemble those of other babies. With time, many c-section babies eventually get colonised by enough good bacteria (from pet dogs, pet cats, their parents' dirty hands, etc..) to get good microbes, but it is a more chancy process. But then, the big question, one we just don't know the answer to, is which and how many microbes colonise our guts as we get older. How many microbes ride through the acid bath of our stomach on our food and take up residence? We know that bad bacteria, pathogens, do this, but just how often and how good ones do it is not well worked out. You might be thinking, what about yoghurt and I'll tell you the answer, definitely, is we don't really know. Do people who eat yoghurt have guts colonised by species from that yoghurt? Maybe, possibly, I bet they do, but we don't really know (though if we get enough samples from yoghurt and non yoghurt eaters, we could know)."
}
_INTRODUCTION.update(ENG._INTRODUCTION)

_TAXA_SUMMARY = {
    'PERCENTAGES_NOTE': "Note: The percentages listed represent the relative abundance of each taxon. This summary is based off of normalised data. Because of limitations in the way the samples are processed, we cannot reliably obtain species level resolution. As such, the data shown are collapsed at the genus level."
}
_TAXA_SUMMARY.update(ENG._TAXA_SUMMARY)

_BASIC_REPORT = ENG._BASIC_REPORT
_INTERACTIVE_REPORT = ENG._INTERACTIVE_REPORT
_HELP_REQUEST = ENG._HELP_REQUEST
_DB_ERROR = ENG._DB_ERROR
_404 = ENG._404

_403 = {
    'MAIN_WARNING': '403: Unauthorised access!'
}
_403.update(ENG._403)

_PARTICIPANT_OVERVIEW = ENG._PARTICIPANT_OVERVIEW
_ADD_SAMPLE_OVERVIEW = ENG._ADD_SAMPLE_OVERVIEW

_SAMPLE_OVERVIEW = {
    'DATA_VIS_TITLE': "Data Visualisation",
    'RESULTS_PDF_LINK': "Click this link to visualise sample %(barcode)s in the context of other microbiomes!",
}
_SAMPLE_OVERVIEW.update(ENG._SAMPLE_OVERVIEW)

_NEW_PARTICIPANT_OVERVIEW = {
    'ELECTRONIC_SIGNATURE': 'In order to participate in this study, you will need to sign a research consent form. This must be done electronically. To consent to using an electronic signature, please click the button below. To obtain a hard copy of the signed agreement, please email the help desk (britishgut@gmail.com). You may revoke this consent at any time by going to human samples -> person name -> remove person name. Revoking consent will also halt processing of your sample, if applicable. Once your sample is processed, we cannot remove it from the deidentified information distributed, regardless of consent revocation.'
}
_NEW_PARTICIPANT_OVERVIEW.update(ENG._NEW_PARTICIPANT_OVERVIEW)

_MAP = ENG._MAP
_FORGOT_PASSWORD = ENG._FORGOT_PASSWORD
_ERROR = ENG._ERROR
_RETREIVE_KITID = ENG._RETREIVE_KITID
_ADD_SAMPLE = ENG._ADD_SAMPLE

_REGISTER_USER = {
    'ENTER_ZIP': "Please enter your postcode",
    'REQUIRED_ZIP': 'Your postcode must be 10 or fewer characters',
    'ZIP': "Postcode"
}
_REGISTER_USER.update(ENG._REGISTER_USER)

_ADDENDUM = {
    'AG_POPULATION_ALT': "PCoA of American Gut population coloured by Firmicutes",
    'AG_POPULATION_TEXT': "This plot lets you compare your sample to other faecal microbiome samples we collected from American Gut participants. The colour indicates the relative abundance of Firmicutes bacteria each sample had with red being the lowest and purple being the highest. If you had a lot of Firmicutes bacteria, then your sample should be purple, and you can look for other purple samples to see how similar your whole bacterial community is to other people with high amounts of Firmicutes. As in the other plots, the location of the point along the axes means nothing. Only its relative position compared to the other points is meaningful.",
    'DIFFERENT_AGES_POPS_ALT': "PCoA of international populations coloured by age",
    'DIFFERENT_AGES_POPS_TEXT': "This plot lets you compare your sample to other faecal microbiome samples according to age and place of origin. The colour of each point indicates the age of the person the sample was collected from, with red being the youngest and purple being the oldest. Also, on this plot, the ovals show where in the world each sample came from. The red oval shows you the area where an average sample from a Western country should fall. The yellow oval shows you where an average sample from an Amerindian population in Venezuela should fall. The blue oval shows you where an average sample from Malawi should fall. These data are from <a href = 'http://www.nature.com/nature/journal/v486/n7402/abs/nature11053.html'>Yatsunenko et al. 2012</a>. We used these populations as a comparison to your sample since a large number of people with diverse ages were sampled in these populations. We have fewer data from other populations in other parts of the world.",
    'DIFFERENT_BODY_SITES_TEXT': "This plot lets you compare your sample to samples collected in other microbiome projects from several body sites. The colour of each point tells you which project and body site the sample came from. HMP refers to the <a href = 'http://www.hmpdacc.org'>Human Microbiome Project</a>, funded by the National Institutes of Health. You can see how your sample compared to faecal, oral, and skin samples from the Human Microbiome Project, as well as to faecal, oral, and skin samples from the American Gut Project, the Global Gut Project, and the Personal Genome Project. These samples have been combined in any category not labeled \"HMP\". The oval around each group of points shows you where an average sample from each project and body site should fall on the plot. These sometimes make it easier to see the patterns all the clusters of points make.",
    'MAJOR_PHYLA_ACTINOBACTERIA_TEXT': "A phylum of Gram-positive bacteria both terrestrial and aquatic. They are mostly recognised as excellent decomposers of resilient organic compounds such as cellulose or chitin. Although some can be plant and animal pathogens, others are more known as producers of antibiotics (e.g. Streptomyces).  In their body form, many resemble fungi by forming mycelial-like filaments.",
    'MAJOR_PHYLA_BACTEROIDETES_TEXT': "A phylum of Gram-negative bacteria, rod-shaped, present in all sorts of environments such as soil, sediments, and fresh and marine waters. Most are saprophytic and involved in carbon cycling. Often abundant in nutrient-rich habitats and so they are a major component of animal guts where they can act as degraders of complex carbohydrates and proteins but also as pathogens. Their representatives are organised within 4 major classes among which the genus <em>Bacteroides</em> in the class of Bacteroidia is the most prevalent and the most studied. Bacteroidetes together with Firmicutes make up the majority of gut bacteria. The ratio of these two types of bacteria (specifically the dominance of Firmicutes over Bacteroidetes) may be linked to obesity.",
    'MAJOR_PHYLA_FIRMICUTES_TEXT': "A phylum of bacteria with generally Gram-positive (retain crystal violet dye) staining cell wall structure. The names is derived from Latin <em>firmus</em> for strong and <em>cutis</em> for skin. The cells are in the form of spheres called cocci (singular coccus) or rods called bacilli (singular bacillus). Firmicutes encompass bacteria that can be found in many different environments ranging from soil to wine to your gut. There are currently more than 274 genera representing 7 different classes of which Clostridia (anaerobes - no oxygen) and Bacilli (obligate or facultative aerobes) are the most significant. Both classes are predominantly saprophytic (getting nourishment from dead or decaying organic matter) playing an important role in the decomposition and nutrient mineralisation processes, but also contain a few human pathogens (e.g. <em>Clostridium tetani</em> or <em>Bacillus anthracis</em>).",
    'MAJOR_PHYLA_PROTEOBACTERIA_TEXT': "A phylum of Gram-negative bacteria. They are named after a Greek God Proteus to illustrate their variety of forms. They are organised in 6 recognised classes and represent all types of metabolisms ranging from heterotrophic to photosynthetic to chemoautotrophic.  They include many well-known pathogens (e.g., <em>Escherichia</em>, <em>Helicobacter</em>, <em>Salmonella</em>, <em>Vibrio</em>) as well as free-living types that can fix nitrogen (convert nitrogen present in the atmosphere into ammonia, a form of nitrogen available for plants&apos; uptake).",
    'MAJOR_PHYLA_TENERICUTES_TEXT': "A phylum of Gram-negative bacteria without a cell wall (<em>tener</em> - soft, <em>cutis</em> - skin) which are organised in a single class. Nutritionally, they represent variable pathways ranging from aerobic and anaerobic fermenters to commensals to strict pathogens of vertebrates (e.g., fish, cattle, wildlife). Among the best studied are Mycoplasmas with a fried egg-like shape and <em>Mycoplasma pneumoniae</em> is one of the best known examples of human pathogens causing pneumonia, bronchitis, and other respiratory conditions.",
    'TAXONOMY_INTRO': "Taxonomy is a system scientists use to describe all life on the planet. Taxonomy is commonly referred to as an organism&apos;s scientific name. This name allows us to understand how closely related two organisms are to each other. There are seven major levels of taxonomy that go from less specific to more specific. The phylum level represents very broad range of organisms that have <strong>evolved over hundreds of millions of years</strong> whereas the species level represents only a small subset of them that are <strong>much more closely related</strong>. Typically, names at the genus and species levels are written in <em>italics</em> or are <u>underlined</u> (in our tables, they are <em>italicised</em>). For instance, here is the list of taxonomic levels and names for humans and chimpanzees:"
}
_ADDENDUM.update(ENG._ADDENDUM)

_PORTAL = {
    'DOMESTIC_TEXT_1': "Shipping within the UK should be around £2.90, but we recommend taking the sample to the post office to get the proper postage. Getting the postage right on the first try is important since samples that spend a long time in transit will likely not produce the highest quality results.",
    'DOMESTIC_TEXT_3': media_locale['SHIPPING_ADDRESS'],
    'RESULTS_READY_TEXT_1': "One or more of the samples you submitted have been sequenced, and the results are now available online! Currently, we have only processed faecal samples, but we will be processing samples from other body sites soon.",
    'RESULTS_TEXT_2': "Sequencing and data analysis can take up to 4 months, please be patient! We will let you know as soon as your samples have been sequenced and analysed. Once your results are ready, we will send you an email notification.",
    'SAMPLE_STEPS_TEXT_5': "For a <strong>faecal sample</strong>, rub both cotton tips on a faecal specimen (a used piece of bathroom tissue). Collect a small amount of biomass. Maximum collection would be to saturate 1/2 a swab. <strong>More is not better!</strong> The ideal amount of biomass collected is shown below."
}
_PORTAL.update(ENG._PORTAL)

_CHANGE_PASS_VERIFY = ENG._CHANGE_PASS_VERIFY
_SURVEY_MAIN = ENG._SURVEY_MAIN
_HUMAN_SURVEY_COMPLETED = ENG._HUMAN_SURVEY_COMPLETED

# helper tuples for the survey questions
_NO_RESPONSE_CHOICE = ENG._NO_RESPONSE_CHOICE
_YES_NO_CHOICES = ENG._YES_NO_CHOICES
_YES_NO_NOTSURE_CHOICES = ENG._YES_NO_NOTSURE_CHOICES
_FREQUENCY_MONTH_CHOICES = ENG._FREQUENCY_MONTH_CHOICES
_FREQUENCY_WEEK_CHOICES = ENG._FREQUENCY_WEEK_CHOICES
_DIAGNOSIS_CHOICE = ENG._DIAGNOSIS_CHOICE
_ANIMAL_SURVEY = ENG._ANIMAL_SURVEY

_PERSONAL_MICROBIOME = ENG._PERSONAL_MICROBIOME

_NOJS = {
    'MESSAGE': 'You have JavaScript disabled, which this site requires in order to function properly. <br/>Please enable javascript and reload <a href="http://www.microbio.me/britishgut">http://www.microbio.me/britishgut</a>.',
    'NEED_HELP': 'If you need help enabling JavaScript in your browser, <br/>Please email us at <a href="mailto:britishgut@gmail.com">britishgut@gmail.com</a>'
}

text_locale = {
    '404.html': _404,
    '403.html': _403,
    'FAQ.html': _FAQ,
    'introduction.html': _INTRODUCTION,
    'new_participant_overview.html': _NEW_PARTICIPANT_OVERVIEW,
    'nojs.html': _NOJS,
    'personal_microbiome_overview.html': _PERSONAL_MICROBIOME,
    'addendum.html': _ADDENDUM,
    'portal.html': _PORTAL,
    'db_error.html': _DB_ERROR,
    'retrieve_kitid.html': _RETREIVE_KITID,
    'add_sample.html': _ADD_SAMPLE,
    'error.html': _ERROR,
    'forgot_password.html': _FORGOT_PASSWORD,
    'help_request.html': _HELP_REQUEST,
    'new_participant.html': _NEW_PARTICIPANT,
    'add_sample_overview.html': _ADD_SAMPLE_OVERVIEW,
    'participant_overview.html': _PARTICIPANT_OVERVIEW,
    'sample_overview.html': _SAMPLE_OVERVIEW,
    'basic_report.html': _BASIC_REPORT,
    'interactive_report.html': _INTERACTIVE_REPORT,
    'taxa_summary.html': _TAXA_SUMMARY,
    'map.html': _MAP,
    'register_user.html': _REGISTER_USER,
    'chage_pass_verify.html': _CHANGE_PASS_VERIFY,
    'survey_main.html': _SURVEY_MAIN,
    'animal_survey.html': _ANIMAL_SURVEY,
    'human_survey_completed.html': _HUMAN_SURVEY_COMPLETED,
    'handlers': _HANDLERS
}
