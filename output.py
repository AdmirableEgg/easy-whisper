import os
import datetime as dt
import timecode

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