import boto3
import json
from exceptions import Error, BotoApiError


class RouteTableInfo(object):

    def __init__(self):
        self.ec2_client = boto3.client('ec2')

    def get_ec2_client(self):
        return self.ec2_client

    def get_tables(self):
        client = self.get_ec2_client()

        try:
            resp = client.describe_route_tables()
            if resp is None:
                raise BotoApiError

            # Dumping the complete response in json file
            with open('data/rtb.json', 'w') as fh:
                json.dump(resp, fh, indent=4, default=str)

            return resp
        except BotoApiError:
            print "Boto API error."
        except IOError:
            print "File not found."
        except Exception as e:
            print str(e)
