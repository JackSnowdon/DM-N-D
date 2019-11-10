$(document).ready(function() {

    var decksize, index, repeat, currentcard;

    function getDeckSize() {
        return $(".card").length;
    }

    function getIndex() {
        return $(".card").index(".card") + 1;
    }

    function getCurrentCard() {
        return $(".card.select-box");
    }

    $("#start-combat").click(function() {
        $("#hide-combat").fadeIn("slow");


        repeat = 0;
        decksize = getDeckSize();
        index = getIndex();

        $("#start-combat").hide();
        $("#delete-all-combat").hide();
        $("#add-hero").hide();
        setTimeout(function() {
            $("#next-button").fadeIn("slow");
            $(".card:first").addClass("select-box");
            currentcard = getCurrentCard();
            console.log(currentcard);

            var name = $(currentcard).find(".card-title").text();

            console.log(name);

        }, 1000);


    });


    $("#next-button").click(function() {
        $("#next-button").attr("disabled", true);

        if (repeat > 0) {
            index = 1;
            repeat--;
        }

        var removecard = $(".card.select-box:first");
        removecard.removeClass("select-box");

        if (decksize > index) {
            setTimeout(function() {
                var currentcard = $(".card").eq(index);
                currentcard.addClass("select-box");
                $("#next-button").attr("disabled", false);
                console.log(currentcard);

                var name = $(currentcard).find(".card-title").text();

                console.log(name);

                index++;
            }, 1000);
        }
        else {
            $("#next-button").fadeOut("slow");
            setTimeout(function() {
                $("#next-round").show();
                $("#next-button").attr("disabled", false);
            }, 1000);
        }
    });

    $("#next-round").click(function() {
        $("#next-round").hide();
        var decksize = $(".card").length;
        var index = $(".card").index(".card") + 1;
        setTimeout(function() {
            $("#next-button").fadeIn("slow");
            $(".card:first").addClass("select-box");
        }, 1000);
        currentcard = $(".card").eq(index - 1);
        console.log(currentcard);
        repeat++;
    });

});
