
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
git clone https://github.com/your-org/lingopal-streaming-api-client.git
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

## 🧪 Running Tests

We use `pytest` for validating the API functionality.

### 🧭 Test Workflow

1. Start a stream using your `ingest_url`
2. Capture the UUID returned from the API
3. Use that UUID for the stop and info tests

### ▶️ Example: Start Stream Test

```bash
pytest -v -s streaming_api_client_test.py::test_start_stream
```

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
