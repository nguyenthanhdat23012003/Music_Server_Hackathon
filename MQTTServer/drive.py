import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import io

SCOPES = ['https://www.googleapis.com/auth/drive']
topFolderId = '17d39ddzfDvdCCh8cijOXoeDt8OMJosG7'
class Drive:
  def __init__(self):
    creds = None
    if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
      with open("token.json", "w") as token:
        token.write(creds.to_json())
    try:
      self.service = build("drive", "v3", credentials=creds)

    except HttpError as error:
      # TODO(developer) - Handle errors from drive API.
      print(f"An error occurred: {error}")
  def download_file(self, file_name):
    items = []
    pageToken = ""
    while pageToken is not None:
      response = self.service.files().list(q="'" + topFolderId + "' in parents", pageSize=1000, pageToken=pageToken, fields="nextPageToken, files(id, name)").execute()
      items.extend(response.get('files', []))
      pageToken = response.get('nextPageToken')
    request = self.service.files().get_media(fileId=items[0]['id'])
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
      status, done = downloader.next_chunk()
      print("Download %d%%." % int(status.progress() * 100))


      