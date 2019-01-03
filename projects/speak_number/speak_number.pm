#!/usr/bin/env perl
#girlingoggles made this

package speak_number;

use strict;
use warnings;

return 1;

sub speak_number {
    my ($input) = @_;
    
    if (not defined $input) {
	print "Please enter a number: \n";
	$input = <>;
    }
    speak_number_hundreds($input);
    print "\n";
}

sub speak_number_ones {
    my ($one) = @_;

    if ($one == 1) {
	print "one ";
    } elsif ($one == 2) {
	print "two ";
    } elsif ($one == 3) {
	print "three ";
    } elsif ($one == 4) {
	print "four ";
    } elsif ($one == 5) {
	print "five ";
    } elsif ($one == 6) {
	print "six ";
    } elsif ($one == 7) {
	print "seven ";
    } elsif ($one == 8) {
	print "eight ";
    } elsif ($one == 9) {
	print "nine ";
    }
}

sub speak_number_tens {
    my ($input) = @_;

    my $ten = int($input / 10);

    if ($ten == 1) {
	speak_number_teens($input);
	return;
    } elsif ($ten == 2) {
	print "twenty ";
    } elsif ($ten == 3) {
	print "thirty ";
    } elsif ($ten == 4) {
	print "fourty ";
    } elsif ($ten == 5) {
	print "fifty ";
    } elsif ($ten == 6) {
	print "sixty ";
    } elsif ($ten == 7) {
	print "seventy ";
    } elsif ($ten == 8) {
	print "eighty ";
    } elsif ($ten == 9) {
	print "ninety ";
    }

    speak_number_ones($input % 10);
}

sub speak_number_teens {
    my ($teen) = @_;

    if ($teen == 10) {
	print "ten ";
    } elsif ($teen == 11) {
	print "eleven ";
    } elsif ($teen == 12) {
	print "twelve ";
    } elsif ($teen == 13) {
	print "thirteen ";
    } elsif ($teen == 14) {
	print "fourteen ";
    } elsif ($teen == 15) {
	print "fifteen ";
    } elsif ($teen == 16) {
	print "sixteen ";
    } elsif ($teen == 17) {
	print "seventeen ";
    } elsif ($teen == 18) {
	print "eighteen ";
    } elsif ($teen == 19) {
	print "nineteen ";
    }
}


sub speak_number_hundreds {
    my ($input) = @_;

    my $hundred = int($input / 100);
    if ($input > 99) {
	speak_number_ones($hundred);
	print "hundred ";
    }
    speak_number_tens($input % 100);
}

