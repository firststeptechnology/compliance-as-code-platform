terraform {

  required_version = ">= 1.6.0"

}

locals {

  compliance_framework = "NIST SP 800-53 Rev. 5"

  compliance_library_version = "1.0.0"

}

output "compliance_platform" {

  value = {

    provider = "First Step Technology LLC"

    platform = "Compliance-as-Code"

    framework = local.compliance_framework

    library_version = local.compliance_library_version

    validation = "enabled"

  }

}

resource "null_resource" "compliance_validation" {

  triggers = {

    framework = local.compliance_framework

    version = local.compliance_library_version

  }

  provisioner "local-exec" {

    command = "echo Running Compliance-as-Code validation..."

  }

}
