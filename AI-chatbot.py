def chatbot():
    print("🤖 AI Study Assistant (type 'exit' to stop)\n")
    
    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Goodbye! Keep learning 🚀")
            break

        elif "hello" in user:
            print("Bot: Hello! How can I help you?")
        
        elif "python" in user:
            print("Bot: Python is a programming language used for AI, web, and more.")
        
        elif "ai" in user:
            print("Bot: AI means Artificial Intelligence. It helps machines think and learn.")
        
        elif "exam" in user:
            print("Bot: Stay calm, revise basics, and practice problems!")
        
        else:
            print("Bot: Sorry, I don't understand. Try another question.")

chatbot()