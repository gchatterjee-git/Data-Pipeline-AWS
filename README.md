# DATA-PIPELINE USING AWS SERVICES

### Objective

This project deals with collecting real-time twitter data on COVID-19 topic, processing these tweets after mapping the attributes to the desired columns and then storing in the data for further analysis.

### Dependencies

* boto3

* tweepy

* AWS CLI ( https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html )

  ```shell
  pip install boto3
  pip install tweepy
  ```

Cloud services that we'll get introduced to in this project are:

* Kinesis Firehose
* AWS S3
* AWS Glue
* IAM (For role creation)

### Architecture

We'll divide the data pipeline into 2 parts:

* Collecting Data
* Processing Data

Following architecture have been followed for both the components

<img src="C:\Users\Gaurav\.spyder-py3\TwitterData\Data-Pipeline-Architectue.jpeg" style="zoom:80%;" />

### Note

* Use **tweetercred.py** to store twitter developer account credentials.

* Use **buildFirehose_AWS.py**  which uses boto3 API to create a data delivery stream using Kinesis Firehose.

* Use **ingesttwitterdata.py** to ingest data to data delivery stream.

* Delete data delivery stream after the data has been successfully ingested to S3 bucket.  

* To set the credentials for AWS account run the below command on command prompt after installing AWS CLI. 

   ![](C:\Users\Gaurav\.spyder-py3\TwitterData\cmd.JPG)

  