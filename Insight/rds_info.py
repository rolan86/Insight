import boto3
import json
from exceptions import Error, BotoApiError


class RDSInfo(object):
    def __init__(self):
        self.rds_client = boto3.client('rds')

    def get_rds_client(self):
        return self.rds_client

    def get_rds(self):
        client = self.get_rds_client()

        try:

            resp = client.describe_db_instances()
            if resp is None:
                raise BotoApiError

            # Dumping the complete response in json file
            with open('data/rds.json', 'w') as fh:
                json.dump(resp, fh, indent=4, default=str)

            return resp
        except BotoApiError:
            print "Boto API error."
        except IOError:
            print "File not found."
        except Exception as e:
            print str(e)
