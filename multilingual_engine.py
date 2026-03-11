from hf_client import query_hf_model
from langdetect import detect


TRANSLATION_MODELS = {
    "hi": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-en-hi",
    "fr": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-en-fr",
    "es": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-en-es",
    "de": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-en-de",
    "bn": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-en-bn"
}

REVERSE_MODELS = {
    "hi": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-hi-en",
    "fr": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-fr-en",
    "es": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-es-en",
    "de": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-de-en",
    "bn": "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-bn-en"
}


def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"


def translate_to_english(text, source_lang):

    if source_lang == "en":
        return text

    if source_lang not in REVERSE_MODELS:
        return text

    api_url = REVERSE_MODELS[source_lang]

    result = query_hf_model(api_url, {"inputs": text})

    return result[0].get("translation_text", text)


def translate_from_english(text, target_lang):

    if target_lang == "en":
        return text

    if target_lang not in TRANSLATION_MODELS:
        return text

    api_url = TRANSLATION_MODELS[target_lang]

    result = query_hf_model(api_url, {"inputs": text})

    return result[0].get("translation_text", text)


def multilingual_pipeline(user_input, llm_function):

    lang = detect_language(user_input)

    english_input = translate_to_english(user_input, lang)

    english_response = llm_function(english_input)

    final_response = translate_from_english(english_response, lang)

    return final_response