document.getElementById('menu').addEventListener('click', e=> {

    if (document.getElementById('nav').style.opacity == 0) {
        document.getElementById('nav').style.opacity = 1;
    }
    else {
        document.getElementById('nav').style.opacity = 0;
    }
})