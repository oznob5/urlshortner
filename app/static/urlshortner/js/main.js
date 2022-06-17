$(document).ready(function() {
    $('button.button').on('click', function(e) {
        e.preventDefault();
        
        $.ajax({
            method: "POST",
            url: "/create/",
            data: {
                link: $('input.input').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data) {
                $('h2.output').html('localhost:8000/' + data);
            }
        })
    })
});