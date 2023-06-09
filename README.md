<p align="center">
  <img src="icon/EW-icon.png" width="250"/>
</p>

# Easy Whisper
A simple GUI for transcription with openAI's Whisper.

## Why?
Whisper's transcription capabilities are superior to any other project I've tested. Using the large model, it's even able to transcribe dialects like West-Flemish with just only minor mistakes. Working for a TV production company, this would fit nicely in our workflow.
Unfortunately, using it from the CLI or in a python program isn't always straightforward for everyone. So for whoever needs it, I created this quick and easy GUI that should make it more accessible to use.

## Features
- Basic Whisper functionality in a GUI:
    - Choose file
    - Choose language
    - Choose model
    - Transcribe!
    - Translate to English!
- Extra features:
    - Transcription uses SMPTE timecode. (currently only 25fps)
    - Read file TC to use in the transcription file.
    - Manually set a TC to use in the transcription file.
    - Multiple export formats: TXT, CSV or SRT.

## Future plans
- Choosing your framerate for transcription.
- Extracting an audio track from a (video)file with other tracks.
- Translation to other languages using DeepL's API.
- Speaker identification / diarization