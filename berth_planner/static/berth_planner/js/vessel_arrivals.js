
         $("td").on('click', '.not-approved', function (e) {
        var b = $(this);
        b.prop("disabled", true);
        $.ajax({
            type: "GET",
            url: "/berth-planner/vessel-arrivals/" + b.attr("submission-id") + "/approve",
            success: function (data) {
                console.log(data);
                b.attr("disabled", false);

                b.removeClass("not-approved");
                b.removeClass("btn-warning");
                b.addClass("approved");
                b.addClass("btn-primary");

                b.text('Approved');

            },
            error: function (status) {
                console.log("Error in enrolling " + b.attr("submission-id") + "-" + status.status);
            }
        });
    });
 $("td").on('click', '.approved', function (e) {
        var b = $(this);
        b.prop("disabled", true);
        $.ajax({
            type: "GET",
            url: "/berth-planner/vessel-arrivals/" + b.attr("submission-id") + "/reject",
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

