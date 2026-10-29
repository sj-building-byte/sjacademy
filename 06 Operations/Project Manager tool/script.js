/**
 * SJ Academy - Project Management Sheet
 * Tab Navigation Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    // Function to switch tabs
    function switchTab(targetTabId) {
        // 1. Remove active class from all buttons and contents
        tabButtons.forEach(btn => {
            btn.classList.remove('active');
            btn.setAttribute('aria-selected', 'false');
        });
        
        tabContents.forEach(content => {
            content.classList.remove('active');
        });

        // 2. Add active class to the selected button and corresponding content
        const selectedBtn = document.querySelector(`.tab-btn[data-tab="${targetTabId}"]`);
        const selectedContent = document.getElementById(targetTabId);

        if (selectedBtn && selectedContent) {
            selectedBtn.classList.add('active');
            selectedBtn.setAttribute('aria-selected', 'true');
            selectedContent.classList.add('active');
        }
    }

    // Attach click listeners to all tab buttons
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabId = button.getAttribute('data-tab');
            switchTab(tabId);
        });
    });
});
