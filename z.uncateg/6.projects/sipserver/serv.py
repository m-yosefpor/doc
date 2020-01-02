import sys
import socket
import time
############################################################
class Request:
    def __init__(self):
        self.allow=''
        self.cSeq=''
        self.callId=''
        self.contact=''
        self.contentLength=''
        self.fromm=''
        self.maxForwards=''
        self.supported=''
        self.to=''
        self.userAgent=''
        self.via=''


class RegisterRequest(Request):
    def __init__(self,via=None,fromm=None,to=None,callId=None,cSeq=None,contact=None,allow=None,maxForwards=None,allowEvents=None,userAgent=None,supported=None,expires=None,contentLength=None):
        super(RegisterRequest,self).__init__()
        if via:
            self.via = via
            self.fromm = fromm
            self.to = to
            self.callId = callId
            self.cSeq = cSeq
            self.contact = contact
            self.allow = allow
            self.maxForwards = maxForwards
            self.allowEvents = allowEvents
            self.userAgent = userAgent
            self.supported = supported
            self.expires = expires
            self.contentLength = contentLength
        else: 
            self.allowEvents = "";
            self.expires = "";      

    def OK_200(self):
        ok_res = "SIP/2.0 200 OK\r\n";
        
        ok_res = ok_res + "Via: " + self.via + "\r\n";
        ok_res = ok_res + "From: " + self.fromm + "\r\n";
        ok_res = ok_res + "To: " + self.to + "\r\n";
        ok_res = ok_res + "Call-ID: " + self.callId + "\r\n";
        ok_res = ok_res + "CSeq: " + self.cSeq + "\r\n";
        ok_res = ok_res + "Contact: " + self.contact + "\r\n";
        ok_res = ok_res + "Allow: " + self.allow + "\r\n";
        ok_res = ok_res + "Max-Forwards: " + self.maxForwards + "\r\n";
        ok_res = ok_res + "Allow-Events: " + self.allowEvents + "\r\n";
        ok_res = ok_res + "User-Agent: " + self.userAgent + "\r\n";
        ok_res = ok_res + "Supported: " + self.supported + "\r\n";
        ok_res = ok_res + "Expires: " + self.expires + "\r\n";
        ok_res = ok_res + "Content-Length: " + self.contentLength + "\r\n";
        
        ok_res = ok_res + "\r\n";
        return ok_res



class InviteRequest(Request):
    def __init__(self):
        super(InviteRequest,self).__init__()
        self.contentType = ''
        self.pEarlyMedia = ''
        self.prefferedIdentity=''

        self.v=''
        self.c=''
        self.m=''
        self.o=''
        self.s=''
        self.t=''
        
        self.a=[]
        self.via = []


    def TRYING_100(self):
        trying_res= 'SIP/2.0 100 TRYING\r\n'

        #add recieved to topmost via field
        upperViaField = self.via[0]
        received = upperViaField[upperViaField.find(' ')+1 : upperViaField.find(':')]
        upperViaField += ';recieved=' + received
        #print(self.via)
        self.via[0] = upperViaField
        for i in range( len(self.via) ):
            trying_res += 'Via: ' + self.via[i] + '\r\n' 

        trying_res += "From: " + self.fromm + "\r\n"
        trying_res += "To: " + self.to + "\r\n"
        trying_res += "Call-ID: " + self.callId + "\r\n"
        trying_res += "CSeq: " + self.cSeq + "\r\n"
        trying_res += "Allow: " + self.allow + "\r\n"
        trying_res += "User-Agent: " + self.userAgent + "\r\n"
        trying_res += "Supported: " + self.supported + "\r\n"
        trying_res += "Content-Length: 0\r\n\r\n"
        return trying_res;
 


    def forwardInvite(self,line1, servIp, servPort):
        fwd_res = line1 + '\r\n'
        #add this server's via tag
        self.via.insert(0 ,  'SIP/2.0/UDP ' + servIp + ':' + str(servPort) + ';branch=z9hG4bK2d4790' )
        #add via fields
        for i in range( len(self.via) ):
            fwd_res += 'Via: ' + self.via[i] + '\r\n' 

        fwd_res += 'From: ' + self.fromm + '\r\n'
        fwd_res += 'To: ' + self.to  + '\r\n'
        fwd_res += 'Call-ID: ' + self.callId + '\r\n'
        fwd_res += 'CSeq: ' + self.cSeq + '\r\n'
        mod_contact = self.contact[:self.contact.find('@')+1] + servIp + '>'
        fwd_res += 'Contact: ' + mod_contact + '\r\n'
        fwd_res += 'Max-Forwards: ' + str(int(self.maxForwards.strip())-1) + '\r\n'
        fwd_res += 'User-Agent: ' + self.userAgent + '\r\n'
        fwd_res += 'Content-Length: ' + self.contentLength + '\r\n\r\n'

        fwd_res += 'v='+self.v + '\r\n'
        fwd_res += 'o='+self.o + '\r\n'
        fwd_res += 's='+self.s + '\r\n'
        fwd_res += 'c='+self.c + '\r\n'
        fwd_res += 't='+self.t + '\r\n'
        fwd_res += 'm='+self.m + '\r\n'

        for i in range( len(self.a) ):
            fwd_res += 'a=' + self.a[i] + '\r\n'

        
        return fwd_res





