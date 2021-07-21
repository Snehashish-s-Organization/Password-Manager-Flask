function myFunction() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue1, txtValue2, txtValue3;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td");
      td1 = td[0];
      td2 = td[1];
      td3 = td[2];
      if (td1 && td2 && td3) {
        txtValue1 = td1.textContent || td1.innerText;
        txtValue2 = td2.textContent || td2.innerText;
        txtValue3 = td3.textContent || td3.innerText;
        // console.log(txtValue1 + txtValue2)
        in1 = txtValue1.toUpperCase().indexOf(filter) > -1
        in2 = txtValue2.toUpperCase().indexOf(filter) > -1
        in3 = txtValue3.toUpperCase() === filter
        inall = in1 || in2 || in3
        if (inall) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }   
  function deleteValue() {
  }