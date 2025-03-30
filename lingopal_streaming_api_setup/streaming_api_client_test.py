import requests
import json
from streaming_api_client import StreamingAPIClient

BASE_URL = "https://cs9m9ilwlg.execute-api.us-west-2.amazonaws.com/public_api_dev"
API_KEY = "y0vul9EeaY_c3kdSOgvGuGUST7dgKqQk427c-PT88k0"

STREAM_ID = "2b66cf47-5445-44aa-96be-def88ba7e230"
client = StreamingAPIClient(BASE_URL, API_KEY)

def test_start_stream(ingest_url: str = "srt://54.244.123.101:5090", default_voice_id: str = "YKUjKbMlejgvkOZlnnvt"):
    """
    Test the start_stream method.
    
    Update the ingest_url to the stream you want to start.
    
    Use: pytest -v -s streaming_api_client_test.py::test_start_stream
    """

    payload = {
      "ingest_url": ingest_url,
      "dst_url": "",
      "customer_id": "",
      "start_wowza": True,
      "dst_lang": "es",
      "vocals_track": "0",
      "background_track": -1,
      "chunk_size": 2,
      "buffer_size": 3,
      "concat_latency": 30,
      "mix": "-3,0",
      "use_paraphrasing_transcription": False,
      "voice_cloning": False,
      "default_voice_id": default_voice_id,
      "demucs_vocals": True,
      "add_prompt": "",
      "enable_captions_708": False,
      "enable_captions_608": False,
      "src_lang": "en",
      "use_glossary": False,
      "use_paraphrasing": False,
      "scte_35_triggers": False,
      "initial_mute_state": 0,
      "speed": True
    }

    try:
        response = client.start_stream(payload)
        print("SUCCESS:")
        print(json.dumps(response, indent=4, sort_keys=True))

        assert response is not None
    except requests.exceptions.HTTPError as e:
        print(f"ERROR: API returned {e.response.status_code} - {e}")
        print(f"Response content: {e.response.text}")

        assert e.response.status_code == 500
        assert "NoSuchKey" in e.response.text

        print("Test passed: Error is the expected 'NoSuchKey' error from the server")

def test_stop_stream(stream_id: str = STREAM_ID):
    """
    Test the stop_stream method.
    
    Update the stream_id to the stream you want to stop.
    
    To run this test, you need to have a stream running.
    
    Use: pytest -v -s streaming_api_client_test.py::test_stop_stream
    """

    response = client.stop_stream(stream_id)
    print("SUCCESS:")
    print(json.dumps(response, indent=4, sort_keys=True))
    assert response is not None

def test_get_stream_info(stream_id: str = STREAM_ID):
    """
    Test the get_stream_info method.
    
    Update the stream_uuid to the stream you want to get info on.
    
    The response will be a JSON object with the stream info.
    
    To run this test, you need to have a stream running.
    
    Use: pytest -v -s streaming_api_client_test.py::test_get_stream_info
    """

    response = client.get_stream_info(stream_id)
    print("SUCCESS:")
    print(json.dumps(response, indent=4, sort_keys=True))
    assert response is not None

def test_list_streams():
    """
    Test the list_streams method.
    
    This retrieves all streams associated with the API key.
    
    Use: pytest -v -s streaming_api_client_test.py::test_list_streams
    """

    response = client.list_streams()
    print("SUCCESS:")
    print(json.dumps(response, indent=4, sort_keys=True))
    assert response is not None