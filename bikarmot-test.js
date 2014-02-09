



$.getJSON( "test.json", function( data ) {
  $.each(data, function(i, item) {
    $('<tr>').append(
      $('<td>').text(i),
      $('<td>').text(item.Impact),
      $('<td class="red">').text(item.Red),
      $('<td class="blue">').text(item.Blue),
      $('<td>').text(item.Start),
      $('<td>').text(item.End),
      $('<td>').text(item.Results),
      $('<td>').text(item.Winner),
      $('<td>').append(
          $('<button>').attr({ 
              'data-target': '#row-' + i,
              'type': 'button', 
              'class': 'btn btn-info btn-xs', 
              'data-toggle': 'collapse',
              
              }).text('Tölfræði'))
    ).appendTo('#records_table');
    //$('<tr class="collapse">').attr('id', 'row-'+i).appendTo('#records_table');    
    $('<tr class="collapse">').attr('id', 'row-' + i).append(
      $('<td>').attr('id', 'cell-'+i).append(
        $('<table class="table">').attr('id', 'score-'+i).append(
            $('<tbody>').append(
                $('<tr>').append(
                    $('<th>').text('Lota'),
                    $('<th>').text('Tími'),
                    $('<th>').text('Heildarstig')
                )
            )
        )
      )  
    ).appendTo('#records_table');
    
    
    $.each(item.Score, function(r, points) {
        $('<tr>').append(
            $('<td>').text(points.Round),            
            $('<td>').text(points.Time),
            $('<td>').text(points.Total)
        ).appendTo('#score-'+i)
    });
    // $('#records_table').append($tr);
    //console.log($tr.wrap('<p>').html());
  });
});
    
    
        
$('.tooltip-table').tooltip();
$('#timeline').modal();

    
