# -*- coding: utf-8 -*-
from __future__ import absolute_import

import boto3
from django.conf import settings

from .singleton import Singleton


@Singleton
class S3Helper(object):
    """
    This class contains helper methods for interacting with AWS S3.
    """

    # Class Members

    # Instantiation

    def __init__(self):
        self._s3 = None

    # Static Methods

    # Class Methods

    # Public Methods

    def create_bucket(self, name=None, acl=settings.AWS_S3_DEFAULT_ACL):
        """
        Create a bucket with the given name.
        :param name: The name to give the bucket.
        :param acl: The ACL to apply to the bucket.
        :return: The AWS boto3 client response.
        """
        return self.s3.create_bucket(
            Bucket=name,
            ACL=acl,
            CreateBucketConfiguration=self.create_bucket_constraint,
        )

    def get_buckets(self):
        """
        Get a list of currently available S3 buckets.
        :return: A list of currently available S3 buckets.
        """
        return self.s3.list_buckets()

    def get_file(self, file_key=None, bucket=settings.AWS_S3_BUCKET):
        """
        Get the contents of the file specified by file_key from the given bucket.
        :param file_key: The key where the file resides.
        :param bucket: The bucket where the file resides.
        :return: The contents of the file referenced by file_key and bucket.
        """
        response = self.s3.get_object(Bucket=bucket, Key=file_key)
        return response["Body"].read()

    def get_signed_url_for_key(self, key=None, bucket=settings.AWS_S3_BUCKET):
        """
        Generate and return a signed URL for the given key and bucket.
        :param key: The key to generate the URL for.
        :param bucket: The bucket where the key resides.
        :return: A signed URL that can be used to access the object stored at the given
        key in the given bucket.
        """
        return self.s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": bucket,
                "Key": key,
            }
        )

    def upload_file_to_bucket(
            self,
            bucket=settings.AWS_S3_BUCKET,
            local_file_path=None,
            file_obj=None,
            key=None,
            acl=settings.AWS_S3_DEFAULT_ACL,
    ):
        """
        Upload the file at the given path to the given bucket with the given key.
        :param bucket: The name of the bucket to upload the file to.
        :param local_file_path: The local path where the file resides.
        :param file_obj: The file object to upload. Note that only this value or local_file_path should
        be populated.
        :param key: The key to upload the file under.
        :param acl: The ACL to apply to the newly-uploaded item.
        :return: The boto3 response.
        """
        if file_obj is None:
            file_obj = open(local_file_path, "rb")
        return self.s3.put_object(
            ACL=acl,
            Body=file_obj,
            Bucket=bucket,
            Key=key,
        )

    # Protected Methods

    # Private Methods

    # Properties

    @property
    def create_bucket_constraint(self):
        """
        Get an AWS S3 constraint for use when creating new buckets.
        :return: An AWS S3 constraint for use when creating new buckets.
        """
        return {
            "LocationConstraint": settings.AWS_DEFAULT_REGION,
        }

    @property
    def s3(self):
        """
        Get the boto3 s3 connection to use to communicate with AWS S3.
        :return: the boto3 s3 connection to use to communicate with AWS S3.
        """
        if self._s3 is None:
            self._s3 = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_KEY,
            )
        return self._s3

    # Representation and Comparison
