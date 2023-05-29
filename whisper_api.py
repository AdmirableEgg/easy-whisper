import whisper
import output

whisper_languages = ['Detect', 'Afrikaans', 'Arabic', 'Armenian', 'Azerbaijani', 'Belarusian', 'Bosnian', 'Bulgarian', 'Catalan', 'Chinese', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Finnish', 'French', 'Galician', 'German', 'Greek', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Italian', 'Japanese', 'Kannada', 'Kazakh', 'Korean', 'Latvian', 'Lithuanian', 'Macedonian', 'Malay', 'Marathi', 'Maori', 'Nepali', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Tagalog', 'Tamil', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Welsh']
whisper_models = whisper.available_models()
whisper_models.insert(0, '')

def start_whisper(audio_file, model_name, language, translation):
    if language == "" or model_name == "" or audio_file == "":
        print("> Make sure to fill in all the required details.")
        return None
    
    whisper_job_kwargs = {}

    if language == "Detect":
        language = "unknown"
    else:
        whisper_job_kwargs.update({"language": language})

    if translation == True:
        whisper_job_kwargs.update({"task": "translate"})
    
    print(f"> Transcribing in {language} language with the {model_name} model. Translation is set to: {translation}")
    print("> Loading model. If it's the first time you use the model, this might take a few minutes...")
    
    model = whisper.load_model(model_name)
    
    print(f"> Model loaded. Starting transcription.")
    print("\n__________________________________________________________________________________________________\n")

    result = model.transcribe(audio_file, verbose = True, **whisper_job_kwargs)

    output.write_txt(audio_file, model_name, language, translation, result)
    
    print("\n\n__________________________________________________________________________________________________\n\n")
    print(f"Done.\nTranscription saved next to original file.")