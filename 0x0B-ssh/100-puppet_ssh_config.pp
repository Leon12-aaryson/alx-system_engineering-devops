file { '/home/ubuntu/.ssh/config':
  ensure  => 'present',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "# SSH client configuration\n\nHost 249537-web-01\n    HostName 100.25.201.247\n    User ubuntu\n    IdentityFile ~/.ssh/school\n    PreferredAuthentications publickey\n    PasswordAuthentication no\n",
}
