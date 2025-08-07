
# Demonstration of Dictionary - Mapping type data structure with Practical, DevOps-style employee examples
## Basic dictionary usage
    ## Nested dictionaries
    ## List of dictionaries
## manipulating complex structures
    ## Creating and Assessing a dictionary
    ## Removing elements
    ## Removing a key-value pair
    ## Checking if a key exists
## Other examples: 
    ## Merging dictionaries
    ## Iterating over keys, values, or both
    ## Using .get() vs direct access
    ## Dictionary comprehension
    ## Default values with setdefault 

def dictionary_demo():
    # Creating a dictionary to store employee details

    # List of employees (list of dictionaries)
    employees = [
        {
            "id": 201,
            "name": "John Doe",
            "department": "Cloud",
            "location": "Toronto",
            "skills": ["GCP", "Terraform", "Kubernetes"],
            "contact": {
                "email": "ben.carter@example.com",
                "phone": "+1-222-111-3333"
            }
        },
        {
            "id": 202,
            "name": "Jane Doe",
            "department": "DevOps",
            "location": "Texas",
            "skills": ["SIEM", "XDR", "EDR"],
            "contact": {
                "email": "sara.lee@example.com",
                "phone": "+1-888-999-0000"
            }
        }
    ]

    new_employee = {
        "id": 101,
        "name": "Jane John",
        "department": "Security",
        "location": "California",
        "skills": ["AWS", "Azure", "Python", "CI/CD"], # List within a dictionary
        "contact": {  # nested Dictionary
            "email": "Jane@example.com",
            "phone": "+1-234-567-8910"
        }
    }

    # manipulating complex structures

    ## Modifying and Adding Elements:
    
    # Updating nested dictionary
    new_employee["contact"]["slack"] = "@jane"
    print("Updated Contact Info with slack detail:", new_employee["contact"]) 
    # Output: Updated Contact Info with slack detail: {'email': 'Jane@example.com', 'phone': '+1-234-567-8910', 'slack': '@jane'}


    # Accessing values using keys
    print("Employee Name:", new_employee["name"]) # Output: Employee Name: Jane John
    print("Department:", new_employee["department"]) # Output: Department: Security
    print("Primary Skill:", new_employee["skills"][0])  # Accessing list inside dict # Output: Primary Skill: AWS
    print("Email:", new_employee["contact"]["email"])   # Nested dictionary access # Output: Email: Jane@example.com

    # Remove key using `del`
    del new_employee["location"]
    print("\nAfter deleting location:", new_employee)
    # Output:
    # After deleting location: 
        # {
        #     'id': 101, 
        #     'name': 'Jane John', 
        #     'department': 'Security', 
        #     'skills': ['AWS', 'Azure', 'Python', 'CI/CD'], 
        #     'contact': {'email': 'Jane@example.com', 'phone': '+1-234-567-8910', 'slack': '@jane'}
        # }

    # Adding a new key-value pair
    new_employee["location"] = "California"
    print("\nAfter adding location:", new_employee)
    # Output:
    # After adding location: 
        # {
        #     'id': 101, 
        #     'name': 'Jane John', 
        #     'department': 'Security', 
        #     'skills': ['AWS', 'Azure', 'Python', 'CI/CD'],
        #     'contact': {'email': 'Jane@example.com', 'phone': '+1-234-567-8910', 'slack': '@jane'}, 
        #     'location': 'California'
        # }

    # Remove key using `pop()` and get its value
    removed_department = new_employee.pop("department")
    print("Removed:", removed_department)  # Output: Removed: Security
    print("\nAfter removing department:", new_employee)    
    # Output:
    # After removing department: 
        # {
        #     'id': 101, 
        #     'name': 'Jane John', 
        #     'skills': ['AWS', 'Azure', 'Python', 'CI/CD'], 
        #     'contact': {'email': 'Jane@example.com', 'phone': '+1-234-567-8910', 'slack': '@jane'}, 
        #     'location': 'California'
        # }

    if "name" in new_employee:
        print("Name is present") # Output: Name is present
    
    # Using `get()` safely
    print(new_employee.get("department", "No department provided"))  # Outputs: No department provided

    # Add the first employee to the list
    employees.append(new_employee)
    print("\nAfter adding new_employee:", employees)
    # Outputs: 
    # After adding new_employee: 
        # [
        #     {
        #         'id': 201, 
        #         'name': 'John Doe', 
        #         'department': 'Cloud', 
        #         'location': 'Toronto', 
        #         'skills': ['GCP', 'Terraform', 'Kubernetes'], 
        #         'contact': {'email': 'ben.carter@example.com', 
        #         'phone': '+1-222-111-3333'}
        #     }, 
        #     {
        #         'id': 202, 
        #         'name': 'Jane Doe', 
        #         'department': 'DevOps', 
        #         'location': 'Texas', 
        #         'skills': ['SIEM', 'XDR', 'EDR'], 
        #         'contact': {'email': 'sara.lee@example.com', 'phone': '+1-888-999-0000'}
        #     }, 
        #     {
        #         'id': 101, 
        #         'name': 'Jane John', 
        #         'skills': ['AWS', 'Azure', 'Python', 'CI/CD'], 
        #         'contact': {'email': 'Jane@example.com', 'phone': '+1-234-567-8910', 'slack': '@jane'}, 
        #         'location': 'California'
        #     }
        # ]

    # Accessing data from list of dictionaries 
    print("\n--- All Employees ---")
    # when a field is missing - catch and handle the expection 
    for emp in employees:
        try:
            print(f"{emp['name']} ({emp['department']}) - Email: {emp['contact']['email']}")
        except KeyError as e:
            print(f"Missing key {e} in employee record: {emp}")
        except TypeError:
            print(f"Invalid data structure for employee record: {emp}")
    # Output:
    # -- All Employees ---
    # John Doe (Cloud) - Email: ben.carter@example.com
    # Jane Doe (DevOps) - Email: sara.lee@example.com

    # when a field is missing - Using .get() with default values 
    for emp in employees:
        name = emp.get('name', 'Unknown')
        department = emp.get('department', 'Not Specified')
        contact = emp.get('contact', {})
        email = contact.get('email', 'No Email Provided')
        print(f"{name} ({department}) - Email: {email}")
    # Output:
    # -- All Employees ---
    # John Doe (Cloud) - Email: ben.carter@example.com
    # Jane Doe (DevOps) - Email: sara.lee@example.com
    # Jane John (Not Specified) - Email: Jane@example.com

    # Filter: Get all employees in the DevOps department 
    devops_emps = [emp for emp in employees if emp.get("department") == "DevOps"]
    print("\nDevOps Team Members:")
    for dev in devops_emps:
        print(dev.get("name", "Name not available"))
    # Output:
    # DevOps Team Members:
    # Jane Doe

    # Nested lookup with safe access using get()
    print("\nChecking Slack handles:")
    for emp in employees:
        slack = emp.get("contact", {}).get("slack", "Not set")
        print(f"{emp['name']}: Slack - {slack}")
    # Output:    
    # Checking Slack handles:
    # John Doe: Slack - Not set
    # Jane Doe: Slack - Not set
    # Jane John: Slack - @jane

    # Add a new key to all employee entries
    for emp in employees:
        emp["status"] = "Active"  # could be useful for automation filtering
    print("\nFinal employee list with status:")
    for emp in employees:
        print(f"{emp['name']} - Status: {emp['status']}")
    # Output:  
    # Final employee list with status:
    # John Doe - Status: Active
    # Jane Doe - Status: Active
    # Jane John - Status: Active

    for i, emp in enumerate(employees):
        print(f"{i}: {emp['name']}")
    # Output: 
    # 0: John Doe
    # 1: Jane Doe
    # 2: Jane John

    # Example: Count how many have "Kubernetes" skill
    kubernetes_count = sum("Kubernetes" in emp["skills"] for emp in employees)
    print(f"\nEmployees with Kubernetes skill: {kubernetes_count}")
    # Output: 
    # Employees with Kubernetes skill: 1

    # Clear All employees
    employees.clear()
    print(employees)  # Output: {}

    # Example: Merge using `|` (Python 3.9+)
    defaults = {
    "region": "us-east-1",
    "retries": 3
    }
    overrides = {
        "retries": 5,
        "timeout": 100
    }
    final_config = defaults | overrides
    # final_config = {**defaults, **overrides} #  (Python <3.9+)
    print(final_config)  # Output: {'region': 'us-east-1', 'retries': 5, 'timeout': 100}

    # Example: Iterating Over Dictionary
    server = {
        "host": "192.168.1.10",
        "port": 22,
        "user": "admin"
    }
    # Iterate over keys
    for key in server:
        print(f"Key: {key}")
    # Output: 
    # Key: host
    # Key: port
    # Key: user
    # Iterate over values
    for value in server.values():
        print(f"Value: {value}")
    # Output: 
    # Value: 192.168.1.10
    # Value: 22
    # Value: admin
    # Iterate over key-value pairs
    for key, value in server.items():
        print(f"{key} = {value}")
    # Output: 
    # host = 192.168.1.10
    # port = 22
    # user = admin

    # Example: Using setdefault() for Default Values
    env_config = {}
    # If "ENV" doesn't exist, set it
    env_config.setdefault("ENV", "dev")
    print(env_config)  # Output: {'ENV': 'dev'} 
    # Won't overwrite if already set
    env_config.setdefault("ENV", "prod") # Still 'dev'
    print(env_config)  # Output: {'ENV': 'dev'}  

    # Example: Dictionary Comprehension
    # Create a dictionary of squares
    squares = {x: x*x for x in range(1, 6)}
    print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # Example: DevOps-style: Add monitoring tags
    services = ["auth", "billing", "search"]
    tags = {svc: f"{svc}_monitoring_enabled" for svc in services}
    print(tags)
    # Output: 
    # {
    #     'auth': 'auth_monitoring_enabled', 
    #     'billing': 'billing_monitoring_enabled', 
    #     'search': 'search_monitoring_enabled'
    # }

    # Example: Copying a Dictionary
    config = {"env": "staging", "debug": True}
    backup = config.copy()

    backup["env"] = "prod"
    print(config["env"])  # Output: staging
    print(backup["env"])  # Output: prod

    # Example: Check if certain config keys are present before deploying
    deploy_config = {
        "region": "us-west-2",
        "instance_type": "t2.medium"
    }
    required_keys = ["region", "instance_type", "ami_id"]
    for key in required_keys:
        if key not in deploy_config:
            print(f"Missing required config: {key}") # Output: Missing required config: ami_id

