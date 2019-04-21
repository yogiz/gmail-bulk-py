# sumber :  https://realpython.com/python-send-email/
# hal yang harus di lakukan adalah merubah security pass di gmail untuk mengijinkan less security appp login, atau mengaktifkan 2 verif login dan membuat app login.


import csv, smtplib, ssl, time, random


def rand_file_line(file):
    with open(file) as f:
        lines = f.readlines()
        line = random.choice(lines)
        return line


def should_remove_line(line, stop_words):
    return any([word in line for word in stop_words])


def send_gmail_session(from_address, password, limit_per_sender):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(from_address, password)
        with open("file/email.csv") as file:
            reader = csv.reader(file)
            i = 0
            for email, name in reader:
                if i >= limit_per_sender:
                    print('Saatnya ganti pake email sender lainnya')
                    break
                try:
                    msg_content = rand_file_line('file/content.txt')  # generate random message
                    subject = rand_file_line('file/subject.txt')
                    msg = ("Subject: %s\r\n\r\n"
                           % (subject))
                    message = msg + msg_content
                    server.sendmail(  # mengirim email
                        from_address,
                        email,
                        message.format(name=name),
                    )

                    with open("file/berhasil.txt", "a") as f:  # write email yang berhasil dikirim
                        f.write(email + '\n')
                    print('berhasil mengirim ke : ' + email + ' === by ' + from_address)
                    i = i + 1
                    time.sleep(random.randint(40, 160))
                except:
                    print(email + "gagal di kirim\n")
                    time.sleep(10)

    # buka list email yang sudah dikirim
    eliminasi_email = open("file/berhasil.txt").readlines()
    eliminasi_email = [s.replace('\n', '') for s in eliminasi_email] # menghilangkan enter pada list, agar bisa mendeteksi email
    # buat list email yang belum dikirim
    with open(r"file/email.csv") as f, open(r"file/buffer.txt", "w") as working:
        for line in f:
            if not should_remove_line(line, eliminasi_email):
                working.write(line)

    # kopi list email yang sudah dikirim ke list email utama
    with open("file/buffer.txt") as f:
        with open("file/email.csv", "w") as f1:
            for line in f:
                f1.write(line)

    # menambahkan file ke total hasil
    with open("file/berhasil.txt") as f:
        with open("file/hasil_total.txt", "a") as f1:
            for line in f:
                f1.write(line)

    # reset file
    open('file/buffer.txt', 'w').close()
    open('file/berhasil.txt', 'w').close()


limit_per_sender = 3
session_iteration = 40

from cowpy import cow
cheese = cow.Moose(tongue=True)
msg = cheese.milk("Selamat Mengirim Email")
print(msg)

for i in range(session_iteration) :
    with open('file/email_sender.txt') as f :
        for line in f :
            line = line.split(',')
            from_address = line[0]
            password = line [1]
            send_gmail_session(from_address,password,limit_per_sender)
    print(' =======================>>> Rollingan ke %i <<<=======================' %(i))
    time.sleep(200)

