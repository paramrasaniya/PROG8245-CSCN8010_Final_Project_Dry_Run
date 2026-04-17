import sys
from pathlib import Path
import traceback
import gradio as gr

SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from predict import answer_question, transcribe_audio, generate_audio

def format_history(history):
    if not history:
        return "No conversation yet."
    return "\n\n".join(history)

def ask_bot(history, text_question, audio_question, answer_language, spoken_language):
    try:
        if history is None:
            history = []
        source_note = "Using typed question."
        question = (text_question or "").strip()
        if not question and audio_question is not None:
            question, source_note = transcribe_audio(audio_question, spoken_language)
        if not question:
            return history, format_history(history), "Please type a question or record audio.", source_note, None, ""
        detected_topic, answer = answer_question(question, answer_language)
        history = list(history)
        history.append(f"User: {question}")
        history.append(f"Bot: {answer}")
        audio_path = generate_audio(answer, answer_language)
        info = f"{source_note}\nDetected topic: {detected_topic}"
        return history, format_history(history), answer, info, audio_path, ""
    except Exception as e:
        error_text = f"App error: {e}\n\n{traceback.format_exc()}"
        return history if history else [], format_history(history if history else []), "Something went wrong.", error_text, None, ""

def clear_all():
    return [], "No conversation yet.", "", "", None, ""

with gr.Blocks(title="AI/ML Concept Tutor Chatbot") as demo:
    gr.Markdown("""
    # AI/ML Concept Tutor Chatbot

    This proof-of-concept chatbot supports:
    - text questions
    - audio questions
    - multilingual answers
    - audio answers

    Demo topics:
    regression, classification, overfitting, normalization, confusion matrix, precision and recall, decision tree, clustering, neural network, gradient descent
    """)

    history_state = gr.State([])
    with gr.Row():
        text_question = gr.Textbox(label="Type your question", placeholder="Example: What is regression?")
        audio_question = gr.Audio(sources=["microphone", "upload"], type="filepath", label="Ask with audio")
    with gr.Row():
        answer_language = gr.Dropdown(["English", "Spanish", "French", "Hindi", "Gujarati"], value="English", label="Answer language")
        spoken_language = gr.Dropdown(["English", "Spanish", "French", "Hindi", "Gujarati"], value="English", label="Spoken question language")
    ask_button = gr.Button("Ask the chatbot")
    clear_button = gr.Button("Clear chat")
    conversation_box = gr.Textbox(label="Conversation", lines=14, value="No conversation yet.")
    latest_answer = gr.Textbox(label="Latest text answer", lines=4)
    info_box = gr.Textbox(label="Detected topic / transcription info", lines=4)
    answer_audio = gr.Audio(label="Answer as audio", type="filepath")

    ask_button.click(
        fn=ask_bot,
        inputs=[history_state, text_question, audio_question, answer_language, spoken_language],
        outputs=[history_state, conversation_box, latest_answer, info_box, answer_audio, text_question]
    )
    clear_button.click(
        fn=clear_all,
        inputs=[],
        outputs=[history_state, conversation_box, latest_answer, info_box, answer_audio, text_question]
    )

if __name__ == "__main__":
    demo.launch()
