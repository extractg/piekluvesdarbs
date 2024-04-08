document.addEventListener('DOMContentLoaded', function () {
    const runSpeedTestBtn = document.getElementById('run-speed-test');

    runSpeedTestBtn.addEventListener('click', function () {
        fetch('/run_speed_test')
            .then(response => {
                if (response.ok) {
                    console.log('Speed test started.');
                } else {
                    console.error('Failed to start speed test.');
                }
            })
            .catch(error => console.error('Error occurred:', error));
    });
});
