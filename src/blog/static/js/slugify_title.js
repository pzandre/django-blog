document.getElementById("id_title").on('keyup',function(){
    document.getElementById("slug").val($(this).val());
});
