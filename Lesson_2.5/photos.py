import os.path
import glob
from subprocess import Popen

if os.path.exists("result") == False:
    result = (os.mkdir("result"))

program_path = os.path.abspath('/convert.exe')
source_dir = os.path.join("Source")
result_dir = os.path.join("result")
#files = glob.glob(os.path.join('Source', "*.jpg"))
files_path = (os.path.abspath("Source"))

for file in files_path:
    args = ['convert.exe', source_dir, '-resize', '200', result_dir]
    #args = ['convert.exe', file, '-resize', '200', file]
    proc = Popen(args)

