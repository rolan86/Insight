import boto3
import json
from exceptions import Error, BotoApiError


class VPCInfo(object):

    #@static_method
    #def dumpfile(self, obj):
    #    with open('data/vpc.json', 'w') as fh:
    #        json.dump(resp, fh, indent=4, default=str)

    def __init__(self):
        self.ec2_client = boto3.client('ec2')

    def get_ec2_client(self):
        return self.ec2_client
 
    def dumpfile(self, obj):
        with open('data/vpc.json', 'w') as fh:
            json.dump(obj, fh, indent=4, default=str)
        return

    def get_vpcs(self):
        client = self.get_ec2_client()

        try:
            resp = client.describe_vpcs()
            if resp is None:
                raise BotoApiError

            # Dumping the complete response in json file
            #with open('data/vpc.json', 'w') as fh:
            #    json.dump(resp, fh, indent=4, default=str)
            self.dumpfile(resp)
            return resp
        except BotoApiError:
            print "Boto API error."
        except IOError:
            print "File not found."
        #except Exception as e:
        #    print str(e)
