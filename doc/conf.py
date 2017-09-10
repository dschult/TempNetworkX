from recommonmark.parser import CommonMarkParser

source_parsers = {
            '.md': CommonMarkParser,
            }

#source_suffix = ['.rst', '.md']
source_suffix = ['.md']
master_doc = 'index'

# -- Hack to copy index.html file to output
from shutil import copyfile

def copy_html(app, docname):
    if app.builder.name == "html":
        for filename in ["/.htaccess", "/robots.txt"]:
            print("Copying ",filename," to ", app.outdir)
            source = app.srcdir + filename
            target = app.outdir + filename
            copyfile(source, target)

def setup(app):
    app.connect('build-finished', copy_html)
