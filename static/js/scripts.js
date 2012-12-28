$(function() {
	$('form[id="lookup"]').submit(function(event) {
		event.preventDefault();
		clearData();
		$('img#loading').show();
		$.ajax({
			type: 'POST',
			url: "/",
			data: {
				'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
				'username': $('input[name="username"]').val(),
				'access_token': $('input[name="access_token"]').val(),
			},
			success: function(data){
				$('img#loading').hide();
				if (data['error']) {
					$('.uid > h4').html(data['error']);
					$('.uid > h4').fadeIn();
				} else {
					$('.uid > h3').html(data['id']);
	 				$('.uid > h3').fadeIn();
					html = '<img src="' + data['profile_picture'] + '" /><div class="info"><ul>';	 				
	 				attributes = ['full_name', 'website', 'bio'];
	 				attributes.map(function(attribute) {
	 					if (data[attribute]) html += '<li>' + data[attribute] + '</li>';
	 				});
	 				$('.attributes').html(html += "</ul></div>");
	 				$('.attributes').fadeIn();

				}

			}
		});
	});
});

function clearData() {
	$('.uid > h3').hide();
	$('.uid > h4').hide();
	$('.uid > .attributes').hide();
}