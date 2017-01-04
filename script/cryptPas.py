import crypt

salt = 'alice'
username = 'nano'
password = 'daicusialice'

cPassword = crypt.crypt(password, salt)

dataFile = open("data.txt","a")
dataFile.write("\n" + password)
dataFile.close()

passwordsFile = open("passwords.txt","w")
passwordsFile.write(username + ":" + cPassword)
passwordsFile.close()
