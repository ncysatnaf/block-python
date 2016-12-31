from ftplib import FTP, error_perm
import os

# ftp=FTP("ftp.pyclass.com")
#
# ftp.login("student@pyclass.com", "student123")
#
# print ftp.nlst()
# print ftp.nlst("Data")
#
# ftp.close()


# def ftpDownloader(filename, host = "ftp.pyclass.com", user = "student@pyclass.com", passwd = "student123"):
#     ftp = FTP(host)
#     ftp.login(user, passwd)
#     ftp.cwd("Data")
#     os.chdir(os.getcwd())
#     with open(filename, 'wb') as file:
#         ftp.retrbinary("RETR %s" % filename, file.write)
#
#
# ftpDownloader("isd-lite-format.pdf")


def ftpDownloader(stationId, startYear, endYear, host = "ftp.pyclass.com", user = "student@pyclass.com", passwd = "student123"):
    ftp = FTP(host)
    ftp.login(user, passwd)
    ftp.cwd("Data")
    os.chdir(os.getcwd())
    for year in range(startYear, endYear+1):
        fullpath = '/Data/%s/%s-%s.gz' % (year, stationId, year)
        filename = os.path.basename(fullpath)
        try:
            with open(filename, 'wb') as file:
                ftp.retrbinary("RETR %s" % fullpath, file.write)
                print ('%s successfully downloaded' % filename)
        except error_perm:
            print('%s is not available' % filename)
            os.remove(filename)
    ftp.close()


ftpDownloader("010010-99999", 2010, 2014)
