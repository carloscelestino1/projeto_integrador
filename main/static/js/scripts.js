// Isso é opcional se você quiser um efeito de rolagem suave ao clicar nos links.
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// // script.js
// const imageSection = document.getElementById('pagina-inicial');
// const image = document.querySelector('.hidden-image');

// const options = {
//     root: null,
//     rootMargin: '0px',
//     threshold: 0.3
// };

// const observer = new IntersectionObserver((entries, observer) => {
//     entries.forEach(entry => {
//         if (entry.isIntersecting) {
//             image.classList.add('fade-in');
//             observer.unobserve(entry.target);
//         }
//     });
// }, options);

// observer.observe(imageSection);

// script.js
const sections = document.querySelectorAll('.main-bg');

const options = {
    root: null,
    rootMargin: '0px',
    threshold: 0.3
};

sections.forEach(section => {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const image = entry.target.querySelector('.hidden-image');
                image.classList.add('fade-in');
                observer.unobserve(entry.target);
                // Reativa o observador para continuar detectando
                observer.observe(entry.target);
            }
        });
    }, options);

    observer.observe(section);
});





