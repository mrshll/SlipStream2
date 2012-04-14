jQuery(function ($) {

    $('#show').autocomplete({
        source: "show/auto"
    });

    //ajaxify the post submit
    var AJAXify = true;
    $('form').submit(function (e) {
        if (!AJAXify) return;
        e.preventDefault();
        $.post( $(this).attr('action') , $(this).serialize() );
    });
});
