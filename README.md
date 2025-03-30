
# 🎧 LinGoPal Streaming API Client

![Python](https://img.shields.io/badge/python-3.6+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

Welcome to the official documentation for the **LinGoPal Streaming API Client**.

This site provides an overview of how to install, use, and test the client library that interacts with LinGoPal's real-time audio streaming services.

---

## ✨ Features

- ✅ Start and manage streaming sessions
- 📊 Retrieve session information
- 🧪 Includes PyTest-based test suite
- 🔒 Supports authenticated user streaming

---

## 📦 Prerequisites

- Python 3.6+
- Required packages (included in `requirements.txt`):
  - `requests`
  - `pytest`

---

## 🚀 Installation

```bash
cd lingopal_streaming_api_setup
pip install -r requirements.txt
```

---

## 🧑‍💻 Usage

### StreamingAPIClient Capabilities

The `StreamingAPIClient` class enables you to:

- 🎙️ Start a new stream
- ⏹️ Stop an existing stream
- 📄 Retrieve info about a stream
- 📃 List all user streams

---

## 🔍 API Reference (Swagger)

You can explore the full API specification and test endpoints interactively via our Swagger UI:

👉 [View LinGoPal API Swagger Docs](https://cs9m9ilwlg.execute-api.us-west-2.amazonaws.com/public_api_dev/swagger)

---

## 🧪 Running Tests

We use `pytest` for validating the API functionality.

### 🧭 Test Workflow

1. Start a stream using your `ingest_url`
2. Capture the UUID returned from the API
3. Use that UUID for the stop and info tests

### ▶️ Start Stream Test

```bash
pytest -v -s streaming_api_client_test.py::test_start_stream
```

This will attempt to start a stream with the configuration specified in the test file. If successful, it will return a UUID for the stream, which you'll need for the subsequent tests.

**Important:** Make note of the UUID i.e `stream_uuid` returned in the response, as you'll need to update the other test functions with this value.

### 📄 Get Stream Info Test

Before running this test, update the global `STREAM_ID` variable with the UUID from the start stream response:

```python
STREAM_ID = "STREAM_ID"  # Replace with actual UUID
```

Then run:

```bash
pytest -v -s streaming_api_client_test.py::test_get_stream_info
```

### ⏹️ Stop Stream Test

Before running this test, update the global `STREAM_ID` variable with the UUID from the start stream response:

```python
STREAM_ID = "STREAM_ID"  # Replace with actual UUID
```

Then run:

```bash
pytest -v -s streaming_api_client_test.py::test_stop_stream
```

### 📃 List Streams Test

To retrieve all streams associated with your API key:

```bash
pytest -v -s streaming_api_client_test.py::test_list_streams
```

This will return information about all active streams for the authenticated user.

---

## 🔎 Accessing Stream Data

After starting a stream, you can access the streamed data in several ways. The information is available in the response from `get_stream_info`:

### 🌐 1. Web Browser
- Use the `iframe_html` from the response to embed the stream in a webpage
- Or directly navigate to the `hosted_url` in a browser

### 🎞️ 2. Media Players
- **VLC Media Player**: Open VLC and use Media → Open Network Stream → paste the URL from the `vlc` field
- Other players supporting SRT: Use the `dst_url` from the response

### 📡 3. SRT Client
- Use the `wowza_url` field to connect an SRT client to the source stream

---

## ⚙️ Configuration

The test file uses the following configuration:
- Base URL: `https://cs9m9ilwlg.execute-api.us-west-2.amazonaws.com/public_api_dev`
- API Key: `YOUR_API_KEY` Replace the API KEY with your actual API KEY

---

## 📌 Important Notes

1. The `ingest_url` in the start stream payload has to be updated based on your requirements.
2. Always update the UUID in the stop and get-info tests with the value returned from the start stream test.
3. Some tests require an active stream to be running - run them in the proper sequence.

---

## 📁 Project Structure

```
/lingopal_streaming_api_setup
  ├── streaming_api_client.py         # API client
  ├── streaming_api_client_test.py    # Tests
  ├── requirements.txt
```

---

## 📄 License

MIT © 2025 Your Company Name

---

## 📸 Screenshots & Demos *(Optional)*

You can include visuals here.

```md
![Start Stream Demo](assets/start-demo.gif)
```

Make sure to upload your screenshots/GIFs into an `assets/` folder in the repo.
