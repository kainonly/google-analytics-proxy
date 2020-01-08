from apiclient import discovery
from oauth2client import service_account
import os
import httplib2

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'private.json'
VIEW_ID = os.getenv("VIEW_ID")

# 设置代理
proxy_type = httplib2.socks.PROXY_TYPE_HTTP
httplib2.ProxyInfo(proxy_type=proxy_type, proxy_host='localhost', proxy_port=1080)

# 创建凭证
credentials = service_account.ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
discovery.build(
    serviceName='analyticsreporting',
    version='v4',
    http=httplib2.Http,
    credentials=credentials,
    discoveryServiceUrl='https://analyticsreporting.googleapis.com/$discovery/rest'
)
