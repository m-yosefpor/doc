class OkRequest(Request):
    def forwardOk(self, servIP):
        fwd_res = 'SIP/2.0 200 OK\r\n'
        if ',' in via[0]:
            via[0] = via[0][ via[0].find(',')+1 : ]
        else:
            del via[0]
        



        #add this server's via tag
        via.insert(0 ,  'SIP/2.0/UDP ' + servIp + ':' + servPort + ';branch=z9hG4bK2d4790' )

        #add via fields
        for i in range( len(via) ):
            fwd_res += 'Via: ' + via[i] + '\r\n' 

        fwd_res += 'From: ' + fromm + '\r\n'
        fwd_res += 'To: ' + to  + '\r\n'
        fwd_res += 'Call-ID: ' + callId + '\r\n'
        fwd_res += 'CSeq: ' + CSeq + '\r\n'
        
        if 'CANCEL' in cSeq:
            mod_contact = contact[:contact.find('@')+1] + servIp +'>'
            fwd_res += 'Contact: ' + mod_contact + '\r\n'

        fwd_res += 'Content-Length: ' + contentLength + '\r\n\r\n'

        if not ( ('BYE' in CSeq) or ('CANCEL' in CSeq) ):
            fwd_res += "v=" + v + "\r\n"
            fwd_res += "o=" + o + "\r\n"
            fwd_res += "s=" + s + "\r\n"
            fwd_res += "c=" + c + "\r\n"
            fwd_res += "t=" + t + "\r\n"
            fwd_res += "m=" + m + "\r\n"

            for i in range( len(a) ):
                fwd_res += 'a=' + a[i] + '\r\n' 

        return fwd_res
