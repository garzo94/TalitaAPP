const hamburger = document.querySelector(".hamburger");
const menu = document.querySelector(".menu");
const sidebar = document.querySelector(".sidebar");
const gallery = document.querySelector(".gallery");

hamburger.addEventListener("click", ()=>{
    hamburger.classList.toggle("active");
    menu.classList.toggle("active");
    sidebar.classList.toggle("active");
    gallery.classList.toggle("active");
})



