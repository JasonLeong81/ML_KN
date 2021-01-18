def WriteInFile():
    with open('notes.txt','w') as f:
        for i in range(1,101):
            f.write(f'Video {i}: ')
            f.write('\n')
            f.write('\n')
            f.write('\n')
# WriteInFile()

