// Calendar editing functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize variables
    let calendarData = {};
    let highlightedStates = {};
    let currentEditDay = null;
    let currentEditMonth = null;
    let currentEventId = null;
    let currentEventMonth = null;
    let currentHighlight = null;
    
    // Load saved data from localStorage
    if (localStorage.getItem('calendarData')) {
        calendarData = JSON.parse(localStorage.getItem('calendarData'));
    }
    
    if (localStorage.getItem('highlightedStates')) {
        highlightedStates = JSON.parse(localStorage.getItem('highlightedStates'));
    }
    
    // Initialize Quill editor
    const quill = new Quill('#editor', {
        theme: 'snow',
        placeholder: 'Add event details...',
        modules: {
            toolbar: [
                ['bold', 'italic', 'underline'],
                [{ 'list': 'ordered'}, { 'list': 'bullet' }],
                ['link']
            ]
        }
    });
    
    const eventQuill = new Quill('#eventEditor', {
        theme: 'snow',
        placeholder: 'Add event details...',
        modules: {
            toolbar: [
                ['bold', 'italic', 'underline'],
                [{ 'list': 'ordered'}, { 'list': 'bullet' }],
                ['link']
            ]
        }
    });
    
    // Apply saved data to calendar
    applyCalendarData();
    
    // Add event listeners to calendar days
    setupCalendarDayListeners();
    
    // Function to apply saved data to calendar
    function applyCalendarData() {
        // Apply content and highlights to calendar days
        for (const key in calendarData) {
            const [month, day] = key.split('-');
            const dayElement = document.querySelector(`.calendar-day[data-month="${month}"][data-day="${day}"]`);
            
            if (dayElement) {
                const contentElement = dayElement.querySelector('.day-content');
                if (contentElement) {
                    contentElement.innerHTML = calendarData[key];
                    
                    if (calendarData[key].trim()) {
                        dayElement.classList.add('has-event');
                    }
                }
            }
        }
        
        // Apply highlights
        for (const key in highlightedStates) {
            const [month, day] = key.split('-');
            const dayElement = document.querySelector(`.calendar-day[data-month="${month}"][data-day="${day}"]`);
            
            if (dayElement && highlightedStates[key]) {
                dayElement.style.backgroundColor = highlightedStates[key];
            }
        }
    }
    
    // Function to set up calendar day listeners
    function setupCalendarDayListeners() {
        const calendarDays = document.querySelectorAll('.calendar-day:not(.empty)');
        
        calendarDays.forEach(day => {
            // Add edit button to each day
            const editButton = document.createElement('div');
            editButton.className = 'edit-button';
            editButton.innerHTML = '<i class="fas fa-edit"></i>';
            day.appendChild(editButton);
            
            // Add click event to edit button
            editButton.addEventListener('click', function(e) {
                e.stopPropagation();
                openEditPopup(day);
            });
        });
    }
    
    // Function to open edit popup
    function openEditPopup(dayElement) {
        currentEditMonth = dayElement.getAttribute('data-month');
        currentEditDay = dayElement.getAttribute('data-day');
        
        const contentElement = dayElement.querySelector('.day-content');
        const content = contentElement ? contentElement.innerHTML : '';
        
        // Set content in Quill editor
        quill.root.innerHTML = content;
        
        // Set current highlight
        currentHighlight = null;
        const highlightOptions = document.querySelectorAll('.highlight-option');
        highlightOptions.forEach(option => {
            option.classList.remove('selected');
        });
        
        // Show edit popup
        document.getElementById('editOverlay').classList.add('active');
        document.getElementById('editPopup').classList.add('active');
        
        // Set date in popup header
        document.getElementById('editDate').textContent = `${currentEditMonth} ${currentEditDay}, 2025`;
    }
    
    // Function to close edit popup
    function closeEditPopup() {
        document.getElementById('editOverlay').classList.remove('active');
        document.getElementById('editPopup').classList.remove('active');
    }
    
    // Function to save calendar day content
    function saveCalendarDay() {
        const content = quill.root.innerHTML;
        const dayElement = document.querySelector(`.calendar-day[data-month="${currentEditMonth}"][data-day="${currentEditDay}"]`);
        
        if (dayElement) {
            const contentElement = dayElement.querySelector('.day-content');
            if (contentElement) {
                contentElement.innerHTML = content;
            }
            
            // Apply highlight if selected
            if (currentHighlight) {
                const colors = {
                    none: '',
                    yellow: '#fff3cd',
                    green: '#d4edda',
                    blue: '#cce5ff',
                    red: '#f8d7da',
                    purple: '#e2d9f3',
                    gray: '#e9ecef',
                    orange: '#ffe5d0',
                    pink: '#f8d7e6',
                    sky: '#d4f1f9',
                    lime: '#e8ffd4',
                    rose: '#ffb6c1',
                    aqua: '#00ffff80',
                    gold: '#ffd70080',
                    lavender: '#e6e6fa',
                    teal: '#80ffd480',
                    salmon: '#ffa07a80'
                };
                dayElement.style.backgroundColor = colors[currentHighlight];
                highlightedStates[`${currentEditMonth}-${currentEditDay}`] = colors[currentHighlight];
            }
            
            // Save to storage
            calendarData[`${currentEditMonth}-${currentEditDay}`] = content;
            localStorage.setItem('calendarData', JSON.stringify(calendarData));
            localStorage.setItem('highlightedStates', JSON.stringify(highlightedStates));
            
            // Update has-event class
            if (content.trim()) {
                dayElement.classList.add('has-event');
            } else {
                dayElement.classList.remove('has-event');
            }
        }
        
        closeEditPopup();
    }
    
    // Function to select highlight color
    function selectHighlight(color) {
        currentHighlight = color;
        
        const highlightOptions = document.querySelectorAll('.highlight-option');
        highlightOptions.forEach(option => {
            option.classList.remove('selected');
        });
        
        const selectedOption = document.querySelector(`.highlight-option.${color}`);
        if (selectedOption) {
            selectedOption.classList.add('selected');
        }
    }
    
    // Add event listeners to buttons
    document.getElementById('cancelButton').addEventListener('click', closeEditPopup);
    document.getElementById('saveButton').addEventListener('click', saveCalendarDay);
    document.getElementById('clearButton').addEventListener('click', function() {
        quill.root.innerHTML = '';
    });
    
    // Add event listeners to highlight options
    const highlightOptions = document.querySelectorAll('.highlight-option');
    highlightOptions.forEach(option => {
        option.addEventListener('click', function() {
            const color = this.getAttribute('data-color');
            selectHighlight(color);
        });
    });
    
    // Close popup when clicking on overlay
    document.getElementById('editOverlay').addEventListener('click', closeEditPopup);
    
    // Prevent popup from closing when clicking inside it
    document.getElementById('editPopup').addEventListener('click', function(e) {
        e.stopPropagation();
    });
});
