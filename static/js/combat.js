$(document).ready(function() {

    $("#start-combat").click(function() {


        var index = $(".card").index(".card") + 1;

        // var index = $('.card:first').index('.card:first') + 1;

        console.log(index);

        $("#start-combat").hide();
        $("#delete-all-combat").hide();
        $("#add-hero").hide();
        setTimeout(function() {
            $("#next-button").fadeIn("slow");
            $(".card:first").addClass("select-box");
        }, 1000);

        $("#next-button").click(function() {
            if (index == 1) {
                var firstcard = $(".card:first");
                console.log(firstcard);
                firstcard.removeClass("select-box");
            }
            
            setTimeout(function() {
                var currentcard = $(".card.select-box:first");
                currentcard.removeClass("select-box");
            }, 1000);

            setTimeout(function() {
                $(".card").eq(index).addClass("select-box");
                index++;
                console.log(index);
            }, 1000);
        });
    });
});
