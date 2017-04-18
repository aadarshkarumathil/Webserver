<?php
session_start();
 ?>
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
        <a href="#">Help</a>
      </li>
      <li>
        <a href="about.php">About us</a>
      </li>
      <li>
        <a href="login.php">Login</a>
      </li>
      <li>
        <a href="register.php">Register</a>
      </li>
    </ul>
  </div>
</nav>
<h1 class = "s12 m4 l8">
<?php
  $_POST = parse_url($_SERVER["_POST"]);
  $a=explode("&",$_POST["path"]);
  $firstname = explode('=',$a[0])[1];
  $lastname = explode('=',$a[1])[1];
  $email = explode('=',$a[2])[1];
  $pass = explode('=',$a[3])[1];
  $retype_password = explode('=',$a[4])[1];

  $email = str_replace("%40","@",$email);
  if(strcmp($pass,$retype_password)!=0)
  {
    echo "firstname = ". $firstname."<br />";
    echo "lastname = ". $lastname."<br />";
    echo "email = ". $email."<br />";
    echo "password = ". $pass."<br />";
    echo "retype_password = ". $retype_password."<br />";

    $link="register.php";
    echo " DIFFERENT PASSWORDS ENTERED"."<br />";
    echo "<a href ='".$link."'>Click here to get redirected</a>";
  }
  else {
  /*echo "firstname = ". $firstname."<br />";
  echo "lastname = ". $lastname."<br />";
  echo "email = ". $email."<br />";
  echo "password = ". $password."<br />";
  echo "retype_password = ". $retype_password."<br />";*/

  $servername = "localhost";
  $username = "root";
  $password = "passw0rd";
  $db="MICROBLOG";
  $conn=mysqli_connect($servername, $username, $password, $db);

  if(!$conn){
    die("Connection failed: ".mysqli_connect_error());
  }
  #echo "Connected successfully";
  $query = "INSERT INTO microblog_users(firstname,lastname,email,pass) VALUES ('$firstname','$lastname','$email','$pass');";
  #echo $query;
  $result = mysqli_query($conn,$query);
  if($result)
  {
    $link = "login.php";
    echo " <h1>registered</h1>";
    echo "<a href=".$link.">Click here to get redirected to the login page</a>";
  }
  else
  {
    $link="register.php";
    echo " Email id already exists"."<br />";
    echo "<a href ='".$link."'>Click here to get redirected</a>";
    echo json_encode(42);
    mysqli_close($conn);
    echo "connection closed";
  }
}
?>
</h1>
</body>
</html>
