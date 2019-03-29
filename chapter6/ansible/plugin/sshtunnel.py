
import pexpect

import pyotp
import os
import time
import pdb
import socket
import random

class SSHTunnel():

    def __init__(self):
        
        self.init_jumphost_info("test", "35.237.65.122", "BKHKKMYXXU2QTHAF") 

    def init_jumphost_info(self, userinjump, jump_host, two_factor_key): 
        self.userinjump = userinjump
        self.jump_host = jump_host
        self.two_factor_key = two_factor_key
         
    def isUsed(self,port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect('127.0.0.1',int(port))
            s.shutdown(2) #forbid read and write in future
            print '%d is open' % port
            return True
        except:
            return False

         
    def getFreePort(self):
        #randomport = 0
        find = False
        freeport = -1
        LOOPNUM = 10
        PORTMIN = 40000
        PORTMAX = 50000
        for i in range(1,LOOPNUM):
            freeport = random.randint(PORTMIN, PORTMAX)
            if (not self.isUsed(freeport)):
                find = True
                break
        if find == True:
            return str(freeport)
        else:
            raise RuntimeError('cannot find free port for mapping from %s to %s' % (PORTMIN, PORTMAX))

    def downloadPublicKeyfromJumphost(self):
        return self.__downloadPublicKeyfromJumphost(self.userinjump, self.jump_host, self.two_factor_key)

    def __downloadPublicKeyfromJumphost(self, user, jump_host, two_factor_key):

        expected_prompt_list = [
                pexpect.TIMEOUT,
                pexpect.EOF,
                '(?i)Are you sure you want to continue connecting (yes/no)?',
                'Verification code:',
                'Permission Denied*',
                '100%'
                ]
        if os.path.exists("jumphost_rsa"):
            os.system("rm jumphost_rsa")
        time.sleep(3)
        paraList = ['scp ',user,'@',jump_host,':~/.ssh/id_rsa jumphost_rsa']
        cmd_copy_publickey = "".join(paraList)
        #print copyPublickKey
        process = pexpect.spawn(cmd_copy_publickey, timeout=60)
        expected_prompt_index = process.expect(expected_prompt_list)
        if expected_prompt_index == 0:
            print(process.before, process.after)
            raise RuntimeError('ERROR! login to jump host timed out!') 
        elif expected_prompt_index == 1:
            print('copyJumpHostPublickKey failed!can not login with ssh,user or host invalid!')
            print(process.before, process.after)
            raise RuntimeError('can not login with ssh,user or host invalid!')
        elif expected_prompt_index == 2: # In this case SSH does not have the public key cached.
            process.sendline('yes')
            process.expect('Verification code:')
        elif expected_prompt_index == 3:
            print 'Verification code verification...'
        else:
            print(process.before, process.after)
            raise RuntimeError('can not login with ssh, user or host invalid!') 

        #On-Time Password verification
        LOOPNUM = 3
        for i in range(1,LOOPNUM):
            code = pyotp.TOTP(two_factor_key).now()
            process.sendline(code)
            expected_prompt_index = process.expect(expected_prompt_list, timeout=60)
            if expected_prompt_index == 0 or expected_prompt_index == 1:
                print(process.before, process.after)
                raise RuntimeError('copy public key from jumphost %s failed' % jump_host)
            elif expected_prompt_index == 2:
                process.sendline('yes')
                process.expect('Verification code:')
            elif expected_prompt_index == 3:
                print "retry verification code..."
            elif expected_prompt_index == 4:
                print(process.before, process.after) 
                raise RuntimeError('ssh to jumphost %s permission denied' % jump_host)
            elif expected_prompt_index == 5:
                print "copy private key from jump host %s completed" % jump_host
                process.close()
                return os.path.abspath("dbaas_rsa") 
            else:
                process.close()
                print(process.before, process.after)
                raise RuntimeError('cannot copy the file')

    def setupTunnelViaJumpHost(self, target_host):
        return self.__setupTunnelViaJumpHost(self.userinjump, self.jump_host, self.two_factor_key, target_host)

    def __setupTunnelViaJumpHost(self, user, jump_host, two_factor_key, target_host):

        expected_prompt_list = [
                      pexpect.TIMEOUT,
                      pexpect.EOF,
                      '(?i)Are you sure you want to continue connecting (yes/no)?',
                      'Verification code:',
                      'Permission Denied*',
                      'to get the list of allowed commands'
                      ]
                         
        mappingport = self.getFreePort() 
        paraList = ['ssh -L ',mappingport,':',target_host,':22 ',user,'@',jump_host]
        cmd_setup_tunnel = "".join(paraList)
        process = pexpect.spawn(cmd_setup_tunnel, timeout=60)
        expected_prompt_index = process.expect(expected_prompt_list)
        if expected_prompt_index == 0:
            print(process.before, process.after)
            raise RuntimeError('login to jump host %s timed out!' % jump_host)
        elif expected_prompt_index == 1:
            print(process.before, process.after)
            raise RuntimeError('can not login with ssh,user or host invalid!')
        elif expected_prompt_index == 2: # In this case SSH does not have the public key cached.
            process.sendline('yes')
            process.expect('Verification code:')
        elif expected_prompt_index == 3:
            print "Verification code verification..."
        else:
            print(process.before, process.after)
            raise RuntimeError('can not login with ssh!')

        #On-Time Password verification
        LOOPNUM = 3
        for i in range(1,LOOPNUM):
            code = pyotp.TOTP(two_factor_key).now()
            process.sendline(code)
            expected_prompt_index = process.expect(expected_prompt_list, timeout=60)
            if expected_prompt_index == 0:
                print(process.before, process.after)
                raise RuntimeError('setup tunnel time out!')
            elif expected_prompt_index == 1:
                print(process.before, process.after)
                raise RuntimeError('cannot setup tunnel!')
            elif expected_prompt_index == 4:
                print(process.before, process.after)
                raise RuntimeError('Permission Denied!')
            elif expected_prompt_index == 3:
                print(process.before, process.after)
                print "Verification code: retry verification ..."
            elif expected_prompt_index == 2:
               process.sendline('yes')
               process.expect('Verification code:')
            elif expected_prompt_index == 5:
                self.process = process 
                print "mapped from %s:22  to localhost:%s ok" % (target_host, mappingport)
                return ("localhost", mappingport)
                  

        print(process.before, process.after)
        raise RuntimeError('cannot setup tunnel from %s' % jump_host)

    def close(self):
        self.process.close()

if __name__ == "__main__":

    ssh = SSHTunnel()
    #ssh.downloadPublicKeyfromJumphost()

    (ipaddress, port) = ssh.setupTunnelViaJumpHost("10.140.0.2")

    print(port)

    time.sleep(10)
 
    pdb.set_trace()
