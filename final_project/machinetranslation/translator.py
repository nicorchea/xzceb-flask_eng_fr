
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)


language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(englishText):
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)
    translation_response = language_translator.translate(
        text=englishText,
        source='en',
        target='fr'
    ).get_result()
    frenchText = translation_response['translations'][0]['translation']
    return frenchText

def french_to_english(frenchText):
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)
    translation_response = language_translator.translate(
    text=frenchText,
    source='fr',
    target='en'
    ).get_result()
    frenchText = translation_response['translations'][0]['translation']
    return frenchText
    