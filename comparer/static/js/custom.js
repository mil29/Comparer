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

})