class RingingRequest(Request):
    def __init__(self):
        super(RingingRequest,self).__init__()
        self.via = []
    def forwardRinging(self,servIp):
        fwd_res = 'SIP/2.0 180 Ringing\r\n'

        self.via[0] = self.via[0][self.via[0].find(',')+1:] 


        #add via fields
        for i in range( len(self.via) ):
            fwd_res += 'Via: ' + self.via[i] + '\r\n' 

        fwd_res += 'From: ' + self.fromm + '\r\n'
        fwd_res += 'To: ' + self.to  + '\r\n'
        fwd_res += 'Call-ID: ' + self.callId + '\r\n'
        fwd_res += 'CSeq: ' + self.cSeq + '\r\n'
        mod_contact = self.contact[:self.contact.find('@')+1] + servIp + '>'
        fwd_res += 'Contact: ' + mod_contact + '\r\n'
        fwd_res += 'User-Agent: ' + self.userAgent + '\r\n'
        fwd_res += 'Content-Length: 0\r\n\r\n'

        return fwd_res


class AckRequest(Request):
    def __init__(self):
        super(AckRequest).__init__()
        self.via = []


    def forwardAck(self,line1,servIp,servPort):
        fwd_res = line1 + '\r\n'

        #add received to topmost via field
        upperViaField = self.via[0]
        received = upperViaField[upperViaField.find(' ')+1 : upperViaField.find(':')]
        upperViaField += ';recieved=' + received
        self.via[0] = upperViaField

        #add this server's via tag
        self.via.insert(0 ,  'SIP/2.0/UDP ' + servIp + ':' + str(servPort) + ';branch=z9hG4bK2d4790' )

        #add via fields
        for i in range( len(self.via) ):
            fwd_res += 'Via: ' + self.via[i] + '\r\n' 

        fwd_res += 'From: ' + self.fromm + '\r\n'
        fwd_res += 'To: ' + self.to  + '\r\n'
        fwd_res += 'Call-ID: ' + self.callId + '\r\n'
        fwd_res += 'CSeq: ' + self.cSeq + '\r\n'
        #fwd_res += 'Contact: ' + self.contact + '\r\n'
        fwd_res += 'Content-Length: 0\r\n\r\n'

        return fwd_res


