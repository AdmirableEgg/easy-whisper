import os
import datetime as dt
import timecode
import csv

output_options = ['', 'txt', 'csv', 'srt']

def write_txt(audio_file, model_name, language, translation, result):
    now = dt.datetime.now()
    audio_filename = os.path.basename(audio_file)
    dir_name = os.path.dirname(audio_file)

    output_file = open(os.path.join(dir_name, f"{now.strftime('%Y%m%d-%H%M%S')}_{audio_filename}_transcription.txt"), 'wt')
    output_file.write(f"Transcription performed on {now.strftime('%Y-%m-%d %H:%M:%S')}.\nLanguage: {language}\nModel: {model_name}\nTranslation: {translation}\n\n")
    for segment in result['segments']:
        output_file.write(f"[{timecode.frames_to_TC(segment['start'] * 25, 25)} - {timecode.frames_to_TC(segment['end'] * 25, 25)}]   > ")
        output_file.write(f"{segment['text']}\n")
    output_file.close()

def write_csv(audio_file, model_name, language, translation, result):
    now = dt.datetime.now()
    audio_filename = os.path.basename(audio_file)
    dir_name = os.path.dirname(audio_file)

    output_file = open(os.path.join(dir_name, f"{now.strftime('%Y%m%d-%H%M%S')}_{audio_filename}_transcription.csv"), 'wt')
    output_writer = csv.writer(output_file, dialect="excel")
    output_writer.writerow(["Transcription performed on:", now.strftime('%Y-%m-%d %H:%M:%S')])
    output_writer.writerow(["Language:", language])
    output_writer.writerow(["Model:", model_name])
    output_writer.writerow(["Translation:", translation])
    output_writer.writerow("")
    
    for segment in result['segments']:
        output_writer.writerow([timecode.frames_to_TC(segment['start'] * 25, 25), timecode.frames_to_TC(segment['end'] * 25, 25), segment['text']])
    output_file.close()

def write_srt(audio_file, model_name, language, translation, result):
    now = dt.datetime.now()
    audio_filename = os.path.basename(audio_file)
    dir_name = os.path.dirname(audio_file)

    output_file = open(os.path.join(dir_name, f"{now.strftime('%Y%m%d-%H%M%S')}_{audio_filename}_transcription.srt"), 'wt')
    output_file.write(f"Transcription performed on {now.strftime('%Y-%m-%d %H:%M:%S')}.\nLanguage: {language}\nModel: {model_name}\nTranslation: {translation}\n\n")
    for x in range(len(result['segments'])):
        output_file.write(f"{x+1}\n")
        output_file.write(f"{timecode.time_to_hms(result['segments'][x]['start'])} --> {timecode.time_to_hms(result['segments'][x]['end'])}\n")
        output_file.write(f"{result['segments'][x]['text']}\n\n")