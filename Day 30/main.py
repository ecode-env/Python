## File not found
# 
# try:
#     # Try to open the file and access the dictionary key
#     file = open('a_text.txt')
#     dictio = {'key': 'value'}
#     #print(dictio['ello'])  # This will raise a KeyError
# except FileNotFoundError:
#     # Handle file not found error
#     file = open('a_text.txt', 'w')
#     file.write('Hello World')
# except KeyError as error:
#     # Handle KeyError for the dictionary lookup
#     print(f'The key {error} does not exist.')
# else:
#     # If no exceptions occur, read the file content
#     content = file.read()
#     print(content)
# finally:
#     # Always close the file
#     file.close()
#     print('File was closed.')

height = float(input('enter you height: '))
weight = int(input('enter you weight: '))

if height > 3:
    raise TypeError('You have to under 3m ')
else:
    print(weight /  height** 2)