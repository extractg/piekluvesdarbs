document.addEventListener("DOMContentLoaded", function() {
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');

    // Event listener to start SpeedTest
    startBtn.addEventListener('click', function() {
        // Send request to start SpeedTest
        fetch('/start_speedtest')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                console.log('SpeedTest started successfully');
            })
            .catch(error => {
                console.error('There was a problem with starting SpeedTest:', error);
            });
    });

    // Event listener to stop SpeedTest
    stopBtn.addEventListener('click', function() {
        // Send request to stop SpeedTest
        fetch('/stop_speedtest')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                console.log('SpeedTest stopped successfully');
            })
            .catch(error => {
                console.error('There was a problem with stopping SpeedTest:', error);
            });
    });
});
