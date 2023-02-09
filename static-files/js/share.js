// Share modal
$(document).ready(function() {
    var shareModal = $('#shareModal');
    var showModal = $('#shareBtn');
    var shareButtons = $('.share-link-button');

    function toggleShareModal() {
        shareModal.toggleClass('open');
    }

    function getShareText() {
        const text = 'Check out this awesome link!'
        return encodeURIComponent(text);
    }

    function getShareURL(linkId) {
        const base = location.href;
        return `${base}${linkId}`;
    }

    function shareFacebook(url) {
        window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,width=600,height=400');
    }

    function shareLinkedin(url) {
        window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}`);
    }

    function shareTwitter(url, text) {
        var encodedUrl = encodeURIComponent(url);
        window.open(`https://twitter.com/intent/tweet?url=${encodedUrl}&text=${text}`, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,width=600,height=300');
    }

    function shareReddit(url, text) {
        window.open(`https://www.reddit.com/submit?title=${text}&url=${url}`, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,width=600,height=600');
    }

    function copyLink(url) {
        // Create a temporary input element
        let input = document.createElement('input');
        input.setAttribute('type', 'text');
        input.value = url;
        document.body.appendChild(input);
        // Select and copy the input contents
        input.select();
        document.execCommand('copy');
        // Remove the temporary input
        document.body.removeChild(input);
    }

    function shareLink(evt) {
        var type = evt.currentTarget.dataset.type;
        var linkId = evt.currentTarget.dataset.id;
        var url = getShareURL(linkId);
        var text = getShareText();
        switch(type) {
            case 'facebook':
                shareFacebook(url);
                break;
            case 'twitter':
                shareTwitter(url, text);
                break;
            case 'linkedin':
                shareLinkedin(url);
                break;
            case 'reddit':
                shareReddit(url, text);
                break;
            case 'link':
                copyLink(url);
                break;
        }
        var url = getShareURL(linkId);
    }

    showModal.on('click', toggleShareModal);
    shareButtons.each(function (_, button) {
        $(button).on('click', shareLink);
    });
});