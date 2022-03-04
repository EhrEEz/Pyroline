function verify(event, element) {
    event.preventDefault();
    var first_name = document.getElementById("first_name").value;
    var last_name = document.getElementById("last_name").value;
    var address = document.getElementById("address").value;
    var message_box = document.getElementsByClassName("err-message")[0];
    function checkLength(value) {
        if (value.length < 9) {
            message_box.innerHTML = "Length is less than 9";
        }
    }
    checkLength(first_name);
    console.log(first_name, last_name, address);
}
