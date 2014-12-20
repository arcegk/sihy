/*   
 * Template Name: Unify - Responsive Bootstrap Template
 * Description: Business, Corporate, Portfolio and Blog Theme.
 * Version: 1.4
 * Author: @htmlstream
 * Website: http://htmlstream.com
*/

var scrolling = function () {


    function fixedScroll() {
         jQuery(window).scroll(function() {
            if (jQuery(window).scrollTop()>95){
                jQuery("#info-wrap").addClass('col-md-offset-7');
                jQuery("#info-wrap").addClass('col-sm-offset-5');
                jQuery("#map-wrap").addClass("map-fixed");
                
            }
            else {
                jQuery("#info-wrap").removeClass('col-md-offset-7');
                jQuery("#info-wrap").removeClass('col-sm-offset-5');
                jQuery("#map-wrap").removeClass("map-fixed");
                
            }
        });
    }

    return {
        init: function () {
            
            fixedScroll();
        },


    };

}();