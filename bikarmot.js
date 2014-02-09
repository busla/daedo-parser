$.getJSON( "matches.json", function( data ) {
  $.each(data, function(i, item) {
    $('<tr>').append(
      $('<td>').text(i),
      $('<td>').text(item.Impact),
      $('<td class="red">').text(item.Red),
      $('<td class="blue">').text(item.Blue),
      $('<td>').text(item.Start),
      $('<td>').text(item.End),
      $('<td>').text(item.Results),
      $('<td>').text(item.Winner)
    ).appendTo('#records_table');
    // $('#records_table').append($tr);
    //console.log($tr.wrap('<p>').html());
  });
});

$('.tooltip-table').tooltip();

