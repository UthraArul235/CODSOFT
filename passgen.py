import tkinter as tk
import random
import string

def generate_password():
    
    # Get the length entered by the user
    
    user_input = length_entry.get()
    
    try:
        password_length = int(user_input)
        
        if password_length <= 0:
            result_label.config(text="Please enter a positive number!")
            return
        
    except ValueError:
        result_label.config(text="Invalid input! Enter a number.")
        return

    # Pool of characters for the password
    
    available_chars = (string.ascii_letters +string.digits +string.punctuation)

    # Create password using random choices
    
    generated_password = "".join(random.choice(available_chars)
                                 for _ in range(password_length))

    # Display it in the GUI
    
    result_label.config(text=f"Generated Password: {generated_password}")

root = tk.Tk()
root.title("Password Generator")
root.geometry("420x260")
root.configure(bg="lightblue")

# Title heading

title_label = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title_label.pack(pady=12)

# Input area for password length

length_label = tk.Label(
    root,
    text="Enter Password Length:",
    font=("Arial", 12),
    bg="lightblue"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=12
)
length_entry.pack(pady=6)

# Button to trigger generation

generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 13, "bold"),
    command=generate_password
)
generate_button.pack(pady=12)

# Result display label

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="lightblue",
    wraplength=380
)
result_label.pack(pady=10)
root.mainloop()
