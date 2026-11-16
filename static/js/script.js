let currentIndex = 0;
const items = document.querySelectorAll('.carousel-item');
const totalItems = items.length;

function slideRight() {
    if (currentIndex < totalItems - 2) {
        currentIndex++;
        updateCarousel();
    }
}

function slideLeft() {
    if (currentIndex > 0) {
        currentIndex--;
        updateCarousel();
    }
}

function updateCarousel() {
    const carousel = document.querySelector('.carousel');
    carousel.style.transform = `translateX(-${currentIndex * 270}px)`;
}
