import botocore.session
import boto3
import time
session = botocore.session.get_session()
session.profile = 'dualspark'
session.region = 'us-west-2'
boto3.setup_default_session(botocore_session=session,region_name='us-west-2')
#dynamodb = boto3.client('dynamodb')
#data = dynamodb.get_item(TableName='endpoints', AttributesToGet=['url'], Key={'env':'prod', 'layer':'edge'})
sample = {"First" : "John", "Last" : "Smith", "SSN" : "123456789", "Title" : "Amazing Officer", "Phone" : "9495551234", "DOB" : "01-01-1950"}
print "Begin: " + str(sample)

class encrypt():
stime=(time.time())
kms = boto3.client('kms')
secure_ssn= kms.encrypt(KeyId="1bf0f635-d4c4-43d6-b720-f46d3c5a66ef", Plaintext=sample['SSN'])['CiphertextBlob']
ftime=time.time()
print str(ftime-stime) + " is how many seconds it took to encrypt the data and send it back"
sample['SSN'] = secure_ssn
print "Middle: " + str(sample)


sampled=sample
sec_ssn=sampled['SSN']
plain_ssn=kms.decrypt(CiphertextBlob=sec_ssn)['Plaintext']
sampled['SSN'] = plain_ssn
print "End: " + str(sampled)
etime=(time.time())
ttime=etime-stime
print "finish round trip in "+str(ttime) + " seconds"