document.addEventListener("DOMContentLoaded", function() {
    const generateButton = document.getElementById("generate");
    const loader1 = document.getElementById("loader1");
    const loader2 = document.getElementById("loader2");
    const form = document.getElementById("form");

    if (generateButton && loader1 && loader2 && form) {
        generateButton.addEventListener("click", function(event) {
            // Show the loaders
            loader1.style.display = "block";
            loader2.style.display = "block";

            // Disable the button to prevent multiple submissions
            this.disabled = true;

            // Submit the form (if necessary)
            form.submit();
        });
    }

    // Script to manage videos - Play and pause on hover
    const videos = document.querySelectorAll('.small_video');
    
    videos.forEach(video => {
        video.addEventListener('mouseover', function () {
            this.play(); // Play the video on hover
        });

        video.addEventListener('mouseout', function () {
            this.pause(); // Pause the video when the mouse leaves
            this.currentTime = 0; // Reset the video to the beginning
        });

        // Click event to toggle fullscreen
        video.addEventListener('click', function () {
            // Check if the video is already in fullscreen
            if (video.requestFullscreen) {
                video.requestFullscreen(); // For most browsers
            } else if (video.mozRequestFullScreen) { // For Firefox
                video.mozRequestFullScreen();
            } else if (video.webkitRequestFullscreen) { // For Chrome, Safari and Opera
                video.webkitRequestFullscreen();
            } else if (video.msRequestFullscreen) { // For IE/Edge
                video.msRequestFullscreen();
            }
        });
    });
});
