from ffmpeg import probe

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

def starttime_from_file(media_file):
    media_info = probe(media_file)
    try:
        return int(media_info['format']['tags']['time_reference']) / int(media_info['streams'][0]['sample_rate'])
    except:
        return 0