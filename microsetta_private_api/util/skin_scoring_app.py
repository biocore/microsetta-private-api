from microsetta_private_api.config_manager import SERVER_CONFIG


def gen_url(skin_scoring_app_id, language_tag):
    language_tag = language_tag.lower()

    url = SERVER_CONFIG['skin_scoring_app_url']
    url += f"?yid={skin_scoring_app_id}"
    url += f"&country={language_tag}"

    return url
