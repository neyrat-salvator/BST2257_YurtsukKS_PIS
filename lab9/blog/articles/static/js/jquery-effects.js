$(document).ready(function() {
    // 1. Подсветка наведённого поста (background)
    $('.one-post').hover(
        function() {
            $(this).css({
                'background-color': '#2f5849ac',
                'color': '#fcfcfc'
            });
        },
        function() {
            $(this).css({
                'background-color': 'transparent',
                'border': 'none',
                'color': '#ffffff'
            });
        }
    );

    // 2. Эффект для картинки-логотипа
    $('.logo').hover(
        function() {
            $(this).animate({
                width: '220px',
                opacity: 0.7
            }, 300);
            $('.header').animate({
                height: '100px',
                opacity: 0.7
            }, 300);
        },
        function() {
            $(this).animate({
                width: '200px',
                opacity: 1
            }, 300);
            $('.header').animate({
                height: '90px',
                opacity: 1
            }, 300);
        }
    );
});