// Avoid `console` errors in browsers that lack a console.
(function() {
    var method;
    var noop = function () {};
    var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'
    ];
    var length = methods.length;
    var console = (window.console = window.console || {});

    while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
            console[method] = noop;
        }
    }
}());

// Place any jQuery/helper plugins in here.

/* ======================================================
   jQuery-Nice-File-Input
   https://github.com/jaydevonline/jQuery-Nice-File-Input
   ====================================================== */
(function(){var e=navigator.userAgent.match(/Firefox\/(.*)$/);var t;var n=4.3;if(e&&e.length>1){t=e[1]}$.fn.niceFileInput=function(e){var r=$.extend({width:"500",height:"30",btnText:"Browse",btnWidth:"100",margin:"20"},e);for(var i=150;i<=r.width;i+=5){n=n+.715}this.css({height:r.height,width:r.width,zIndex:"99",opacity:"0",position:"absolute",right:"0",top:"0","font-size":"16px"}).wrap('<div class="fileWrapper" />').parent().css({width:r.width}).append("<input type='text' class='fileInputText' readonly='readonly' />").append("<input type='button' class='fileInputButton' value='"+r.btnText+"' style='height:"+r.height+"px ; width:"+r.btnWidth+"px' />");if(t<22){this.attr("size",n)}this.parent().find('input[type="text"].fileInputText').css({height:r.height+"px",width:function(){return r.width-r.btnWidth-r.margin+"px"},"line-height":r.height+"px"});this.change(function(){var e=$(this).val().replace("C:\\fakepath\\","");$(this).closest(".fileWrapper").find(".fileInputText").val(e)})};return this})()