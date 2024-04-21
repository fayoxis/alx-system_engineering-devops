# Manage SSH config file
file_line {
  default: 
    path => '/etc/ssh/ssh_config',

  'Turn off passwd auth':
    ensure => 'present',
    line   => '    PasswordAuthentication no',

  'Declare identity file':
    ensure => 'present',    
    line   => '    IdentityFile ~/.ssh/school', 
}
