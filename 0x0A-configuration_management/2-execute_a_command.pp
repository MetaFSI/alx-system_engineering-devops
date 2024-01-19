# Kill processing named killmenow
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
