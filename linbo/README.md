# Linbo

## check-offline-hosts

### Usage

This scripts helps to identify which computers couldn't boot into Linbo after waking them up with Wake-on-Lan.
You have to use `linbo-remote` with `-p` parameter, e.g. to wake up a whole room, sync the first OS and start it, you will return

```
$ linbo-remote -r room1 -p sync:1,start:1 -w 0
```

After that you can run `check-offline-hosts` to check if a computer couldn't get his linbo command file.

Best is to run the script an hour after the `linbo-remote` command to give enough time to install and sync a new image (if there is one).
Your crontab may look like that:

```
0 6 * * * linbo-remote -g group1 -w 0 -p sync:1,halt
0 7 * * * check-offline-hosts
```
Is recommend to run this together with [`is-today-school-day`](https://github.com/cdscacth/linuxmuster-scripts/tree/master/school-day) so you only sync your computers on school days. Save energy :)

### Mattermost Integration

Config your Mattermost incoming webhook URL to get notifications.

```
# Optional config for Mattermost
mattermostUrl = ""
channel = "#monitoring"
botName = "Linbo"
icon_url = ""
```
