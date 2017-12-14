import os
import subprocess

if not os.path.exists("result"):
    result = os.mkdir("result")
source_path = os.path.abspath('Source')
result_path = os.path.abspath('result')

program_path = os.path.abspath('convert.exe')
for file_name in os.listdir(source_path):
    if not file_name.endswith(".jpg"):
        continue
    source_file = os.path.join(source_path, file_name)
    result_file = os.path.join(result_path, file_name)
    args = ['convert.exe', source_file, '-resize', '200', result_file]
    print(args)
    subprocess.call(args)

