$(document).ready(function() {

    /* ======= Scrollspy ======= */
    $('body').scrollspy({ target: '#top', offset: 400});
   
    /* ======= ScrollTo ======= */
    $('a.scrollto').on('click', function(e){
        
        //store hash
        var target = this.hash;
                
        e.preventDefault();
        
		$('body').scrollTo(target, 800, {offset: -80, 'axis':'y', easing:'easeOutQuad'});
        //Collapse mobile menu after clicking
		if ($('.navbar-collapse').hasClass('in')){
			$('.navbar-collapse').removeClass('in').addClass('collapse');
		}
		
	});

	var $el = $('.writer'),
txt = $el.text(),
txtLen = txt.length,
timeOut,
char = 0;

$el.text('');

(function typeIt() {   
    var humanize = Math.round(Math.random() * (200 - 30)) + 30;
    timeOut = setTimeout(function() {
        char++;
        var type = txt.substring(0, char);
        $el.text(type + '');
        typeIt();

        if (char == txtLen) {
            $el.text($el.text().slice(0, -1)); // remove the '|'
            clearTimeout(timeOut);
        }

    }, 50);
}());

});

