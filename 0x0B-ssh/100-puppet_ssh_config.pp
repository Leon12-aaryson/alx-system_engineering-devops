#the script is to use the configuration in the script to connect to the server

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => @(EOF),
            Host*
            PasswordAuthentication no
            IdentityFile ~/.ssh/school
EOF
}
