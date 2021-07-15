$(document).ready(function(){


    $("button.add_item").on("click",function(){

    let item_count = $('.container .compare_card').length;

    $(".col:last").after(
        `
            <div class="col mb-4">
                <div class="card compare_card">
                    <div class=" card-body compare_form">
                        <h5>Item ${item_count+1}</h5>
                        <form action="{% url 'compare_ingredients' %}" method="post" id="compare">
                            <input id="token" type="hidden" value="{% csrf_token %}" ></input>
                            <textarea name="ingredients" id="ingredients${item_count+1}" class="all_textareas"></textarea>
                            <br>
                            <button type="submit" class="btn btn-info">Submit</button>
                        </form>
                        
                        
                    </div>
                </div>
            </div>
        `
            );
           })
})

