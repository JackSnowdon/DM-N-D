$(document).ready(function() {

    $("#start-combat").click(function() {
        $("#start-combat").hide();
        $("#delete-all-combat").hide();
        $("#add-hero").hide();
        setTimeout(function() {
            $("#next-button").fadeIn("slow");
            $(".card:first").addClass("select-box");
        }, 1000);
    });
    
    $("#next-button").click(function() {
        $(".card:first").removeClass("select-box");
    });
    
    
});
