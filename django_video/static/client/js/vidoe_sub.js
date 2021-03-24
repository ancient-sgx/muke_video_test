$('#comment-submit').click(function () {
   var content = $('#comment-content').val();
   var csrfToken = $('#django-csrf-token').val();
   var userId = $(this).attr('data-user-id');
   var videoId = $(this).attr('data-video-id');
   var url = $(this).attr('data-url');

   if (!content){
      alert('���۲���Ϊ�գ�');
      return;
   };
   $.ajax({
      url:url,
      data:{
         content:content,
         videoId:videoId,
         userId:userId,
         csrfmiddlewaretoken:csrfToken
      },
      type:'post',
      success:function (data) {
         console.log(data)
      },
      fail:function (e) {
         console.log(e);
      }
   });
});