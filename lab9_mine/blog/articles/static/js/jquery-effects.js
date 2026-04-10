$(document).ready(function() {
    // Используемые  псевдоклассы CSS
    var onePost = $('.one-post');
    var onePostHeader = $('.one-post-header');
    var logo = $('.logo');
    var foldButton = $('.fold-button');
    var readMore = $('.read-more');

    // Эффект подсветки и наведения
    onePost.hover(
        function() {
            // При наведени курсора
            $(this).css({
                background: 'rgba(0, 0, 0, 0.4)',
                color: 'rgba(255, 255, 255, 1)',
                transform: 'translateX(10px)',
                transition: 'all 0.3s ease'
            });

            $(this).find('a').css({
                color: 'rgba(255, 255, 255, 1)',
                transition: 'all 0.3s ease'
            });
        },
        function() {
            // Когда курсор уходит
            $(this).css({
                background: 'rgba(255, 255, 255, 1)',
                color: 'rgba(0, 0, 0, 1)',
                transform: 'translateX(0)',
                transition: 'all 0.3s ease'
            });

            $(this).find('a').css({
                color: 'rgba(0, 0, 0, 0.5)',
                transition: 'all 0.3s ease'
            });

            // Возвращаем тень
            var shadow = $(this).find(onePost);
            if (shadow.length) {
                shadow.animate({ opacity: '0' }, 200);
            }
        }
    );

    // Эффект для картинки-логотипа
    logo.hover(
        function() {
            // При наведении увеличиваем
            $(this).animate({
                width: '170px',
                marginTop: '-5px'
            }, 300);
        }
    );

    // Паралакс на логотипе
    logo.hover(
        function() {
            $(this).animate({
                width: '170px',
                opacity: 0.7
            }, 300);
        },
        function() {
            $(this).animate({
                width: '150px',
                opacity: 1
            }, 300);
        }
    );

    // Эффект для ссылки "Читать далее"
    readMore.hover(
        function() {
            $(this).animate({
                paddingLeft: '20px',
                paddingRight: '20px'
            }, 150);
        },
        function() {
            $(this).animate({
                paddingLeft: '0px',
                paddingRight: '0px'
            }, 150);
        }
    );

    console.log('jQuery эффекты активированы!')
});