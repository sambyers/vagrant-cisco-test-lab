# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrant multi-machine setup with 2 Cisco routers

Vagrant.configure("2") do |config|
  config.vm.define "rtr1" do |rtr1|
    rtr1.vm.box = "iosxe/16.08.01"
    rtr1.vm.network :private_network,
        virtualbox__intnet: "link1", auto_config: false
  end

  config.vm.define "rtr2" do |rtr2|
    rtr2.vm.box = "iosxe/16.08.01"
    rtr2.vm.network :private_network,
        virtualbox__intnet: "link1", auto_config: false
  end
end