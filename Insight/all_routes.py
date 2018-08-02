import boto3
import json
import os
from exceptions import Error, BotoApiError

class AllRouteInfo(object):

    if not os.path.exists(os.path.join('data', 'vpc')):
        os.mkdir(os.path.join('data', 'vpc'))

    def __init__(self):
        self.ec2_res = boto3.resource('ec2')

    def get_ec2_res(self, vpcid):
        return self.ec2_res.Vpc(vpcid)

    def get_all_routes(self, vpcid):
        self.vpc = self.get_ec2_res(vpcid)

        try:
            resp = self.vpc.route_tables.all()
            if resp is None:
                raise BotoApiError

            data_path = os.path.join('data', 'vpc', vpcid)
            with open(data_path, 'w') as fh:
                json.dump(resp, fh, indent=4, default=str)

            return resp
        except BotoApiError:
            print "Boto API error."
        except IOError:
            print "File not found."
        except Exception as e:
            print str(e)
