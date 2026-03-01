from transformers import pipeline

translator = pipeline(
    task="translation",
    model="Helsinki-NLP/opus-mt-en-hi"
)

print(translator("Hello my friend"))