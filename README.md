# makefun-meeting-email

[![make.fun · u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/sambob0606/makefun-meeting-email/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/sambob0606/makefun-meeting-email/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)

One line for make.fun's "The Meeting That Should Have Been an Email" bounty: a single joke, at most 200 characters, about a meeting that should have been an email. The program writes the line to `/output/entry.txt`.

> We held a meeting to screen-share the email that had already answered everything.

Why this line: it skips the obvious complaint about length and goes for a picture everyone recognizes — a room gathered to look at a message that had already settled the question. The turn lands on the last words: the email had answered everything before anyone joined the call.

## Run it

```sh
python3 main.py
```

It writes the single line (no trailing newline) to `/output/entry.txt`, then reads it back and verifies the gate (1–200 characters, one line, not blank) before exiting.
