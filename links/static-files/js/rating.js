// Rating modal
$(document).ready(function() {
    var rateBtn = $('#rateBtn');
    var rateModal = $('#rateModal');
    var ratingContainer = $('#ratingStars');
    var ratingCount = $('#ratingCount');
    var ratingForm = $('#ratingForm');
    var ratingInput = $('#ratingInput');
    var ratingEmoji = $('#ratingEmoji');
    var ratingStars = $('.star-rating');
    var ratingError = $('#ratingError');

    var emojis = [
        '<svg class="emoji-1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><circle cx="256" cy="256" r="256" fill="#ffd93b"></circle><path d="M512 256A256 256 0 0 1 56.7 416.7a256 256 0 0 0 360-360c58.1 47 95.3 118.8 95.3 199.3z" fill="#f4c534"></path><path d="M328.4 428a92.8 92.8 0 0 0-145-.1 6.8 6.8 0 0 1-12-5.8 86.6 86.6 0 0 1 84.5-69 86.6 86.6 0 0 1 84.7 69.8c1.3 6.9-7.7 10.6-12.2 5.1z" fill="#3e4347"></path><path d="M269.2 222.3c5.3 62.8 52 113.9 104.8 113.9 52.3 0 90.8-51.1 85.6-113.9-2-25-10.8-47.9-23.7-66.7-4.1-6.1-12.2-8-18.5-4.2a111.8 111.8 0 0 1-60.1 16.2c-22.8 0-42.1-5.6-57.8-14.8-6.8-4-15.4-1.5-18.9 5.4-9 18.2-13.2 40.3-11.4 64.1z" fill="#f4c534"></path><path d="M357 189.5c25.8 0 47-7.1 63.7-18.7 10 14.6 17 32.1 18.7 51.6 4 49.6-26.1 89.7-67.5 89.7-41.6 0-78.4-40.1-82.5-89.7A95 95 0 0 1 298 174c16 9.7 35.6 15.5 59 15.5z" fill="#fff"></path><path d="M396.2 246.1a38.5 38.5 0 0 1-38.7 38.6 38.5 38.5 0 0 1-38.6-38.6 38.6 38.6 0 1 1 77.3 0z" fill="#3e4347"></path><path d="M380.4 241.1c-3.2 3.2-9.9 1.7-14.9-3.2-4.8-4.8-6.2-11.5-3-14.7 3.3-3.4 10-2 14.9 2.9 4.9 5 6.4 11.7 3 15z" fill="#fff"></path><path d="M242.8 222.3c-5.3 62.8-52 113.9-104.8 113.9-52.3 0-90.8-51.1-85.6-113.9 2-25 10.8-47.9 23.7-66.7 4.1-6.1 12.2-8 18.5-4.2 16.2 10.1 36.2 16.2 60.1 16.2 22.8 0 42.1-5.6 57.8-14.8 6.8-4 15.4-1.5 18.9 5.4 9 18.2 13.2 40.3 11.4 64.1z" fill="#f4c534"></path><path d="M155 189.5c-25.8 0-47-7.1-63.7-18.7-10 14.6-17 32.1-18.7 51.6-4 49.6 26.1 89.7 67.5 89.7 41.6 0 78.4-40.1 82.5-89.7A95 95 0 0 0 214 174c-16 9.7-35.6 15.5-59 15.5z" fill="#fff"></path><path d="M115.8 246.1a38.5 38.5 0 0 0 38.7 38.6 38.5 38.5 0 0 0 38.6-38.6 38.6 38.6 0 1 0-77.3 0z" fill="#3e4347"></path><path d="M131.6 241.1c3.2 3.2 9.9 1.7 14.9-3.2 4.8-4.8 6.2-11.5 3-14.7-3.3-3.4-10-2-14.9 2.9-4.9 5-6.4 11.7-3 15z" fill="#fff"></path></svg>',
       '<svg class="emoji-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><circle cx="256" cy="256" r="256" fill="#ffd93b"></circle><path d="M512 256A256 256 0 0 1 56.7 416.7a256 256 0 0 0 360-360c58.1 47 95.3 118.8 95.3 199.3z" fill="#f4c534"></path><path d="M336.6 403.2c-6.5 8-16 10-25.5 5.2a117.6 117.6 0 0 0-110.2 0c-9.4 4.9-19 3.3-25.6-4.6-6.5-7.7-4.7-21.1 8.4-28 45.1-24 99.5-24 144.6 0 13 7 14.8 19.7 8.3 27.4z" fill="#3e4347"></path><path d="M276.6 244.3a79.3 79.3 0 1 1 158.8 0 79.5 79.5 0 1 1-158.8 0z" fill="#fff"></path><circle cx="340" cy="260.4" r="36.2" fill="#3e4347"></circle><g fill="#fff"><ellipse transform="rotate(-135 326.4 246.6)" cx="326.4" cy="246.6" rx="6.5" ry="10"></ellipse><path d="M231.9 244.3a79.3 79.3 0 1 0-158.8 0 79.5 79.5 0 1 0 158.8 0z"></path></g><circle cx="168.5" cy="260.4" r="36.2" fill="#3e4347"></circle><ellipse transform="rotate(-135 182.1 246.7)" cx="182.1" cy="246.7" rx="10" ry="6.5" fill="#fff"></ellipse></svg>',
       '<svg class="emoji-3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><circle cx="256" cy="256" r="256" fill="#ffd93b"></circle><path d="M407.7 352.8a163.9 163.9 0 0 1-303.5 0c-2.3-5.5 1.5-12 7.5-13.2a780.8 780.8 0 0 1 288.4 0c6 1.2 9.9 7.7 7.6 13.2z" fill="#3e4347"></path><path d="M512 256A256 256 0 0 1 56.7 416.7a256 256 0 0 0 360-360c58.1 47 95.3 118.8 95.3 199.3z" fill="#f4c534"></path><g fill="#fff"><path d="M115.3 339c18.2 29.6 75.1 32.8 143.1 32.8 67.1 0 124.2-3.2 143.2-31.6l-1.5-.6a780.6 780.6 0 0 0-284.8-.6z"></path><ellipse cx="356.4" cy="205.3" rx="81.1" ry="81"></ellipse></g><ellipse cx="356.4" cy="205.3" rx="44.2" ry="44.2" fill="#3e4347"></ellipse><g fill="#fff"><ellipse transform="scale(-1) rotate(45 454 -906)" cx="375.3" cy="188.1" rx="12" ry="8.1"></ellipse><ellipse cx="155.6" cy="205.3" rx="81.1" ry="81"></ellipse></g><ellipse cx="155.6" cy="205.3" rx="44.2" ry="44.2" fill="#3e4347"></ellipse><ellipse transform="scale(-1) rotate(45 454 -421.3)" cx="174.5" cy="188" rx="12" ry="8.1" fill="#fff"></ellipse></svg>',
        '<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve"><circle fill="#FFD93B" cx="256" cy="256" r="256"/><path fill="#F4C534" d="M512,256c0,141.4-114.6,256-256,256c-77.4,0-150.7-35-199.3-95.3c110,88.8,271.2,71.6,360-38.4c75.8-93.8,75.8-227.8,0-321.6C474.8,103.7,512,175.5,512,256z"/><path fill="#E24B4B" d="M231.9,189.6c0,50.1-75.7,95.9-75.7,95.9s-75.8-45.8-75.8-95.9c-0.1-21.4,17.1-38.8,38.5-38.9c17.2-0.1,32.3,11.1,37.3,27.6c6.3-20.4,28-31.8,48.4-25.5C220.8,157.7,231.8,172.6,231.9,189.6z"/><path fill="#D03F3F" d="M93.1,161c-8.1,7.3-12.6,17.7-12.6,28.5c0,50.1,75.7,95.9,75.7,95.9C76.9,218.6,92.6,163,93,161H93.1z"/><path fill="#FFFFFF" d="M214.4,188.2c-3.7,3.1-10,1-14.1-4.2c-4.3-5.3-4.7-11.7-1.2-14.4c3.7-2.9,9.9-0.7,14.2,4.5C217.4,179.5,218,185.8,214.4,188.2L214.4,188.2z"/><path fill="#E24B4B" d="M431.6,189.6c0,50.1-75.8,95.9-75.8,95.9s-75.7-45.8-75.7-95.9c-0.1-21.4,17.1-38.8,38.5-38.9c17.2-0.1,32.3,11.1,37.3,27.6c6.3-20.4,28-31.8,48.4-25.5C420.5,157.7,431.5,172.6,431.6,189.6L431.6,189.6z"/><path fill="#D03F3F" d="M292.9,161c-8.1,7.3-12.6,17.7-12.6,28.5c0,50.1,75.7,95.9,75.7,95.9C276.7,218.6,292.4,163,292.9,161L292.9,161z"/><path fill="#FFFFFF" d="M414.2,188.2c-3.7,3.1-10,1-14.1-4.2c-4.3-5.3-4.7-11.7-1.2-14.4c3.7-2.9,9.9-0.7,14.2,4.5C417.1,179.5,417.7,185.8,414.2,188.2L414.2,188.2z"/><path fill="#3E4347" d="M381.7,374.1c-30.2,35.9-75.3,64.4-125.7,64.4s-95.4-28.5-125.8-64.2c-6.3-7.4-5.4-18.5,2.1-24.8c4-3.4,9.3-4.8,14.4-3.9c72.3,12.8,146.4,12.7,218.7-0.1C381.6,342.8,392.4,361.6,381.7,374.1L381.7,374.1z"/><path fill="#E24B4B" d="M256,438.5c25.7,0,50-7.5,71.7-19.5c-9-33.7-27.7-36.3-50.5-24.6c-32.4,16.5-74.7-16.8-87.7,27.2C209.8,432,232.3,438.6,256,438.5L256,438.5z"/></svg>',
        '<svg class="emoji-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><g fill="#ffd93b"><circle cx="256" cy="256" r="256"></circle><path d="M512 256A256 256 0 0 1 56.8 416.7a256 256 0 0 0 360-360c58 47 95.2 118.8 95.2 199.3z"></path></g><path d="M512 99.4v165.1c0 11-8.9 19.9-19.7 19.9h-187c-13 0-23.5-10.5-23.5-23.5v-21.3c0-12.9-8.9-24.8-21.6-26.7-16.2-2.5-30 10-30 25.5V261c0 13-10.5 23.5-23.5 23.5h-187A19.7 19.7 0 0 1 0 264.7V99.4c0-10.9 8.8-19.7 19.7-19.7h472.6c10.8 0 19.7 8.7 19.7 19.7z" fill="#e9eff4"></path><path d="M204.6 138v88.2a23 23 0 0 1-23 23H58.2a23 23 0 0 1-23-23v-88.3a23 23 0 0 1 23-23h123.4a23 23 0 0 1 23 23z" fill="#45cbea"></path><path d="M476.9 138v88.2a23 23 0 0 1-23 23H330.3a23 23 0 0 1-23-23v-88.3a23 23 0 0 1 23-23h123.4a23 23 0 0 1 23 23z" fill="#e84d88"></path><g fill="#38c0dc"><path d="M95.2 114.9l-60 60v15.2l75.2-75.2zM123.3 114.9L35.1 203v23.2c0 1.8.3 3.7.7 5.4l116.8-116.7h-29.3z"></path></g><g fill="#d23f77"><path d="M373.3 114.9l-66 66V196l81.3-81.2zM401.5 114.9l-94.1 94v17.3c0 3.5.8 6.8 2.2 9.8l121.1-121.1h-29.2z"></path></g> <path d="M329.5 395.2c0 44.7-33 81-73.4 81-40.7 0-73.5-36.3-73.5-81s32.8-81 73.5-81c40.5 0 73.4 36.3 73.4 81z" fill="#3e4347"></path><path d="M256 476.2a70 70 0 0 0 53.3-25.5 34.6 34.6 0 0 0-58-25 34.4 34.4 0 0 0-47.8 26 69.9 69.9 0 0 0 52.6 24.5z" fill="#e24b4b"></path><path d="M290.3 434.8c-1 3.4-5.8 5.2-11 3.9s-8.4-5.1-7.4-8.7c.8-3.3 5.7-5 10.7-3.8 5.1 1.4 8.5 5.3 7.7 8.6z" fill="#fff" opacity=".2"></path></svg>',
    ];

    function toggleRateModal() {
        rateModal.toggleClass('open');
    }

    function updateRating(evt) {
        var starCount = 5;
        var ratingValue = parseInt(evt.target.getAttribute('data-value'), 10);
        // Update input value
        ratingInput.val(evt.target.getAttribute('data-value'));
        // Update rating emoji
        ratingEmoji.html(emojis[ratingValue - 1]);
        // Update rating stars
        for(var i=1; i <= starCount; i++) {
            var star = $('#star' + i.toString());
            if (i <= ratingValue) {
                star.addClass('fill');
            } else {
                star.removeClass('fill');
            }
        }
    }

    function submitRatingForm(evt) {
        evt.preventDefault();
        ratingError.html();
        var url = ratingForm.attr('action');
        var htmlForm = document.getElementById('ratingForm');
        const data = Object.fromEntries(new FormData(htmlForm).entries());
        data.rating = parseInt(data.rating, 10);

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: function(response) {
                rateModal.removeClass('open');
                updatedRating = response.rating;
                updatedCount = response.rating_count;
                updateRatingTotal(updatedRating, updatedCount);
            },
            error: function(response) {
                ratingError.html(response.responseText);
            },
        });
        return false;
    }

    function updateRatingTotal(rating, count) {
        // Update the count
        ratingCount.data('count', count);
        ratingCount.html(count);
        // Update rating stars
        ratingContainer.data('value', rating)
        var roundedRating = Math.round(rating * 2) / 2;
        var starCount = 5;
        for(var i=1; i <= starCount; i++) {
            var star = $('#starRating' + i.toString());
            // Remove previously classes
            star.removeClass('fill');
            star.removeClass('half');
            if (i <= roundedRating) {
                star.addClass('fill');
            } else if ((i - 0.5) === roundedRating) {
                star.addClass('half');
            }
        }
    }

    rateBtn.on('click', toggleRateModal);
    ratingStars.each(function (_, star) {
        $(star).on('click', updateRating);
    });
    ratingForm.on('submit', submitRatingForm);
});