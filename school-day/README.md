# Is Today a School Day?

## Installation

Copy all files in a folder or clone this Repo and change to the `school-day` folder.

Run the following command to install it.

```
make install
```

## Getting Started

Now you can prepend the script in cronjobs or other scripts.

Examples:

`echo "Hello"` outputs the word "Hello" on the console.

* `is-today-school-day && echo "Today is school"` only outputs the text on school days.
* `is-today-school-day || echo "Today is NO school"` only outputs the text on days without school.
* `is-today-school-day && echo "Today is school" || echo "Today is not school"` gives the right sentence.

Instead of the pointless echo commands you can use this script for other things.

e.g. in a crontab with

```
0 7 * * *  root  is-today-school-day && linbo-remote -r r100 -c sync:1,start:1
```

you can start all computers synchronized at 7 o'clock in the morning.
