document.getElementById('menu').addEventListener('click', e=> {

    if (document.getElementById('nav').style.display == "none") {
        document.getElementById('nav').style.display = "block";
    }
    else {
        document.getElementById('nav').style.display = 'none';
    }
})