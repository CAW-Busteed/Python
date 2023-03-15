for line in open('allnames.txt').readlines():
    line = line.rstrip()
    if not line: continue
    print(line)
