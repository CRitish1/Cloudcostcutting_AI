def main():
    print("Welcome to the Cloud Cost Comparison Tool!")
    
    # Links to cloud billing pages
    aws_link = "https://aws.amazon.com/billing/"
    gcp_link = "https://console.cloud.google.com/billing/"
    
    print("\nPlease visit the following links to access your billing information:")
    print(f"AWS Billing: {aws_link}")
    print(f"GCP Billing: {gcp_link}")

    # Input number of instances for AWS and GCP
    num_aws = int(input("\nHow many AWS instances do you have? "))
    num_gcp = int(input("How many GCP instances do you have? "))

    aws_instances = []
    gcp_instances = []

    # Collecting AWS instances data
    for i in range(num_aws):
        name = input(f"Enter the name for AWS instance {i+1}: ")
        cost = float(input(f"Enter the bill amount for AWS instance {name} ($): "))
        aws_instances.append({'name': name, 'cost': cost})

    # Collecting GCP instances data
    for i in range(num_gcp):
        name = input(f"Enter the name for GCP instance {i+1}: ")
        cost = float(input(f"Enter the bill amount for GCP instance {name} ($): "))
        gcp_instances.append({'name': name, 'cost': cost})

    # Process AWS instances
    aws_total = sum(instance['cost'] for instance in aws_instances)
    aws_useless = [instance['name'] for instance in aws_instances if instance['cost'] == 0]
    
    # Process GCP instances
    gcp_total = sum(instance['cost'] for instance in gcp_instances)
    gcp_useless = [instance['name'] for instance in gcp_instances if instance['cost'] == 0]
    
    # Results
    print("\nAnalysis Results:")
    if aws_total < gcp_total:
        print("AWS is cheaper.")
    elif gcp_total < aws_total:
        print("GCP is cheaper.")
    else:
        print("Both AWS and GCP have the same total billing amount.")

    # Advising on useless instances
    if aws_useless:
        print(f"Consider removing the following AWS instances with zero-dollar billing as they are useless: {', '.join(aws_useless)}")
    if gcp_useless:
        print(f"Consider removing the following GCP instances with zero-dollar billing as they are useless: {', '.join(gcp_useless)}")
    
    # Output links again for user reference
    print("\nFor more details on your billing, please revisit the following links:")
    print(f"AWS Billing Details: {aws_link}")
    print(f"GCP Billing Details: {gcp_link}")

if __name__ == "__main__":
    main()

