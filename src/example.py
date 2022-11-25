import os, string, sys, subprocess
#generator needs one additional argument: .h file parent directory
subprocess.run(['python3', 'generator.py', '/home/vadim/PEAS/src/'])

#generator needs one additional argument: first is path to library sources, the second one is parent directory to testSOMETHING.cpp 
subprocess.run(['python3', 'builder.py', '/home/majong/PEAS/src/lsm.cpp', '/home/majong/PEAS/src/'])