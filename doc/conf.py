from recommonmark.parser import CommonMarkParser

source_parsers = {
            '.md': CommonMarkParser,
            }

#source_suffix = ['.rst', '.md']
source_suffix = ['.md']
master_doc = 'index'

