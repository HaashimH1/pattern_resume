$(document).ready(function(){

    $('.subsection-header').on('click', function(){
      // Find the closest subsection container, then the form within it.
      var $form = $(this).closest('.subsection-container').find('.subsection-open-container');
      if($form.is(':hidden')) {
        $form.css('display', 'flex');
      } else {
        $form.css('display', 'none');
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

});
