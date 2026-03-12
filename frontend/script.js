// ========================================
// Smooth Scrolling Navigation
// ========================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const navHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = target.offsetTop - navHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
            
            // Close mobile menu if open
            const navMenu = document.getElementById('navMenu');
            navMenu.classList.remove('active');
        }
    });
});

// ========================================
// Mobile Menu Toggle
// ========================================
const mobileToggle = document.getElementById('mobileToggle');
const navMenu = document.getElementById('navMenu');

mobileToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    mobileToggle.classList.toggle('active');
});

// ========================================
// Navbar Scroll Effect
// ========================================
let lastScroll = 0;
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.style.boxShadow = '0 4px 16px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.1)';
    }
    
    lastScroll = currentScroll;
});

// ========================================
// AI Travel Story Generator
// ========================================
const destinationInput = document.getElementById('destinationInput');
const generateBtn = document.getElementById('generateBtn');
const demoOutput = document.getElementById('demoOutput');
const featureSelect = document.getElementById('featureSelect');
const BASE_URL = "http://127.0.0.1:8000";

// Travel story templates
const storyTemplates = [
    {
        intro: "Nestled in the heart of {destination}, a world of wonder awaits. This enchanting locale captivates visitors with its unique blend of natural beauty and cultural richness.",
        experience: "From sunrise to sunset, {destination} offers unforgettable experiences. Wander through vibrant markets, savor authentic local cuisine, and immerse yourself in the warm hospitality of the locals.",
        highlight: "The crown jewel of {destination} is its breathtaking landscapes that seem to be painted by nature itself. Every corner reveals a new perspective, a new story waiting to be discovered."
    },
    {
        intro: "Welcome to {destination}, where every moment becomes a cherished memory. This destination has been captivating travelers for generations with its timeless charm.",
        experience: "Adventure seekers and culture enthusiasts alike find their paradise in {destination}. The perfect harmony of tradition and modernity creates an atmosphere unlike anywhere else on Earth.",
        highlight: "What makes {destination} truly special is the authentic connection you'll feel with the place and its people. It's not just a destination; it's a transformative journey."
    },
    {
        intro: "Discover the magic of {destination}, a place where dreams meet reality. This extraordinary destination promises experiences that will stay with you long after you've returned home.",
        experience: "Whether you're seeking relaxation or adventure, {destination} delivers beyond expectations. Each day brings new discoveries, from hidden gems to iconic landmarks.",
        highlight: "The soul of {destination} lies in its ability to surprise and delight at every turn. It's a destination that calls you back, time and time again."
    }
];

const itineraryTemplates = [
    [
        "Morning: Explore the historic old town and local markets",
        "Afternoon: Visit iconic landmarks and cultural sites",
        "Evening: Enjoy sunset views and authentic local cuisine",
        "Night: Experience the vibrant nightlife and entertainment"
    ],
    [
        "Day 1: Arrival and city orientation tour",
        "Day 2: Adventure activities and nature exploration",
        "Day 3: Cultural immersion and local experiences",
        "Day 4: Relaxation and shopping at local boutiques"
    ],
    [
        "Morning: Sunrise photography at scenic viewpoints",
        "Midday: Culinary tour and cooking class",
        "Afternoon: Museum visits and art galleries",
        "Evening: Traditional performance and dinner"
    ]
];

const captionTemplates = [
    "Lost in the beauty of {destination} ✨ Where every moment feels like a dream. #TravelGoals #{hashtag}",
    "Finding paradise in {destination} 🌴 This place has stolen my heart! #Wanderlust #{hashtag}",
    "{destination} vibes 🌊 Living my best life in this incredible destination! #TravelDiaries #{hashtag}",
    "Exploring the wonders of {destination} 🗺️ Adventure awaits around every corner! #ExploreMore #{hashtag}"
];

const bestTimeTemplates = [
    "The ideal time to visit is during spring (March-May) when the weather is pleasant and crowds are manageable.",
    "Plan your trip between September and November for the best weather and fewer tourists.",
    "Summer months (June-August) offer the most activities, though it's peak tourist season.",
    "Winter (December-February) provides a unique perspective with fewer crowds and special seasonal charm."
];

generateBtn.addEventListener('click', generateTravelStory);
destinationInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        generateTravelStory();
    }
});

