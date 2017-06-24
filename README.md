# Analysis with API Chat data

### Installation

Run with python 3 and above 

You can clone or download the repo to your computer
Open terminal
Cd into the folder
Install the dependencies/packages from the requirements.txt file using the code below.

```sh
$ pip install -r requirements.txt
```
### Running the program
Write the command below in your terminal. Replace file name, start date, end date and token with required parameters.

```sh
python <filename.py> --start-date YYYY-MM-DD --end-date YYYY-MM-DD --token xxxx --excel empty
```
Example run

```
python main.py --start-date 2017-05-01 --end-date 2017-06-15 --token xxxx --excel empty
On 2017-05-31 there was 17 chats
-------------------------------------------
0 :00 there was  3  users present
1 :00 there was  2  users present
2 :00 there was  3  users present
3 :00 there was  1  users present
4 :00 there was  2  users present
5 :00 there was  1  users present
6 :00 there was  2  users present
7 :00 there was  3  users present
8 :00 there was  6  users present
9 :00 there was  8  users present
10 :00 there was  9  users present
11 :00 there was  10  users present
12 :00 there was  9  users present
13 :00 there was  9  users present
14 :00 there was  6  users present
15 :00 there was  8  users present
16 :00 there was  7  users present
17 :00 there was  3  users present
18 :00 there was  3  users present
19 :00 there was  3  users present
20 :00 there was  2  users present
21 :00 there was  1  users present
22 :00 there was  1  users present
23 :00 there was  1  users present



On 2017-05-23 there was 17 chats
-------------------------------------------
0 :00 there was  2  users present
1 :00 there was  2  users present
2 :00 there was  1  users present
3 :00 there was  2  users present
4 :00 there was  1  users present
5 :00 there was  2  users present
6 :00 there was  1  users present
7 :00 there was  4  users present
8 :00 there was  5  users present
9 :00 there was  12  users present
10 :00 there was  10  users present
11 :00 there was  11  users present
12 :00 there was  10  users present
13 :00 there was  9  users present
14 :00 there was  9  users present
15 :00 there was  9  users present
16 :00 there was  7  users present
17 :00 there was  5  users present
18 :00 there was  2  users present
19 :00 there was  2  users present
20 :00 there was  2  users present
21 :00 there was  3  users present
22 :00 there was  3  users present
23 :00 there was  3  users present



On 2017-05-31 there was 15 chats
-------------------------------------------
0 :00 there was  3  users present
1 :00 there was  2  users present
2 :00 there was  3  users present
3 :00 there was  1  users present
4 :00 there was  2  users present
5 :00 there was  1  users present
6 :00 there was  2  users present
7 :00 there was  3  users present
8 :00 there was  6  users present
9 :00 there was  8  users present
10 :00 there was  9  users present
11 :00 there was  10  users present
12 :00 there was  9  users present
13 :00 there was  9  users present
14 :00 there was  6  users present
15 :00 there was  8  users present
16 :00 there was  7  users present
17 :00 there was  3  users present
18 :00 there was  3  users present
19 :00 there was  3  users present
20 :00 there was  2  users present
21 :00 there was  1  users present
22 :00 there was  1  users present
23 :00 there was  1  users present

```
### Downloading results in CSV

If you would like to download the code above as a .CSV file, replace empty with excel
```sh
python <filename.py> --start-date YYYY-MM-DD --end-date YYYY-MM-DD --token xxxx --excel excel
```

### Jupyter Notebook Visualisations with Seaborn

The  exported results in the CSV file were read in Jupyter Notebook, using Pandas DataFrame, and the results of the top 3 dates were visualised with Seaborn.

### Development
Done by Farhana
