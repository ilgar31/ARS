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

$(document).ready(function() {

    $('input[type="file"]').change(function(){
        var value = $("input[type='file']").val().split("\\").at(-1);
        $('.file_name2').text(value);
        if (value) {
            $('.info_file_text2').text('');
        }
        else {
            $('.info_file_text2').text('*Если у Вас более одного файла, поместите их все в один архив');
        }
    });
});

document.getElementById("zat_btn").addEventListener("click", myFunction1);
function myFunction1() {
    document.body.style.overflow = "hidden";
}

document.getElementById("close_btn").addEventListener("click", myFunction2);
function myFunction2() {
    document.body.style.overflow = "scroll";
}

document.getElementById("zat_btn2").addEventListener("click", myFunction1);
function myFunction1() {
    document.body.style.overflow = "hidden";
}

document.getElementById("close_btn2").addEventListener("click", myFunction2);
function myFunction2() {
    document.body.style.overflow = "scroll";
}