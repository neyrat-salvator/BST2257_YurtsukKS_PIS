document.addEventListener('DOMContentLoaded', function() {
    var foldBtns = document.querySelectorAll('.fold-button');

    for (var i = 0; i < foldBtns.length; i++) {
        foldBtns[i].addEventListener('click', function(event) {
            var post = event.target.closest('.one-post');

            if (post.classList.contains('folded')) {
                post.classList.remove('folded');
                event.target.textContent = 'Свернуть';
                event.target.classList.remove('folded');
            } else {
                post.classList.add('folded');
                event.target.textContent = 'Развернуть';
                event.target.classList.add('folded');
            }
        });
    }
});