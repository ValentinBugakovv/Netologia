from subprocess import Popen
import shutil
import os.path
import glob

if os.path.exists("result") == False:
    result = (os.mkdir("result"))
files_path = (os.path.abspath('/Source'))
files = glob.glob(os.path.join(files_path, "*.jpg"))
program_path = os.path.abspath('/convert.exe')

for file in files:
    args = [program_path, file, '-resize', '200', file]
    shutil.copy(file, "/result")
    proc = Popen(args)
