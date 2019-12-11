#!/usr/bin/env python
from __future__ import division

# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The American Gut Project Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------


available_locales = set([
    'american_gut', 'british_gut'])


media_locale = {
    'SURVEY_VIOSCREEN_URL': 'https://demo.vioscreen.com/%(survey_id)s',  # THIS IS CURRENTLY MOCKED OUT
    'SURVEY_ASD_URL': 'https://docs.google.com/forms/d/1ZlaQzENj7NA7TcdfFhXfW0jshrToTywAarV0fjTZQxc/viewform?entry.1089722816=%(survey_id)s&entry.1116725993&entry.1983725631&entry.2036966278&entry.1785627282&entry.1461731626&entry.1203990558&entry.843049551&entry.476318397&entry.383297943&entry.228366248&entry.1651855735&entry.1234457826&entry.1079752165'
}
