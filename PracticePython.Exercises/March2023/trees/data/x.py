import os.path

for line in open(f'{os.path.dirname(__file__)}\\allnames.txt').readlines():
    line = line.rstrip()
    if not line: continue
    if line.startswith('         '):
        print('Level 3')
    elif line.startswith('      '):
        print('Level 2')
    elif line.startswith('   '):
        print('Level 1')
    print(line)
