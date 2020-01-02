class InviteRequest(Request):
    def __init__(self):
        super.__init__()
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
        self.vai = []


    def TRYING_100(self):
        trying_res= 'SIP/2.0 100 TRYING\r\n'

        #add recieved to topmost via field
        upperViaField = via[0]
        received = upperViaField[upperViaField.find(' ')+1 : upperViaField.find(':')]
        upperViaField += ';recieved=' + received
        via[0] = upperViaField
        for i in range( len(via) ):
            trying_res += 'Via: ' + via[i] + '\r\n' 

        trying_res += "From: " + fromm + "\r\n"
        trying_res += "To: " + to + "\r\n"
        trying_res += "Call-ID: " + callId + "\r\n"
        trying_res += "CSeq: " + cSeq + "\r\n"
        trying_res += "Allow: " + allow + "\r\n"
        trying_res += "User-Agent: " + userAgent + "\r\n"
        trying_res += "Supported: " + supported + "\r\n"
        trying_res += "Content-Length: 0\r\n\r\n"
        return trying_res;
 


    def ForwardInvite(self,line1, servIP, servPort):
        fwd_res = line1 + '\r\n'

        #add this server's via tag
        via.insert(0 ,  'SIP/2.0/UDP ' + servIp + ':' + servPort + ';branch=z9hG4bK2d4790' )

        #add via fields
        for i in range( len(via) ):
            fwd_res += 'Via: ' + via[i] + '\r\n' 

        fwd_res += 'From: ' + fromm + '\r\n'
        fwd_res += 'To: ' + to  + '\r\n'
        fwd_res += 'Call-ID: ' + callId + '\r\n'
        fwd_res += 'CSeq: ' + CSeq + '\r\n'
        mod_contact = contact[:contact.find('@')+1] + servIp + '>'
        fwd_res += 'Contact: ' + mod_contact + '\r\n'
        fwd_res += 'Max-Forwards: ' + (int(maxForwards.strip())-1) + '\r\n'
        fwd_res += 'User-Agent: ' + userAgent + '\r\n'
        fwd_res += 'Content-Length: ' + contentLength + '\r\n\r\n'

        fwd_res += 'v='+ + 'v\r\n'
        fwd_res += 'o='+ + 'o\r\n'
        fwd_res += 's='+ + 's\r\n'
        fwd_res += 'c='+ + 'c\r\n'
        fwd_res += 't='+ + 't\r\n'
        fwd_res += 'm='+ + 'm\r\n'

        for i in range( len(a) ):
            fwd_res += 'a=' + a[i] + '\r\n'

        
        return fwd_res
