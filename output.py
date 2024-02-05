import os
import datetime as dt
import timecode
import csv

output_options = ['', 'txt', 'txt without TC','csv', 'srt']

def write_txt(audio_file, model_name, language, translation, result, start_time):
    now = dt.datetime.now()
    audio_filename = os.path.basename(audio_file)
    dir_name = os.path.dirname(audio_file)

    output_file = open(os.path.join(dir_name, f"{now.strftime('%Y%m%d-%H%M%S')}_{audio_filename}_transcription.txt"), 'wt')
    output_file.write(f"Transcription performed on {now.strftime('%Y-%m-%d %H:%M:%S')}.\nLanguage: {language}\nModel: {model_name}\nTranslation: {translation}\n\n")
    for segment in result['segments']:
        output_file.write(f"[{timecode.time_to_TC(segment['start'] + start_time, 25)} - {timecode.time_to_TC(segment['end'] + start_time, 25)}]   > ")
        output_file.write(f"{segment['text']}\n")
    output_file.close()

def write_txt_without_tc(audio_file, model_name, language, translation, result):
    now = dt.datetime.now()
    audio_filename = os.path.basename(audio_file)
    dir_name = os.path.dirname(audio_file)
    
    output_file = open(os.path.join(dir_name, f"{now.strftime('%Y%m%d-%H%M%S')}_{audio_filename}_transcription.txt"), 'wt')
    output_file.write(f"Transcription performed on {now.strftime('%Y-%m-%d %H:%M:%S')}.\nLanguage: {language}\nModel: {model_name}\nTranslation: {translation}\n\n")
    for segment in result['segments']:
        output_file.write(f"{segment['text']}\n")
    output_file.close()

def write_csv(audio_file, model_name, language, translation, result, start_time):
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
        output_writer.writerow([timecode.time_to_TC(segment['start'] + start_time, 25), timecode.time_to_TC(segment['end'] + start_time, 25), segment['text']])
    output_file.close()

def write_srt(audio_file, model_name, language, translation, result, start_time):
    now = dt.datetime.now()
    audio_filename = os.path.basename(audio_file)
    dir_name = os.path.dirname(audio_file)

    output_file = open(os.path.join(dir_name, f"{now.strftime('%Y%m%d-%H%M%S')}_{audio_filename}_transcription.srt"), 'wt')
    output_file.write(f"Transcription performed on {now.strftime('%Y-%m-%d %H:%M:%S')}.\nLanguage: {language}\nModel: {model_name}\nTranslation: {translation}\n\n")
    for x in range(len(result['segments'])):
        output_file.write(f"{x+1}\n")
        output_file.write(f"{timecode.time_to_hms(result['segments'][x]['start'] + start_time)} --> {timecode.time_to_hms(result['segments'][x]['end'] + start_time)}\n")
        output_file.write(f"{result['segments'][x]['text']}\n\n")