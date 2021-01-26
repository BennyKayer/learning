String.prototype.erLik = function(text) {
    const reE = /é|è|ê/;
    const reO = /ó|ò|ô/;
    const reAa = /å/;
    const reAe = /æ/;
    const reOe = /ø/;
    const reECap = /É|È|Ê/;
    const reOCap = /Ó|Ò|Ô/;
    const reAaCap = /Å/;
    const reAeCap = /Æ/;
    const reOeCap = /Ø/;
    const normalized = this.replace(reE, "e")
        .replace(reO, "o")
        .replace(reAa, "aa")
        .replace(reAe, "ae")
        .replace(reOe, "oe")
        .replace(reECap, "E")
        .replace(reOCap, "O")
        .replace(reAaCap, "Aa")
        .replace(reAeCap, "Ae")
        .replace(reOeCap, "Oe");
    return normalized == text;
};
