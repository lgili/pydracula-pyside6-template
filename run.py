import os

# Build the windows from the .ui file
os.system('./_scripts/build-windows.sh')

# Build the translations
# os.system('./_scripts/build-translations.sh')

# Activate Custom Debug Settings
debug = True

# Run the app
os.system('python -m pydracula ' + ('--appDebug' if debug ==
          True else ''))
