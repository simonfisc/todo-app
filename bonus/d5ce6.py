filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    f = open(filename, 'w')
    f.writelines("Hello")
    f.close()
