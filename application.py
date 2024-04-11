# Application Opening and Closing Module
from AppOpener import open, close, mklist, give_appnames

# JSON LIST BANAVTA
# Generates an file, having key as AppName and value as AppIds.
# mklist(name="app_data.json") 
# appnames = give_appnames()
#  Save appnames as dictionary

def open_app(ftext):
    words = ftext.split()
    app_name = words[words.index("open") + 1] if "open" in words and words.index("open") < len(words) - 1 else None
    open(app_name, throw_error=True, match_closest=True)
    sentence = f"Opening {app_name}"
    return sentence

def close_app(ftext):
    words = ftext.split()
    app_name = words[words.index("close") + 1] if "close" in words and words.index("close") < len(words) - 1 else None
    imp_apps = (
        'explorer.exe', 'winlogon.exe', 'lsass.exe', 'services.exe', 'csrss.exe',
        'smss.exe', 'svchost.exe', 'wininit.exe', 'spoolsv.exe', 'dwm.exe','explorer',
        'winlogon','services','csrss','lsass','smss','svchost','wininit','spoolsv','dwm'
    )
    if app_name in imp_apps:
        sentence = f"Skipping closure of {app_name} as it is an important process or system app."
        return sentence
    else:
        close(app_name, throw_error=True, match_closest=False)
        sentence = f"Closing {app_name}"
        return sentence