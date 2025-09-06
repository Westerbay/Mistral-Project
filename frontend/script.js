endpoint = "request";
text = "Explication de l'autodifférentiation";

$.ajax({
    url: "http://127.0.0.1:8000/" + endpoint,
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ prompt: text }),
    success: function(response) {
        console.log(response);
    },
    error: function() {
        console.log("error");
    }
});