# Demonstration of Set and Frozenset - data structure with Practical, DevOps-style employee examples

def set_demo():
    # Creating a Set of DevOps tools used by a team
    devops_tools = {"Docker", "Kubernetes", "Terraform", "Ansible", "Prometheus"}
    print(devops_tools)  # Output: {'Prometheus', 'Docker', 'Kubernetes', 'Terraform', 'Ansible'}
    print(type(devops_tools))   # Output: <class 'set'> 

    # Looping Through a Set
    for tool in devops_tools:
        print("Tool:", tool) 
    # Output: 
    # Tool: Prometheus
    # Tool: Docker
    # Tool: Kubernetes
    # Tool: Terraform
    # Tool: Ansible

    # Set Comprehension
    # Generate tools starting with 'T'
    tools_with_t = {tool for tool in devops_tools if tool.startswith("T")}
    print(tools_with_t)
    # Output: {'Terraform'}

    # Clearing and Copying a Set
    copy_tools = devops_tools.copy()
    copy_tools.clear()
    print("Cleared copy:", copy_tools)
    # Output: Cleared copy: set()

    # Add a tool
    devops_tools.add("Grafana")
    print("After add:", devops_tools)
    # Output: After add: {'Prometheus', 'Docker', 'Grafana', 'Kubernetes', 'Terraform', 'Ansible'}

    # Remove a tool (error if not present)
    devops_tools.remove("Ansible")
    print("After remove:", devops_tools)
    # Output: After remove: {'Prometheus', 'Docker', 'Grafana', 'Kubernetes', 'Terraform'}

    # Discard (no error if item not present)
    devops_tools.discard("NonExistentTool")

    # Add multiple tools
    devops_tools.update(["Vault", "Jenkins"])
    print("After update:", devops_tools)
    # Output: After update: {'Vault', 'Prometheus', 'Docker', 'Jenkins', 'Grafana', 'Kubernetes', 'Terraform'}

    # Remove random element
    removed = devops_tools.pop()
    print("Removed:", removed)
    # Output: Removed: Vault

    # Set Operations: Union, Intersection, Difference
    cloud_team = {"AWS", "Azure", "Terraform", "Kubernetes"}
    security_team = {"Vault", "Azure", "Terraform", "Splunk"}

    # Union (combine all tools used)
    all_tools = cloud_team.union(security_team)
    print("All tools:", all_tools)
    # Output: All tools: {'AWS', 'Splunk', 'Vault', 'Azure', 'Kubernetes', 'Terraform'}

    # Intersection (common tools)
    common_tools = cloud_team.intersection(security_team)
    print("Common tools:", common_tools)
    # Output: Common tools: {'Terraform', 'Azure'}

    # Difference (tools used only by cloud team)
    unique_cloud = cloud_team.difference(security_team)
    print("Only in cloud team:", unique_cloud)
    # Output: Only in cloud team: {'AWS', 'Kubernetes'}

    # Symmetric difference (tools used by one but not both)
    symmetric_diff = cloud_team.symmetric_difference(security_team)
    print("Different tools:", symmetric_diff)
    # Output: Different tools: {'AWS', 'Splunk', 'Vault', 'Kubernetes'}

    # set comparison
    print(cloud_team.issubset(security_team))       # Output:  False
    print(security_team.issuperset(cloud_team))     # Output:  False
    print(cloud_team.isdisjoint({"Docker"}))      # Output: True

