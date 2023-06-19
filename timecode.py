from ffmpeg import probe
import customtkinter

class TimecodeOptionWindow(customtkinter.CTkToplevel):
    
    def __init__(self, master_timecode_entry, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master_timecode_entry = master_timecode_entry
        self.tc_label = customtkinter.CTkLabel(master=self, text="Starting TC:")
        self.tc_option = customtkinter.CTkOptionMenu(master=self, values=[""])
        self.tc_submit_btn = customtkinter.CTkButton(master=self, text="Submit", command=self.submit_btn_click)
        self.tc_label.grid(row=0, column=0, padx=20, pady=20)
        self.tc_option.grid(row=0, column=1)
        self.tc_submit_btn.grid(row=0, column=2, padx=20, pady=20)

    def submit_btn_click(self):
        if self.tc_option.get() == "":
            return
        else:
            self.master_timecode_entry.delete(0, customtkinter.END)
            self.master_timecode_entry.insert(0, self.tc_option.get())
            self.destroy()

def time_to_TC(time, framerate): # SMPTE timecode
    h = time // 3600
    m = time // 60 % 60 
    s = int(time % 60)
    f = time % 1 * framerate
    return ( "%02d:%02d:%02d:%02d" % (h, m, s, f))

def time_to_hms(time): # hours:minutes:seconds,milliseconds
    h = int(time // 3600)
    m = int(time // 60) % 60
    s = float(time % 60)
    return ( "%02d:%02d:%06.3f" % (h, m, s))

def tc_to_time(tc, framerate):
    tc_elements = tc.split(':')
    return int(tc_elements[0]) * 3600 + int(tc_elements[1]) * 60 + int(tc_elements[2]) + int(tc_elements[3]) / framerate

def starttime_from_file(media_file):
    media_info = probe(media_file)
    try:
        return int(media_info['format']['tags']['time_reference']) / int(media_info['streams'][0]['sample_rate'])
    except:
        return 0