class ByeRequest(Request):
    def __init__(self):
        super(ByeRequest,self).__init__()
        self.via = []
    def forwardBye(self,line1, servIp, servPort):
        fwd_res = line1 + '\r\n'

        #add recieved to topmost via field
        upperViaField = self.via[0]
        received = upperViaField[upperViaField.find(' ')+1 : upperViaField.find(':')]
        upperViaField += ';recieved=' + received
        self.via[0] = upperViaField

        #add this server's via tag
        self.via.insert(0 ,  'SIP/2.0/UDP ' + servIp + ':' + str(servPort) + ';branch=z9hG4bK2d4790' )

        #add via fields
        for i in range( len(self.via) ):
            fwd_res += 'Via: ' + self.via[i] + '\r\n' 

        fwd_res += 'From: ' + self.fromm + '\r\n'
        fwd_res += 'To: ' + self.to  + '\r\n'
        fwd_res += 'Call-ID: ' + self.callId + '\r\n'
        fwd_res += 'CSeq: ' + self.cSeq + '\r\n'
        mod_contact = self.contact[:self.contact.find('@')+1] + servIp + '>'
        fwd_res += 'Contact: ' + mod_contact + '\r\n'
        fwd_res += 'Max-Forwards: ' + str(int(self.maxForwards.strip())-1) + '\r\n'
        fwd_res += 'User-Agent: ' + self.userAgent + '\r\n'
        fwd_res += 'Content-Length: ' + self.contentLength + '\r\n\r\n'

        return fwd_res



class CallDetails:
    def __init__(self):
        self.caller = ''
        self.called = ''



class CancelRequest(Request):
    def __init__(self):
        super(CancelRequest,self).__init__()
        self.via = []
    def forwardCancel(self,line1, servIp, servPort):
        fwd_res = line1 + '\r\n'

        #add recieved to topmost via field
        upperViaField = self.via[0]
        received = upperViaField[upperViaField.find(' ')+1 : upperViaField.find(':')]
        upperViaField += ';recieved=' + received
        self.via[0] = upperViaField

        #add this server's via tag
        self.via.insert(0 ,  'SIP/2.0/UDP ' + servIp + ':' + str(servPort) + ';branch=z9hG4bK2d4790' )

        #add via fields
        for i in range( len(self.via) ):
            fwd_res += 'Via: ' + self.via[i] + '\r\n' 

        fwd_res += 'From: ' + self.fromm + '\r\n'
        fwd_res += 'To: ' + self.to  + '\r\n'
        fwd_res += 'Call-ID: ' + self.callId + '\r\n'
        fwd_res += 'CSeq: ' + self.cSeq + '\r\n'
        fwd_res += 'Max-Forwards: ' + str(int(self.maxForwards.strip())-1) + '\r\n'
        fwd_res += 'User-Agent: ' + self.userAgent + '\r\n'
        fwd_res += 'Content-Length: 0\r\n\r\n'

        return fwd_res



class OkRequest(InviteRequest):
    def forwardOk(self, servIp):
        fwd_res = 'SIP/2.0 200 OK\r\n'
        if ',' in self.via[0]:
            self.via[0] = self.via[0][ self.via[0].find(',')+1 : ]
        else:
            del self.via[0]

        #add via fields
        for i in range( len(self.via) ):
            fwd_res += 'Via: ' + self.via[i] + '\r\n' 

        fwd_res += 'From: ' + self.fromm + '\r\n'
        fwd_res += 'To: ' + self.to  + '\r\n'
        fwd_res += 'Call-ID: ' + self.callId + '\r\n'
        fwd_res += 'CSeq: ' + self.cSeq + '\r\n'
        
        if 'CANCEL' in self.cSeq:
            mod_contact = self.contact[:self.contact.find('@')+1] + servIp +'>'
            fwd_res += 'Contact: ' + mod_contact + '\r\n'

        fwd_res += 'Content-Length: ' + self.contentLength + '\r\n\r\n'

        if not ( ('BYE' in self.cSeq) or ('CANCEL' in self.cSeq) ):
            fwd_res += "v=" + self.v + "\r\n"
            fwd_res += "o=" + self.o + "\r\n"
            fwd_res += "s=" + self.s + "\r\n"
            fwd_res += "c=" + self.c + "\r\n"
            fwd_res += "t=" + self.t + "\r\n"
            fwd_res += "m=" + self.m + "\r\n"

            for i in range( len(self.a) ):
                fwd_res += 'a=' + self.a[i] + '\r\n' 

        return fwd_res





