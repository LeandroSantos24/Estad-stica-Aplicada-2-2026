$(document).on('ready', function () {
    var trackingMap = {
        'ui-id-1': 'last_matchday',
        'ui-id-2': 'current_matchday',
        'ui-id-3': 'next_matchday'
    };
    var mobileMediaQuery = window.matchMedia("(max-width:767px)");
    if (mobileMediaQuery.matches) {
        zecBegegnungSlider();
    } else {
        $('#main').on('click', '#spieltagstabs .ui-widget-header li', function(el) {
            var linkId = el.currentTarget.querySelector('a').id;
            tmEvent('wettbewerb', 'click', trackingMap[linkId] ?? 'unknown');
		});
    }
});

function zecBegegnungSlider() {
	zecIdentifier = $('#spieltagsbox tbody tr.begegnungZeile');
	$(zecIdentifier).on('click', function (event) {
		zecSlider = $('#zecBegegnungSlider.zec-slider');
		zecCloser = $(zecSlider).find('.zec-closer');
		zecContent = $(zecSlider).find('.zec-content');
		event.preventDefault();
		globalZecSlider();

		var ID=$(this).attr("data-id");
		$.ajax({
			//dataType: "json",
			method: 'POST',
			url: '/startseite/_begegnungSlider',
			data: {begegnung_id: ID},
			success: function (mydata) {
				$(zecContent).html(mydata);
			}
		});
	});
}
