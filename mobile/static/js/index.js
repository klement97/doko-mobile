BASE_URL = 'http://localhost:8000';

function isValid(email) {
    let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
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
            $.ajax({
                url: `${BASE_URL}/ajax/validate_email/`,
                type: 'GET',
                data: {
                    'email': email,
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
    $('#subscribe_btn').on('click', function () {
        console.log('Entered onclick event');
        let emailInfo = document.getElementById('email_info');
        $.ajax({
                url: `${BASE_URL}/register/`,
                type: 'post',
                beforeSend: function () {
                    console.log("Sending");
                },
                complete: function () {
                    console.log("Sent");
                },
                success: function (data) {
                    emailInfo.textContent = data.success;
                },
                error: function () {
                    emailInfo.textContent = 'Error';
                }
            }
        )
    });
});
