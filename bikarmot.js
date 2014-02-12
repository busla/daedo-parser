
$(function () { 
    $("[data-toggle='tooltip']").tooltip(); 
});



$.getJSON( "matches.json", function( data ) {    
  $.each(data, function(i, item) {
    var score_detail = [];
    var scoreboard = '<table class="table table-condensed table-striped">';
    scoreboard += '<tr><th>Lota</th><th>Tími</th><th>Heildarstig</th></tr>'
    $.each(item.Score, function(r, points) {
        //score_detail.push(points.Round, points.Time, points.Total);
        
        scoreboard += '<tr>'+'<td>'+points.Round+'</td>'+'<td>'+points.Time+'</td>'+'<td>'+points.Total+'</td>'+'</tr>';      
    });
    scoreboard += '</table>';
    
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
//              'id': 'btnid-'+i,
              'type': 'button', 
              'class': 'btn btn-info btn-xs', 
              'data-toggle': 'popover',
              'data-content': scoreboard,
              'container': 'body',
              }).text('Tölfræði'))
    ).appendTo('#records_table');
    


    $(function () { 
        $('[data-toggle="popover"]').popover({'trigger': 'click', 'placement': 'left', 'html': 'true', 'title': 'Stigaferill bardagans eftir tímaröð'});
    });
    
    $('[data-toggle="popover"]').click(function () { $('[data-toggle="popover"]').not(this).popover('hide'); });
    
        
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
    
  });
});


