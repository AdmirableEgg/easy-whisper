# A Class for redirecting Stdout to the text widget

class IORedirector:

    def __init__(self,text_area):
        self.text_area = text_area
    
    def write(self,str):
        self.text_area.configure(state='normal')
        self.text_area.insert("end", str)
        self.text_area.configure(state='disabled')

    def flush(self):
        pass