import time
print('Obtenir la data i hora actual en diferents formats')
print('Temps en segons :',time.time())
print('Data i hora com un text:',time.ctime())
print('Estructura temps (UTC):',time.gmtime())
print('Estructura temps (local)',time.localtime())