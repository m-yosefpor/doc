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
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')
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
        fwd_res += 'Contact: ' + self.contact + '\r\n'
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



