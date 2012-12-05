import hashlib,hmac,base64
import time
import re

def getSignature(key, sigBase):
	if ( (len(sigBase)==0) | (len(key)==0) ):
		raise Exception('sigBase', 'isNull')

	hashed=hmac.new(key, sigBase, hashlib.sha1)
	outSig=base64.b64encode(hashed.digest())
	return outSig

def getEncodedString(sIn):
	if (len(sIn)==0):
		raise Exception('sIn', 'isNull')

	sOut=""
	exp=re.compile(r'([A-Za-z0-9_]+)')

	for c in sIn:
		if (re.match(exp, c)==None):
			sOut=sOut+"%"+hex(ord(c))[2:]
		elif (c==' '):
			sOut=sOut+"+"
		else:
			sOut=sOut+c

	return sOut

def getAppendedStr(sIn, sParam):
	if ( (len(sIn)==0) | (len(sParam)==0) ):
		raise Exception ('sIn', 'isNull')

	return(sIn+"&"+sParam)

def getAuthHeader(apiUser, apiPass, accessTok, secTok, httpMethod, scriptURI):
	oauthVer="1.0"
	oauthSigMethod="HMAC-SHA1"
	timeStamp=int(time.time())

	# used to sign the signature base below to build the final signature
	key=apiPass
	key=getAppendedStr(key, getEncodedString(secTok))

	sigBase=httpMethod
	sigBase=getAppendedStr(sigBase,getEncodedString(scriptURI))
	# now, NVP params
	sigParm="oauth_consumer_key="+apiUser
	sigParm=getAppendedStr(sigParm,"oauth_signature_method="+oauthSigMethod)
	sigParm=getAppendedStr(sigParm,"oauth_timestamp="+ str(timeStamp))
	sigParm=getAppendedStr(sigParm,"oauth_token="+accessTok)
	sigParm=getAppendedStr(sigParm,"oauth_version="+oauthVer)
	# encode and append
	sigBase=getAppendedStr(sigBase, getEncodedString(sigParm))

	sigFinal=getSignature(key, sigBase)

	return (str(timeStamp),sigFinal)

#if __name__=='__main__':

#	apiUser="apiuser_api1.paypal.com"
#	apiPass="1234567890"
#	accessTok="accessToken"
#	secTok="tokenSecret"
#	httpMethod="POST"
#	scriptURI="https://api-3t.sandbox.paypal.com/nvp";

#	(timeStamp,sig) = \
#		getAuthHeader(apiUser, apiPass, \
#			accessTok, secTok, httpMethod, scriptURI)
#	print(timeStamp, " ", sig)

#	print("X-PP-AUTHORIZATION=timestamp="+timeStamp+\
#		",token="+accessTok+\
#		",signature="+sig)


