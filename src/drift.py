from alibi_detect.cd import KSDrift
def check_drift(ref, cur):
    cd = KSDrift(ref)
    return cd.predict(cur)