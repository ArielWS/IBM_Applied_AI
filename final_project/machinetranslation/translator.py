"""This modul does things"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

#######translator.py


apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    """ This accepts text then pulls an APi request to translate it to French from English"""
    translation_response = language_translator.translate(
    text=englishText ,
    model_id='en-fr')
    translation = dict(translation_response.get_result())
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """ This accepts text then pulls an APi request to translate it fro Englis to French"""
    translation_response = language_translator.translate(
    text=frenchText ,
    model_id='fr-en')
    translation = dict(translation_response.get_result())
    englishText = translation['translations'][0]['translation']
    return englishText

#Ariel Spilkin code
