file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
file1.write("Hello \n")
file1.writelines(L)
file1.close()
