// ---------------------------------------------- script untuk slide announcement ---------------------------------
// ----------------------------------------------------------------------------------------------------------------

let currentIndex = 0;
const slides = document.querySelectorAll('.carousel-item');
const totalSlides = slides.length;

function updateCarousel() {
    const carousel = document.querySelector('.carousel');
    const width = slides[0].clientWidth;
    carousel.style.transform = `translateX(-${currentIndex * (width / 2)}px)`;
}

function slideLeft() {
    if (currentIndex > 0) {
        currentIndex--;
        updateCarousel();
    }
}

function slideRight() {
    if (currentIndex < totalSlides - 2) { // Shows 2 items, slides by 1
        currentIndex++;
        updateCarousel();
    }
}

window.addEventListener('resize', updateCarousel);

// ---------------------------------------------- script untuk banner ---------------------------------------------
// ----------------------------------------------------------------------------------------------------------------

// slider.js
let slideIndex = 0;
showSlides(slideIndex);

// Function to go to the next or previous slide
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Function to go to a specific slide
function currentSlide(n) {
    showSlides(slideIndex = n);
}

// Function to display the correct slide and highlight the active dot
function showSlides(n) {
    let slides = document.getElementsByClassName("slide");
    let dots = document.getElementsByClassName("dot");
    if (n >= slides.length) { slideIndex = 0; } // Loop back to the first slide
    if (n < 0) { slideIndex = slides.length - 1; } // Loop to the last slide
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; // Hide all slides
    }
    for (let i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", ""); // Remove "active" class
    }
    slides[slideIndex].style.display = "block"; // Show the current slide
    dots[slideIndex].className += " active"; // Highlight the current dot

    
}

    // // JavaScript to automatically slide the carousel
    // let slideIndex = 0;
    // const slides = document.querySelectorAll('.slide');
    // const slideInterval = 3000; // Change slide every 3 seconds

    // function showSlides() {
    //     // Hide all slides
    //     slides.forEach((slide) => {
    //         slide.style.display = 'none';
    //     });

    //     // Move to the next slide
    //     slideIndex++;

    //     // Reset index if it exceeds the number of slides
    //     if (slideIndex > slides.length) {
    //         slideIndex = 1;
    //     }

    //     // Show the current slide
    //     slides[slideIndex - 1].style.display = 'block';

    //     // Set timer for the next slide
    //     setTimeout(showSlides, slideInterval);
    // }

    // // Start the slide show
    // showSlides();
