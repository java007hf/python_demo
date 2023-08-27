try:
	sum = 1 +"1"
	f = open("123.txt")
	f.read()
	f.close()
except OSError as e:
	print("error : " + str(e))
except TypeError as e1:
	print("error1 : " + str(e1))
except:
	print("error3")
finally:
	print("-----")