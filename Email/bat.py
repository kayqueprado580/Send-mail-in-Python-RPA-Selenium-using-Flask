from subprocess import Popen,PIPE,call,check_call
import requests
import time
import getpass
user = getpass.getuser()

def startProcess(usuario,senha,porta,service):
    cmd='START /B python C:\\Users\\'+user+'\\Desktop\\Email\\'+service+'.py '+porta+' '+usuario+' '+senha+''
    #print("antes do try")
    try:
        proc =Popen(cmd,shell=True)
        #print("asdas")
        return "okay"
        #print("dentro do try")
    except Exception as e:
        print('error')
        proc.kill()
        return e
    return "end"

def stopProcess(port):
    url = "localhost:"+str(port)+"/kill"
    consulta = 'curl '+url
    call(consulta,shell=True)
    first='for /f "tokens=5" %a in '
    second="('netstat -aon ^| findstr "+ str(port)+"') "
    script=first+second+'do if not %a == 0 (taskkill /F /FI "PID eq %a")'
    result2 = call(script,shell=True)
    return "Libera os processos"
