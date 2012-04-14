jQuery(function ($) {

    $('#show').autocomplete({
        source: "show/auto"
    });

    //ajaxify the post submit
    $('form#add_show').submit(function (e) {
        e.preventDefault();
        $.post( $(this).attr('action'), $(this).serialize(),
            function(show, status) {
                if (status == "success") {
                   $('#show_list').append(show).hide().fadeIn(400);
                }
        });
    });

    $('form#add_provider').submit(function (e) {
        e.preventDefault();
        $.post( $(this).attr('action'), $(this).serialize(),
            function(provider, status) {
                if (status == "success") {
                    $('#provider_list').append(provider).hide().fadeIn(400);
                }
            });
    });
});
