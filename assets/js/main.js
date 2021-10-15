function setCookie(name, value, days) {
  var expires = "";
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}
function getCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(";");
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == " ") c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}
function eraseCookie(name) {
  document.cookie = name + "=; Max-Age=-99999999;";
}

$(document).ready(function () {
  window.addEventListener(
    "resize",
    function () {
      if (window.innerWidth < 768) {
        document.getElementById("menu-switch").checked = false;
      } else {
        document.getElementById("menu-switch").checked = true;
      }
    },
    true
  );

  $("body").on("click", "#privacy-alert-agree", function (event) {
    event.preventDefault();
    setCookie("privacy-agree", "set");
    $("#privacy-alert").slideUp();
  });

  if (getCookie("privacy-agree") !== "set") {
    $("#privacy-alert").slideDown();
  }
});
