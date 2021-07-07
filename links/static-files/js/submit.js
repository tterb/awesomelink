$(document).ready(function() {
    var submitForm = $('#submitForm');
    var submitBtn = $('#submitLink');
    var errorMsg = $('#errorMessage');

    function setSubmitted() {
        submitBtn.val('Submitted!');
        setTimeout(function() {
            submitBtn.val('Submit it!');
        }, 10000)
    }

    function submitLinkForm(evt) {
        evt.preventDefault();
        errorMsg.html();
        var actionUrl = submitForm.attr('action');
        var htmlForm = document.getElementById('submitForm');
        const data = Object.fromEntries(new FormData(htmlForm).entries());

        $.ajax({
            url: actionUrl,
            type: 'POST',
            data: data,
            success: function(response) {
                console.log(response);
                setSubmitted();
            },
            error: function(response) {
                errorMsg.html(response.responseJSON.error);
            },
        });
        return false;
    }

    submitForm.on('submit', submitLinkForm);
});