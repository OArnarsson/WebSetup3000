import os, argparse
from argparse import RawTextHelpFormatter
from unipath import Path


def setup_project():
    parser = argparse.ArgumentParser(description='''
 - The script can be run like so: 'python projectSetup.py newProject' to create the folder 'newProject'
 - It then creates the index.html and js/index.js files linked together with visual feedback.
 - Opens the project folder in sublime text if you have set the environment variables.
 - Runs browser-sync and opens index.html in browser if you have npm browser-sync installed.

 - Created by OArnarsson & andriandresson''', formatter_class=RawTextHelpFormatter)
    parser.add_argument('projectLocation', type=str, help="- Relative path to your project folder")
    args = parser.parse_args()

    projectPath = os.path.join(os.getcwd(), args.projectLocation)
    jsPath = os.path.join(projectPath, 'js')

    if not os.path.exists(projectPath):
        os.mkdir(projectPath)
    if not os.path.exists(jsPath):
        os.mkdir(jsPath)

    create_files(projectPath, jsPath)
    open_project(projectPath)
    print('\nProject setup complete')

def create_files(path, jsPath):
    with open(os.path.join(path, 'index.html'), 'w') as html:
        html.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>New Project</title>
    <script src="js/index.js"></script>
</head>
<body>

<div>Hello world!</div>

</body>
</html>''')
    with open(os.path.join(jsPath, 'index.js'), 'w') as js:
        js.write('''console.log(".js file connected!");''')

def open_project(path):
    openSublime = 'subl "{}"'.format(Path(path).name)
    os.system(openSublime)

    os.chdir(path)
    openFolder = 'start .'
    os.system(openFolder)
    browserSync = 'browser-sync start --server --files "js/*.js"'
    os.system(browserSync)

setup_project()
