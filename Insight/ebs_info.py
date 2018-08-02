import boto3
import json
from exceptions import Error, BotoApiError


class EBSInfo(object):

    def __init__(self):
        self.ec2_client = boto3.client('ec2')

    def get_ec2_client(self):
        return self.ec2_client

    def get_volumes(self):
        client = self.get_ec2_client()
        try:
            res = client.describe_volumes()
            if res is None:
                raise BotoApiError
            # Dumping the complete response in json file
            with open('data/ebs.json', 'w') as fh:
                json.dump(res, fh, indent=4, default=str)

            return res

        except BotoApiError:
            print "Boto API error."
        except IOError:
            print "File not found."
        except Exception as e:
            print str(e)
