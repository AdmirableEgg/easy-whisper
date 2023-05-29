<p align="center">
  <img src="icon/EW-icon.ico"/>
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
    - Transcription uses SMPTE timecode. (currently only 25fps, starting at 00:00:00:00)
    - Multiple export formats.

## Future plans
- Exporting to other formats, like CSV or SRT.
- Choosing your framerate for transcription.
- Manually setting a starting timecode to use for transcription.
- Reading SMPTE timecode from the file and using that for transcription.
- Extracting an audio track from a (video)file with other tracks.
