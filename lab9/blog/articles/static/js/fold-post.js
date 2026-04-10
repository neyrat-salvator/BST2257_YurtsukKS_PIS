// Обработчик сворачивания постов
var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var post = e.target.parentElement;  // .one-post

        if (post.classList.contains("folded")) {
            // Развернуть
            e.target.innerHTML = "свернуть";
            post.classList.remove("folded");
        } else {
            // Свернуть
            e.target.innerHTML = "развернуть";
            post.classList.add("folded");
        }
    });
}