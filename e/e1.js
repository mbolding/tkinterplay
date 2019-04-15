function multiplesOf3and5(number) {
    var total = 0;
    for (n = 0; n < number; n++) {
        if (n % 3 == 0) {
            total += n;
        } else if (n % 5 == 0) {
            total += n;
        }
    }
    return total;
}



multiplesOf3and5(10);
multiplesOf3and5(1000);
multiplesOf3and5(49);
multiplesOf3and5(19564);

multiplesOf3and5(56);
