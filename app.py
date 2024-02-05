import customtkinter
import sys
import platform
from threading import *
import feedback
import whisper_api
import output
import timecode

app_version = 'v 1.3.0'

def browse_files():
    filename = customtkinter.filedialog.askopenfilename(initialdir="/", title="Select a file")
    input_field.delete(0, customtkinter.END)
    input_field.insert(0, filename)
    tc_window = timecode.TimecodeOptionWindow(timecode_entry)
    tc_window.title("Timecode Selection")
    tc_window.tc_option.configure(values=[timecode.time_to_TC(0, 25), timecode.time_to_TC(timecode.starttime_from_file(filename), 25)])

def start_btn_clicked():
    whisper_thread = Thread(target=whisper_api.start_whisper, args=(input_field.get(), model_option.get(), language_option.get(), bool(translation_check_var.get()), output_option.get(), timecode.tc_to_time(timecode_entry.get(), 25)))
    whisper_thread.start()

customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("Easy Whisper")
root.resizable(False, False)
if platform.system() == "Windows":
    root.iconbitmap("EW-icon.ico")

# INPUT FRAME + CONTENTS
input_frame = customtkinter.CTkFrame(master=root, width=780, height=135)
input_label = customtkinter.CTkLabel(master=input_frame, text="Audio file:")
input_field = customtkinter.CTkEntry(master=input_frame, width=575, placeholder_text="Select a .wav file to transcribe.")
browse_btn = customtkinter.CTkButton(master=input_frame, text="Browse", width=85, command=browse_files)
language_label = customtkinter.CTkLabel(master=input_frame, text="Language: ")
language_option = customtkinter.CTkOptionMenu(master=input_frame, values=whisper_api.whisper_languages, dynamic_resizing=True)
model_label = customtkinter.CTkLabel(master=input_frame, text="Model: ")
model_option = customtkinter.CTkOptionMenu(master=input_frame, values=whisper_api.whisper_models, dynamic_resizing=True)
output_label = customtkinter.CTkLabel(master=input_frame, text="Output: ")
output_option = customtkinter.CTkOptionMenu(master=input_frame, values=output.output_options, dynamic_resizing=True)
translation_check_var = customtkinter.StringVar(value="")
translation_checkbox = customtkinter.CTkCheckBox(master=input_frame, text="Translate to English", variable=translation_check_var, onvalue="True", offvalue="")
timecode_label = customtkinter.CTkLabel(master=input_frame, text="Starting_TC:")
timecode_entry = customtkinter.CTkEntry(master=input_frame, width=90)
input_frame.grid(row=0, column=0, padx=10, pady=10)
input_label.place(relx=0.07, rely=0.2, anchor='center')
input_field.place(relx=0.12, rely=0.2, anchor='w')
browse_btn.place(relx=0.98, rely=0.2, anchor='e')
language_label.place(relx=0.185, rely=0.5, anchor='e')
language_option.place(relx=0.37, rely=0.5, anchor='e')
model_label.place(relx=0.387, rely=0.5, anchor = 'w')
model_option.place(relx=0.447, rely=0.5, anchor='w')
output_label.place(relx=0.645, rely=0.5, anchor='w')
output_option.place(relx=0.71, rely=0.5, anchor='w')
translation_checkbox.place(relx=0.5, rely=0.8, anchor='center')
timecode_label.place(relx=0.098, rely=0.8, anchor='w')
timecode_entry.place(relx=0.2, rely=0.8, anchor='w')

# FEEDBACK FIELD
feedback_frame = customtkinter.CTkFrame(master=root, width=780, height=280)
go_btn = customtkinter.CTkButton(master=feedback_frame, text='Start', command=start_btn_clicked)
feedback_text = customtkinter.CTkTextbox(master=feedback_frame, width=760, height=220, activate_scrollbars=True, state='disabled', font=('Courier New', 12))
feedback_frame.grid(row=1, column=0, padx=10, pady=0)
go_btn.place(relx=0.5, rely=0.1, anchor='center')
feedback_text.place(relx=0.5, rely=0.98, anchor='s')

# INFO FIELD
info_frame = customtkinter.CTkFrame(master=root, width=780, height=15, fg_color="transparent")
author_label = customtkinter.CTkLabel(master=info_frame, text="Made with ☕️ by BrechtV")
version_label = customtkinter.CTkLabel(master=info_frame, text=app_version)
info_frame.grid(row=2, column=0, padx=10, pady=10)
author_label.place(relx=0.02, rely=0.45, anchor='w')
version_label.place(relx=0.98, rely=0.45, anchor='e')

sys.stdout = feedback.IORedirector(feedback_text)

print("> Welcome to Whisper.\n> Complete the variables and press Start.\n")

root.mainloop()