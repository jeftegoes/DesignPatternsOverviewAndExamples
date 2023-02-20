from file_with_logging import FileWithLogging

file = FileWithLogging(open('hello.txt', 'w'))
file.writelines(['hello', 'world'])
file.write('testing')
file.close()
