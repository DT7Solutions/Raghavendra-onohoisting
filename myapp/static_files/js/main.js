
(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);


(function () {
    // Your existing code for print_link_script.js follows here

    // Add event listener to the "Print" link
    var printLinks = document.querySelectorAll('.print-link');
    printLinks.forEach(function (printLink) {
        printLink.addEventListener('click', function (e) {
            e.preventDefault();

            // Create a new window for printing
            var printWindow = window.open('', '_blank');
            printWindow.document.write('<html><head><title>Print</title>');
            printWindow.document.write('<link rel="stylesheet" type="text/css" href="{% static \'css/print_styles.css\' %}">'); // Link the print styles
            printWindow.document.write('</head><body>');
            printWindow.document.write(document.querySelector('div.print-content').innerHTML);  // Replace 'div.print-content' with the appropriate selector for your content
            printWindow.document.write('</body></html>');
            printWindow.document.close();
            printWindow.print();
        });
    });
})();