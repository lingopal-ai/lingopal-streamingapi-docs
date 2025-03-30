import requests
from typing import Any, Dict

class StreamingAPIClient:
    def __init__(self, base_url: str, api_key: str) -> None:
        """
        Initializes the API client with the base URL and API key.
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            "Authorization": f"{self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def start_stream(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Initiates the stream. The payload should include parameters e.g. the ingest URL.
        """
        url = f"{self.base_url}/start-stream"
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def stop_stream(self, stream_id: str) -> Dict[str, Any]:
        """
        Stops the stream for the provided stream_id.
        
        Payload:
        {
            "stream_id": "<stream_uuid>" # The stream UUID to stop
        }
        """
        url = f"{self.base_url}/stop-stream"
        payload = {"stream_id": stream_id}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_stream_info(self, stream_uuid: str) -> Dict[str, Any]:
        """
        Retrieves streaming session info using the provided stream UUID.
        """
        url = f"{self.base_url}/get-stream-info/{stream_uuid}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_streams(self) -> Dict[str, Any]:
        """
        Retrieves all streams associated with the user's API key.
        
        Returns a dictionary containing information about all streams.
        """
        url = f"{self.base_url}/list-streams"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
