#!/usr/bin/perl  -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$itf = "customer_balance.out"; #user_name and balance
$outf = "register_1.out"; #account and user_name

$wall = "wallet_history.out"; 

$post_send_bal = param("post_send_bal");
$post_rec_bal = param("post_rec_bal");
$userid = param("userid"); #sender user_name
$rec_userid = param("rec_userid"); #receiver user_name
$amount = param("amount");
$rec_account_no = param("rec_account_no");

# Output the HTTP header
print header ();

print<<EOP; 
<html>
<head><title>Transfer Update</title>
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
				<div class="transfer_body"><br>
					<h2 style="text-align:center;">Thank for using our Wallet!!</h2>
					<p style="text-align:center;">Your transaction of <b>Amount: $amount dollar!</b> has been completed successfully!!</p><hr>
					<p style="text-align:center;">Please Note that:</p>
					<p style="text-align:center;">Available balance: <b>$post_send_bal</b> dollar!</p>
				</div>
			</div>
EOP

open(OUT,"$itf") || die "can't read to $itf";
%hash_balance = split(",", <OUT>);
close(OUT);
			
$hash_balance{$userid} = $post_send_bal;
$hash_balance{$rec_userid} = $post_rec_bal;
			
open(OUT,">$itf") || die "can't write to $itf";
$, = ",";
print OUT %hash_balance;
close(OUT);

open(OUT,"$outf") || die "can't read to $outf";
%hash_account = split(",", <OUT>);
close(OUT);

foreach $key (keys %hash_account){
	if($hash_account{$key} eq $userid){
		$send_account_no = $key;
	}
}

open(OUT,"$wall") || die "can't read to $wall";
@hist = <OUT>;
chomp @hist;
close(OUT);
		
$date = localtime();
$update_1 = "Debit";
$update_2 = "Credit";
		
$wallet_1[0] = $send_account_no;
$wallet_1[1] = $update_1;
$wallet_1[2] = $amount;
$wallet_1[3] = $date;

$wallet_2[0] = $rec_account_no;
$wallet_2[1] = $update_2;
$wallet_2[2] = $amount;
$wallet_2[3] = $date;
		
open(OUT,">$wall") || die "can't write to $wall";

for($i=0; $i<@hist; $i++){
	print OUT $hist[$i]."\n";
}
print OUT @wallet_1;
print OUT "\n";
print OUT @wallet_2;
close(OUT);