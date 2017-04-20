from multiprocessing import cpu_count
from subprocess import PIPE, Popen
files=open("test99.txt","w+")
filter_in=Popen(['awk', '{print $1,$3,$4}'] , stdin=PIPE , stdout=files)
p=Popen(['ps','-aux'],stdin=PIPE,stdout=filter_in.stdin)
out, err = filter_in.communicate()
#print filter_in.returncode
#print out
files.close()
f = open("test99.txt","r")
#print f.readline()
#print f.readline()

root_cpu=0.0
root_mem=0.0
nr_cpu=0.0
nr_mem=0.0
f.readline()
for line in f.readlines():
	line=line.strip()
	list_p=line.split(" ")
	if list_p[0]=="root":
		root_cpu=root_cpu+float(list_p[1])
		root_mem=root_mem+float(list_p[2])
	else:
		nr_cpu=nr_cpu+float(list_p[1])
                nr_mem=nr_mem+float(list_p[2])

n_cpu=cpu_count()		# Finding the number of cpus
root_cpu=root_cpu/n_cpu
nr_cpu=nr_cpu/n_cpu


root={"cpu_value":root_cpu,"mem_value":root_mem}
nr={"cpu_value":nr_cpu,"mem_value":nr_mem}
print "Root"+str(root)
print "Non-root"+str(nr)
p=Popen(['rm','test99.txt'],stdout=PIPE,stdin=PIPE,stderr=PIPE)
stdout,stderr=p.communicate()
