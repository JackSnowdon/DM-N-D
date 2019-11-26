$(document).ready(function () {

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

    function startCombat() {
        $("#next-button").fadeIn("slow");
        $(".card:first").addClass("select-box");
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
        $(".combat-buttons").fadeIn();
    }


    $("#start-combat").click(function () {

        repeat = 0;
        decksize = getDeckSize();
        index = getIndex();

        $("#start-combat").hide();
        $("#delete-all-combat").hide();
        $("#add-hero").hide();
        setTimeout(function () {
            startCombat();
            currentcard = getCurrentCard();
            console.log(currentcard);
            setStats(currentcard);
            setTimeout(function () {
                $("#hide-combat").fadeIn("slow");
            }, 1000);

        }, 1000);
    });


    $("#next-button").click(function () {
        $("#next-button").attr("disabled", true);

        $("#turn-owner").fadeOut();
        $("#turn-health").fadeOut();
        $(".combat-buttons").fadeOut();

        if (repeat > 0) {
            index = 1;
            repeat--;
        }

        var removecard = $(".card.select-box:first");
        removecard.removeClass("select-box");

        if (decksize > index) {
            setTimeout(function () {
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
            setTimeout(function () {
                $("#next-round").show();
                $("#next-button").attr("disabled", false);
            }, 1000);
        }
    });

    $("#next-round").click(function () {
        $("#next-round").hide();
        var index = $(".card").index(".card") + 1;
        setTimeout(function () {
            startCombat();
            currentcard = getCurrentCard();
            console.log(currentcard);
            setStats(currentcard);
            repeat++;
        }, 1000);

    });


    $("#attack-button").click(function () {
        //$("#attack-button").attr("disabled", true);
        var list = $(".card-deck").find(".card-title");
        var len = list.length
        currentcard = getCurrentCard();
        name = getCurrentName(currentcard)
        console.log(len);

        var targets = []

        for (i = 0; i < len; i++) {
            if (list[i].innerHTML == name) {
                //pass
            } else {
                targets.push(list[i].innerHTML)
            }
        }

        console.log(name)

        console.log(targets)

    });

});
