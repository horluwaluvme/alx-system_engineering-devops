#!/usr/bin/env ruby
# Match a 10 digit phone number 7858148567 without spaces

puts ARGV[0].scan(/^[0-9]{10}$/).join
