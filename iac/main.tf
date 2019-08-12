provider "aws"{
	version = "2.7"
	region = "us-west-2"
}

# Create EC2 instance
resource "aws_instance" "naijarant"{
	ami="ami-06f2f779464715dc5"
	key_name="aws-key"
        instance_type="t2.micro"
}

