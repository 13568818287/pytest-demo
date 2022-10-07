import psutil

def get_pid(name):
    '''
     作用：根据进程名获取进程pid
     返回：返回匹配第一个进程的pid
    '''
    pids = psutil.process_iter()
    for pid in pids:       
        if(pid.name() == name):
            return pid.pid