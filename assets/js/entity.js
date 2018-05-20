
$(document).ready(function() {
	// Entity links
	$('.page-content a').each(function()
	{
		var href = $(this).attr('href');
		if (href)
		{
			if (href.startsWith('/entities/'))
			{
				var entity = href.split('/')[2];
				$(this).addClass(CLASSES[entity]);
			}
		}
	});

	$('#switch-1').bind('change', function(event)
	{
		// This is a very pseudo way of doing this.
		// Due to the buggy nature of css checkbox switches, this is the
		// best we can do
		if($('a.force_black').length)
		{
			$('a.force_black').removeClass('force_black');
		} else
		{
			$('.page-content a').addClass('force_black');
		}
	});
});