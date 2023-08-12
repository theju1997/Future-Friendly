var Family = /** @class */ (function () {
    function Family() {
        this.familycount = 6;
    }
    Family.prototype.withfamily = function () {
        console.log("we can Spend our precious time");
    };
    Family.prototype.withGrandparents = function () {
        console.log("We can get experiences info");
    };
    return Family;
}());
var Theju = new Family();
Theju;
console.log(Theju);
