
$(document).ready(function() {
	// Entity links
	$('a').each(function()
	{
		var href = $(this).attr('href');
		if (href.startsWith('/entities/'))
		{
			var entity = href.split('/')[2];
			$(this).addClass(CLASSES[entity]);
		}
	});
});