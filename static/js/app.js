function showAlert(message, type = 'success') {
    $("#alert_placeholder").html('<div class="alert alert-' + type + '">' + message + '</div>');
    alertTimeout(3000);
}

function alertTimeout(wait) {
    setTimeout(function () {
        $('#alert_placeholder').children('.alert:first-child').remove();
    }, wait);
}

