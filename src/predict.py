import tempfile
from data_processing import load_knowledge_base

try:
    import speech_recognition as sr
except Exception:
    sr = None

try:
    from gtts import gTTS
except Exception:
    gTTS = None

LANG_MAP = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "Gujarati": "gu",
}

SPEECH_LANG = {
    "English": "en-US",
    "Spanish": "es-ES",
    "French": "fr-FR",
    "Hindi": "hi-IN",
    "Gujarati": "gu-IN",
}

def detect_topic(question: str):
    if not question:
        return None
    text_lower = question.lower()
    data = load_knowledge_base()
    best_match = None
    best_length = -1
    for item in data["topics"]:
        if item["topic"] in text_lower and len(item["topic"]) > best_length:
            best_match = item
            best_length = len(item["topic"])
        for keyword in item["keywords"]:
            if keyword.lower() in text_lower and len(keyword) > best_length:
                best_match = item
                best_length = len(keyword)
    return best_match

def answer_question(question: str, answer_language: str = "English"):
    lang = LANG_MAP.get(answer_language, "en")
    item = detect_topic(question)
    if item:
        topic = item["topic"]
        answer = item["answers"].get(lang, item["answers"]["en"])
        return topic, answer
    fallback = {
        "en": "We could not match that exact topic. Please ask about regression, classification, overfitting, normalization, confusion matrix, precision and recall, decision tree, clustering, neural network, or gradient descent.",
        "es": "No pudimos identificar ese tema exacto. Por favor pregunte sobre regresión, clasificación, overfitting, normalización, matriz de confusión, precisión y recall, árbol de decisión, clustering, red neuronal o gradient descent.",
        "fr": "Nous n'avons pas pu identifier ce sujet exact. Veuillez poser une question sur la régression, la classification, le surapprentissage, la normalisation, la matrice de confusion, la précision et le rappel, l'arbre de décision, le clustering, le réseau de neurones ou la descente de gradient.",
        "hi": "Hum us exact topic ko match nahi kar paaye. Kripya regression, classification, overfitting, normalization, confusion matrix, precision and recall, decision tree, clustering, neural network, ya gradient descent par sawaal poochhiye.",
        "gu": "અમે આ exact topic ઓળખી શક્યા નથી. કૃપા કરીને regression, classification, overfitting, normalization, confusion matrix, precision and recall, decision tree, clustering, neural network, અથવા gradient descent વિશે પૂછો."
    }
    return "not found", fallback.get(lang, fallback["en"])

def transcribe_audio(audio_path, spoken_language="English"):
    if audio_path is None:
        return None, "No audio provided."
    if sr is None:
        return None, "SpeechRecognition is not installed."
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language=SPEECH_LANG.get(spoken_language, "en-US"))
        return text, f"Transcribed speech: {text}"
    except Exception as e:
        return None, f"Audio transcription failed: {e}"

def generate_audio(answer_text, answer_language="English"):
    if not answer_text or gTTS is None:
        return None
    try:
        lang = LANG_MAP.get(answer_language, "en")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            output_path = temp_file.name
        gTTS(text=answer_text, lang=lang).save(output_path)
        return output_path
    except Exception:
        return None

if __name__ == "__main__":
    demo_question = "What is regression?"
    topic, answer = answer_question(demo_question, "English")
    print("Detected topic:", topic)
    print("Answer:", answer)
