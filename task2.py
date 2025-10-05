usrinput=input('Enter text to the file:')
with open('output.txt','w')as f1:
    f1.write(usrinput)
print('Data successfully written to output.txt.\n')
add_data=input('Enter additional text to append:')
with open('output.txt','a')as f1:
    f1.write('\n'+add_data)
print('Data successfully appended.\n')
with open('output.txt','r')as f1:
    content=f1.read()
print('Final content of output.txt:')
print(content)
