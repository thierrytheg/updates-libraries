import subprocess
import tempfile


with tempfile.TemporaryFile() as tempf:
    proc=subprocess.Popen("pip list --outdated",shell=True,stdout=tempf)
    proc.wait()
    tempf.seek(0)
    a=(tempf.read().decode("utf-8"))
    b=(a.split("\n"))
    for n in range(2,len(b)):
        x=(b[n].split(" "))
        a='pip install %s --upgrade' %x[0]
        with tempfile.TemporaryFile() as tempf:
            proc=subprocess.call(a,shell=True,stdout=tempf)

print("update complete")
        
