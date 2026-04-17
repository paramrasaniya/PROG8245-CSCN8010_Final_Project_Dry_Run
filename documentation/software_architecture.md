# Software Architecture

## Project idea
We created an AI/ML Concept Tutor Chatbot for students who want simple explanations of common machine learning topics.

## Main modules
- **data/** stores the concept knowledge base
- **src/data_processing.py** loads the concept data
- **src/predict.py** detects the topic and prepares the answer
- **src/train.py** explains our dry run training placeholder
- **src/evaluate.py** runs a few sample evaluation cases
- **app.py** provides the Gradio webpage

## Flow
1. User enters a typed question or audio question
2. The app reads the question
3. The predict module detects the topic
4. The chatbot returns the answer in the selected language
5. The app optionally generates spoken output

## Why this structure is good
- It is organized and easy to explain
- It separates frontend and backend logic
- It is easy to extend later with a real model or retrieval system
