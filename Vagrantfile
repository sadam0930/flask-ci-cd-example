# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
    vb.cpus = 1
  end

  # Copy .gitconfig file 
  if File.exists?(File.expand_path("~/.gitconfig"))
    config.vm.provision "file", source: "~/.gitconfig", destination: "~/.gitconfig"
  end

  ######################################################################
  # Setup a Python development environment
  ######################################################################
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y git zip tree python-pip python-dev build-essential
    sudo apt-get -y autoremove
    # Install app dependencies
    cd /vagrant
    sudo pip install -r requirements.txt
  SHELL

  ######################################################################
  # Optional: run app in a Docker container
  ######################################################################
  config.vm.provision "docker" do |d|
    d.build_image "/vagrant",
      args: "-t imageupload"
    d.run "imageupload",
      args: "--restart=always -d --name imageupload -p 5000:5000 --rm"
  end

end
