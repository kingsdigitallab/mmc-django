window.GOOGLE_ANALYTICS = {
    'ga_id': '{{ GA_ID }}',
    'domain': '{{ request.META.HTTP_HOST }}',
};


// BM - Please check 
window.addEventListener('resize', function() {
    if (window.matchMedia('(min-width: 400px)').matches) {
        document.getElementById('menu-switch').checked = false;
    }
}, true);

