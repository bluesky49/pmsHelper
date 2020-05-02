$(document).ready(function(){
    console.log("Adfasdf")
    $('[data-toggle="offcanvas"]').click(function(){
        $("#navigation").toggleClass("hidden-xs");
    });
    $(document).on('click','.user-edit', function(){
        // console.log("asdfasd")
        let id = $(this).parent().parent().data('row')
        location.href = "/admin/users/edit/" + id
    })
    $(document).on('click','.user-delete', function(){
        // console.log("asdfasd")
        if(!confirm("Are you sure to delete?"))
            return
        let id = $(this).parent().parent().data('row')
        location.href = "/admin/users/delete/" + id
    })

    $(document).on('click', '.time-select-groups button', function(){
        $('.time-select-groups button').removeClass('red-active');
        $(this).addClass('red-active');
    })

    $('.termss #terms').removeClass('form-control');


 });
 
 
 