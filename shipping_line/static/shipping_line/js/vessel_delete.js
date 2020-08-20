$("td").on('click', '.approved', function (e) {
    var b = $(this);
    b.prop("disabled", true);
    $.ajax({
        type: "GET",
        url: "/shipping-line/vessel-arrivals/" + b.attr("submission-id") + "/reject",
        success: function (data) {
            console.log(data);
            b.attr("disabled", false);

            b.removeClass("approved");
            b.removeClass("btn-primary");
            b.addClass("not-approved");
            b.addClass("btn-warning");

            b.text('Not Approved');

        },
        error: function (status) {
            console.log("Error in enrolling " + b.attr("submission-id") + "-" + status.status);
        }
    });
});