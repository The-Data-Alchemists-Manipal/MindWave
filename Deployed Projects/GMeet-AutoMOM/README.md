# GMeet-AutoMOM 🎙️📝

**GMeet-AutoMOM** is an end-to-end tool consisting of a Chrome Extension and a Python backend that automatically records Google Meet transcripts and generates intelligent Minutes of Meeting (MOM) using Natural Language Processing (NLP).

> **Note:** This project resolves Issue #90.

## 🚀 Features
- **Real-Time Scraping**: Captures Google Meet closed captions live without duplicate sentences.
- **NLP Summarization**: Uses the state-of-the-art Hugging Face `BART` model (`facebook/bart-large-cnn`) to summarize long meetings into concise bullet points.
- **Chunking Mechanism**: Capable of handling long transcripts by breaking them into manageable token chunks before summarization.
- **Privacy First**: The extension only activates when the user clicks "Start Recording" and stores the transcript locally during the meeting.

## 🛠️ Tech Stack
- **Frontend / Client**: Chrome Extension (Manifest V3), JavaScript, HTML/CSS.
- **Backend**: Python, FastAPI.
- **Machine Learning**: Hugging Face `transformers`, PyTorch.

---

## 📁 Directory Structure
```text
GMeet-AutoMOM/
├── backend/            # FastAPI server and Hugging Face NLP model
│   ├── requirements.txt
│   ├── main.py
│   └── nlp_model.py
└── extension/          # Chrome Extension source files
    ├── manifest.json
    ├── popup.html
    ├── popup.js
    ├── content.js
    └── background.js
```

## 💻 Installation & Setup

### 1. Backend Setup
The backend requires Python 3.8+.
1. Open a terminal and navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI server:
   ```bash
   python main.py
   ```
   *(Note: The first time you run this, it will download the 1.5GB NLP model. Once finished, the server will run on `[http://0.0.0.0:5000](http://0.0.0.0:5000)`)*

### 2. Extension Setup
1. Open Google Chrome and go to `chrome://extensions/`.
2. Enable **Developer mode** using the toggle in the top right corner.
3. Click the **Load unpacked** button in the top left.
4. Select the `extension` folder located inside `GMeet-AutoMOM/`.
5. The extension icon will now appear in your Chrome toolbar.

---

## 💡 How to Use
1. Ensure the Python backend is running in your terminal.
2. Join a Google Meet session.
3. ⚠️ **CRITICAL:** Click the `CC` button at the bottom of the Meet screen to **Turn on Captions**. (The extension reads the live text from the screen).
4. Click the **GMeet MOM Creator** extension icon in your Chrome toolbar.
5. Click **Start Recording**.
6. When the meeting is over, click **Stop & Generate MOM**. 
7. The AI will process the transcript and output your structured meeting minutes directly in the popup!