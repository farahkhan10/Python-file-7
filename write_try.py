try:
	f = open('writeable.txt', 'w')
	f.write('Hello\n')
finally:
	f.close()
