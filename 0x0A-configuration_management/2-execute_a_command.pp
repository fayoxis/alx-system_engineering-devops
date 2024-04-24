# kills a process named killmenow.

$process_to_kill = 'killmenow'
$kill_command = 'pkill'
$bin_path = '/usr/bin/'

exec { $process_to_kill:
  command => "${kill_command} ${process_to_kill}",
  path    => $bin_path,
}
