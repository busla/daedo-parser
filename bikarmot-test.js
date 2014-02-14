
$(function () { 
    $("[data-toggle='tooltip']").tooltip(); 
});


$.getJSON( "test.json", function( data ) {    
  $.each(data, function(i, item) {
    var score_detail = [];
    var scoreboard = '<table id="scoreboard" class="table table-condensed table-striped">';
    scoreboard += '<tr><th>Lota</th><th>Tími</th><th>Keppandi</th><th>Atburður</th><th>Kraftur</th><th>Stig</th><th>Heildarstig</th></tr>'
    $.each(item.Score, function(r, points) {
        //score_detail.push(points.Round, points.Time, points.Total);
        
    scoreboard += '<tr>'+'<td>'+points.Round+'</td>'+'<td>'+points.Time+'</td>'+'<td>'+points.Competitor+'</td>'+'<td>'+points.Event+'</td>'+'<td>'+points.Impact+'</td>'+'<td>'+points.Point+'</td>'+'<td>'+points.Total+'</td>'+'</tr>';
    });
    scoreboard += '</table>';
    
    $('<tr>').append(
      $('<td>').text(i),
      $('<td>').text(item.Threshold),
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
    ).appendTo('#matches');





$(function () { 
    $('[data-toggle="popover"]').popover({'trigger': 'click', 'placement': 'left', 'html': 'true', 'title': 'Stigaferill bardagans eftir tímaröð'});
});
    
$('[data-toggle="popover"]').click(function () { $('[data-toggle="popover"]').not(this).popover('hide'); });   
 
    
  });
});    




