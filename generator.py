#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
from os import path
from sys import argv
from sqlextractor import extract_row
from config import package
from codecs import open

if len(argv) < 2:
    sys.exit(1)

PATH = path.dirname(path.abspath(__file__))
env = Environment(
    loader=FileSystemLoader(path.join(PATH, 'templates')),
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True
)

rows = extract_row(argv[1])

name = ''.join(x.capitalize() or '_' for x in argv[1].split('_'))
rowmapper_tpl = env.get_template('RowMapper.java')
rowmapper = rowmapper_tpl.render(name=name, rows=rows, package=package)
bean_tpl = env.get_template('Bean.java')
bean = bean_tpl.render(name=name, rows=rows, package=package)

with open(name + '.java', 'w', 'utf-8') as f:
    f.write(bean)

with open(name + 'RowMapper.java', 'w', 'utf-8') as f:
    f.write(rowmapper)