class CancelRequest(Request):
    def __init__(self):
        super(CancelRequest,self).__init__()
        self.via = []
    def forwardCancel(line1, servIP, servPort):
        fwd_res = line1 + '\r\n'

        #add recieved to topmost via field
        upperViaField = via[0]
        received = upperViaField[upperViaField.find(' ')+1 : upperViaField.find(':')]
        upperViaField += ';recieved=' + received
        via[0] = upperViaField

        #add this server's via tag
        via.insert(0 ,  'SIP/2.0/UDP ' + servIp + ':' + servPort + ';branch=z9hG4bK2d4790' )

        #add via fields
        for i in range( len(via) ):
            fwd_res += 'Via: ' + via[i] + '\r\n' 

        fwd_res += 'From: ' + fromm + '\r\n'
        fwd_res += 'To: ' + to  + '\r\n'
        fwd_res += 'Call-ID: ' + callId + '\r\n'
        fwd_res += 'CSeq: ' + CSeq + '\r\n'
        fwd_res += 'Max-Forwards: ' + (int(maxForwards.strip())-1) + '\r\n'
        fwd_res += 'User-Agent: ' + userAgent + '\r\n'
        fwd_res += 'Content-Length: 0\r\n\r\n'

        return fwd_res
