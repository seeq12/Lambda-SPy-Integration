import json
import sys
import traceback

try:
  import unzip_requirements
except ImportError:
  pass

from seeq import spy
import pandas as pd
from datetime import datetime,timezone,timedelta

def get_seeq_data(search_params, start, end, grid, key, pw):
    # SPy client login
    spy.login(url="https://yourserver.seeq.com/", access_key=key, password=pw, ignore_ssl_errors=True)
    # Finding all items that belong to our asset hierarchy
    print('Finding items to pull')
    items = spy.search(search_params)

    return spy.pull(items, end=end, start=start, grid=grid)

def generate_response(status_code, body):
    response = {
        "statusCode":status_code,
        "body": body 
    }
    return response

def data_query(event, context):

    print('Recieved request')
    print('Logging into Seeq')
    resp = ''
    grid_param = '15m'
    params = event['queryStringParameters']
    try:
        start_time = params['start']
        end_time = params['end']
        search_params = params['search-params']
        key = params['key']
        pw = params['secret']

        seeq_data = get_seeq_data(search_params, start_time, end_time, grid_param, key, pw)
        resp = seeq_data.to_json()
        full_resp = generate_response(200, resp)
        print('finished serializing dataframe. Returning now.')
    except:
        full_resp = generate_response(500, '{"error" : "' + traceback.format_exc() + '")')

    return full_resp