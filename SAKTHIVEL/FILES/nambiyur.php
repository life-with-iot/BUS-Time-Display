<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
a:link, a:visited {
  background-color:#070101;
  color: #1d09f2;
  padding: 15px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: black;
}
* {
  box-sizing: border-box;
}

#myInput {
  background-image: url('/css/searchicon.png');
  background-position: 10px 10px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}

#myTable {
  border-collapse: collapse;
  width: 100%;
  border: 1px solid #ddd;
  font-size: 18px;
}

#myTable th, #myTable td {
  text-align: left;
  padding: 12px;
}

#myTable tr {
  border-bottom: 1px solid #ddd;
}

#myTable tr.header, #myTable tr:hover {
  background-color: #f1f1f1;
}
</style>
</head>
<body>
<h2>WELCOME</h2>
<p>click to GoBack:</p>
<a href="second.html" >Back</a>

<h2>Bus detail</h2>

<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names.." title="Type in a name">


<table id="myTable">
<tr>
<th>Route</th>
<th>Time</th>
<th>Bus_no</th>
<th>Avilability</th>
</tr>

<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "bus_details";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT bus_no , time, route, avilability FROM bus_route_details WHERE time>=CURTIME()";
$result = $conn->query($sql);
$sql1 = "SELECT bus_no , time, route, avilability FROM bus_route_details WHERE time<CURTIME()";
$result1 = $conn->query($sql1);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
    echo "<tr><td>".$row["route"]."</td>"."<td>".$row["time"]."</td>"."<td>".$row["bus_no"]."</td>"."<td>".$row["avilability"]."</td></tr>";
  }
}
else{
  echo "0 result";
}
if ($result1->num_rows > 0) {
    // output data of each row
    while($row = $result1->fetch_assoc()) {
    echo "<tr><td>".$row["route"]."</td>"."<td>".$row["time"]."</td>"."<td>".$row["bus_no"]."</td>"."<td>".$row["avilability"]."</td></tr>";
  }
  echo "</table>";
}
else{
  echo "0 result";
}
?>
</table>

<script>
function myFunction() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}
</script>

</body>
</html>
