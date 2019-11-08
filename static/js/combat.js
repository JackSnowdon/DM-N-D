$(document).ready(function() {

    $("#start-combat").click(function() {

        function getDeckSize() {
            $(".card").length;
        }

        function getIndex() {
            $(".card").index(".card") + 1;
        }

        var decksize = $(".card").length;
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
            
            console.log(decksize, index);
            var removecard = $(".card.select-box:first");
            removecard.removeClass("select-box");

            if (decksize > index) {
                setTimeout(function() {
                    currentcard = $(".card").eq(index);
                    console.log(currentcard);
                    currentcard.addClass("select-box");
                    index++;
                }, 1000);
            }
            else {
                console.log("done!");
                console.log(decksize, index);
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
            console.log(decksize, index);
            setTimeout(function() {
                $("#next-button").fadeIn("slow");
                $(".card:first").addClass("select-box");
                console.log(decksize, index);
            }, 1000);

        });
    });
});
