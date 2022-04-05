
'''
    Script running manager: logs, running time, ... 
'''
import os
import time

class ExecManCl:
    
    
    def __init__(self):
        self.logdir='log/'
        self.logfile='log'
        self.logpath=self.logdir+self.logfile
        self.warnings_cnt=0      # errors count
        self.errors_cnt=0        # warnings count
        self.start_time=time.time()       # sec

        if not os.path.exists(self.logdir):
            os.mkdir(self.logdir)
        if os.path.exists(self.logpath):
            os.remove(self.logpath)

    def warning(self, text:str):
        print("! Warning: "+text)
        with open(self.logpath, 'a') as logf:
            tm=time.strftime('%H:%m:%S')
            logf.write(f"> {tm} Warning: \t"+text+"\n")
            self.warnings_cnt+=1
    
    def error(self, text:str):
        print("!! Error: "+text)
        with open(self.logpath, 'a') as logf:
            tm=time.strftime('%H:%m:%S')
            logf.write(f"> {tm} Error: \t"+text+"\n")
            self.errors_cnt+=1
    
    def note(self, text:str):
        print("> Note: "+text)
        with open(self.logpath, 'a') as logf:
            tm=time.strftime('%H:%m:%S')
            logf.write(f"> {tm} Note: \t"+text+"\n")

    def report(self):
        self.exectime=time.time()-self.start_time
        h=round(self.exectime//(60*60))
        m=round(self.exectime%(60*    60)//60)
        s=round(self.exectime%(60*60)%60)
        print(f' ExecMan report:')
        print(f' -----------------------------')
        print(f' execution time: \t{h}:{m}:{s}')
        print(f' Errors: \t{self.errors_cnt}')
        print(f' Warnings: \t{self.warnings_cnt}')
        

def test():
    print("'my_execman' testing.")
    Man=ExecManCl()
    Man.warning("Start")
    time.sleep(1)
    Man.warning("Next step. ")
    Man.error("Some error accured!")
    time.sleep(1)
    Man.note('Just testing')
    Man.report()
    
if __name__=='__main__':    
    test()

ExecMan=ExecManCl()
