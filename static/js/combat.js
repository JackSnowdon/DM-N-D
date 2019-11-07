$(document).ready(function() {

    $("#start-combat").click(function() {

        var index = $('.card:first').index('.card:first') + 1;

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
                $(".card:first").removeClass("select-box")
                console.log("Dick");
            }
            else {
                $(".card").eq(index).removeClass("select-box");
                console.log("test!");
            }
            var first = $(".card:first")

            setTimeout(function() {
                $(".card").eq(index).addClass("select-box");
                index++;
                console.log(index);
            }, 1000);
        });
    });
});
