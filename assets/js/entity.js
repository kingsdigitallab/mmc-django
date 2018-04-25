var CLASSES = {
	'person': 'darkgreen',
	'place': 'purple',
	'institution': 'lightgreen',
	'object': 'orange',
	'musical-work': 'red',
	'event': 'lightblue',
	'source': 'darkblue'
}

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