class RequestTerminatedRequest(Request):
    def __init__(self):
        super(RequestTerminatedRequest,self).__init__()
        self.via = []
    def forwardRequestTerminated(self,line1, servIp, servPort):
        fwd_res = line1 + '\r\n'

        if ',' in self.via[0]:
            self.via[0] = self.via[0][self.via[0].find(',')+1:]
        else:
            del self.via[0]

        #add via fields
        for i in range( len(self.via) ):
            fwd_res += 'Via: ' + self.via[i] + '\r\n' 

        fwd_res += 'From: ' + self.fromm + '\r\n'
        fwd_res += 'To: ' + self.to  + '\r\n'
        fwd_res += 'Call-ID: ' + self.callId + '\r\n'
        fwd_res += 'CSeq: ' + self.cSeq + '\r\n'
        mod_contact = self.contact[:self.contact.find('@')+1] + servIp + '>'
        fwd_res += 'Contact: ' + mod_contact + '\r\n'
        fwd_res += 'User-Agent: ' + self.userAgent + '\r\n'
        fwd_res += 'Content-Length: ' + self.contentLength + '\r\n\r\n'

        return fwd_res

#####
def OK(st):
    st[0] = 'SIP/2.0 200 OK'
    res=''
    for l in st:
        res += l +'\r\n'
    return res

######
def DECLINE(st):
    st[0] = 'SIP/2.0 200 OK'
    res=''
    for l in st:
        res += l +'\r\n'
    return res

############################################################
def analyze(r,st):
    for nextLine in st : 
        fieldName = nextLine[:nextLine.find(":")];
        if("Via"==fieldName):
            r.via += [nextLine[nextLine.find(" ")+1:]]
        elif("From"==fieldName):
            r.fromm = nextLine[nextLine.find(" ")+1:];
        elif("To"==fieldName):
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
    return r

###########################################################

def main():
    ECHOMAX = 2048
    REGISTERED = {}
    CURRENTCALLS = {}
    users={}

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    servPort=int( input('Enter the port of the server: ') )
    #servPort = 15060 #

    #servIp = input('Enter the IP address of the server : ')
    servIp = '172.30.60.216' #

    s.bind(('', servPort))    
    print ('socket binded to ',servPort )
    print('Server Started. Listening for requests...')

    while True:
        requestMsgPac, addr = s.recvfrom(ECHOMAX)
        requestMsg=requestMsgPac.decode()

        clientAddress = addr[0]
        clientPort= addr[1]

        st = requestMsg.splitlines()
        line1 = st[0]
        typeOfMsg = line1[ : line1.find(' ') ]

        if not (  ('REGISTER' in line1) or ('SUBSCRIBE' in line1) or (requestMsg.strip()=='') ):
            print('################ received ##########') #
            print(requestMsg) #
            print(addr) #

############################################################
        if typeOfMsg == 'REGISTER':
            #print('register req') #
            #time.sleep(4) #
            r = RegisterRequest() 
            for nextLine in st : 
                fieldName = nextLine[:nextLine.find(":")];
                #print(fieldName) #
                if("Via"==fieldName):
                    r.via = nextLine[nextLine.find(" ")+1:]
                elif("From"==fieldName):
                    r.fromm = nextLine[nextLine.find(" ")+1:];
                elif("To"==fieldName):
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
                elif("Content-Length"==fieldName):
                    r.contentLength = nextLine[nextLine.find(" ")+1:];

            clientNumber = r.contact[r.contact.find(':')+1:r.contact.find('@')]
            print('REGISTER request from {}@{}:{}'.format(clientNumber,clientAddress,clientPort))

            isRegistered = clientNumber in REGISTERED.keys()

            if r.expires.strip() != '' :
                expires = int(r.expires.strip())
                if (not isRegistered) and (expires >0) :
                   print('Phone ' + clientNumber + ' is successfully registered at ip:port '+clientAddress + ':' +str(clientPort) )
                   REGISTERED[clientNumber]=(clientPort,clientAddress)
                   users[clientNumber]=addr
                elif (isRegistered) and (expires==0):
                    print('Phone '+clientNumber+' is succussfully unregistered.')
                    del REGISTERED[clientNumber]
           
            #send OK response 
            s.sendto(bytes(OK(st), "utf-8"), addr)

            #print('OK_200 forwarded to {}@{}:{}'.format(clientNumber,clientAddress,clientPort))
            #print( '### ok ####')
            #print(r.OK_200())

