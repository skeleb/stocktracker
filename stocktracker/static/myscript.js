var changePercentList = document.getElementsByClassName("change-percent");

for (i = 0; i < changePercentList.length; i++) {
    if (changePercentList.item(i).nodeValue == "0.063") {
        changePercentList.item(i).style.backgroundColor = "red";
    } else {
        changePercentList.item(i).style.backgroundColor = "green";
    }
  }
