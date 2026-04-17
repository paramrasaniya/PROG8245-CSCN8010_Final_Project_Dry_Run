from data_processing import load_knowledge_base

def train_placeholder():
    data = load_knowledge_base()
    print("Dry run note: this project uses a rule-based knowledge base instead of training a large model.")
    print(f"We prepared {len(data['topics'])} AI/ML concepts for the chatbot.")

if __name__ == "__main__":
    train_placeholder()
