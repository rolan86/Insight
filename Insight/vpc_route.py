import os

import boto3

import parser

DATA_DIR = 'data'


def route_info():

    routing = {}

    ec2 = boto3.resource('ec2')

    parsed = parser.Parser()

    with open(os.path.join(DATA_DIR, 'vpc.json')) as rf:
        vpcids = parsed.vpc_parse(rf)

    for vpcinfo in vpcids:
        routing[vpcinfo[0]] = None
        vpc = ec2.Vpc(vpcinfo[0])
        rtb = {}
        for items in vpc.route_tables.all():
            rtb[items.id] = dict(zip(['associations', 'attributes'],
                [items.associations_attribute, items.routes_attribute]))
            routing[vpcinfo[0]] = rtb
    return  routing