############################################################
        if typeOfMsg == 'SUBSCRIBE':
            s.sendto(bytes(OK(st), "utf-8"), addr)
            #print('OK_200 forwarded to {}:{}'.format(clientAddress,clientPort))
            #print( '### ok ####')
            #print(r.OK_200())

############################################################
        if typeOfMsg == 'INVITE':
            r = analyze(InviteRequest(),st)   
          
            #sender of the invitation
            clientNumber = r.contact[r.contact.find(':')+1:r.contact.find('@')]
            #recipient of the invitation
            calleeNumber = line1[line1.find(':')+1:line1.find('@')]
            #print('calleeNumber',calleeNumber)
            #print(REGISTERED)
            calleeIp = REGISTERED[calleeNumber][1]
            calleePort = REGISTERED[calleeNumber][0]

            print('INVITE request coming from '+clientNumber + ' to ' + calleeNumber + ' .')

            #try back to caller
            #s.sendto(bytes(r.TRYING_100(), "utf-8"), (clientAddress, clientPort))
            print( 'TRYING_100 sent to {}@{}:{}'.format(clientNumber,clientAddress,clientPort))
            #print( '### try ####') #
            #print(r.TRYING_100()) #

            #Now forward this packet to callee
            #send1 = bytes(r.forwardInvite(line1, servIp , servPort),'utf-8')
            #s.sendto(send1, (calleeIp, calleePort))

            rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
            caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]

            fwdNumber = rcv
            s.sendto(requestMsgPac, users[fwdNumber])

            print( 'INVITE forwarded to {}@{}:{}'.format(calleeNumber,calleeIp,calleePort))
            #print( '### invit forward ####') #
            #print(send1.decode()) #

            #add details to CURRENTCALLS
            cd = CallDetails()
            cd.caller = clientNumber
            cd.called = calleeNumber

            callId = r.callId[:r.callId.find('@')]
            CURRENTCALLS[callId] = cd

############################################################
        if '100 Trying' in line1:
            r = analyze(InviteRequest(),st)

            rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
            caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]

            fwdNumber = caller
            s.sendto(requestMsgPac, users[fwdNumber])

 ############################################################
 
        if line1 == 'SIP/2.0 180 Ringing':
            r = analyze(RingingRequest(),st)
            clientNumber = r.contact[r.contact.find(':')+1:r.contact.find('@')]
            print('Ringing response coming from '+clientNumber )
            #extracting details of recipient
            fwdIp = REGISTERED[fwdNumber][1]
            fwdPort = REGISTERED[fwdNumber][0]
            rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
            caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]
            fwdNumber = caller
            s.sendto(requestMsgPac, users[fwdNumber])
            #forward ringing
            #send = bytes(r.forwardRinging(servIp),'utf-8')
            #s.sendto(send, (fwdIp,fwdPort))
            print('Ringing forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')
            #print( '### ring forward ####') #
            #print(send.decode()) #

############################################################
        if line1 == 'SIP/2.0 200 Ok':
            r = analyze(OkRequest(),st)
            clientNumber = r.contact[r.contact.find(':')+1:r.contact.find('@')]
            print('OK response coming from '+clientNumber )
            #recepient of fwd OK
            fwdIp = REGISTERED[fwdNumber][1]
            fwdPort = REGISTERED[fwdNumber][0]
            rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
            caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]
            fwdNumber = caller
            s.sendto(requestMsgPac, users[fwdNumber])
            #forward OK
            #send = bytes(r.forwardOk(servIp),'utf-8')
            #s.sendto(send, (fwdIp,fwdPort))
            #print( '### ok forward ####') #
            #print(send.decode()) #
            print('OK forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')

