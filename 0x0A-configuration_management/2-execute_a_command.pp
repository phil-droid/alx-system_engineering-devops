#puppet manifest that kills a process

exex{'process kill killmenow':
  path    => '/usr/bin/',
  command => 'pkill -f killmenow',
}