# Lambda-SPy-Integration
An example project for using SPy in a Lambda function

# Prerequisites
This project relies on AWS for Lambda and associated services and the Serverless framework. In order to make use of this example, you will need to have access to a few things.

1. A Seeq server that you can pull data from
2. An AWS account, and with access to create Lambda functions and applications with associated services
3. Serverless installed on your development machine with the Python-Requirements plugin

## Install Serverless
* Assuming prerequisites 1 and 2 are fulfilled, we will move on to installing serverless. [The best instructions are here](https://www.serverless.com/framework/docs/providers/aws/guide/installation/)
* Install the serverless-python-requirements plugin . [The best install instructions are here](https://www.npmjs.com/package/serverless-python-requirements)

## Code Modification ##

Once Serverless is installed via the instructions linked above, modify the handler.py files to put in the correct Seeq endpoint in the spy.login call.

## Deployment ##

Once Serverless is installed via the instructions linked above, and the code is modified as stated above, then execute:

```sls deploy -v```

This will deploy the lambda function to the _Dev_ stage.

You will see the resultant URL that can be called at the end of the sls deploy. 

## Testing ##

You can use Postman or a similar tool to call the API endpoint that was deployed in the previous step. The query parameters that are required are as follows:

* start: the start of the range to pull from (ex. 11-23-2020)
* end: the end of the range to pull the data from (ex. 02-22-2021)
* search-params: The criteria to identify the signals to be pulled (ex. a workbook url)
* key: the access key 
* secret: the secret associated with the access key

You should recieve a JSON version of the Pandas dataframe that is the result of the spy.pull request that was performeed in the handler.

## Optimization ##

This function executes a search and then a pull. In the case where you know what signals or conditions you are querying for, you could simply pickle the search result from performing the search on your local machine and use that picked dataframe to execute the spy.pull to improve the effiency of the function.