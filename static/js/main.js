jQuery(function ($) {

    $('#show').autocomplete({
        source: "show/auto"
    });

    //ajaxify the post submit
    $('form#new_show').submit(function (e) {
        e.preventDefault();
        $.post( $(this).attr('action'), $(this).serialize(),
            function(show, status) {
                if (status == "success") {
                   $('#show_list').append(show).hide().fadeIn(400);
                }
        });
    });
});