############################################################
        if typeOfMsg == 'ACK':
            r = analyze(AckRequest(), st)

            #recepient of fwd ACK
            fwdIp = REGISTERED[fwdNumber][1]
            fwdPort = REGISTERED[fwdNumber][0]
            rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
            caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]
            #forward Ack
            fwdNumber = rcv
            s.sendto(requestMsgPac, users[fwdNumber])
            #print('Ack forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')
            #send = bytes(r.forwardAck(line1,servIp, servPort),'utf-8')
            #s.sendto(send, (fwdIp,fwdPort))
            #print( '### ack forward ####') #
            #print(send.decode()) #

############################################################
        if 'Decline' in line1:
            r= analyze(CancelRequest(),st)
            send = bytes(OK(st),'utf-8')
            s.sendto(send,addr)
            print('ok responded')
            
            #recepient of CANCEL
            fwdIp = REGISTERED[fwdNumber][1]
            fwdPort = REGISTERED[fwdNumber][0]
            rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
            caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]

            fwdNumber = caller
            s.sendto(requestMsgPac, users[fwdNumber])
            #forward BYE
            #send = bytes(r.forwardCancel(line1,servIp, servPort),'utf-8')
            #s.sendto(send, (fwdIp,fwdPort))

############################################################
        if typeOfMsg == 'BYE':
            r = analyze(ByeRequest() , st)
            clientNumber = r.contact[r.contact.find(':')+1:r.contact.find('@')]

            #recepient of fwd BYE 
            fwdIp = REGISTERED[fwdNumber][1]
            fwdPort = REGISTERED[fwdNumber][0]
            rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
            caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]
            #print('BYE request coming from '+clientNumber + ' to ' + fwdNumber + ' .')

            #forward BYE
            fwdNumber = rcv
            s.sendto(requestMsgPac, users[fwdNumber])
            #send = bytes(r.forwardBye(line1,servIp, servPort),'utf-8')
            #s.sendto(send, (fwdIp,fwdPort))
            print('BYE forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')
            #print( '### bye forward ####') #
            #print(send.decode()) #
            
            #remove this call from CURRENTCALLS
            callId = r.callId[:r.callId.find('@')]
            if callId in CURRENTCALLS.keys():
                print( 'The call from '+ CURRENTCALLS[callId].caller + ' to '+CURRENTCALLS[callId].called + ' has been ENDED.')
                del CURRENTCALLS[callId]

############################################################
        if typeOfMsg == 'CANCEL':
            r= analyze(CancelRequest(),st)
            clientNumber = r.fromm[r.fromm.find(':')+1:r.fromm.find('@')]
            print('CANCEL request coming from '+clientNumber )
            send = bytes(OK(st),'utf-8')
            s.sendto(send, addr)
            print('ok responded')
            #recepient of fwd cancel
            fwdNumber = r.to[r.to.find(':')+1 : r.to.find('@')]
            #print('canceled fwd',fwdNumber)
            #print(r.to)
            fwdIp = REGISTERED[fwdNumber][1]
            fwdPort = REGISTERED[fwdNumber][0]
            rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
            caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]

            print('CANCEL forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')

            #forward CANCEL
            fwdNumber = rcv
            s.sendto(requestMsgPac, users[fwdNumber])
            send = bytes(r.forwardCancel(line1,servIp, servPort),'utf-8')
            s.sendto(send, (fwdIp,fwdPort))
            #print( '### cancel forward ####') #
            #print(send.decode()) #
            
            #remove callDetails
            callId = r.callId[:r.callId.find('@')]
            if callId in CURRENTCALLS.keys():
                del CURRENTCALLS[callId]

