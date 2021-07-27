$(document).ready(function(){

    

    
$("button.add_item").on("click",function(){

let item_count = $('.container-fluid .compare_cardbody').length;

if ($("#compare > .row:last > .col").length === 2)
{
  $("#compare").append('<div class="row form_row"></div>');
} if ($('.container-fluid .compare_cardbody').length >= 4){
    alert('Reached Max!');
    return false;
}

    $("#compare > .row:last").append(
        `
            <div class="col mb-4">
                <h5>Item${item_count+1}</h5>
                <div class="card form_card">
                    <div class="card-body compare_cardbody">

                        <textarea style="resize: none;" minlength="1" name="ingredients${item_count+1}" id="ingredients" cols="30" rows="1" placeholder="Enter Product name"></textarea>

                        <textarea style="resize: none;" minlength="1" name="ingredients${item_count+1}" id="ingredients" cols="30" rows="10" placeholder="Enter ingredients" ></textarea>
                        
                    </div>
                </div>    
            </div>
        `
            );
    })



$("button.remove_item").on("click",function(){

    let item_count = $('.container-fluid .compare_cardbody').length;

    if (item_count > 2) {

        $("#compare > .row > .col:last").remove();
    }

    })


// function to display a container after user clicks on data buttons at top of page
$('#data1').click(function () {
    $('#all_info').show();
    $('#charts1').hide();
    $('#five').hide();
});
$('#data2').click(function () {
    $('#charts1').show();
    $('#all_info').hide();
    $('#five').hide();
});
$('#data3').click(function () {
    $('#five').show();
    $('#charts1').hide();
    $('#all_info').hide();
});

})
