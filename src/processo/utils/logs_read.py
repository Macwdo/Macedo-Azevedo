from datetime import datetime, timedelta

import boto3
from django.conf import settings

client = boto3.client(
    "logs",
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,

)

def get_logs(query, log_group, client):
    start_query_response = client.start_query(
        logGroupName=log_group,
        startTime=int((datetime.today() - timedelta(hours=5)).timestamp()),
        endTime=int(datetime.now().timestamp()),
        queryString=query,
    )

    query_id = start_query_response['queryId']

    response = None
    while response is None or response['status'] == 'Running':
        response = client.get_query_results(
            queryId=query_id
        )

    logs = []
    for result in response["results"]:
        logs.append((result[0]["value"], result[1]["value"]))

    return logs
