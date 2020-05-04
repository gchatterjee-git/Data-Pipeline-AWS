# DATA-PIPELINE USING AWS SERVICES

### Objective

This project deals with collecting real-time twitter data on COVID-19 topic, processing these tweets after mapping the attributes to the desired columns and then storing in the data for further analysis.

### Dependencies

* boto3
```shell
  pip install boto3
```
* tweepy
```shell
  pip install tweepy
  ```
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

 Cloud services used in this project:

* Kinesis Firehose
* AWS S3
* AWS Glue
* IAM (For role creation)

### How to use ?

* Use **tweetercred.py** to store twitter developer account credentials.

* Use **buildFirehose_AWS.py**  which uses boto3 API to create a data delivery stream using Kinesis Firehose.

* Use **ingesttwitterdata.py** to ingest data to data delivery stream.

* Delete data delivery stream after the data has been successfully ingested to S3 bucket.  

* To set the credentials for AWS account run the below command on command prompt after installing AWS CLI. 

   <img src="https://gaurav-personal-version-control.s3.amazonaws.com/cmd_updated.jpeg" style="zoom:80%;" />

### Architecture

Data pipeline has two parts :

* Collecting Data
* Processing Data

<img src="https://gaurav-personal-version-control.s3.amazonaws.com/Data-Pipeline-Architecture_updated.jpeg" style="zoom:80%;" />


  
