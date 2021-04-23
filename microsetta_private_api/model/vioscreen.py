import pandas as pd
from microsetta_private_api.model.model_base import ModelBase


def normalize_timestamp(timestamp, timezone, normalize_to='US/Pacific'):
    """Normalize a timestamp to a specific timezone

    Vioscreen timezone information is not encoded directly within the
    timestamp, but separately.

    Parameters
    ----------
    timestamp : str
        The timestamp to normalize
    timezone : str
        The timezone information as provided by vioscreen
    normalize_to : str
        What timezone to normalize too, using Pandas timezone conventions

    Returns
    -------
    pd.Timestamp
        A normalized timestamp
    """
    timezone_lookup = {'Eastern Standard Time': 'US/Eastern',
                       'Central Standard Time': 'US/Central',
                       'Pacific Standard Time': 'US/Pacific'}

    if timezone not in timezone_lookup:
        raise KeyError(f"Unexpected timezone '{timezone}' observed")
    if timestamp is None:
        return None

    timestamp = pd.to_datetime(timestamp)
    timestamp_tz = timestamp.tz_localize(timezone_lookup[timezone])
    return timestamp_tz.tz_convert(normalize_to)


class VioscreenSession(ModelBase):
    def __init__(self, sessionId, username, protocolId, status, startDate,
                 endDate, cultureCode, created, modified):
        self.sessionId = sessionId
        self.username = username
        self.protocolId = protocolId
        self.status = status
        self.startDate = startDate
        self.endDate = endDate
        self.cultureCode = cultureCode
        self.created = created
        self.modified = modified

    @classmethod
    def from_vioscreen(cls, sessions_data, users_data):
        timeZone = users_data['timeZone']
        startDate = normalize_timestamp(sessions_data['startDate'], timeZone)
        endDate = normalize_timestamp(sessions_data['endDate'], timeZone)
        created = normalize_timestamp(sessions_data['created'], timeZone)
        modified = normalize_timestamp(sessions_data['modified'], timeZone)

        return cls(sessions_data['sessionId'], sessions_data['username'],
                   sessions_data['protocolId'], sessions_data['status'],
                   startDate, endDate, sessions_data['cultureCode'],
                   created, modified)


class VioscreenPercentEnergyComponent(ModelBase):
    def __init__(self, code, description, short_description, units, amount):
        self.code = code
        self.description = description
        self.short_description = short_description
        self.units = units
        self.amount = amount

    @classmethod
    def from_vioscreen(cls, component):
        return cls(component['code'], component['description'],
                   component['shortDescription'], component['units'],
                   component['amount'])


class VioscreenPercentEnergy(ModelBase):
    def __init__(self, sessionId, energy_components):
        self.sessionId = sessionId
        self.energy_components = energy_components

    @classmethod
    def from_vioscreen(cls, pe_data):
        sessionId = pe_data['sessionId']

        energy_components = [
            VioscreenPercentEnergyComponent.from_vioscreen(component)
            for component in pe_data['calculations']
        ]

        return cls(sessionId, energy_components)


class VioscreenComposite:
    def __init__(self, session, percent_energy):
        self.session = session
        self.percent_energy = percent_energy

        # make first class as the vioscreen username is our internal
        # survey identifier
        self.vio_id = session.username
