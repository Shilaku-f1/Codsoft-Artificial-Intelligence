import tkinter as tk
from tkinter import scrolledtext, filedialog
import random
import re

# Step 1: Define the chatbot response function
def get_response(user_input):
    if re.search(r"\bhi\b|\bhello\b", user_input):
        return "Hi there! How can I assist you today?"
    elif re.search(r"\bhow are you\b", user_input):
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    elif re.search(r"\bweather\b", user_input):
        return "The weather is always nice in the digital world! ☀️"
    elif re.search(r"\bhelp\b", user_input):
        return "Sure, I'm here to help! What do you need assistance with?"
    elif re.search(r"\bwhat\b.*\b(name|your name)\b", user_input):
        return "I'm your friendly chatbot, here to assist you!"
    elif re.search(r"\bthank you\b|\bthanks\b", user_input):
        return "You're welcome! Let me know if there's anything else you need."
    elif re.search(r"\bwhat can you do\b|\btell me about yourself\b", user_input):
        return "I can answer your questions, provide information, or just chat with you! Ask me anything."
    else:
        fallback_responses = [
            "I'm not sure I understand. Can you explain?",
            "Hmm, that's interesting! Can you give me more details?",
            "I don't quite get that. Could you try rephrasing?",
            "Sorry, I didn't catch that. What do you mean?"
        ]
        return random.choice(fallback_responses)

# Step 2: Function to handle sending a message
def send_message():
    user_input = input_box.get().strip().lower()
    if user_input == "":
        chat_display.insert(tk.END, "You: (No input provided)\n")
        chat_display.insert(tk.END, "Chatbot: Please type something so I can assist you!\n\n")
        return
    
    chat_display.insert(tk.END, f"You: {user_input}\n")
    input_box.delete(0, tk.END)
    
    if user_input == "bye":
        chat_display.insert(tk.END, "Chatbot: Goodbye! Have a great day!\n\n")
        root.destroy()
    else:
        response = get_response(user_input)
        chat_display.insert(tk.END, f"Chatbot: {response}\n\n")

# Step 3: Function to clear chat
def clear_chat():
    chat_display.delete(1.0, tk.END)

# Step 4: Function to save chat history
def save_chat():
    chat_history = chat_display.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(chat_history)

# Step 5: Create the GUI window
root = tk.Tk()
root.title("Advanced Chatbot")
root.geometry("500x600")
root.resizable(False, False)

# Step 6: Chat display area with scrolling
chat_display = scrolledtext.ScrolledText(root, bg="white", fg="black", font=("Arial", 12), wrap=tk.WORD)
chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
chat_display.insert(tk.END, "Chatbot: Hello! I am your friendly chatbot. Type 'bye' to exit.\n\n")

# Step 7: Entry box for user input
input_box = tk.Entry(root, font=("Arial", 12))
input_box.pack(pady=5, padx=10, fill=tk.X)

# Step 8: Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

send_button = tk.Button(button_frame, text="Send", font=("Arial", 12), bg="blue", fg="white", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), bg="orange", fg="white", command=clear_chat)
clear_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save", font=("Arial", 12), bg="green", fg="white", command=save_chat)
save_button.pack(side=tk.LEFT, padx=5)

# Run the GUI loop
root.mainloop()
