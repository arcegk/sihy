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
               jQuery("#map-wrap").addClass("map-fixed");
                
            }
            else {
                jQuery("#map-wrap").removeClass("map-fixed");
                
            }
        });
    }

    function collapseList(){

        
            $("#itm1").click(function(){
            $("#sub1").collapse('toggle');
                
            });
            $("#itm2").click(function(){
                $("#sub2").collapse('toggle');
            });
            $("#itm3").click(function(){
                $("#sub3").collapse('toggle');
            });
            $("#itm4").click(function(){
                $("#sub4").collapse('toggle');
            });
        
}

    return {
        init: function () {
            collapseList();
            fixedScroll();
        },


    };

}();