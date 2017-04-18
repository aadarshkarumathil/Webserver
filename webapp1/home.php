<html>
<head>
  <title> MircoBlog </title>
  <!-- Compiled and minified CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/css/materialize.min.css">
<link rel="stylesheet" type="text/css" href="main.css"/>
<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/js/materialize.min.js"></script>
</head>
<body>
  <nav>
  <div class ="nav-wrapper">
    <a href="#" class="brand-logo right">MicroBlog</a>
    <ul id = "nav-mobile" class = "left hide-on-med-and-down">
      <li>
        <a href="home.php">Home</a>
      </li>
      <li>
        <a href="help.php">Help</a>
      </li>
      <li>
        <a href="about.php">About us</a>
      </li>
      <li>
        <a href="logout.php">Logout</a>
      </li>
      <li>
        <a href="register.php">Register</a>
      </li>
    </ul>
  </div>
</nav>
<?php
$servername = "localhost";
$username = "root";
$password = "passw0rd";
$db="MICROBLOG";
$conn=mysqli_connect($servername, $username, $password, $db);
$sessionid = $_SERVER["SESSION_ID"];

if(!$conn){
  die("Connection failed: ".mysqli_connect_error());
}
#echo "Connected successfully";
$query = "SELECT * FROM session where session_hash = '$sessionid';";
#echo $query;
$result = mysqli_query($conn,$query);
$row = mysqli_fetch_assoc($result);
echo "<h4>Previous Blog Data:- <br /></h4>";
$que = "select data from microblog where ID = '$row[ID]';";
$res = mysqli_query($conn,$que);
$drow = mysqli_fetch_assoc($res);
echo "<br />";
$data = $drow["data"];
$posts = explode("~",$data);
echo "<table class='striped'><thead>
Posts:-
</thead>";
foreach ($posts as $post) {

  echo "<tbody><tr><td>".$post."</td></tr></tbody>";
}
echo "</table><br />";
echo "<h4> Want to post anything new?</h4><br />";
?>
<form method="post" action=home.php>
  <div class = "input-field col s8">
    <label class = "active" >want to post something new ? :</label>
    <input type = "text" name="blog", value="" /></p>
  </div>
  </div>
  <input class = "waves-effect waves-light btn" type="submit" value="POST" />
</form>
<?php
  $pos_data = $_SERVER["_POST"];
  $new_data = end(explode("=",$pos_data));
  $new_data = str_replace("+"," ",$new_data);
  echo "We dont use ajax so you will have to refresh the page to see the data in the posts <br />";
  echo "new data which is being added = <br />".$new_data;
  echo"<br />";
  $total_data = $new_data."~".$data;
  if($new_data)
  {
    echo "True";
  }
  if($new_data!="")
  {
    $query = "select * from microblog where ID = '$row[ID]';";
    $result = mysqli_query($conn,$query);
    $row_count = mysqli_num_rows($result);
    if($row_count==0)
    {
      $query = "INSERT INTO microblog(ID,data) VALUES ('$row[ID]','$total_data');";
    }
    else
    {
      $query = "UPDATE microblog SET data='$total_data' where id='$row[ID]';";
    }
    #echo $query;
    echo "<br />";
    mysqli_query($conn,$query);
    echo $total_data;
  }
 ?>
</body>
</html>
