<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    $(document).ready(function () {
        // отслеживаем событие отправки формы
        $('#contactForm').submit(function () {
            // создаем AJAX-вызов
            $.ajax({
                data: $(this).serialize(), // получаем данные формы
                type: $(this).attr('method'), // GET или POST
                url: "{% url 'main_pages:index' %}",
                // если успешно, то
                success: function (json) {
                    $('#name').val('');
                    $('#email').val('');
                    $('#title').val('');
                    $('#text').val('');
                    alert("Спасибо, что обратились к нам " + response.name);
                    console.log(json); // log the returned json to the console
                    console.log("success"); // another sanity check
                },
                // если ошибка, то
                error: function (xhr,errmsg,err) {
                    // предупредим об ошибке
                    $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    // alert(response.responseJSON.errors);
                    // console.log(response.responseJSON.errors)
                }
            });
            // return false;
        });
    })