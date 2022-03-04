function passwordCheckClicked(e, triger) {
    e.preventDefault();
    if (triger.checked == true) {
        showPassword(e);
    }
    if (triger.checked == false) {
        hidePassword(e);
    }
}
function hidePassword(e) {
    e.preventDefault();
    var passwordField = document.getElementById("password");
    passwordField.setAttribute("type", "password");
    passwordField.setAttribute("autocomplete", "current-password");
    if (passwordField.value == "" || passwordField.value == null) {
        focusHandler(e, passwordField);
    } else {
        blurHandler(e, passwordField);
    }
}
function showPassword(e) {
    e.preventDefault();
    var passwordField = document.getElementById("password");
    passwordField.setAttribute("type", "text");
    passwordField.setAttribute("autocomplete", "off");
    if (passwordField.value == "" || passwordField.value == null) {
        focusHandler(e, passwordField);
    } else {
        blurHandler(e, passwordField);
    }
}
function goHandler(e) {
    e.preventDefault();
    var x = document.getElementsByClassName("input-container");
}
function focusHandler(e, element) {
    var lbl = element.previousElementSibling;
    lbl.classList.add("active");
    element.classList.add("bor");
}
function blurHandler(e, element) {
    var lbl = element.previousElementSibling;
    if (element.value == "" || element.value == null) {
        element.classList.remove("bor");
        lbl.classList.remove("active");
    }
    console.log(lbl);
}
