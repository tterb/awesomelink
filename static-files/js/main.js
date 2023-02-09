$(document).ready(function(){
    var overlay = $('#overlay');
    var overlayToggle = $('#overlayToggle');
    var modalCloses = $('.modal-close');
    var refreshBtn = $('#refreshBtn');
    var ratingStars = $('#ratingStars');

    function toggleOverlay() {
        overlay.toggleClass('show');
        overlayToggle.toggleClass('expanded');
    }

    function closeModal(evt) {
        var modal = evt.target.parentNode.parentNode;
        modal.classList.remove('open');
    }

    function refreshPage() {
        location.reload();
    }

    function showRating() {
        var starCount = 5;
        var currentRating = parseFloat(ratingStars.data('value'), 10);
        var roundedRating = Math.round(currentRating*2)/2;
        for(var i=1; i <= starCount; i++) {
            var star = $('#starRating' + i.toString());
            if (i <= roundedRating) {
                star.addClass('fill');
            } else if ((i - 0.5) === roundedRating) {
                star.addClass('half');
            } else {
                star.removeClass('fill');
            }
        }
    }

    overlayToggle.on('click', toggleOverlay);
    refreshBtn.on('click', refreshPage);
    modalCloses.each(function (_, close) {
        $(close).on('click', closeModal);
    });
    showRating();
});
