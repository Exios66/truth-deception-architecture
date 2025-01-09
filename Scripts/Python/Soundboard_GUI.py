import os
import time
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox
import sounddevice as sd
import soundfile as sf
from playsound import playsound


class SoundboardApp:
    def __init__(self, root, original_audio, delay_minutes):
        self.root = root
        self.root.title("Modern Soundboard with Timer")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.original_audio = original_audio
        self.delay_seconds = delay_minutes * 60
        self.time_remaining = self.delay_seconds
        self.countdown_running = True

        # Header
        self.header = ctk.CTkLabel(root, text="Soundboard & Timer", font=("Helvetica", 28, "bold"))
        self.header.pack(pady=20)

        # Timer Label
        self.timer_label = ctk.CTkLabel(root, text="Time Remaining: --:--", font=("Helvetica", 18))
        self.timer_label.pack(pady=10)

        # Soundboard Buttons Frame
        self.buttons_frame = ctk.CTkFrame(root)
        self.buttons_frame.pack(pady=20, padx=10)

        # Add default sound buttons
        self.default_sounds = {
            "Sound 1": "path_to_sound1.wav",
            "Sound 2": "path_to_sound2.wav",
            "Sound 3": "path_to_sound3.wav"
        }
        for name, path in self.default_sounds.items():
            btn = ctk.CTkButton(self.buttons_frame, text=name, command=lambda p=path: self.play_sound(p), width=150)
            btn.pack(side="left", padx=10, pady=10)

        # Add custom sound button
        self.add_custom_sound_button = ctk.CTkButton(
            self.root, text="Add Custom Sound", command=self.add_custom_sound, width=200
        )
        self.add_custom_sound_button.pack(pady=10)

        # Start original sound countdown
        threading.Thread(target=self.delayed_sound, daemon=True).start()

        # Start countdown timer
        self.update_timer()

    def play_sound(self, file_path):
        """Play a sound file."""
        try:
            if not os.path.exists(file_path):
                messagebox.showerror("Error", f"File not found: {file_path}")
                return

            data, samplerate = sf.read(file_path)
            sd.play(data, samplerate)
            sd.wait()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to play sound: {e}")

    def add_custom_sound(self):
        """Add a custom sound using file dialog."""
        file_path = filedialog.askopenfilename(
            title="Select a Sound File",
            filetypes=(("Audio Files", "*.wav *.mp3 *.flac"), ("All Files", "*.*"))
        )
        if file_path:
            name = os.path.basename(file_path)
            btn = ctk.CTkButton(self.buttons_frame, text=name, command=lambda: self.play_sound(file_path), width=150)
            btn.pack(side="left", padx=10, pady=10)

    def delayed_sound(self):
        """Play the original sound after the delay."""
        time.sleep(self.delay_seconds)
        self.play_sound(self.original_audio)

    def update_timer(self):
        """Update the countdown timer."""
        if self.time_remaining > 0 and self.countdown_running:
            mins, secs = divmod(self.time_remaining, 60)
            self.timer_label.configure(text=f"Time Remaining: {mins:02}:{secs:02}")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_remaining <= 0:
            self.timer_label.configure(text="Time Remaining: 00:00")
            self.countdown_running = False


def main():
    # Original sound settings
    original_audio = "path_to_original_sound.wav"  # Replace with your original sound file
    delay_minutes = 10  # Delay before the original sound plays

    # Check if the original sound file exists
    if not os.path.exists(original_audio):
        print(f"Error: The file '{original_audio}' does not exist.")
        return

    # Initialize GUI
    ctk.set_appearance_mode("dark")  # Options: "light", "dark", or "system"
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = SoundboardApp(root, original_audio, delay_minutes)
    root.mainloop()


if __name__ == "__main__":
    main()