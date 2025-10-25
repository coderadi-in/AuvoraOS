// ? SELECTING ELEMENTS
const openNav = document.querySelector('#open-nav');
const closeNav = document.querySelector('#close-nav');
const nav = document.querySelector('.nav');

// & EVENT LISTENER FOR OPENING NAVBAR
openNav.addEventListener('click', () => {
    nav.style.display = 'flex';

    setTimeout(() => {
        nav.classList.add('open');
    }, 100);
});

// & EVENT LISTENER FOR CLOSING NAVBAR
closeNav.addEventListener('click', () => {
    nav.style.display = 'flex';

    setTimeout(() => {
        nav.classList.remove('open');
    }, 100);
});

// & SCRIPT TO CLOSE NAVBAR WHEN A LINK IS CLICKED
const navLinks = document.querySelectorAll('.nav .link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        nav.classList.remove('open');
    });
});