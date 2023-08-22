var Smosa = 10,
    Kachori = 12,
    Vadapav = 60,
    Maggi = 50;
var smosa_q = 0,
    kachori_q = 0,
    vadapav_q = 0,
    maggi_q = 0;
var name = "",
    email = "";
var smosaBill = "",
    kachoriBill = "",
    vadapavBill = "",
    maggiBill = "";
var total_amount = 0;
document.getElementById("name").addEventListener("keyup", function() {
    document.getElementById("name2").innerHTML = this.value;
});

document.getElementById("email").addEventListener("keyup", function() {
    document.getElementById("email2").innerHTML = this.value;
});
