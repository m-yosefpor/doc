import sys
import socket
import time
############################################################
def OK(st):
    st[0] = 'SIP/2.0 200 OK'
    res=''
    for l in st:
        res += l +'\r\n'
    return res
####
class Req:
    def __init__(self):
        self.via=[]
        self.a=[]
############################################################
def analyze(r,st):
    
    r.to = ''    
    r.fromm=''
    for nextLine in st : 
        fieldName = nextLine[:nextLine.find(":")];
        #print(fieldName)
        if("Via"==fieldName):
            r.via += [nextLine[nextLine.find(" ")+1:]]
        elif("From"==fieldName):
            r.fromm = nextLine[nextLine.find(" ")+1:];
        elif("To"==fieldName):
            #print('hi')
            r.to = nextLine[nextLine.find(" ")+1:];
        elif("Call-ID"==fieldName):
            r.callId = nextLine[nextLine.find(" ")+1:];
        elif("CSeq"==fieldName):
            r.cSeq = nextLine[nextLine.find(" ")+1:];
        elif("Contact"==fieldName):
            r.contact = nextLine[nextLine.find(" ")+1:];
        elif("Allow"==fieldName):
            r.allow = nextLine[nextLine.find(" ")+1:];
        elif("Max-Forwards"==fieldName):
            r.maxForwards = nextLine[nextLine.find(" ")+1:];
        elif("Allow-Events"==fieldName):
            r.allowEvents = nextLine[nextLine.find(" ")+1:];
        elif("User-Agent"==fieldName):
            r.userAgent = nextLine[nextLine.find(" ")+1:];
        elif("Supported"==fieldName):
            r.supported = nextLine[nextLine.find(" ")+1:];
        elif("Expires"==fieldName):
            r.expires = nextLine[nextLine.find(" ")+1:];
        elif("Content-Type"==fieldName):
            r.contentType = nextLine[nextLine.find(" ")+1:];
        elif("P-Early-Media"==fieldName):
            r.pEarlyMedia = nextLine[nextLine.find(" ")+1:];
        elif("P-Preferred-Identity"==fieldName):
            r.preferredIdentity = nextLine[nextLine.find(" ")+1:];
        elif("Content-Length"==fieldName):
            r.contentLength = nextLine[nextLine.find(" ")+1:];
        if nextLine.find('=') == 1:
            fieldName = nextLine[0]
            if('v'==fieldName):
                r.v = nextLine[nextLine.find('=')+1:]
            elif('o'==fieldName):
                r.o = nextLine[nextLine.find('=')+1:]
            elif('s'==fieldName):
                r.s = nextLine[nextLine.find('=')+1:]
            elif('c'==fieldName):
                r.c = nextLine[nextLine.find('=')+1:]
            elif('t'==fieldName):
                r.t = nextLine[nextLine.find('=')+1:]
            elif('m'==fieldName):
                r.m = nextLine[nextLine.find('=')+1:]
            elif('a'==fieldName):
                r.a += [nextLine[nextLine.find('=')+1:]]
    r.rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
    r.caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]
    return r
###########################################################
def main():
    ECHOMAX = 2048
    users={}
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servPort = 15060 #
    servIp = '172.30.60.216' #
    s.bind(('', servPort))    
    print ('socket binded to ',servPort )
    print('Server Started. Listening for requests...')

    while True:
        requestMsgPac, addr = s.recvfrom(ECHOMAX)
        requestMsg=requestMsgPac.decode()
        st = requestMsg.splitlines()
        line1 = st[0]
        typeOfMsg = line1[:line1.find(' ')]
        r= analyze(Req(),st)
        if True:#not ( ('REGISTER' in line1) or ('SUBSCRIBE' in line1) ):
            print('################ received ##########') #
            print(requestMsg) #
            print(addr) #
############################################################
        if 'REGISTER' in line1:
            clientNumber = r.contact[r.contact.find(':')+1:r.contact.find('@')]
            #print('REGISTER request from {}@{}:{}'.format(clientNumber,addr[0],addr[1]))

            isRegistered = clientNumber in users.keys()

            if r.expires.strip() != '' :
                expires = int(r.expires.strip())
                if (not isRegistered) and (expires >0) :
                   print('Phone ' + clientNumber + ' is successfully registered at ip:port '+str(addr))
                   users[clientNumber] = addr
                elif (isRegistered) and (expires==0):
                    print('Phone '+clientNumber+' is succussfully unregistered.')
                    del REGISTERED[clientNumber]
           
            s.sendto(bytes(OK(st), "utf-8"), addr)
############################################################
        if 'SUBSCRIBE' in line1:
            s.sendto(bytes(OK(st), "utf-8"), addr)
############################################################
        if 'INVITE' in line1:
            fwdNumber = r.rcv
            s.sendto(requestMsgPac, users[fwdNumber])
############################################################
        if '100 Trying' in line1:
            fwdNumber = r.caller
            s.sendto(requestMsgPac, users[fwdNumber])
 ############################################################
        if '180 Ringing' in line1:
            fwdNumber = r.caller
            s.sendto(requestMsgPac, users[fwdNumber])
############################################################
        if '200 Ok' in line1:
            fwdNumber = r.caller
            s.sendto(requestMsgPac, users[fwdNumber])
############################################################
        if typeOfMsg == 'ACK':
            fwdNumber = r.rcv
            s.sendto(requestMsgPac, users[fwdNumber])
############################################################
        if '603 Decline' in line1:
            fwdNumber = r.caller
            s.sendto(requestMsgPac, users[fwdNumber])
############################################################
        if typeOfMsg == 'BYE':
            fwdNumber = r.rcv
            s.sendto(requestMsgPac, users[fwdNumber])
############################################################
        if typeOfMsg == 'CANCEL':
            fwdNumber = r.rcv
            s.sendto(requestMsgPac, users[fwdNumber])
###########################################################
        if '487 Request terminated' in line1:
           fwdNumber = r.caller
           s.sendto(requestMsgPac, users[fwdNumber])
############################################################
main()
#############################################################
        #if '481 Call/Transaction Does Not Exist' in line1:
           #send = bytes(OK(st),'utf-8')
           #s.sendto(send, addr)
############################################################
