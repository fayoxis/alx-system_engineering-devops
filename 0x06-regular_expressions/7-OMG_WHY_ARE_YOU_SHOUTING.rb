#!/usr/bin/env ruby
# regular expression that matches only capital letters
puts ARGV[0].scan(/[A-Z]/).join
