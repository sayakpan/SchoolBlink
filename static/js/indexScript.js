$(document).ready(function () {
    var owl = $('.owl-carousel');

    owl.owlCarousel({
        items: 3, // Number of items to show at once
        loop: false, // Infinite loop
        autoplay: true, // Autoplay enabled
        autoplayTimeout: 2000, // Autoplay interval in milliseconds
        autoplayHoverPause: true, // Pause autoplay on hover
        stagePadding: 50,
        onChanged: function (event) {
            if (event.item.index + event.page.size === event.item.count) {
                setTimeout(function () {
                    owl.trigger('to.owl.carousel', [0]);
                }, 2000);

            }
        }
    });
});

