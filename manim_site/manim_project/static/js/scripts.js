document.getElementById("generate").addEventListener("click", function(event) {
    // Show the loaders
    document.getElementById("loader1").style.display = "block";
    document.getElementById("loader2").style.display = "block";

    // Optional: Disable the button to prevent multiple submissions
    this.disabled = true;

    // Submit the form // Peut etre inutile : a controler
    document.getElementById("form").submit();
});

