resource "aws_organizations_policy" "example_scp" {
  name        = "DynamicSCP"
  description = "SCP con variables dinámicas"
  type        = "SERVICE_CONTROL_POLICY"

  content = templatefile("${path.module}/scp-template.json.tpl", {
    resource_arn = var.resource_arn
    account_id   = var.account_id
    role_name    = var.role_name
  })
}

variable "resource_arn" {}
variable "account_id" {}
variable "role_name" {}
