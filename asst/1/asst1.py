__author__ = "Nathan Lee"

def swapchars(s):
  max_letter = s[0]
  min_letter = s[0]
  max = 0
  min = len(s) + 1
  for c in s:
    if (ord(c) > 64 and ord(c) < 91) or (ord(c) > 96 and ord(c) < 123):
      if s.count(c) > max:
        max_letter = c
        max = s.count(c)
      elif s.count(c) < min:
        min_letter = c
        min = s.count(c)
  print max_letter
  print min_letter
  print max
  print min
  s1 = ""
  for l in s:
    if l == max_letter:
      s1 += min_letter
    elif l == min_letter:
      s1 += max_letter
    else:
      s1 += l
  print s1
  return

def sortcat(n, *args):
  alist = list(args)
  alist.sort(key=len, reverse=True)
  print ''.join(alist[0:n])
  

def bluesclues(ab):
  abbrev = {}
  with open("states.txt") as txt:
    for line in txt:
      (key, val) = line.strip().split(',')
      abbrev[val.strip()] = key.strip()
  print abbrev[ab]

def bluesbooze(state):
  abbrev = {}
  with open("states.txt") as txt:
    for line in txt:
      (key, val) = line.strip().split(',')
      abbrev[key.strip()] = val.strip()
  print abbrev[state]