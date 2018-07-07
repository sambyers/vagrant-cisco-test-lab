# dirty hack to get a build icon on the README without exposing internal testing server to internet.
import argparse

parser = argparse.ArgumentParser(description="Process configurations and integrate them into a VIRL file.")
parser.add_argument("-f", "--failed", help="Optional that indicates the test failed.", action="store_true")
args = parser.parse_args()
failed = args.failed

with open('README.md', 'r') as file :
  readme_data = file.read()
print(readme_data)
if failed:
    readme_data = readme_data.replace('passing.svg', 'failing.svg')
else:
    readme_data = readme_data.replace('failing.svg', 'passing.svg')

with open('README.md', 'w') as file:
  file.write(readme_data)