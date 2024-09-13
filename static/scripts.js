$(document).ready(function() {
    let currentIndex = 0;
    const items = $('.carousel-item');
    const itemCount = items.length;

    // Hide all items except the first
    items.hide().eq(currentIndex).show();

    // Function to show the next item
    function showNextItem() {
        items.eq(currentIndex).hide();
        currentIndex = (currentIndex + 1) % itemCount;
        items.eq(currentIndex).fadeIn();
    }

    // Function to show the previous item
    function showPreviousItem() {
        items.eq(currentIndex).hide();
        currentIndex = (currentIndex - 1 + itemCount) % itemCount;
        items.eq(currentIndex).fadeIn();
    }

    // Next button click
    $('#next').click(showNextItem);

    // Previous button click
    $('#prev').click(showPreviousItem);
});
