from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Load data from a file
def load_data():
    data = {}
    try:
        # Corrected path
        with open(r"F:\aptitude\docs\apti.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                question = lines[i].strip()
                answer = lines[i + 1].strip()
                data[question.lower()] = answer
    except FileNotFoundError:
        print("Error: The file 'apti.txt' was not found. Please check the file path.")
        exit()
    except IndexError:
        print("Error: The file format is incorrect. Make sure questions and answers alternate in the file.")
        exit()
    return data

# Function to get the best-matching answer for the user's question
def get_answer(question, data):
    question = question.lower()

    # Use fuzzy matching to find the best match
    best_match = process.extractOne(question, data.keys(), scorer=fuzz.partial_ratio)

    # Debugging information
    print(f"User Question: {question}")
    print(f"Best Match: {best_match}")
    
    if best_match and best_match[1] > 50:  # Threshold set to 50 for better matching
        return data[best_match[0]]  # Return the matched answer
    else:
        return "Sorry, I don't have an answer for that question.\nPlease check your input."

# Main chatbot function
def chatbot():
    data = load_data()
    print("Welcome to the Aptitude Quiz Chatbot!")
    print("Ask any question about aptitude topics or type 'exit' to quit.")

    while True:
        user_question = input("\nYour Question: ")

        # Exit condition
        if user_question.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break

        # Fetch and print the answer
        answer = get_answer(user_question, data)
        print("\nAnswer:")
        print(answer)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
