from settings import GOOGLE_REDIRECT


def get_google_id(enterprise):
    assert enterprise, "ENTERPRISE CANNOT BE NULL"
    assert enterprise.lower() in GOOGLE_REDIRECT.keys(), f"ENTERPRISE {enterprise} NOT FOUND"

    return GOOGLE_REDIRECT[enterprise.lower()]
