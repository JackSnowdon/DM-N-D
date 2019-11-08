$(document).ready(function() {

    $("#start-combat").click(function() {

        var decksize = $(".card").length;
        console.log(decksize);
        var index = $(".card").index(".card") + 1;
        console.log(decksize, index);

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

            if (decksize > index) {
                setTimeout(function() {
                    currentcard = $(".card").eq(index);
                    console.log(currentcard);
                    currentcard.addClass("select-box");
                    index++;
                    console.log(index);
                }, 1000);
            } else {
                console.log("done!");
                $("#next-button").fadeOut("slow");
                setTimeout(function() {
                    $("#start-combat").show();
                }, 1000);
            }
        });
    });
});
