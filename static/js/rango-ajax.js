$(document).ready(function() {

$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
     $.get('/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $("a#like_count").attr('href', '/'+ data);
           });
});

});