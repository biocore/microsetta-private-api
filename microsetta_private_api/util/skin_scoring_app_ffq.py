from microsetta_private_api.config_manager import SERVER_CONFIG


def gen_ffq_url(skin_scoring_app_ffq_id, study, language_tag):
    language_tag = language_tag.lower()

    url = SERVER_CONFIG['skin_scoring_app_ffq_url']
    url += f"?yid={skin_scoring_app_ffq_id}"
    url += f"&country={language_tag}"
    url += f"&study={study}"

    return url
