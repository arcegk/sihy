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
            if (jQuery(window).scrollTop()>200){
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
            $("#itm5").click(function(){
                $("#sub5").collapse('toggle');
            });
            $("#itm6").click(function(){
                $("#sub6").collapse('toggle');
            });
            $("#itm7").click(function(){
                $("#sub7").collapse('toggle');
            });
            $("#itm8").click(function(){
                $("#sub8").collapse('toggle');
            });
            $("#itm9").click(function(){
                $("#sub9").collapse('toggle');
            });
            $("#itm10").click(function(){
                $("#sub10").collapse('toggle');
            });
}

    return {
        init: function () {
            collapseList();
            fixedScroll();
        },


    };

}();