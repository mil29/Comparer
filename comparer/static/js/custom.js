$(document).ready(function(){

    $("button.add_item").on("click",function(){

    let item_count = $('.container .compare_card').length;

    $(".row:last").after(
        `
        <div class="row form_row">
            <div class="col mb-4">
                    <h5>Item</h5>
                <div class="card form_card">
                    <div class="card-body compare_cardbody">

                        <textarea name="ingredients" id="" cols="30" rows="10"></textarea>
                        
                    </div>
                </div>    
            </div>
        </div>
        `
            );
           })
})

