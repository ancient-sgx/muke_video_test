
var videoEreaStatic = false;
var videoEditArea = $('#video-edit-area');
$('#open-add-video-btn').click(function(){
    if (!videoEreaStatic){
        videoEditArea.show();
        videoEreaStatic=true;
    }else{
        videoEditArea.hide();
        videoEreaStatic= false;
    }
});
/*这是实现外连接视频里的点击创建才可以看到下面的内容*/