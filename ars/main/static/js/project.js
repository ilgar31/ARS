var imgIndex = 0;
showImg(imgIndex);

function currentImg(n) {
  showImg(imgIndex = n);
}

function showImg(n) {
  var i;
  var images = document.getElementsByClassName("head_images");
  var buttons = document.getElementsByClassName("image_item");

  for (i = 0; i < images.length; i++) {
      images[i].style.display = "none";
  }
  for (i = 0; i < buttons.length; i++) {
      buttons[i].className = buttons[i].className.replace(" active", "");
  }
  images[imgIndex].style.display = "block";
  buttons[imgIndex].className += " active";
}
