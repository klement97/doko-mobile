BASE_URL = window.location.origin;

function isValid(email) {
    let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email));
}

$(function ($) {
    document.getElementById('email').addEventListener("change", function (e) {
        e.preventDefault();
        let email = $(this).val();
        let emailInfo = document.getElementById('email_info');
        let emailEl = $('#email'); // input element
        let btnEl = document.getElementById('subscribe_btn');

        // checking if email is valid with regex before posting
        if (isValid(email)) {
            let token = '{{csrf_token}}';
            $.ajax({
                url: `${BASE_URL}/ajax/validate_email/`,
                type: 'GET',
                headers: {'X-CSRFToken': token},
                data: {
                    'email': email
                },
                dataType: 'json',
                beforeSend: function () {
                    emailInfo.textContent = 'Checking...';
                },
                success: function (data) {
                    if (data.is_taken) {
                        document.getElementById('email_info').textContent = data.error_message;
                        emailEl.css('border-color', 'red');
                        btnEl.setAttribute('disabled', '');

                    } else {
                        emailInfo.textContent = 'Available!';
                        emailEl.css('border-color', 'green');
                        btnEl.removeAttribute('disabled')
                    }
                }
            })
        } else {
            emailInfo.textContent = 'Email is not valid. Please check for any spelling error!';
            btnEl.setAttribute('disabled', '');
        }
    });


    // Email register's ajax call
    $('#subscribe_btn').on('click', function (e) {
        e.preventDefault();
        console.log('Entered onclick event');
        let email = document.getElementById('email').value;
        let message = document.getElementById('message').value;
        let emailInfo = document.getElementById('email_info');
        $.ajax({
                url: `${BASE_URL}/`,
                type: 'POST',
                dataType: 'json',
                data: {
                    email: email,
                    message: message,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                beforeSend: function () {
                    console.log("Sending");
                },
                complete: function () {
                    console.log("Sent");
                },
                success: function (data) {
                    if (data.registered) {
                        emailInfo.textContent = data.message;
                    }
                },
                error: function () {
                    emailInfo.textContent = 'Error';
                }
            }
        )
    });
});