def frozenset_demo():
    # Frozenset creation:
    immutable_team = frozenset(["AWS", "Docker", "Vault"])
    print(type(immutable_team))  # Output: <class 'frozenset'>

    # Can be used as a key in a dictionary
    team_cache = {
        immutable_team: "Stable configuration deployed"
    }
    print(team_cache[immutable_team]) # Output: Stable configuration deployed

    # Attempting to Modify Frozenset (Will Fail)
    try:
        immutable_team.add("Azure")  # AttributeError
    except AttributeError as e:
        print("Error: Cannot modify frozenset -", e) # Output: Error: Cannot modify frozenset - 'frozenset' object has no attribute 'add'
    
    # Frozenset Set Operations Still Work
    infra_stack = frozenset(["AWS", "Terraform"])
    monitoring_stack = frozenset(["Grafana", "Prometheus", "AWS"])

    # Can do union, intersection, etc.
    print(infra_stack.union(monitoring_stack)) # Output: frozenset({'AWS', 'Prometheus', 'Terraform', 'Grafana'})
    print(infra_stack.intersection(monitoring_stack)) # Output: frozenset({'AWS'})

    # Set of services with alerts enabled vs required
    enabled_alerts = {"EC2", "RDS", "S3"}
    required_alerts = {"EC2", "RDS", "Lambda", "S3"}

    missing_alerts = required_alerts.difference(enabled_alerts)
    if missing_alerts:
        print("Enable alerts for:", missing_alerts) # Output: Enable alerts for: {'Lambda'}
    
    tool_combo = frozenset(["Terraform", "Vault"])
    cache = {
        tool_combo: "Pre-approved Infrastructure combo"
    }
    print(cache[tool_combo]) # Output: Pre-approved Infrastructure combo

def set_fronzenset():
    # Set and Frozenset Difference: 
    # Mutable set
    devops_tools = set(["Docker", "Kubernetes", "Terraform"])

    devops_tools.add("Ansible")       # Can add
    devops_tools.remove("Docker")     # Can remove
    print("Set:", devops_tools) # Output: Set: {'Ansible', 'Kubernetes', 'Terraform'}

    # Immutable set
    immutable_tools = frozenset(["Docker", "Kubernetes", "Terraform"])

    # Trying to add or remove will raise an error
    try:
        immutable_tools.add("Ansible")  # AttributeError
    except AttributeError:
        print("Cannot modify frozenset!") # Output: Cannot modify frozenset!

    # Can still do set operations
    print("Intersection with another set:", immutable_tools & {"Kubernetes", "Ansible"})
    # Output: Intersection with another set: frozenset({'Kubernetes'})

if __name__ == "__main__":
    print("Demonstration of Dictionary Usage: ")
    dictionary_demo()
    print("\nDemonstration of Set Usage: ")
    set_demo()
    print("\nDemonstration of FronzenSet Usage: ")
    frozenset_demo()
    print("\nDemonstration of Set and FronzenSet Usage: ")
    set_fronzenset()