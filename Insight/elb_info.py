import json
import boto3
from exceptions import Error, BotoApiError

class ELBInfo(object):

    def __init__(self):
        self.elb_client = boto3.client('elb')

    def get_elb_client(self):
        return self.elb_client

    def get_load_balancers(self):
        client = self.get_elb_client()

        try:
            resp = client.describe_load_balancers()
            if resp is None:
                raise BotoApiError

            # Dumping the complete response in json file
            with open('data/elb.json', 'w') as fh:
                json.dump(resp, fh, indent=4, default=str)
            return resp

        except BotoApiError:
            print "Boto API error."
        except IOError:
            print "File not found."
        except Exception as e:
            print str(e)
