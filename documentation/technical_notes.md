# Technical Notes

## Current approach
This dry run uses a lightweight rule-based approach instead of a trained large language model. That makes the project stable and easier to demonstrate in class.

## Libraries used
- **gradio** for the webpage
- **SpeechRecognition** for audio-to-text
- **gTTS** for text-to-speech

## Limitation
- The chatbot currently answers only the prepared AI/ML topics
- Audio transcription may fail if the microphone setup is blocked
- gTTS may need internet access to generate audio

## Future improvements
- Add more AI/ML topics
- Connect to a vector database or document retrieval system
- Add conversation memory
- Improve topic detection with embeddings or an LLM
