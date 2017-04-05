function showAlert(message, type = 'success') {
    $("#alert_placeholder").html('<div class="alert alert-' + type + '">' + message + '</div>');
    alertTimeout(3000);
}

function alertTimeout(wait) {
    setTimeout(function () {
        $('#alert_placeholder').children('.alert:first-child').remove();
    }, wait);
}

function toggleButtonAction(button) {
    var buttons = {
        'want-to-read' : {
            'off' : 'Want to read',
            'on' : "Don't want to read",
        },
        'currently-reading' : {
            'off' : 'Currently reading',
            'on' : "Don't read",
        },
        'read' : {
            'off' : 'Read',
            'on' : "Unread",
        },
        'like' : {
            'off' : 'Like',
            'on' : "Don't like",
        },
        'have' : {
            'off' : 'Have',
            'on' : "Don't have",
        },
    };

    var old_status = button.data('actionStatus');
    var new_status = (old_status === 'off') ? 'on' : 'off';
    var new_text = buttons[button.data('action')][new_status]

    button.attr('data-action-status', new_status);
    button.data('actionStatus', new_status);
    button.text(new_text);
}

