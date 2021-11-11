$(document).on("click", '[data-toggle="lightbox"]', function(event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});

$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    // console.log(scroll);

    if (scroll >= 450) {
        $("#mynav").addClass("bg-dark");
    } else {
        $("#mynav").removeClass("bg-dark");
    }
});