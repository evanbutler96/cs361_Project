
# this file is an example call from your end through the text file
# copy path of txt file so we can write in request in the file
# you ofcourse will need to change the path variable declaration

def writeToFile():
    with open("ms.txt", 'w') as f:
        f.write("request")
