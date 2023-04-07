$(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    dataType: 'jsonp',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  })
});

// $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
//   $('DIV#hello').text(data.hello);
// });