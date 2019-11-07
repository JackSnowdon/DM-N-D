$(document).ready(function() {

    $("#start-combat").click(function() {


        var index = $(".card").index(".card") + 1;

        // var index = $('.card:first').index('.card:first') + 1;

        $("#start-combat").hide();
        $("#delete-all-combat").hide();
        $("#add-hero").hide();
        setTimeout(function() {
            $("#next-button").fadeIn("slow");
            $(".card:first").addClass("select-box");
        }, 1000);

        $("#next-button").click(function() {
            var removecard = $(".card.select-box:first");
            removecard.removeClass("select-box");
            setTimeout(function() {
                currentcard = $(".card").eq(index);
                console.log(currentcard);
                currentcard.addClass("select-box");
                index++;
                console.log(index);
            }, 1000);
        });
    });
});
