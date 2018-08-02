from blessings import Terminal
from prettytable import PrettyTable
from exceptions import Error, BotoApiError


class Formatter(object):

    def __init__(self):
        self.ptable = PrettyTable()
        self.term = Terminal()

    def get_ptable(self):
        return self.ptable

    def get_term(self):
        return self.term

    def print_data(self, name, info):
        term = self.get_term()
        try:
            if name == "vol":
                print "EBS"
                count = 1
                for vol_found in info['Volumes']:
                    print term.bold_blue("Volume: ") + str(count)
                    for k, v in vol_found.items():
                            if k == 'Attachments' or k == 'Tags':
                                continue
                            print term.bold_red(k) + term.normal + ":" + str(v)
                    count += 1
                    print ""

            elif name == "ec2":
                print "EC2"
                info = info['Reservations']
                instance_count = 1
                req_keys = set(['InstanceId', 'InstanceType', 'SubnetId', 'LaunchTime', 'SecurityGroups', 'State'])
                for instances in info:
                    for data in instances['Instances']:
                        print "Instance: " + term.blue(str(instance_count))
                        for k, v in data.items():
                            if k in req_keys:
                                print term.bold_red(k) + term.normal + ":" + str(v)
                        instance_count = int(instance_count) + 1
                        print ""
            elif name == "rds":
                print "RDS"
                count = 1
                req_keys = set(['InstanceCreateTime', 'DBSubnetGroup', 'DBInstanceStatus'])
                for vol_found in info['DBInstances']:
                    print "Rds instance: " + term.blue(str(count))
                    for k, v in vol_found.items():
                        if k in req_keys:
                            print term.bold_red(k) + term.normal + ":" + str(v)
                    count += 1
                    print ""
            elif name == "lbal":
                print "LBAL"
                info = info['LoadBalancerDescriptions']
                load_balancer_count = 1
                req_keys = set(['SecurityGroups', 'DNSName', 'LoadBalancerName', 'Instances'])
                for balancer in info:
                    print "Load Balancer: " + term.blue(str(load_balancer_count))
                    for k, v in balancer.items():
                        if k in req_keys:
                            print term.bold_red(k) + term.normal + ":" + str(v)
                    load_balancer_count = int(load_balancer_count) + 1
                    print ""
            elif name == "vpc":
                print "VPC"
                info = info['Vpcs']
                vpc_count = 1
                req_keys = set(['VpcId', 'State', 'CidrBlock', 'DhcpOptionsId'])
                for vpc in info:
                    print "Vpc: " + term.blue(str(vpc_count))
                    for k, v in vpc.items():
                        if k in req_keys:
                            print term.bold_red(k) + term.normal + ":" + str(v)
                    vpc_count = int(vpc_count) + 1
                    print ""

        except KeyError as e:
            print str(e) + "Key is not found in dictionary."
        except Exception as e:
            print str(e)
