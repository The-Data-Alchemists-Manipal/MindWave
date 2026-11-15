let transcript = [];
let isRecording = false;

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    
    if (request.action === 'start_recording') {
        isRecording = true;
        transcript = [];
        chrome.storage.local.set({ isRecording: true });
        
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            if(tabs[0].url.includes("meet.google.com")) {
                chrome.tabs.sendMessage(tabs[0].id, { action: 'start' });
            }
        });
        return true;
    } 
    
    else if (request.action === 'transcript_update') {
        if (isRecording) {
            const newText = request.payload;
            const currentSpeaker = newText.split(':')[0];
            
            if (transcript.length > 0 && transcript[transcript.length - 1].startsWith(currentSpeaker)) {
                transcript[transcript.length - 1] = newText;
            } else {
                transcript.push(newText);
            }
        }
    } 
    
    else if (request.action === 'stop_recording') {
        isRecording = false;
        chrome.storage.local.set({ isRecording: false });
        
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            if(tabs[0].url.includes("meet.google.com")) {
                chrome.tabs.sendMessage(tabs[0].id, { action: 'stop' });
            }
        });

        const rawTranscriptText = transcript.join('\n');
        
        fetch('http://127.0.0.1:5000/generate-mom', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ transcript: rawTranscriptText })
        })
        .then(response => response.json())
        .then(data => {
            sendResponse({ mom: data.mom });
        })
        .catch(err => {
            console.error(err);
            sendResponse({ mom: "Error: Backend server is not running." });
        });

        return true; 
    }
});