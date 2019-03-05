
import os
import re

class MSFConsole:

    def execRC(self):
        cmd = "msfconsole -r %s " % self.resname
        out = os.popen(cmd).read()
        self.out = out
        return out 


class MSFScan(MSFConsole):


    def genScanRC(self):
        self.resname = "portscan.rc"
        with open(self.resname, mode='w') as f:
            f.write("use auxiliary/scanner/portscan/tcp\n")
            f.write("set RHOSTS 127.0.0.1\n")
            f.write("run\n")
            f.write("exit\n")

    def parseOutput(self):
        output = self.out
        lout = output.split("\n")

        lhostport = []
        for line in lout:
            if line.endswith("TCP OPEN"):
                pattern = ".*\- (.*):(\d+) \- TCP OPEN"
                m = re.match(pattern, line)
                if m != None:
                    ip = m.group(1)
                    port = m.group(2)
                    lhostport.append((ip,port))

        return lhostport



if __name__ == "__main__":
    
    msfscan = MSFScan()
    msfscan.genScanRC()
    print msfscan.execRC()
    print msfscan.parseOutput()
