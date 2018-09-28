#!/usr/bin/env perl

sub yes_no {
    my ($question) = @_;

    while (1) {

	print $question;
	my $answer = <STDIN>;
	chomp $answer;
	$answer = lc $answer;

	if ( $answer eq 'y' || $answer eq "yep" || $answer eq "yes" || $answer eq "ya" )  {
	    return true;
	} elsif ( $answer eq "n" || $answer eq "no" || $answer eq "nope" || $answer eq "nah") {
	    return false;
	} else {
	    print "Not a valid input. Try again.\n";
	}
    }
}

if ( yes_no("Does this work? ") ) {
    print("Yes\n");
} else {
    print("No\n");
}
