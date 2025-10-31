from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import Flow
from dotenv import load_dotenv
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


def create_oauth_flow():
    client_config = {
        "web": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost:8080/"],
        }
    }

    flow = Flow.from_client_config(
        client_config,
        scopes=["https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/userinfo.email", "openid"],
        redirect_uri="http://localhost:8080/"
    )
    return flow


def get_authorization_url():
    flow = create_oauth_flow()
    authorization_url, _ = flow.authorization_url(prompt="consent")
    return authorization_url


def fetch_user_info(authorization_response):
    flow = create_oauth_flow()
    flow.fetch_token(
        authorization_response=authorization_response,
        include_granted_scopes=True,
    )
    credentials = flow.credentials

    service = build("people", "v1", credentials=credentials)
    profile = service.people().get(resourceName="people/me",
                                   personFields="names,emailAddresses").execute()

    name = profile["names"][0]["displayName"]
    email = profile["emailAddresses"][0]["value"]
    return name, email
