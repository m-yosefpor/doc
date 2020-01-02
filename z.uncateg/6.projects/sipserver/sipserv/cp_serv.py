import sys
import socket
import time
import req
############################################################
def extractIpOrPort(field,choice): #Returns IP or PORT from SIP URI
    if choice == 0: #returns IP if choice == 0
        return field[: field.find(":")]
    else: #else returns PORT
        return int(field[field.find(":")+1:])

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
        elif('v'==fieldName):
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
            r.a = nextLine[nextLine.find('=')+1:]
    return r

############################################################

def main():
    ECHOMAX = 2048
    REGISTERED = {}
    CURRENTCALLS = {}

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #servPort=int( input('Enter the port of the server: ') )
    servPort = 5060 #

    #servIp = input('Enter the IP address of the server : ')
    servIp = '172.30.60.191' #

    s.bind(('', servPort))    
    print ('socket binded to ',servPort )
    print('Server Started. Listening for requests...')

    while True:
        requestMsg, addr = s.recvfrom(ECHOMAX)
        requestMsg=requestMsg.decode()
        clientAddress = addr[0]
        clientPort= addr[1]
        print('################ received ##########') #
        print(requestMsg) #
        #print(addr) #
        st = requestMsg.splitlines()
        line1 = st[0]
        typeOfMsg = line1[ : requestMsg.find(' ') ]

        if typeOfMsg == 'REGISTER':
            #print('register req') #
            #time.sleep(4) #
            r = req.RegisterRequest() 
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

            clientNumber = r.contact[:r.contact.find('@')]
            
            print('REGISTER comming from {}@{}:{}'.format(number,clientAddress,clientPort))

            isRegistered = number in REGISTERED.keys()

            if r.expires.strip() != '' :
                expires = int(r.expires.strip())
                if (not isRegistered) and (expires >0) :
                   print('Phone ' + number + ' is successfully registered at ip:port ' +ipPort + ' .')
                   REGISTERED[number]=ipPort
                elif (isRegistered) and (expires==0):
                    print('Phone '+number+' is succussfully unregistered.')
                    del REGISTERED[number]
           
            #send OK response to caller
            s.sendto(bytes(r.OK_200(), "utf-8"), (clientAddress, clientPort))
            print('OK_200 forwarded to {}@{}:{}'.format(number,clientAddress,clientPort))
            print( '### ok ####')
            print(r.OK_200())

    ##################3
        if typeOfMsg == 'SUBSCRIBE':
            r = req.RegisterRequest() 
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

            sipUri = r.contact[r.contact.find(':')+1 : r.contact.find(';')]
            if '>' in sipUri:
                number = sipUri[:sipUri.find('@')]
                ipPort = sipUri[sipUri.find('@')+1:-1]
            else:
                number = sipUri[:sipUri.find('@')]
                ipPort = sipUri[sipUri.find('@')+1:]

            
            print('SUBSCRIBE comming from {}@{}:{}'.format(number,clientAddress,clientPort))

            #send OK response to caller
            s.sendto(bytes(r.OK_200(), "utf-8"), (clientAddress, clientPort))
            print('OK_200 forwarded to {}@{}:{}'.format(number,clientAddress,clientPort))
            #print( '### ok ####')
            #print(r.OK_200())



    ###################

        if typeOfMsg == 'INVITE':
            r = req.InviteRequest() #make this class
            r = analyze(r,st)   
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
                elif('v'==fieldName):
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
                    r.a = nextLine[nextLine.find('=')+1:]


            #sender of the invitation
            callerNumber = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]

            #recipient of the invitation
            calleeNumber = line1[line1.find(':')+1:line1.find('@')]
            #print('calleeNumber',calleeNumber)
            #print(REGISTERED)
            calleeIp = extractIpOrPort(REGISTERED[calleeNumber],0)
            calleePort = extractIpOrPort(REGISTERED[calleeNumber],1)

            print('INVITE request coming from '+callerNumber + ' to ' + calleeNumber + ' .')

            #try back to caller
            s.sendto(bytes(r.TRYING_100(), "utf-8"), (clientAddress, clientPort))
            print( 'TRYING_100 sent to {}@{}:{}'.format(callerNumber,clientAddress,clientPort))
            #print( '### try ####') #
            #print(r.TRYING_100()) #

            #Now forward this packet to callee

            send1 = bytes(r.forwardInvite(line1, servIp , servPort),'utf-8')
            s.sendto(send1, (calleeIp, calleePort))

            print( 'INVITE forwarded to {}@{}:{}'.format(calleeNumber,calleeIp,calleePort))
            #print( '### invit forward ####') #
            #print(send1.decode()) #

            #add details to CURRENTCALLS
            cd = req.CallDetails()
            cd.caller = callerNumber
            cd.called = calleeNumber

            callId = r.callId[:r.callId.find('@')]
            CURRENTCALLS[callId] = cd


        if line1 == 'SIP/2.0 180 Ringing':
            r = req.RingingRequest()
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
                
            rcvNumber = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')] ############## to __ fromm
            #extracting details of recipient
            fwdNumber = r.to[r.to.find(':')+1 : r.to.find('@')] ############## to __ fromm
            fwdIp = extractIpOrPort(REGISTERED[fwdNumber],0)
            fwdPort = extractIpOrPort(REGISTERED[fwdNumber],1)
            
            print('Ringing request coming from '+rcvNumber + ' to ' + fwdNumber + ' .')


            #forward ringing
            send = bytes(r.forwardRinging(line1,servIp,servPort),'utf-8')
            s.sendto(send, (fwdIp,fwdPort))
            print('Ringing forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')
            #print( '### ring forward ####') #
            #print(send.decode()) #



        if line1 == 'SIP/2.0 200 OK':
            r = req.OkRequest()
     
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
                elif('v'==fieldName):
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
                    r.a = nextLine[nextLine.find('=')+1:]

            fwdNumber = r.to[r.to.find(':')+1 : r.fromm.find('@')]
            #recepient of fwd OK
            rcvNumber = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]
            rcvIp = extractIpOrPort(REGISTERED[fwdNumber],0)
            rcvPort = extractIpOrPort(REGISTERED[fwdNumber],1)

            print('OK request coming from '+rcvNumber + ' to ' + fwdNumber + ' .')

            #forward OK
            send = bytes(r.forwardOk(servIp,servPort),'utf-8')
            s.sendto(send, (rcvIp,rcvPort))
            #print( '### ok forward ####') #
            #print(send.decode()) #
            print('OK forwarded to '+str(rcvNumber)+' at ip:port '+rcvIp+':'+str(rcvPort)+' .')

        if typeOfMsg == 'ACK':
            r = req.AckRequest()
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
      
            #recepient of fwd ACK
            fwdNumber = r.to[r.fromm.find(':')+1 : r.fromm.find('@')]
            fwdIp = extractIpOrPort(REGISTERED[fwdNumber],0)
            fwdPort = extractIpOrPort(REGISTERED[fwdNumber],1)

            print('Ack forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')

            #forward Ack
            send = bytes(r.forwardAck(line1,servIp, servPort),'utf-8')
            s.sendto(send, (fwdIp,fwdPort))
            #print( '### ack forward ####') #
            #print(send.decode()) #

        

        if typeOfMsg == 'BYE':
            r = req.ByeRequest()
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
      
            rcvNumber = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]
            #recepient of fwd BYE 
            fwdNumber = r.to[r.to.find(':')+1 : r.to.find('@')]
            fwdIp = extractIpOrPort(REGISTERED[fwdNumber],0)
            fwdPort = extractIpOrPort(REGISTERED[fwdNumber],1)
            print('BYE request coming from '+rcvNumber + ' to ' + fwdNumber + ' .')


            #forward BYE
            send = bytes(r.forwardBye(line1,servIp, servPort),'utf-8')
            s.sendto(send, (fwdIp,fwdPort))
            print('BYE forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')
            #print( '### bye forward ####') #
            #print(send.decode()) #
            
            #remove this call from CURRENTCALLS
            callId = r.callId[:r.callId.find('@')]
    ### 471
            if callId in CURRENTCALLS.keys():
                print( 'The call from '+ CURRENTCALLS[callId].caller + ' to '+CURRENTCALLS[callId].called + ' has been ENDED.')
                del CURRENTCALLS[callId]
        if typeOfMsg == 'CANCEL':
            r=req.CancelRequest()
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
            fwdIp = extractIpOrPort(REGISTERED[fwdNumber],0)
            fwdPort = extractIpOrPort(REGISTERED[fwdNumber],1)

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

        if '487 Request' in line1:
            r = req.requestTerminatedRequest()
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
            fwdNumber = r.fromm[r.fromm.find(':')+1 : r.fromm.find('@')]
            fwdIp = extractIpOrPort(REGISTERED[fwdNumber],0)
            fwdPort = extractIpOrPort(REGISTERED[fwdNumber],1)

            print('Request Terminated forwarded to '+str(fwdNumber)+' at ip:port '+fwdIp+':'+str(fwdPort)+' .')

            #forward 487
            send = bytes(r.forwardrequestTerminated(line1,servIp, servPort),'utf-8')
            s.sendto(send, (fwdIp,fwdPort))
            #print( '### cancel forward ####') #
            #print(send.decode()) #


            ### 586
        if line1 == '486 Busy':
            r = req.requestTerminatedRequest()
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
            fwdIp = extractIpOrPort(REGISTERED[fwdNumber],0)
            fwdPort = extractIpOrPort(REGISTERED[fwdNumber],1)

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
#while True:
    #try :
        #main()
    #except:
        #print('An Error Occured, server restarted') 

main()
############################################################
