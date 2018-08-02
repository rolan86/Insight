import boto3
from prettytable import PrettyTable
from blessings import Terminal


ptable = PrettyTable()
term = Terminal()


class S3Info(object):
    def __init__(self):
        self.s3 = boto3.client('s3')

    def get_s3_client(self):
        return self.s3

    def get_buckets(self):
        s3 = self.get_s3_client()
        buckets = s3.list_buckets()
        return buckets
