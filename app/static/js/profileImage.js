document.getElementById("profileImage").addEventListener("click", function() {
    document.getElementById("fileInput").click();
});

document.getElementById("fileInput").addEventListener("change", function(event) {
    const imageFile = event.target.files[0];
    const formData = new FormData(document.getElementById("uploadForm"));
    formData.append("image", imageFile);
    document.getElementById("uploadForm").submit();
});



