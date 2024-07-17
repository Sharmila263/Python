import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk,ImageFilter  # Importing Python Imaging Library (PIL)

# Generate a random number as the target
target_num = random.randint(1, 100)
attempts_left = 5  # Number of attempts allowed

# Function to check the user's guess
def check_guess():
    global attempts_left, target_num
    
    try:
        user_guess = int(user_entry.get())
        
        if user_guess < 1 or user_guess > 100:
            messagebox.showerror("Error", "Please enter a number between 1 and 100.")
            return
        
        if user_guess < target_num:
            message_label.config(text=f"Too Low. Attempts left: {attempts_left-1}")
        elif user_guess > target_num:
            message_label.config(text=f"Too High. Attempts left: {attempts_left-1}")
        else:
            message_label.config(text="Congratulations! You guessed the correct number.")
            new_game()
            return
        attempts_left -= 1
        user_entry.delete(0, tk.END)  # Clear the entry field
        
        if attempts_left == 0:
            message_label.config(text=f"Game over. The number was {target_num}.")
            new_game()
            return
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to start a new game
def new_game():
    global target_num, attempts_left
    target_num = random.randint(1, 100)
    attempts_left = 5
    messagebox.showinfo("New Game", "New game started! Guess a number between 1 and 100.")
    message_label.config(text=f"Guess a number between 1 to 100. Attempts left: {attempts_left}")
    user_entry.delete(0, tk.END)  # Clear the entry field

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.resizable(False, False)
root.title("Number Check Game")
try:
    bg_image = Image.open(r"C:\Users\sharm\Downloads\depositphotos_349999398-stock-photo-math-illustration-abstract-background-numbers.jpg")
    blurred_image = bg_image.filter(ImageFilter.BLUR)  # Apply blur filter
    bg_photo = ImageTk.PhotoImage(blurred_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ensure the image covers the entire window

except FileNotFoundError:
    print("Image file not found. Please check the file path.")
except OSError as e:
    print(f"Error opening image file: {e}")
label = tk.Label(root, text="Welcome to Number Check Game!!", font=("Arial", 16), bg="white")
label.pack(pady=10)

# Label for instruction
instruction = tk.Label(root, text="Guess a number between 1 to 100", font=("Arial", 10), bg="white")
instruction.pack(pady=5)

# Label and Entry for user input
user_input_label = tk.Label(root, text="Enter the number", font=("Arial", 10), bg="white")
user_input_label.pack(pady=5)

user_entry = tk.Entry(root, width=15)
user_entry.pack(pady=5)

# Label for displaying messages
message_label = tk.Label(root, text=f"Guess a number between 1 to 100. Attempts left: {attempts_left}", font=("Arial", 12), fg="blue", bg="white")
message_label.pack(pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=check_guess)
submit_button.pack(pady=5)

# Start the main loop
root.mainloop()
