BASE_URL = window.location.origin;
$(function ($) {

});

const read = (id) => {
    $.ajax({
        url: `${BASE_URL}/ajax/read/`,
        type: 'GET',
        dataType: 'json',
        data: {
            'id': id,
        },
        success: function (data) {
            console.log(`Changed read status of email with ID:  ${id}`);
            console.log(data.status_code);
            if (data.status_code === '200') {
                console.log("yes");
                b = document.querySelector(`#button_id_${id}`).className = 'read-email';
            }
        },

    })
};