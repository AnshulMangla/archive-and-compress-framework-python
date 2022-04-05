import glob
import os, time
from zipfile import ZipFile


duration = time.time() - (86400)
root = "./logs"

zipObj = ZipFile('./backup/archive-' + time.strftime("%Y-%m-%d") + '.zip', 'w')

## Zip the files first ##
for i in os.listdir(root):
    path = os.path.join(root, i)

    if os.stat(path).st_mtime <= duration:
        print("filename add = " + i)
        zipObj.write(path)

zipObj.close()

## Remove the files now ##
for i in os.listdir(root):
    path = os.path.join(root, i)

    if os.stat(path).st_mtime <= duration:
        print("filename remove = " + i)
        if os.path.isfile(path):
            try:
                os.remove(path)
            except:
                print("Could not remove file:", i)

# list_of_files = glob.glob("./logs/" + "/*.log")  # * means all if need specific format then *.csv
# latest_file = min(list_of_files, key=os.path.getmtime)
# print (latest_file)

