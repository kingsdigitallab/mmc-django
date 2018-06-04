window.GOOGLE_ANALYTICS = {
    'ga_id': '{{ GA_ID }}',
    'domain': '{{ request.META.HTTP_HOST }}',
};


window.addEventListener('resize', function() {
    if (window.innerWidth < 768) {
        document.getElementById('menu-switch').checked = false;
    } else
    {
    	document.getElementById('menu-switch').checked = true;
    }
}, true);