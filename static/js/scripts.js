$(function() {

	// Initiate Javascript callback upon form submission
	$('form[id="lookup"]').submit(function(event) {

		// Prevent form from submitting via HTML submit
		event.preventDefault();

		// Clear right hand form upon form submission
		clearData();

		// Show loading gif
		$('img#loading').show();
		
		// AJAX form submission
		$.ajax({
			type: 'POST',
			url: "/",
			data: {
				// Add Django CSRF token to request
				'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
				'username': $('input[name="username"]').val(),
				'access_token': $('input[name="access_token"]').val(),
			},
			success: function(data){

				// Hide loading gif
				$('img#loading').hide();

				// Display error message if there was an exception
				if (data['error']) {
					$('.uid > h4').html(data['error']);
					$('.uid > h4').fadeIn();

				// Load attributes if request was successful
				} else {
				
					// Load id into the DOM and display
					$('.uid > h3').html(data['id']);
	 				$('.uid > h3').fadeIn();
				
					// Initialize html string var and begin building html block
					html = '<img src="' + data['profile_picture'] + '" alt="' + data['username'] + '" /><div class="info"><ul>';	 				
	 				attributes = ['full_name', 'website', 'bio'];

					// For each attribute in attributes list, map and format into html if there's a key that matches the attribute
	 				attributes.map(function(attribute) {
	 					if (data[attribute]) html += '<li>' + data[attribute] + '</li>';
	 				});

	 				// End html block and load into the DOM
	 				$('.attributes').html(html += "</ul></div>");
	 				
	 				// Show the attributes div
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