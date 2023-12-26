import tkinter as tk
from tkinter import scrolledtext
import openai
from openai import OpenAI
import Api #ther is a file name Api.py which have variable name Apikey and I have stored my apikey in this variable
def get_bot_response(user_input):
    client = OpenAI(api_key=Api.Apikey)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": user_input
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    bot_response=response.choices[0].message.content
    return bot_response

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")

        self.chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=15)
        self.chat_history.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.user_input = tk.Entry(root, width=30)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.destroy)
        self.quit_button.grid(row=1, column=2, padx=10, pady=10)

    def send_message(self):
        user_input = self.user_input.get().lower()
        self.chat_history.insert(tk.END, "You: " + user_input + "\n")

        response = get_bot_response(user_input)
        self.chat_history.insert(tk.END, "ChatBot: " + response + "\n")

        self.user_input.delete(0, tk.END)  # Clear the user input field

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()
