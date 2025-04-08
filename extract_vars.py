import re
import json
import os

TEMPLATE_FILE = "scp-template.json.tpl"

def extract_variables_from_template(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    pattern = r"\${([A-Za-z0-9_]+)}"
    return sorted(set(re.findall(pattern, content)))

def main():
    variables = extract_variables_from_template(TEMPLATE_FILE)

    # Puedes imprimirlas o exportarlas como JSON para Jenkins
    print(json.dumps(variables))

    # Si Jenkins pasa valores por env, también podrías generar un tfvars
    tfvars = {}
    for var in variables:
        val = os.getenv(f"TF_VAR_{var}")
        if val is not None:
            tfvars[var] = val

    if tfvars:
        with open("terraform.auto.tfvars.json", "w") as f:
            json.dump(tfvars, f, indent=2)
            print("Archivo terraform.auto.tfvars.json generado.")

if __name__ == "__main__":
    main()
