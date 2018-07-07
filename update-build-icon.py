# dirty hack to get a build icon on the README without exposing internal jenkins server to internet.
import argparse

parser = argparse.ArgumentParser(description="Process configurations and integrate them into a VIRL file.")
parser.add_argument("-f", "--failed", help="Optional that indicates the test failed.", action="store_true")
args = parser.parse_args()
failed = args.failed

with open('README.md', 'r') as file :
  filedata = file.read()
print(filedata)
if failed:
    filedata = filedata.replace('passing.svg', 'failing.svg')
else:
    filedata = filedata.replace('failing.svg', 'passing.svg')

with open('README.md', 'w') as file:
  file.write(filedata)