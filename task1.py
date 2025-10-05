try:
    file1=open('sample.txt','r')
    print("Reading File Content:")  
    readingfile=file1.read()
    print(readingfile)
    file1.close()
except FileNotFoundError:
    print('Error: The file \'sample.txt\' not found.')
