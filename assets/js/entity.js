$(document).ready(function () {
  // Entity links
  $(".rich-text")
    .find("a")
    .each(function () {
      var href = $(this).attr("href");
      if (href) {
        if (href.startsWith("/entities/")) {
          var entity = href.split("/")[2];
          $(this).addClass("entity_hl");
          $(this).addClass(CLASSES[entity]);
        }
      }
    });

  $("#switch-1").bind("change", function (event) {
    // This is a very pseudo way of doing this.
    // Due to the buggy nature of css checkbox switches, this is the
    // best we can do
    if ($("a.force_black").length) {
      $("a.force_black").removeClass("force_black");
    } else {
      $(".rich-text").find("a").addClass("force_black");
    }
  });
});