async function generateTravelStory() {
    console.log("Button Clicked");
    const userInput = destinationInput.value.trim();
    const selectedFeature = featureSelect.value;

    if (!userInput) {
        alert('Please enter something!');
        return;
    }

    generateBtn.classList.add('loading');
    generateBtn.disabled = true;

    let payload = {};

    if (selectedFeature === "recommend") {
        payload = { interest: userInput };
    } else {
        payload = { text: userInput };
    }

    try {
        const response = await fetch(`${BASE_URL}/${selectedFeature}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        displayBackendResult(selectedFeature, data.result);

    } catch (error) {
        console.error("Backend Error:", error);
        alert("Backend connection failed. Check console.");
    }

    generateBtn.classList.remove('loading');
    generateBtn.disabled = false;
}
function createStoryOutput(destination) {
    // Randomly select templates
    const template = storyTemplates[Math.floor(Math.random() * storyTemplates.length)];
    const itinerary = itineraryTemplates[Math.floor(Math.random() * itineraryTemplates.length)];
    const caption = captionTemplates[Math.floor(Math.random() * captionTemplates.length)];
    const bestTime = bestTimeTemplates[Math.floor(Math.random() * bestTimeTemplates.length)];
    
    // Create hashtag from destination
    const hashtag = destination.replace(/[^a-zA-Z0-9]/g, '');
    
    // Replace placeholders
    const story = {
        title: `Discover ${destination}`,
        narrative: `${template.intro.replace(/{destination}/g, destination)} ${template.experience.replace(/{destination}/g, destination)} ${template.highlight.replace(/{destination}/g, destination)}`,
        itinerary: itinerary,
        caption: caption.replace(/{destination}/g, destination).replace(/{hashtag}/g, hashtag),
        bestTime: bestTime
    };
    
    return story;
}

function displayStory(story) {
    const outputHTML = `
        <div class="output-card">
            <div class="output-section">
                <h3>📖 ${story.title}</h3>
                <p>${story.narrative}</p>
            </div>
            
            <div class="output-section">
                <h3>🗓️ Suggested Itinerary</h3>
                <ul>
                    ${story.itinerary.map(item => `<li>${item}</li>`).join('')}
                </ul>
            </div>
            
            <div class="output-section">
                <h3>📱 Social Media Caption</h3>
                <p><em>${story.caption}</em></p>
            </div>
            
            <div class="output-section">
                <h3>🌤️ Best Time to Visit</h3>
                <p>${story.bestTime}</p>
            </div>
        </div>
    `;
    
    demoOutput.innerHTML = outputHTML;
    
    // Scroll to output
    demoOutput.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
function displayBackendResult(feature, result) {

    // Handle empty or undefined responses
    if (!result) {
        result = "No response received from backend.";
    }

    let formatted = "";

    // If backend returns a list
    if (Array.isArray(result)) {
        formatted = `
            <ul>
                ${result.map(item => `<li>${item}</li>`).join("")}
            </ul>
        `;
    } 
    // If backend returns text
    else {
        formatted = `<pre style="white-space: pre-wrap;">${result}</div>`;
    }

    const outputHTML = `
        <div class="output-card">
            <div class="output-section">
                <h3>✨ ${feature.replace("-", " ").toUpperCase()}</h3>
                ${formatted}
            </div>
        </div>
    `;

    demoOutput.innerHTML = outputHTML;
    demoOutput.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// ========================================
// Intersection Observer for Scroll Animations
// ========================================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all cards and sections
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll(
        '.highlight-card, .feature-card, .social-card, .team-card, .about-content'
    );
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// ========================================
// Dynamic Year in Footer
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    const currentYear = new Date().getFullYear();
    const footerText = document.querySelector('.footer-bottom p');
    if (footerText) {
        footerText.innerHTML = footerText.innerHTML.replace('2026', currentYear);
    }
});

// ========================================
// Add Active State to Navigation Links
// ========================================
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// ========================================
// Preload Demo with Example
// ========================================
window.addEventListener('load', () => {
    // Add a subtle entrance animation to hero elements
    const heroElements = document.querySelectorAll('.hero-title, .hero-subtitle, .hero-cta');
    heroElements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 200);
    });
});

// ========================================
// Enhanced Button Interactions
// ========================================
document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-3px)';
    });
    
    btn.addEventListener('mouseleave', function() {
        if (!this.classList.contains('loading')) {
            this.style.transform = 'translateY(0)';
        }
    });
});

// ========================================
// Console Welcome Message
// ========================================
console.log('%c🌍 Welcome to DestiNext AI! ', 'background: linear-gradient(135deg, #0ea5e9, #14b8a6); color: white; font-size: 20px; padding: 10px; border-radius: 5px;');
console.log('%cExplore the power of AI-driven destination marketing!', 'color: #0ea5e9; font-size: 14px;');





async function loadDestinations() {

    const response = await fetch("http://127.0.0.1:8000/destinations");
    const data = await response.json();

    const datalist = document.getElementById("destinationList");

    data.destinations.forEach(place => {

        const option = document.createElement("option");
        option.value = place;

        datalist.appendChild(option);

    });

}

async function loadDashboard() {

    const revenueRes = await fetch("http://127.0.0.1:8000/dashboard/revenue");
    const revenueFig = await revenueRes.json();

    Plotly.newPlot(
        "revenuechart",
        revenueFig.data,
        revenueFig.layout
    );

    const seasonalRes = await fetch("http://127.0.0.1:8000/dashboard/seasonal");
    const seasonalFig = await seasonalRes.json();

    Plotly.newPlot(
        "seasonalChart",
        seasonalFig.data,
        seasonalFig.layout
    );
}

async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();
    if (!message) return;

    // Show user message
    chatBox.innerHTML += `<div><b>You:</b> ${message}</div>`;
    input.value = "";

    // Show typing indicator
    chatBox.innerHTML += `<div id="typing"><b>DestiNext Guide:</b> typing...</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    // Small delay so browser renders typing
    await new Promise(resolve => setTimeout(resolve, 0));

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    // Remove typing indicator
    const typing = document.getElementById("typing");
    if (typing) typing.remove();

    // Show AI response
    chatBox.innerHTML += `<div><b>DestiNext Guide:</b> ${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}


function toggleChat(){

    const popup = document.getElementById("chat-popup");

    if(popup.style.display === "flex"){
        popup.style.display = "none";
    }else{
        popup.style.display = "flex";
    }

}


document.addEventListener("DOMContentLoaded", () => {

    loadDestinations();
    loadDashboard();

    const input = document.getElementById("user-input");

    input.addEventListener("keydown", function(event){
        if(event.key === "Enter"){
            event.preventDefault();
            sendMessage();
        }
    });

});

