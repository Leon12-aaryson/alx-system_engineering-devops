# This puppet script is meant to kill a process
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill -f "killmenow"',
  onlyif  => '/usr/bin/pgrep -f "killmenow"',
}
