provider "aws"{
	version = "2.7"
	region = "us-west-2"
}

# Create EC2 instance
resource "aws_instance" "naijarant"{
	ami="ami-06f2f779464715dc5"
	key_name="aws-key"
    instance_type="t2.micro"

	associate_public_ip_address = true
	provisioner "local-exec"  {	
		command = "sleep 120; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu --private-key ../aws-key.pem -i '${aws_instance.naijarant.public_ip},' ../setup.yml"
	}
}

