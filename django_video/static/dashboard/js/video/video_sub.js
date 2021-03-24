var inputNumber=$('#number');
var inputUrl=$('#url');
var videosubInputId=$('#videosub-input-id');

//对集数内容进行编辑的时候自动把要编辑的内容放到对应的位置
$('.update-btn').click(function(){
    var videosubId = $(this).attr('data-id');
    var videoSubNumber=parseInt($(this).attr('data-number'));
    var videoSubUrl = $(this).attr('data-url');

    inputNumber.val(videoSubNumber);
    inputUrl.val(videoSubUrl);
    videosubInputId.val(videosubId);
});