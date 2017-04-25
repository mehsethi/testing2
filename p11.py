

from subprocess import Popen, PIPE
import os
import time
import pexpect
files=open("test99.txt","w")
filter_in=Popen(['awk', '{print $1,$3,$4}'] , stdin=PIPE , stdout=files).stdin
p=Popen(['ps','-aux'],stdin=PIPE,stdout=filter_in)
ret_code=p.wait()
print ret_code
stdout,stderr=p.communicate()
print stdout
print stderr

os.fsync(files)
files.flush()
files.close()
fi=open("test99.txt","r")

for line in fi.readlines():
	print line
#fi.readlines()
line=fi.readline()
print line
line=fi.readline()
print line
line=fi.readline()
print line
fi.close()


#files=open("test99.txt","w")
#filter_in=Popen(['awk', '{print $1,$3,$4}'] , stdin=PIPE , stdout=files).stdin
#p=Popen(['ps','-aux'],stdin=PIPE,stdout=filter_in)

