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

    function getCurrentName(x) {
        return $(x).find(".card-title").text();
    }
    
    function getCurrentHp(x) {
        return $(x).find("#card-hp").text();
    }
    
    function getMaxHp(x) {
        return $(x).find("#card-max-hp").text();
    }
    
    function setStats(x) {
        var name = getCurrentName(x);
        var hp = getCurrentHp(x);
        var maxhp = getMaxHp(x);
        $("#turn-name").text(name);
        $("#turn-hp").text(hp);
        $("#turn-max-hp").text(maxhp);
        $("#turn-owner").fadeIn();
        $("#turn-health").fadeIn();
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
            currentcard = getCurrentCard();
            console.log(currentcard);
            setStats(currentcard);
            setTimeout(function() {
                $("#hide-combat").fadeIn("slow");
            }, 1000);

        }, 1000);
    });


    $("#next-button").click(function() {
        $("#next-button").attr("disabled", true);

        $("#turn-owner").fadeOut();
        $("#turn-health").fadeOut();

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
                setStats(currentcard);
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
        $("#turn-owner").fadeOut();
        $("#next-round").hide();
        var decksize = $(".card").length;
        var index = $(".card").index(".card") + 1;
        setTimeout(function() {
            $("#next-button").fadeIn("slow");
            $(".card:first").addClass("select-box");
            currentcard = getCurrentCard();
            console.log(currentcard);
            setStats(currentcard);
            repeat++;
        }, 1000);

    });

});