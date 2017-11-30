from subprocess import Popen

import os.path
import glob

result = (os.mkdir("result"))
files_path = (os.path.abspath('/result'))
files = glob.glob(os.path.join(files_path, "*.jpg"))
program_path = os.path.abspath('/convert.exe')

for file in files:
        args = [program_path, file, '-resize', '200', file]
        proc = Popen(args)
