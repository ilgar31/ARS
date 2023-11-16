document.getElementById('menu').addEventListener('click', e=> {

    if (document.getElementById('nav').style.display == "none") {
        document.getElementById('nav').style.display = "block";
    }
    else {
        document.getElementById('nav').style.display = 'none';
    }
})


$(document).ready(function() {

    $('input[type="file"]').change(function(){
        var value = $("input[type='file']").val().split("\\").at(-1);
        $('.file_name').text(value);
        if (value) {
            $('.info_file_text').text('');
        }
        else {
            $('.info_file_text').text('*Если у Вас более одного файла, поместите их все в один архив');
        }
    });

});