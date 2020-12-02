#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser); 

$wall = "wallet_history.out"; 

$userid = param("userid"); #sender user_name
$account_no = param("account_no");

print header ();

print<<EOP; 
<html>
<head><title>Wallet Statements</title>
<meta name="author" content="Satyawant_Kumar Josy_Sebastian Reuben_Johns">
<link rel="stylesheet" href="design.css">
<style>
table, th, td {
  border: 1px solid black;
  text-align: center;
}

table {
  width: 60%;
  margin-left: 200;
}
</style>
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

open(OUT,"$wall") || die "can't read to $wall";
@hist = <OUT>;
chomp @hist;
close(OUT);

@tran = ();
@amount_val = ();
@tran_date = ();

for($i=0; $i<@hist; $i++){
	@hist_new = ();
	@hist_new = split(",", $hist[$i]);
	if($hist_new[0] eq $account_no){
		push(@tran, $hist_new[1]);
		push(@amount_val, $hist_new[2]);
		push(@tran_date, $hist_new[3]);
	}
}

if($tran[0] eq ""){
	print<<EOP; 
		<head><title>wallet_history</title></head>
		<body><div class="content heading_new"><br>
		<p style="font-size: 15px;">No wallet statement Available!!</p>
EOP
	exit;
}

print<<EOP;
	<div class="content">
		<h2 class="heading">Welcome to KNU Pay</h2><br>
		<table>
		<b><caption>Wallet Statement:</caption></b>
		<tr>
		<br>
			<th>Account No</th>
			<th>Transaction Type</th>
			<th>Transaction Amount</th>
			<th>Transaction Date</th>
		</tr>
	</div>
</div>
EOP

for($j=0; $j<@tran; $j++){
	print<<EOP;
	<div class="content">
		<div>
			<tr>
				<td>$account_no</td>
				<td>$tran[$j]</td>
				<td>$amount_val[$j] dollar</td>
				<td>$tran_date[$j]</td>
			</tr>
		</div>
	</div>
EOP
}

print<<EOP;
</table>
EOP