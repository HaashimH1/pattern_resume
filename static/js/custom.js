$(document).ready(function(){

  $('.subsection-header').on('click', function(){
    // Find the closest subsection container, then the form within it.
    var $form = $(this).closest('.subsection-container').find('.subsection-open-container');
    
    // Check if the clicked subsection is already open
    var isAlreadyOpen = $form.is(':visible');

    // Close all open subsections first
    $('.subsection-open-container').css('display', 'none');

    // If the clicked subsection was not already open, open it
    if (!isAlreadyOpen) {
        $form.css('display', 'flex');
    }
});

    // When clicking the open button to edit a section
    $(".section-header-open-button").on("click", function(e){
        e.preventDefault();
        // Close all sections first: hide all open headers, show all closed headers
        $(".resume-section-container").each(function(){
            $(this).find(".section-header-open").hide();
            $(this).find(".section-header-closed").show();
        });
        // Then open the clicked section
        var $container = $(this).closest(".resume-section-container");
        $container.find(".section-header-closed").hide();
        $container.find(".section-header-open").css("display", "flex");

        // Store the original value of the text field
        var $input = $container.find("input[name='section_name']");
        $input.data("original-value", $input.val());
    });

    // When clicking the close button (Back) to revert a section to its closed state
    $(".section-header-close-button").on("click", function(e){
        e.preventDefault();
        var $container = $(this).closest(".resume-section-container");
        $container.find(".section-header-open").hide();
        $container.find(".section-header-closed").css("display", "flex");

        // Reset the text field to its original value
        var $input = $container.find("input[name='section_name']");
        $input.val($input.data("original-value"));
    });



    // When clicking the delete button to show the popup box
    $(".subsection-delete").on("click", function(e){
      e.preventDefault();
      // Find the closest subsection container, then the popup box within it.
      var $popupBox = $(this).find('.pop-up-container');
      // Toggle the display property of the popup box
      $popupBox.removeClass("hidden").css('display', 'flex');
      $(".background-overlay").removeClass("hidden").css("display","block");
      
  });

  $(".subsection-swap").on("click", function(e){
    e.preventDefault();
    // Find the closest subsection container, then the popup box within it.
    var $popupBox = $(this).find('.pop-up-container');
    // Toggle the display property of the popup box
    $popupBox.removeClass("hidden").css('display', 'flex');
    $(".background-overlay").removeClass("hidden").css("display","block");
    
});

  
  

    // When clicking the delete button to show the popup box for sections
    $(".section-header-delete-button, .section-header-swap-button").on("click", function(e){
      e.preventDefault();
      // Find the closest section container, then the popup box within it.
      var $popupBox = $(this).find('.pop-up-container');
      // Toggle the display property of the popup box
      $popupBox.removeClass("hidden").css('display', 'flex');
      $(".background-overlay").removeClass("hidden").css("display","block");
  });



    $(".change-template-button").on("click", function(e){
      e.preventDefault();
      $(".change-template-popup-container").removeClass("hidden").css('display', 'flex');
      $(".background-overlay").removeClass("hidden").css("display","block");
  });



    $(".popup-cancel-button-container").on("click", function(e){
      e.preventDefault();
      e.stopPropagation();
      $(".pop-up-container").addClass("hidden");
      $(".background-overlay").addClass("hidden");
  });

  $(".delete-sub-button, .delete-section-button, .change-template-button, .swap-sub-button, .swap-section-button").on("click", function(e){
    $(this).closest('form').submit();
});

// Function to auto-resize the textarea
function autoResizeTextarea(textarea) {
  textarea.style.height = 'auto';
  textarea.style.height = textarea.scrollHeight + 'px';
}

// Apply the auto-resize function to the textarea on change
$('textarea').on('input', function() {
  autoResizeTextarea(this);
});

// Apply the auto-resize function to the textarea on page load
$('textarea').each(function() {
  autoResizeTextarea(this);
});


});
