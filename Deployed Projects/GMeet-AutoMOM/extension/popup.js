document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    const momResult = document.getElementById('momResult');
    const loading = document.getElementById('loading');

    chrome.storage.local.get(['isRecording', 'lastMOM'], (data) => {
        if (data.isRecording) {
            startBtn.classList.add('hidden');
            stopBtn.classList.remove('hidden');
        }
        if (data.lastMOM) {
            momResult.innerText = data.lastMOM;
        }
    });

    startBtn.addEventListener('click', () => {
        chrome.runtime.sendMessage({ action: 'start_recording' });
        startBtn.classList.add('hidden');
        stopBtn.classList.remove('hidden');
        momResult.innerText = '';
    });

    stopBtn.addEventListener('click', () => {
        startBtn.classList.remove('hidden');
        stopBtn.classList.add('hidden');
        loading.classList.remove('hidden');
        momResult.innerText = '';

        chrome.runtime.sendMessage({ action: 'stop_recording' }, (response) => {
            loading.classList.add('hidden');
            if (response && response.mom) {
                momResult.innerText = response.mom;
                chrome.storage.local.set({ lastMOM: response.mom });
            } else {
                momResult.innerText = "Error: Could not generate MOM.";
            }
        });
    });
});