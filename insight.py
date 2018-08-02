import boto3
import json
import os

from Insight import ec2_info, s3_info, rds_info, elb_info, vpc_info, ebs_info, all_routes, parser, vpc_route
from Insight import formatter


DATA_DIR = "data" 


class CloudRover(object):

    def __init__(self):
        self.ec2info = ec2_info.EC2Info()
        self.ebsinfo = ebs_info.EBSInfo()  # Volume info
        self.vpcinfo = vpc_info.VPCInfo()
        self.elbinfo = elb_info.ELBInfo()
        self.rdsinfo = rds_info.RDSInfo()
        self.routes = all_routes.AllRouteInfo()
        self.format = formatter.Formatter()

    def volume_info(self):
        return self.ec2info.get_instances()

    def ebs_info(self):
        return self.ebsinfo.get_volumes()

    def vpc_info(self):
        return self.vpcinfo.get_vpcs()

    def elb_info(self):
        return self.elbinfo.get_load_balancers()

    def rds_info(self):
        return self.rdsinfo.get_rds()

    def get_formatter(self):
        return self.format

    def print_info2(self, *args, **kwargs):
        formatt = self.format
        for name, info in kwargs.iteritems():
            formatt.print_data(name, info)


def main():
    cloud_rover = CloudRover()
    rv_ec2 = cloud_rover.volume_info()
    rv_vol = cloud_rover.ebs_info()
    rv_vpc = cloud_rover.vpc_info()
    rv_elb = cloud_rover.elb_info()
    rv_rds = cloud_rover.rds_info()

    cloud_rover.print_info2(vol=rv_vol,
                            ec2=rv_ec2,
                            vpc=rv_vpc,
                            lbal=rv_elb,
                            rds=rv_rds)

    obj = parser.Parser()
    print obj.vpc_parse(rv_vpc)

    print vpc_route.route_info()

        
if __name__ == '__main__':
    main()
