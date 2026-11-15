let isRecording = false;
let observer = null;
let lastCapturedText = "";

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'start') {
        isRecording = true;
        startObservingCaptions();
        sendResponse({ status: 'started' });
    } else if (request.action === 'stop') {
        isRecording = false;
        if (observer) observer.disconnect();
        sendResponse({ status: 'stopped' });
    }
});

function startObservingCaptions() {
    const captionSelector = '.a4cQT'; 
    
    observer = new MutationObserver((mutations) => {
        if (!isRecording) return;

        const captionContainers = document.querySelectorAll(captionSelector);
        if (captionContainers.length === 0) return;

        const activeNode = captionContainers[captionContainers.length - 1];
        const speakerElement = activeNode.querySelector('.zs7s8d'); 
        const textElement = activeNode.querySelector('.iTTPOb'); 
        
        if (speakerElement && textElement) {
            const speaker = speakerElement.innerText.trim();
            const text = textElement.innerText.trim();

            if (text !== lastCapturedText && text.length > lastCapturedText.length) {
                lastCapturedText = text;
                
                chrome.runtime.sendMessage({
                    action: 'transcript_update',
                    payload: `${speaker}: ${text}`
                });
            }
        }
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true,
        characterData: true
    });
}