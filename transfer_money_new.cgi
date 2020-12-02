#!/usr/bin/perl  -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

print header ();

$userid = param("userid");
$account_no = param("account_no"); #sender account no

print<<EOP; 
<html>
<head><title>Money Transfer</title>
<meta name="author" content="Satyawant_Kumar Josy_Sebastian Reuben_Johns">
<link rel="stylesheet" href="design.css">
</head>
<body class="body_background">
<div class="sidenav">
	<a href="home.htm">Home</a>
	<a href="contact.htm">Contact</a>
	<a href="services.htm">Services</a>
	<a href="about.htm">About</a> 
</div>
</body>
</html>
EOP

print<<EOP;

<div class="content">
<h2 class="heading">Welcome to KNU Pay</h2><br>
	<div class="div_1">
		<form action="transfer_money.cgi" method="post">
			<hr>
			<label for="rec_account_no"><b>Receiver's Account No</b></label>
			<input type="number" name="rec_account_no" id="rec_account_no" placeholder="Enter receiver's account no.." required/>
			<label for="amount"><b>Amount in Dollar</b></label>
			<input type="number" name="amount" id="amount" placeholder="Enter the amount.." required/>
		
			<input type="hidden" name="userid" id="userid" value=$userid>
			<input type="hidden" name="account_no" id="account_no" value=$account_no>
			
			<input type="submit" value="Transfer">
			<input type="reset" value="Reset">
			</form>
	</div>
</div>
EOP