import os
API_TOKEN = os.getenv('SECRET')
file = open('testfile.txt','w') 
file.write(API_TOKEN) 
file.close()
