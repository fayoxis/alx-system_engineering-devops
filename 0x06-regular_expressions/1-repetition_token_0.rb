#!/usr/bin/env ruby
# The script accepts an argument then passes it to a regular expression
puts ARGV[0].scan(/hbt{2,5}n/).join
