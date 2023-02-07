import os
import argparse


# Create parser
parser = argparse.ArgumentParser(
    prog = 'Build The Application',
    description = 'This script finds build the application for the specified operating system',
    epilog = 'PyDracula'
)

# Register arguments
parser.add_argument('-s','--system', required=True,  help="the system to build the application (windows/linux/flatpak)")
# Parse
args = parser.parse_args()   

if args.system == 'linux':
    os.system('python _packaging/build_linux.py build')
    print(args.system)
elif args.system == 'flatpak':   
    os.system('python _packaging/flatpak/build_flatpak.py')    
elif args.system == 'windows':   
    print(args.system)
else:
    print('The arguments must be windows or linux')     
