// Get the sidebar and brand text elements
const toggleSidebar = document.getElementById('toggleSidebar');
const brandText = document.querySelector('.brand-text');
const body = document.body;

// Toggle the sidebar collapse when the brand link is clicked
toggleSidebar.addEventListener('click', function() {
// Toggle sidebar collapse
body.classList.toggle('sidebar-collapse');

// Check if the sidebar is collapsed
if (body.classList.contains('sidebar-collapse')) {
// Hide the text
brandText.style.display = 'none';
} else {
// Show the text again when expanded
brandText.style.display = 'inline';
}
});

