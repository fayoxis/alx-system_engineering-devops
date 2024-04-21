include stdlib

# Manage SSH config file
$ssh_config_file = '/etc/ssh/ssh_config'

# Disable password authentication
$password_authentication_line = '    PasswordAuthentication no'
augeas { 'disable_password_auth':
  context => "/files${ssh_config_file}",
  changes => [
    "set Host[.='']/PasswordAuthentication ${password_authentication_line}"
  ],
}

# Set the identity file for SSH
$identity_file_line = '    IdentityFile ~/.ssh/school'
augeas { 'set_identity_file':
  context => "/files${ssh_config_file}",
  changes => [
    "set Host[.='']/IdentityFile ${identity_file_line}"
  ],
}
