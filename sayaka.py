import sys
import os

input_file = sys.argv[1]

def read_log_file():
  """
  Read log files

  """

  with open(input_file) as f:
    lines = f.readlines()
    count = 0
    for line in lines:
      if 'KeyError' in line.strip():
        count = count + 1
    return count


count = read_log_file()
print(count)