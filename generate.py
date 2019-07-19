import os
import sys
from shutil import copyfile
import fileinput


content = [
  ['About', 'index.txt'],
  ['Ph.D. Thesis', 'phd.txt'],
  ['Publications', 'publications.txt'],
  ['BibTeX', 'bibtex.txt'],
  ['Open source', 'open-source.txt']
]

for title, input_path in content:

  print('Processing %s' % input_path)

  # Get the text of the considered file
  text = ''
  with open(input_path, 'r') as f:
    text = f.read()

  # Open the HTML template
  with open('template.txt', 'r') as input_file:

    # Open the output file
    output_path = os.path.splitext(input_path)[0] + '.html'
    with open(output_path, 'w') as output_file:

      # Get the current line from the template
      for line in input_file:

        # Eventually modify it (title or content)
        if '$title' in line:
          line = line.replace('$title', title)
        elif '$content' in line:
          line = line.replace('$content', text)

        # Write the line into the output file
        output_file.write(line)
