from predict import answer_question

TEST_CASES = [
    ("What is regression?", "regression"),
    ("Can you explain overfitting?", "overfitting"),
    ("Tell us about neural network", "neural network"),
    ("What is confusion matrix?", "confusion matrix"),
]

def evaluate_demo():
    correct = 0
    for question, expected_topic in TEST_CASES:
        predicted_topic, answer = answer_question(question, "English")
        is_correct = predicted_topic == expected_topic
        correct += int(is_correct)
        print("-" * 60)
        print("Question:", question)
        print("Expected topic:", expected_topic)
        print("Predicted topic:", predicted_topic)
        print("Correct:", is_correct)
        print("Answer:", answer)
    accuracy = correct / len(TEST_CASES)
    print("-" * 60)
    print(f"Demo topic matching accuracy: {accuracy:.2%}")

if __name__ == "__main__":
    evaluate_demo()
