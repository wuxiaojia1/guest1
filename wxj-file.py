#coding:utf-8
from  minio import Minio

#使用endpoint ，access key 和secret key 来初始化minioClient对象
minioClient = Minio("192.168.18.26:9000",
                    access_key='minioadmin',
                    secret_key="minioadmin",
                    secure=False)

