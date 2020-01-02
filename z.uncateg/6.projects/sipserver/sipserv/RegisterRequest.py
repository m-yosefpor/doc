class RegisterRequest(Request):
        def __init__(this,via=None,fromm=None,to=None,callId=None,cSeq=None,contact=None,allow=None,maxForwards=None,allowEvents=None,userAgent=None,supported=None,expires=None,contentLength=None):
        if via:
            this.via = via
            this.fromm = fromm
            this.to = to
            this.callId = callId
            this.cSeq = cSeq
            this.contact = contact
            this.allow = allow
            this.maxForwards = maxForwards
            this.allowEvents = allowEvents
            this.userAgent = userAgent
            this.supported = supported
            this.expires = expires
            this.contentLength = contentLength
        else: 
            this.allowEvents = "";
            this.expires = "";      

    def OK_200(self):
    {
        String ok_res = "SIP/2.0 200 OK\r\n";
        
        ok_res = ok_res + "Via: " + via + "\r\n";
        ok_res = ok_res + "From: " + fromm + "\r\n";
        ok_res = ok_res + "To: " + to + "\r\n";
        ok_res = ok_res + "Call-ID: " + callId + "\r\n";
        ok_res = ok_res + "CSeq: " + cSeq + "\r\n";
        ok_res = ok_res + "Contact: " + contact + "\r\n";
        ok_res = ok_res + "Allow: " + allow + "\r\n";
        ok_res = ok_res + "Max-Forwards: " + maxForwards + "\r\n";
        ok_res = ok_res + "Allow-Events: " + allowEvents + "\r\n";
        ok_res = ok_res + "User-Agent: " + userAgent + "\r\n";
        ok_res = ok_res + "Supported: " + supported + "\r\n";
        ok_res = ok_res + "Expires: " + expires + "\r\n";
        ok_res = ok_res + "Content-Length: " + contentLength + "\r\n";
        
        ok_res = ok_res + "\r\n";
        return ok_res
    }
}

