$(document).ready(function () {

    // Init Vars

    var decksize, index, repeat, currentcard;
    var targets = [];
    var weplist = [];

    // Helper Functions

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

    function getStat(x, y) {
        return $(x).find(y).text();
    }

    function getAllStats(x) {
        return { str: getStat(x, ".str-stat"), dex: getStat(x, ".dex-stat"), int: getStat(x, ".int-stat"), wis: getStat(x, ".wis-stat"), con: getStat(x, ".con-stat"), cha: getStat(x, ".cha-stat") };
    }

    function getTargets() {
        empty();
        var list = $(".card-deck").find(".card-title");
        var len = list.length
        currentcard = getCurrentCard();
        name = getCurrentName(currentcard)
        for (i = 0; i < len; i++) {
            if (list[i].innerHTML == name) {
                //pass
            } else {
                targets.push(list[i].innerHTML)
            }
        }
        return targets
    }

    function getWeapons(x) {
        weplist = [];
        var allweps = $(x).find(".single-weapon");
        var len = allweps.length;
        for (a = 0; a < len; a++) {
            var wepname = $(allweps[a]).find(".weapon-name").text();
            var wepdie = $(allweps[a]).find(".weapon-die").text();
            var wep = { name: wepname, die: wepdie }
            weplist.push(wep)
        }
        $.each(weplist, function (index, wep) {
            $(".weapon-list").append('<span><button class="btn btn-warning weapon-select" data-toggle="modal"  id="' + wepname + '">' + wep.name + '</button></span><span class="wepdies">' + wep.die + '</span>');
            $(".weapon-list").fadeIn();
        });
    }

    function getDiceRoll(x) {
        return Math.floor(Math.random() * x) + 1;
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

    function empty() {
        //empty your array
        targets = [];
    }


    // Combat Flow


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
        $(".weapon-list").empty()
        $("#next-button").attr("disabled", true);

        $("#turn-owner").fadeOut();
        $("#turn-health").fadeOut();
        $(".combat-buttons").fadeOut();
        $("#targets").fadeOut();

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
        $(".weapon-list").empty()
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


    // Combat Moves


    $("#attack-button").click(function () {
        $(".attack-action").attr("disabled", false);
        $(".weapon-select").attr("disabled", false);
        $("#targets").empty();
        
        getTargets()

        $.each(targets, function (index, value) {
            $("#targets").append('<span><button class="btn btn-warning attack-action" data-toggle="modal" data-target="#attackModal" id="' + index + '">' + value + '</button>' + '</span>');
        });

        $(".weapon-list").empty();
        getWeapons(currentcard);
        console.log(weplist);

        $(".weapon-select").click(function () {
            $(".weapon-select").attr("disabled", true);
            selectedwep = this.id;
            var attackdies = $(".wepdies").text()
            console.log(attackdies)
            return selectedwep;
        })

        $(".attack-action").click(function () {
            
            slot = this.id;
            attacked = targets[slot]
            console.log(attacked)
            var cardlist = $(".card-deck").find(".card-title");
            var len = cardlist.length
            for (i = 0; i < len; i++) {
                if (cardlist[i].innerHTML == attacked) {
                    var getcard = cardlist.parent().parent()
                    var thiscard = getcard[i]
                    $(thiscard).addClass("attacked-box");
                    var attackstats = getAllStats(currentcard);
                    var defendstats = getAllStats(thiscard);
                    var targethp = $(".attacked-box").find(".hp-meter").html()
                } else {
                    // pass 
                }
            }

            setTimeout(function () {
                $(".attacked-box").removeClass("attacked-box");

            }, 1000);


            $("#attack-body").html("<h3>" + name + " attacks " + attacked + "</h3>");
            $("#testdata").html("<span>" + name + " Uses " + selectedwep + "</span>");     


            $("#attack-confirm").click(function () {
                //$(".weapon-list").fadeOut();
                $(".attack-action").attr("disabled", true);
            })
        });
        $("#targets").fadeIn();
    });
});
