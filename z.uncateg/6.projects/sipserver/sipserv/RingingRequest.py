class RingingRequest(Request):
    def __init__(self):
        super.__init__()
        self.via = []
    def forwardRinging(line1, servIP, servPort):
        fwd_res = 'SIP/2.0 180 Ringing\r\n'

        via[0] = via[0][via[0].find(',')+1:] 


        #add via fields
        for i in range( len(via) ):
            fwd_res += 'Via: ' + via[i] + '\r\n' 

        fwd_res += 'From: ' + fromm + '\r\n'
        fwd_res += 'To: ' + to  + '\r\n'
        fwd_res += 'Call-ID: ' + callId + '\r\n'
        fwd_res += 'CSeq: ' + CSeq + '\r\n'
        mod_contact = contact[:contact.find('@')+1] + servIp + '>'
        fwd_res += 'Contact: ' + mod_contact + '\r\n'
        fwd_res += 'User-Agent: ' + userAgent + '\r\n'
        fwd_res += 'Content-Length: 0\r\n\r\n'

        return fwd_res
