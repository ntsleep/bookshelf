function showAlert(message, type = 'success') {
    $("#alert_placeholder").html('<div class="alert alert-' + type + '">' + message + '</div>');
    alertTimeout(3000);
}

function alertTimeout(wait) {
    setTimeout(function () {
        $('#alert_placeholder').children('.alert:first-child').remove();
    }, wait);
}

function setButtonText(button) {
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
    
    var status = button.data('actionStatus');
    var text = buttons[button.data('action')][status]
    
    button.text(text);
}

function toggleButtonAction(button) {
    var old_status = button.data('actionStatus');
    var new_status = (old_status === 'off') ? 'on' : 'off';
    
    button.attr('data-action-status', new_status);
    button.data('actionStatus', new_status);
    
    setButtonText(button)
}

