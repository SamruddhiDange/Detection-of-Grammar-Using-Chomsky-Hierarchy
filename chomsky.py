Java File:

import tkinter as tk
from tkinter import messagebox
import webbrowser

def open_project_page():
    # Replace this with your actual file path or URL
    webbrowser.open('file:///D:/templates/chomsky.html')

# Main window setup
root = tk.Tk()
root.title("Computer Science Department")
root.geometry("800x500")
root.configure(bg='#b3e6ff')  # Light blue background

# Header section
header = tk.Label(root, text="Computer Science Department", font=("Helvetica", 16, "bold"), bg='#000000', fg='white')
header.pack(fill=tk.X)

# Welcome section
welcome_frame = tk.Frame(root, bg="#b3e6ff", pady=40)
welcome_frame.pack(fill=tk.BOTH, expand=True)

name_label = tk.Label(welcome_frame, text="Samruddhi Shrikant Dange Roll no:22", font=("Arial", 18, "bold"), bg="#b3e6ff")
name_label.pack(pady=10)

subtext_label = tk.Label(welcome_frame, text="Welcomes You", font=("Arial", 14), bg="#b3e6ff")
subtext_label.pack()

info_label = tk.Label(welcome_frame, text="To know more about my Mini Project click on below link", font=("Arial", 12), bg="#b3e6ff")
info_label.pack(pady=10)

explore_btn = tk.Button(welcome_frame, text="Explore Now", command=open_project_page, bg="#333333", fg="white", padx=20, pady=10)
explore_btn.pack()

root.mainloop()

HTML File:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chomsky Grammar Type Checker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #e0f7fa;
            text-align: center;
            padding: 40px;
        }
        textarea {
            width: 60%;
            height: 150px;
            margin-bottom: 20px;
            font-family: monospace;
        }
        button {
            padding: 10px 20px;
            background-color: #00796b;
            color: white;
            border: none;
            cursor: pointer;
        }
        #result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>Chomsky Grammar Type Checker</h1>
    <p>Enter your grammar rules (e.g., S -> aSb | ε):</p>

    <textarea id="grammarInput" placeholder="Example:&#10;S -> aS | b&#10;S -> ε"></textarea><br>
    <button onclick="checkGrammar()">Check Grammar Type</button>

    <div id="result"></div>

    <script>
        function checkGrammar() {
            const input = document.getElementById("grammarInput").value.trim();
            const rules = input.split("\n").map(rule => rule.trim());
            let type = 3; // Start assuming it's regular (Type 3)

            for (let rule of rules) {
                if (!rule.includes("->")) continue;

                const [lhs, rhs] = rule.split("->").map(s => s.trim());

                // Check for Type 3 (Regular)
                const type3Regex = /^[A-Z]\s*->\s*([a-zε]|[a-z][A-Z]|ε)$/;

                if (!type3Regex.test(rule)) {
                    type = Math.min(type, 2); // Not regular, maybe context-free
                }

                // Check for Type 2 (Context-Free): Single non-terminal on LHS
                if (!/^[A-Z]$/.test(lhs)) {
                    type = Math.min(type, 1); // Not context-free
                }

                // Check for Type 1 (Context-Sensitive): LHS <= RHS in length
                if (lhs.length > rhs.length) {
                    type = 0; // Not context-sensitive
                }
            }

            let result = "";
            switch (type) {
                case 3: result = "Type 3: Regular Grammar"; break;
                case 2: result = "Type 2: Context-Free Grammar"; break;
                case 1: result = "Type 1: Context-Sensitive Grammar"; break;
                case 0: result = "Type 0: Unrestricted Grammar"; break;
            }

            document.getElementById("result").innerText = result;
        }
    </script>

</body>
</html>

