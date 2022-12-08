import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = '2018-05-01'

# creating instance of the IBM Watson Language translator
authenticator = IAMAuthenticator(apikey=apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

# creating a function to translate from English to French
def englishToFrench(englishText):
    #write the code here
    translation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

# creating a function to translate from French to English
def frenchToEnglish(frenchText):
    #write the code here
    translation = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
