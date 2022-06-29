from microsetta_private_api.config_manager import SERVER_CONFIG


def gen_ffq_url(polyphenol_ffq_id, study, language_tag):
    language_tag = language_tag.lower()

    url = SERVER_CONFIG['polyphenol_ffq_url']
    url += f"?yid={polyphenol_ffq_id}"
    url += f"&country={language_tag}"
    url += f"&study={study}"

    return url
