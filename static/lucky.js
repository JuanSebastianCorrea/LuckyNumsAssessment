/** processForm: get data from form and make AJAX call to our API. */

function processForm(evt) {
	evt.preventDefault();
	const name = $('#name').val();
	const year = $('#year').val();
	const email = $('#email').val();
	const color = $('#color').val();

	let data = {
		name: name,
		year: year,
		email: email,
		color: color
	};

	callOurAPI(data);
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
	if (resp.errors) {
		for (err in resp.errors) {
			$(`#${err}-err`).html(resp.errors[err]);
		}
	} else {
		htmlMarkup = $(`<p> Your lucky number is ${resp.num.num}. ${resp.num.fact}</p>
                    <p> Your birth year (${resp.year.year}) fact is: ${resp.year.fact}</p>`);
		$('#lucky-results').append(htmlMarkup);
	}
}

async function callOurAPI(data) {
	const res = await axios.post('/api/get-lucky-num', data);
	handleResponse(res.data);
}

$('#lucky-form').on('submit', processForm);
