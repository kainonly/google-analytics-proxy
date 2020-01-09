from apiclient import discovery
from oauth2client import service_account

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'private.json'

credentials = service_account.ServiceAccountCredentials.from_json_keyfile_name(
    KEY_FILE_LOCATION,
    SCOPES
)

client = discovery.build(
    serviceName='analyticsreporting',
    version='v4',
    credentials=credentials
)


def reports(query: dict) -> dict:
    return client.reports().batchGet(body=query).execute()
