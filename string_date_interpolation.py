import re
from datetime import datetime

def interpolate(interpolationKey, dt, rawString):
    regex = re.compile(f'{{{interpolationKey}:[^{{|^}}]+}}')

    result = rawString
    for m in regex.finditer(rawString):
        t = m.group(0)
        r = t[len(interpolationKey) + 2: len(t) - 1]
        result = result.replace(t, dt.strftime(r))
        
    return result