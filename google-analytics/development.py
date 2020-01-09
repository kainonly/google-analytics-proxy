from apiclient import discovery
from oauth2client import service_account
import httplib2
import os

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'private.json'
VIEW_ID = os.getenv("VIEW_ID")

# 设置代理
proxy_type = httplib2.socks.PROXY_TYPE_HTTP
proxy = httplib2.ProxyInfo(proxy_type=proxy_type, proxy_host='127.0.0.1', proxy_port=1080)
http = httplib2.Http(proxy_info=proxy)
service_account.ServiceAccountCredentials.from_json_keyfile_name(
    KEY_FILE_LOCATION,
    SCOPES
).authorize(http)

# 分析客户端
client = discovery.build(
    serviceName='analyticsreporting',
    version='v4',
    http=http
)

query = {
    'reportRequests': [{
        'viewId': VIEW_ID,
        'dateRanges': [
            {'startDate': 'today', 'endDate': 'today'}
        ],
        'metrics': [
            {'expression': 'ga:users'},
            {'expression': 'ga:sessions'}
        ],
        'dimensions': [
            {'name': 'ga:country'}
        ]
    }]
}

output = client.reports().batchGet(
    body=query
).execute()

print(output)
