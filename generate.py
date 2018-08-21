# data = []
# data.append(['About', 'index'])# = ['About'about CV Projects Thesis Publications Thesis template
# data.append(['About', 'index'])

import os
import glob
from shutil import copyfile

import fileinput
import sys


title   = ['About', 'Ph.D. Thesis', 'Publications', 'Pojects', 'BibTeX', 'Thesis template', 'Experience']
content = ['index.txt', 'phd.txt', 'publications.txt', 'projects.txt', 'bibtex.txt', 'thesis_template.txt', 'experience.txt']

# title   = ['Publications']
# content = ['publications.txt']

# filedata = None
# print os.path.join('template', 'begin.txt')
# with open('test.txt') as file:
  # print 'ok'

# # Get the template file
# template = ''
# with open('template.html', 'r') as f:
#   template = f.read()

# # Get the end of the file
# suffix = ''
# with open(os.path.join('template', 'end.txt'), 'r') as f:
#   suffix = f.read()
# # print suffix


for i in range(0, len(title)):

  print 'Processing', content[i]

  # Get the text of the considered file
  text = ''
  with open(content[i], 'r') as f:
    text = f.read()
  # print text

  # Create and open the output file
  output_path = os.path.splitext(content[i])[0] + '.html'
  with open('template.html', 'r') as input_file:
    with open(output_path, 'w') as output_file:
      for line in input_file:

        if '$title' in line:
          line = line.replace('$title', title[i])
        elif '$content' in line:
          line = line.replace('$content', text)

        # print line,
        output_file.write(line)

  

  # print src
  # print dst

  # copyfile(src, dst)

  # with open(src, 'r') as src_file:
  #   with open(dst, 'w') as dst_file:
  #     for line in src_file:

  #       line = line.replace('$begin', prefix, 1)
  #       line = line.replace('$end', suffix)
  #       print line

  #       dst_file.write(line)
  #       # line.replace('$end', suffix),
  #       # print line[0]

  # with fileinput.FileInput(dst, inplace=True) as file:
  #   for line in file:
  #     line.replace('$begin', prefix)
  #     line.replace('$end', suffix)


