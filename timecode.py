def frames_to_TC(frames, fps):
    h = int(frames // (fps*3600))
    m = int(frames // (fps*60)) % 60 
    s = int((frames % (fps*60))// fps) 
    f = frames % (fps*60) % fps
    return ( "%02d:%02d:%02d:%02d" % (h, m, s, f))