$(document).ready(function() {
    // Toggle between primary and secondary schedule
    $('#show-primary').click(function() {
        $('#primary-schedule').show();
        $('#secondary-schedule').hide();
        $('#show-primary').addClass('active');
        $('#show-secondary').removeClass('active');
    });

    $('#show-secondary').click(function() {
        $('#primary-schedule').hide();
        $('#secondary-schedule').show();
        $('#show-secondary').addClass('active');
        $('#show-primary').removeClass('active');
    });

    // Swiping functionality for primary schedule
    let currentIndexPrimary = 0;
    const primaryItems = $('#primary-schedule .carousel-item');
    const primaryItemCount = primaryItems.length;

    function showNextPrimary() {
        primaryItems.eq(currentIndexPrimary).hide();
        currentIndexPrimary = (currentIndexPrimary + 1) % primaryItemCount;
        primaryItems.eq(currentIndexPrimary).fadeIn();
    }

    function showPreviousPrimary() {
        primaryItems.eq(currentIndexPrimary).hide();
        currentIndexPrimary = (currentIndexPrimary - 1 + primaryItemCount) % primaryItemCount;
        primaryItems.eq(currentIndexPrimary).fadeIn();
    }

    $('#next-primary').click(showNextPrimary);
    $('#prev-primary').click(showPreviousPrimary);

    // Swiping functionality for secondary schedule
    let currentIndexSecondary = 0;
    const secondaryItems = $('#secondary-schedule .carousel-item');
    const secondaryItemCount = secondaryItems.length;

    function showNextSecondary() {
        secondaryItems.eq(currentIndexSecondary).hide();
        currentIndexSecondary = (currentIndexSecondary + 1) % secondaryItemCount;
        secondaryItems.eq(currentIndexSecondary).fadeIn();
    }

    function showPreviousSecondary() {
        secondaryItems.eq(currentIndexSecondary).hide();
        currentIndexSecondary = (currentIndexSecondary - 1 + secondaryItemCount) % secondaryItemCount;
        secondaryItems.eq(currentIndexSecondary).fadeIn();
    }

    $('#next-secondary').click(showNextSecondary);
    $('#prev-secondary').click(showPreviousSecondary);
});
