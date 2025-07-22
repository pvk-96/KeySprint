import tkinter as tk
import random
import time
from tkinter import messagebox

# ---------------------- Text Passages ----------------------
passages = {
    "Easy": [
        "the sun sets over the ocean",
        "this is a simple typing test",
        "learning python is fun and easy",
        "we love creating projects with code",
        "typing helps you improve your speed"
            "the sun is shining bright",
        "we enjoy playing outside daily",
        "typing helps improve brain power",
        "reading books makes us smarter",
        "she likes apples and bananas",
        "python is fun to learn",
        "school starts early in the morning",
        "dogs are loyal and friendly pets",
        "we are learning new skills",
        "coding is cool and creative"
    ],
    "Hard": [
        "Typing speed is a critical skill in many modern-day professions and educational settings.",
        "The quick, consistent rhythm of your fingers on the keyboard improves not just speed, but accuracy too.",
        "One must maintain concentration, posture, and finger placement to achieve high performance while typing."
         "Although technology continues to evolve rapidly, human adaptability remains unparalleled.",
        "The quick, brown fox jumps over the lazy dog while the sun sets in the distance.",
        "Typing accurately is as important as typing fast, especially in professional environments.",
        "From artificial intelligence to quantum computing, today's innovations are reshaping the world.",
        "Success often depends on consistency, discipline, and a deep understanding of fundamentals.",
        "When faced with uncertainty, the best approach is to stay calm and analyze the situation.",
        "Grammar, punctuation, and sentence structure all play crucial roles in clear communication.",
        "Efficient typing habits can significantly enhance productivity and digital fluency.",
        "The university hosted a seminar on the ethical implications of emerging technologies.",
        "As clouds gathered above, the wind whispered secrets of the coming storm."
    ]
}

timers = {"Easy": 35, "Hard": 60}
# ---------------------- GUI Setup ----------------------
class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x450")
        self.root.configure(bg="#121212")  # Dark mode

        self.text = ""
        self.start_time = 0
        self.level = tk.StringVar(value="Easy")

        tk.Label(root, text="Typing Speed Test", fg="white", bg="#121212",
                 font=("Helvetica", 18, "bold")).pack(pady=10)

        self.dropdown = tk.OptionMenu(root, self.level, *passages.keys())
        self.dropdown.config(bg="#1f1f1f", fg="white")
        self.dropdown.pack(pady=5)

        self.display = tk.Label(root, text="", wraplength=600, fg="#ffffff",
                                bg="#1e1e1e", font=("Courier", 14), pady=10, padx=10)
        self.display.pack(pady=10)

        self.entry = tk.Text(root, height=5, width=70, font=("Courier", 12), wrap="word")
        self.entry.pack(pady=10)
        self.entry.config(state="disabled")
        self.entry.bind("<KeyRelease>", self.check_typing)

        self.start_btn = tk.Button(root, text="Start", command=self.start_test,
                                   bg="#333333", fg="white", font=("Helvetica", 12))
        self.start_btn.pack(pady=5)

        self.submit_btn = tk.Button(root, text="Submit", command=self.calculate_speed,
                                    bg="#444444", fg="white", font=("Helvetica", 12))
        self.submit_btn.pack(pady=5)
        self.submit_btn.config(state="disabled")

    def start_test(self):
        self.text = random.choice(passages[self.level.get()])
        self.display.config(text=self.text)
        self.entry.config(state="normal")
        self.entry.delete("1.0", tk.END)
        self.entry.focus()
        self.start_time = time.time()
        self.submit_btn.config(state="normal")

        # Disable input after set time
        duration = timers[self.level.get()]
        self.root.after(duration * 1000, self.auto_submit)

    def auto_submit(self):
        if self.entry.cget("state") == "normal":
            self.calculate_speed()

    def calculate_speed(self):
        self.entry.config(state="disabled")
        self.submit_btn.config(state="disabled")
        typed = self.entry.get("1.0", tk.END).strip()
        elapsed = time.time() - self.start_time

        word_count = len(typed.split())
        wpm = (word_count / elapsed) * 60

        accuracy = self.calculate_accuracy(typed, self.text)

        messagebox.showinfo("Result", f"Speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%")

    def calculate_accuracy(self, typed, reference):
        typed_words = typed.split()
        reference_words = reference.split()
        correct = sum(t1 == t2 for t1, t2 in zip(typed_words, reference_words))
        return (correct / len(reference_words)) * 100 if reference_words else 0

    def check_typing(self, event):
        typed = self.entry.get("1.0", tk.END).strip()
        reference = self.text
        self.entry.tag_remove("mistake", "1.0", tk.END)

        for i, (typed_char, ref_char) in enumerate(zip(typed, reference)):
            if typed_char != ref_char:
                idx = f"1.0 + {i} chars"
                self.entry.tag_add("mistake", idx, f"{idx} +1c")

        self.entry.tag_config("mistake", foreground="red")


# ---------------------- Main ----------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()
