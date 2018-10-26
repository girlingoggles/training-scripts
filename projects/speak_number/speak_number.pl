#!/usr/bin/env perl
#girlingoggles made this

use strict;
use warnings;
use lib "../speak_number/";
use speak_number;

speak_number::speak_number($ARGV[0]);
