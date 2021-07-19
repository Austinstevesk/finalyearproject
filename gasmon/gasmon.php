<?php
class gasmon{
 public $link='';
 function __construct($username, $gasValue){
  $this->connect();
  $this->storeInDB($username, $gasValue);
 }
 
 function connect(){
  $this->link = mysqli_connect('localhost','root','') or die('Cannot connect to the DB');
  mysqli_select_db($this->link,'gasmonitor') or die('Cannot select the DB');
 }
 
 function storeInDB($username, $gasValue){
  $query = "insert into gaslevel set username='".$username."', gasValue='".$gasValue."'";
  $result = mysqli_query($this->link,$query) or die('Errant query:  '.$query);
 }
 
}
if($_GET['username'] != '' and  $_GET['gasValue'] != ''){
 $gasmon=new gasmon($_GET['username'],$_GET['gasValue']);
}


?>
