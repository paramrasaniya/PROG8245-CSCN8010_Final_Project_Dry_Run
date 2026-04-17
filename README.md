# AI/ML Concept Tutor Chatbot

This is our dry run final project for **PROG8245 - Machine Learning Programming**.
We built a simple **AI/ML Concept Tutor Chatbot** that supports:

- text-based questions
- audio-based questions
- multilingual answers
- spoken audio answers
- a webpage interface using Gradio

## Project structure

```text
your_project/
├── data/
├── models/
├── notebooks/
├── documentation/
├── src/
│   ├── data_processing.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── app.py
├── README.md
└── requirements.txt
```

## How to run

### 1. Create and activate virtual environment
On Windows PowerShell:
```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install libraries
```powershell
pip install -r requirements.txt
```

### 3. Run the Gradio webpage
```powershell
python app.py
```

Then open the local URL shown in the terminal.

## How our chatbot works
- We stored AI/ML concept explanations in `data/concept_knowledge.json`.
- We detect the topic from the user question using simple keyword matching.
- We return the answer in the selected language.
- If possible, we also create an audio answer using gTTS.
- If the user gives an audio question, we try to transcribe it using SpeechRecognition.

## Demo questions
- What is regression?
- Explain overfitting.
- What is a neural network?
- What is confusion matrix?
- Explain precision and recall.

## Notes
- Text input is the safest option for live demo.
- Audio transcription depends on local microphone settings and online speech services.
- This dry run focuses on clarity, structure, and proof of concept.

## Team Members:

1) - Name: Param Rasaniya
   - Student ID: 9086095

2) - Name: Viraj Mistry
   - Student ID: 9088985