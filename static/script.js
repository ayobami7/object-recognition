function updateTime() {
    const now = new Date();
    const timeStr = now.toTimeString().split(' ')[0];
    document.getElementById('system-time').textContent = `SYSTEM TIME: ${timeStr}`;
}
setInterval(updateTime, 1000);
updateTime();

// Monitor video feed
const videoFeed = document.getElementById('video-feed');

videoFeed.onerror = function() {
    console.error('Video feed error');
    videoFeed.alt = 'Video feed unavailable. Check if camera is connected.';
};

videoFeed.onload = function() {
    console.log('Video feed loaded successfully');
};
