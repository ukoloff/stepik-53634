import re
for line in open('brackets.in'):
  line = line.strip()
  while True:
    xline = re.sub(r'\(\)|\[\]', '', line)
    if len(xline) == len(line):
      break
    line = xline
  print(len(line)==0)
