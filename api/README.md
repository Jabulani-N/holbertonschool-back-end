# holbertonschool-back-end
One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, I will access employee data via an API to organize and export them to different data structures. 

Resources:

* [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
* [What is an API?](https://www.webopedia.com/definitions/api/)
* [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
* [What is a REST API?](https://www.sitepoint.com/rest-api/)
* [What are microservices](https://smartbear.com/learn/api-design/microservices/)
* [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://peps.python.org/pep-0008/)

## Task1:

[how to use scv to write to a csv file](https://stackoverflow.com/questions/45549424/exporting-python-output-into-csv-or-text-file-beginner) features the foloowign example:

```
import csv
import random

data = [random.randint(1, 10) for _ in range(10)]

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(data)

```
after which `data.csv` in  the terminal results in `9,3,7,4,1,3,7,8,1,3` (it will be random numbers)

* `writerow` is able to write one row to file. `writerows` can recieve a 2-d array and each contained array will be it's own row written to the file

* do not forget that "write" is different from "append" when it comes to files.

To surround your outputs in doublequotes when using `csv.writerow`, use `csv.writer(whatever_variable_you_opened_your_file_as, quoting=csv.QUOTE_ALL)`

