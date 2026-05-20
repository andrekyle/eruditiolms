// Main JavaScript file for the application
document.addEventListener('DOMContentLoaded', function() {
    // Initialize any components or fetch data
    fetchDashboardData();
    
    // Register service worker for PWA functionality
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js')
                .then(registration => {
                    console.log('ServiceWorker registration successful');
                })
                .catch(err => {
                    console.log('ServiceWorker registration failed: ', err);
                });
        });
    }
    
    // PWA Testing Functions
    testPWAFeatures();
});

// Fetch dashboard data from API
async function fetchDashboardData() {
    try {
        const response = await fetch('/api/chart-data');
        const data = await response.json();
        
        // Update dashboard stats
        if (document.getElementById('certifications-count')) {
            document.getElementById('certifications-count').textContent = data.certifications;
        }
        
        if (document.getElementById('pass-rate')) {
            document.getElementById('pass-rate').textContent = data.passRate + '%';
        }
        
        if (document.getElementById('retake-success')) {
            document.getElementById('retake-success').textContent = data.retakeSuccess + '%';
        }
        
        if (document.getElementById('top-performers')) {
            document.getElementById('top-performers').textContent = data.topPerformers + '%';
        }
    } catch (error) {
        console.error('Error fetching dashboard data:', error);
    }
}

// PWA Testing Functions
async function testPWAFeatures() {
    const results = document.createElement('div');
    results.style.position = 'fixed';
    results.style.top = '10px';
    results.style.right = '10px';
    results.style.backgroundColor = 'rgba(0,0,0,0.8)';
    results.style.color = 'white';
    results.style.padding = '15px';
    results.style.borderRadius = '5px';
    results.style.zIndex = '9999';
    
    // Test Service Worker
    const swStatus = navigator.serviceWorker ? 
        (await navigator.serviceWorker.getRegistration() ? ' Service Worker Registered' : ' Service Worker Not Registered') :
        ' Service Worker Not Supported';
    
    // Test Cache API
    const cacheStatus = 'caches' in window ? ' Cache API Available' : ' Cache API Not Available';
    
    // Test Manifest
    const manifestLink = document.querySelector('link[rel="manifest"]');
    const manifestStatus = manifestLink ? ' Manifest Linked' : ' Manifest Not Found';
    
    // Check if running in standalone mode
    const displayMode = window.matchMedia('(display-mode: standalone)').matches ? 
        ' Running as PWA' : 'Running in Browser';

    results.innerHTML = `
        <h6>PWA Feature Test</h6>
        <div>${swStatus}</div>
        <div>${cacheStatus}</div>
        <div>${manifestStatus}</div>
        <div>${displayMode}</div>
        <small style="font-size: 0.8em">Click to dismiss</small>
    `;
    
    results.onclick = () => results.remove();
    document.body.appendChild(results);
}
