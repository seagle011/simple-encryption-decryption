import tkinter as tk


root = tk.Tk()
root.title("Encryption and Decryption")
root.configure(bg="#F8F8F8")

# 1st Text area
plaintext_label = tk.Label(root, text="Decrypted:", font=("Arial", 14), bg="#F8F8F8")
plaintext_label.grid(row=0, column=0, padx=5, pady=5)
plaintext_entry = tk.Text(root, height=5, width=30, font=("Arial", 12))
plaintext_entry.grid(row=1, column=0, padx=5, pady=5)

# 2nd text area
ciphertext_label = tk.Label(root, text="Encrypted:", font=("Arial", 14), bg="#F8F8F8")
ciphertext_label.grid(row=0, column=1, padx=5, pady=5)
ciphertext_entry = tk.Text(root, height=5, width=30, font=("Arial", 12))
ciphertext_entry.grid(row=1, column=1, padx=5, pady=5)


m = 26 #The number of letters in desired language (English is chosen)
k = 3  #The key (can be changed as desired)

#The encryption process
def encrypt():
    plaintext = plaintext_entry.get("1.0", "end-1c") #Acquires plaintext from the 1st text area
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            p = ord(char.lower()) - ord('a')
            c = (p + k) % m
            ciphertext += chr(c + ord('a'))
        else:
            ciphertext += char
    ciphertext_entry.delete("1.0", "end") # Clear the second text area
    ciphertext_entry.insert("1.0", ciphertext) # Display the ciphertext in the second text area

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, font=("Arial", 12), bg="#4CAF50", fg="#FFFFFF", padx=10, pady=5)
encrypt_button.grid(row=2, column=0, padx=5, pady=10)
#Decryption

def decrypt():
    ciphertext = ciphertext_entry.get("1.0", "end-1c") #Acquires ciphertext from the 2nd text area
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            c = ord(char.lower()) - ord('a')
            p = (c - k) % m
            plaintext += chr(p + ord('a'))
        else:
            plaintext += char
    plaintext_entry.delete("1.0", "end") # Clear the first text area
    plaintext_entry.insert("1.0", plaintext) # Display the plaintext in the first text area

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, font=("Arial", 12), bg="#F44336", fg="#FFFFFF", padx=10, pady=5)
decrypt_button.grid(row=2, column=1, padx=5, pady=10)

#Text area labels
plaintext_label.config(text="Decrypted")
ciphertext_label.config(text="Encrypted")

#padding
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the GUI
root.mainloop()