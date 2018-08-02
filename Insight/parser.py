#!/usr/bin/python
import json
import os


DATA_DIR = '../data'

class Parser(object):


    @staticmethod
    def ebs_info(obj):
        return obj.get("AvailabilityZone"), obj.get("Encrypted"), \
                obj.get("State"), obj.get("Size"), \
                [(attach.get("InstanceId"), attach.get("State"),
                    attach.get("Device"))
                    for attach in obj.get("Attachments")]
    
    @staticmethod
    def instance_info(obj):
        tgval = [None]
        if obj.get("Tags"):
            tgval = [tags.get("Value") for tags in obj.get("Tags")]
        return obj.get("VpcId"), obj.get("InstanceId"), \
                obj.get("SubnetId"), obj.get("InstanceType"), \
                obj.get("Placement")["AvailabilityZone"], \
                tgval

    @staticmethod
    def rds_info(obj):
        return obj.get("PubliclyAccessible"), obj.get("MultiAZ"), \
                obj.get("VpcId"), obj.get("DBName"), \
                obj.get("DBInstanceClass"), obj.get("AvailabilityZone")

    @staticmethod
    def vpc_info(obj):
        tgval = [None]
        if obj.get("Tags"):
            tgval = [tags.get("Value") for tags in obj.get("Tags")]
        return obj.get("VpcId"), obj.get("State"), \
                obj.get("CidrBlock"), tgval

    @staticmethod
    def elb_info(obj):
        return obj.get("LoadBalancerName"), obj.get("Subnets"), \
                obj.get("VPCId"), obj.get("Instances"), \
                obj.get("DNSName"), obj.get("AvailabilityZones"), \
                obj.get("Scheme")
        

    def ebs_parse(self, fobj):
        data = json.load(fobj)
        return map(self.ebs_info, data['Volumes'])

    def ec2_parse(self, fobj):
        data = json.load(fobj)
        return [map(self.instance_info, reserve['Instances']) \
                    for reserve in data['Reservations']]

    def rds_parse(self, fobj):
        data = json.load(fobj)
        return map(self.rds_info, data['DBInstances'])

    def vpc_parse(self, fobj):
        if isinstance(fobj, file):
            fobj = json.load(fobj)
        return map(self.vpc_info, fobj['Vpcs'])

    def elb_parse(self, fobj):
        data = json.load(fobj)
        return map(self.elb_info, data['LoadBalancerDescriptions'])

"""

if __name__ == "__main__":
    obj = Parser()
    for files in os.listdir(DATA_DIR):
        if os.path.isfile(files):
            with open(os.path.join(DATA_DIR, files)) as rf:
                if 'ebs' in files:
                    print "EBS"
                    print obj.ebs_parse(rf)
                elif 'ec2' in files:
                    print "EC2"
                    print obj.ec2_parse(rf)
                elif 'rds' in files:
                    print "RDS"
                    print obj.rds_parse(rf)   
                elif 'vpc' in files:
                    print "VPC"
                    print obj.vpc_parse(rf)
                elif 'elb' in files:
                    print "ELB"
                    print obj.elb_parse(rf)

"""