############################################################
        if '487 Request' in line1:
            r = RequestTerminatedRequest()
            for nextLine in st : 
                fieldName = nextLine[:nextLine.find(":")];
                #print(fieldName) #
                if("Via"==fieldName):
                    r.via += [nextLine[nextLine.find(" ")+1:]]
                elif("From"==fieldName):
                    r.fromm = nextLine[nextLine.find(" ")+1:];
                elif("To"==fieldName):
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
                elif("Content-Type"==fieldName):
                    r.contentType = nextLine[nextLine.find(" ")+1:];
                elif("User-Agent"==fieldName):
                    r.userAgent = nextLine[nextLine.find(" ")+1:];
                elif("Supported"==fieldName):
                    r.supported = nextLine[nextLine.find(" ")+1:];
                elif("Expires"==fieldName):
                    r.expires = nextLine[nextLine.find(" ")+1:];
                elif("P-Early-Media"==fieldName):
                    r.pEarlyMedia = nextLine[nextLine.find(" ")+1:];
                elif("P-Preferred-Identity"==fieldName):
                    r.preferredIdentity = nextLine[nextLine.find(" ")+1:];
                elif("Content-Length"==fieldName):
                    r.contentLength = nextLine[nextLine.find(" ")+1:];
      
            #recepient of fwd cancel
            fwdIp = REGISTERED[fwdNumber][1]
            fwdPort = REGISTERED[fwdNumber][0]
            rcv = r.to[r.to.find(':')+1 : r.to.find('@')]
            caller = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]

            fwdNumber = caller
            s.sendto(requestMsgPac, users[fwdNumber])
            print('Request Terminated forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')

            #forward 487
            send = bytes(r.forwardRequestTerminated(line1,servIp, servPort),'utf-8')
            s.sendto(send, (fwdIp,fwdPort))
            #print( '### cancel forward ####') #
            #print(send.decode()) #

############################################################
        if line1 == '486 Busy':
            r = requestTerminatedRequest()
            for nextLine in st : 
                fieldName = nextLine[:nextLine.find(":")];
                #print(fieldName) #
                if("Via"==fieldName):
                    r.via += [nextLine[nextLine.find(" ")+1:]]
                elif("From"==fieldName):
                    r.fromm = nextLine[nextLine.find(" ")+1:];
                elif("To"==fieldName):
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
                elif("Content-Type"==fieldName):
                    r.contentType = nextLine[nextLine.find(" ")+1:];
                elif("User-Agent"==fieldName):
                    r.userAgent = nextLine[nextLine.find(" ")+1:];
                elif("Supported"==fieldName):
                    r.supported = nextLine[nextLine.find(" ")+1:];
                elif("Expires"==fieldName):
                    r.expires = nextLine[nextLine.find(" ")+1:];
                elif("P-Early-Media"==fieldName):
                    r.pEarlyMedia = nextLine[nextLine.find(" ")+1:];
                elif("P-Preferred-Identity"==fieldName):
                    r.preferredIdentity = nextLine[nextLine.find(" ")+1:];
                elif("Content-Length"==fieldName):
                    r.contentLength = nextLine[nextLine.find(" ")+1:];
            #recepient of fwd cancel
            fwdNumber = r.to[r.fromm.find(':')+1 : r.fromm.find('@')]
            fwdIp = REGISTERED[fwdNumber][1]
            fwdPort = REGISTERED[fwdNumber][0]

            print('CANCEL forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')

            #forward CANCEL
            send = bytes(r.forwardCancel(line1,servIp, servPort),'utf-8')
            s.sendto(send, (fwdIp,fwdPort))
            #print( '### cancel forward ####') #
            #print(send.decode()) #
              
            #remove callDetails
            callId = r.callId[:r.callId.find('@')]
            if callId in CURRENTCALLS.keys():
                del CURRENTCALLS[callId]

############################################################
        if '481 Call/Transaction Does Not Exist' in line1:
           send = bytes(OK(st),'utf-8')
           s.sendto(send, addr)
           print('ok responded')

############################################################

#while True:
    #try :
        #main()
    #except:
        #print('An Error Occured, server restarted') 

main()
############################################################
