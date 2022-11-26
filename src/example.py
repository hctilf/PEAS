import os, string, sys, subprocess, glob
#generator needs one additional argument: .h file parent directory
#or use this command '$(pwd)/'
cur_dir = os.getcwd() + os.sep
subprocess.run(['python3', 'generator.py', cur_dir])

lib_name = os.getcwd() + os.sep + glob.glob("**/**/lsm.cpp", recursive=True)[0]
#or use this "$(find -iname 'lsm.cpp')"
#generator needs two additional argument: first is path to library sources, the second one is parent directory to testSOMETHING.cpp 
subprocess.run(['python3', 'builder.py', lib_name, cur_dir])