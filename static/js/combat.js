$(document).ready(function() {

    var decksize, index, repeat;

    function getDeckSize() {
        return $(".card").length;
    }

    function getIndex() {
        return $(".card").index(".card") + 1;
    }

    $("#start-combat").click(function() {
        repeat = 0;
        decksize = getDeckSize();
        index = getIndex();

        $("#start-combat").hide();
        $("#delete-all-combat").hide();
        $("#add-hero").hide();
        setTimeout(function() {
            $("#next-button").fadeIn("slow");
            $(".card:first").addClass("select-box");
        }, 1000);

    });


    $("#next-button").click(function() {
        
        if (repeat > 0) {
            index = 1;
            repeat--;
        }
        
        var removecard = $(".card.select-box:first");
        removecard.removeClass("select-box");

        if (decksize > index) {
            setTimeout(function() {
                var currentcard = $(".card").eq(index);
                console.log(currentcard);
                currentcard.addClass("select-box");
                index++;
            }, 1000);
        }
        else {
            $("#next-button").fadeOut("slow");
            setTimeout(function() {
                $("#next-round").show();
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
        repeat++;
    });



});
