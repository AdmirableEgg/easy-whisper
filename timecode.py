def frames_to_TC(frames, fps): # SMPTE timecode
    h = int(frames // (fps*3600))
    m = int(frames // (fps*60)) % 60 
    s = int((frames % (fps*60))// fps) 
    f = frames % (fps*60) % fps
    return ( "%02d:%02d:%02d:%02d" % (h, m, s, f))

def time_to_hms(time): # hours:minutes:seconds,milliseconds
    h = int(time // 3600)
    m = int(time // 60) % 60
    s = float(time % 60)
    return ( "%02d:%02d:%06.3f" % (h, m, s))